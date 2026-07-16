#!/usr/bin/env python3
"""Validate the repository's declared research-content baseline using stdlib only."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
BASELINE_PATH = ROOT / "validation/content-baseline.json"
MANIFEST_PATH = ROOT / "MANIFEST.txt"
INLINE_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
REFERENCE_LINK_RE = re.compile(r"^\[[^\]]+\]:\s*(\S+)", re.MULTILINE)
EXPERIMENT_ID_RE = re.compile(r"\bEXP-C\d{2}-\d{2}\b")
SOURCE_FILENAME_RE = re.compile(r"SRC-[A-Z0-9]+-\d{3}\.md")
MANIFEST_LINE_RE = re.compile(r"^(.*?)\t(\d+) bytes$")


class Validator:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.checks = 0

    def require(self, condition: bool, message: str) -> None:
        self.checks += 1
        if not condition:
            self.errors.append(message)

    def require_contains(self, path: Path, needle: str, context: str) -> None:
        self.require(path.is_file(), f"{context}: missing file {path.relative_to(ROOT)}")
        if path.is_file():
            self.require(
                needle in path.read_text(encoding="utf-8"),
                f"{context}: {path.relative_to(ROOT)} is missing {needle!r}",
            )


def load_baseline(validator: Validator) -> dict:
    try:
        baseline = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        validator.errors.append(f"baseline: cannot read {BASELINE_PATH.relative_to(ROOT)}: {exc}")
        return {}

    validator.require(baseline.get("schema_version") == 1, "baseline: unsupported schema_version")
    return baseline


def repository_files() -> set[str]:
    command = ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"]
    completed = subprocess.run(command, cwd=ROOT, check=True, capture_output=True)
    return {
        item.decode("utf-8")
        for item in completed.stdout.split(b"\0")
        if item
    }


def expected_manifest_paths(baseline: dict) -> list[str]:
    excluded = set(baseline["manifest"]["excluded_paths"])
    return sorted(path for path in repository_files() if path not in excluded)


def render_manifest(paths: list[str]) -> str:
    return "".join(f"{path}\t{(ROOT / path).stat().st_size} bytes\n" for path in paths)


def check_manifest(validator: Validator, baseline: dict, write_manifest: bool) -> None:
    expected_paths = expected_manifest_paths(baseline)
    if write_manifest:
        MANIFEST_PATH.write_text(render_manifest(expected_paths), encoding="utf-8")

    try:
        lines = MANIFEST_PATH.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        validator.errors.append(f"manifest: cannot read MANIFEST.txt: {exc}")
        return

    entries: dict[str, int] = {}
    for line_number, line in enumerate(lines, start=1):
        match = MANIFEST_LINE_RE.fullmatch(line)
        validator.require(match is not None, f"manifest:{line_number}: invalid entry format")
        if match is None:
            continue
        path, size = match.groups()
        validator.require(path not in entries, f"manifest:{line_number}: duplicate path {path}")
        entries[path] = int(size)

    actual_paths = sorted(entries)
    validator.require(
        actual_paths == expected_paths,
        "manifest: inventory differs from repository files; run "
        "`python3 scripts/validate_content.py --write-manifest`",
    )
    for path, expected_size in entries.items():
        file_path = ROOT / path
        validator.require(file_path.is_file(), f"manifest: missing file {path}")
        if file_path.is_file():
            validator.require(
                file_path.stat().st_size == expected_size,
                f"manifest: byte size mismatch for {path}: "
                f"expected {expected_size}, got {file_path.stat().st_size}",
            )


def extract_link_target(raw_target: str) -> str:
    target = raw_target.strip()
    if target.startswith("<") and ">" in target:
        return target[1 : target.index(">")]
    return target.split(maxsplit=1)[0]


def check_markdown_links(validator: Validator) -> None:
    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        raw_targets = [*INLINE_LINK_RE.findall(text), *REFERENCE_LINK_RE.findall(text)]
        for raw_target in raw_targets:
            target = extract_link_target(raw_target)
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            target = unquote(target.split("#", 1)[0])
            if not target or any(marker in target for marker in ("<", ">", "{", "}")):
                continue
            resolved = ROOT / target.lstrip("/") if target.startswith("/") else path.parent / target
            validator.require(
                resolved.resolve().exists(),
                f"links: {path.relative_to(ROOT)} points to missing target {target}",
            )


def check_program_contract(validator: Validator, baseline: dict) -> None:
    program = baseline["program"]
    state = baseline["content_state"]
    required_paths = baseline["required_paths"]
    for relative_path in required_paths:
        validator.require((ROOT / relative_path).is_file(), f"program: missing required path {relative_path}")

    validator.require(program["version"] == "V4.3", "program: current validator supports V4.3 only")
    validator.require(state["completed_batches"] == list(range(1, 9)), "program: completed batches must be 1 through 8")
    validator.require(state["active_batch"] is None, "program: active content Batch must be null")
    validator.require(len(program["primary_hosts"]) == 4, "program: primary Host set must contain four entries")
    validator.require(len(set(program["primary_hosts"])) == 4, "program: primary Host names must be unique")

    readme = ROOT / "README.md"
    agents = ROOT / "AGENTS.md"
    validator.require_contains(readme, "- 计划（Program）：V4.3", "program")
    validator.require_contains(readme, "当前活动内容 Batch：无", "program")
    validator.require_contains(agents, "* Program version: V4.3", "program")
    for host in program["primary_hosts"]:
        validator.require_contains(ROOT / "docs/10-V4.3-Qwen-Code-Host-Amendment.md", host, "program")
    for amendment in program["amendments"]:
        for relative_path in (
            "docs/10-V4.3-Qwen-Code-Host-Amendment.md",
            "research/templates/experiment-record.template.md",
            "research/templates/run-metadata.template.yaml",
        ):
            validator.require_contains(ROOT / relative_path, amendment, "protocol binding")
    validator.require_contains(
        ROOT / "research/templates/run-metadata.template.yaml",
        'schema_version: "v4.3-r1"',
        "protocol binding",
    )
    validator.require_contains(
        ROOT / "research/templates/run-metadata.template.yaml",
        f'base_schema_version: "{program["base_protocol_schema"]}"',
        "protocol binding",
    )


def check_public_governance(validator: Validator, baseline: dict) -> None:
    governance = baseline["governance"]
    maintainer = governance["maintainer"]
    codeowners = ROOT / ".github/CODEOWNERS"
    validator.require_contains(codeowners, f"* {maintainer}", "governance")
    validator.require_contains(codeowners, f"/.github/ {maintainer}", "governance")

    if governance["license_status"] == "NOT_DECLARED":
        license_files = [path.name for path in ROOT.glob("LICENSE*") if path.is_file()]
        validator.require(not license_files, f"governance: license is NOT_DECLARED but found {license_files}")
    else:
        validator.require(False, f"governance: unsupported license_status {governance['license_status']!r}")

    validator.require_contains(ROOT / "CONTRIBUTING.md", "python3 scripts/validate_content.py", "governance")
    validator.require_contains(ROOT / "CONTRIBUTING.md", "仓库当前没有项目级 `LICENSE`", "governance")
    validator.require_contains(ROOT / "GOVERNANCE.md", maintainer, "governance")
    validator.require_contains(ROOT / "CODE_OF_CONDUCT.md", "Security Policy", "governance")
    validator.require_contains(
        ROOT / "SECURITY.md",
        "https://github.com/yanaoyong/HarnessEngineeringResearchProgram/security/advisories/new",
        "governance",
    )
    validator.require_contains(ROOT / "README.md", "docs/README.md", "navigation")
    validator.require_contains(ROOT / "README.md", "CONTRIBUTING.md", "navigation")
    validator.require_contains(ROOT / "docs/README.md", "V4.3 Qwen Code Host-set Amendment", "navigation")

    pull_request_template = ROOT / ".github/pull_request_template.md"
    validator.require_contains(pull_request_template, "python3 scripts/validate_content.py", "governance")
    validator.require_contains(pull_request_template, "Impact and boundaries", "governance")

    issue_ids: set[str] = set()
    for relative_path in governance["issue_forms"]:
        path = ROOT / relative_path
        validator.require(path.is_file(), f"governance: missing Issue Form {relative_path}")
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for required_key in ("name:", "description:", "body:"):
            validator.require(re.search(rf"^{required_key}", text, re.MULTILINE) is not None, f"governance: {relative_path} is missing {required_key}")
        ids = re.findall(r"^\s+id:\s+([a-zA-Z0-9_-]+)\s*$", text, re.MULTILINE)
        validator.require(bool(ids), f"governance: {relative_path} defines no input IDs")
        for item_id in ids:
            validator.require(item_id not in issue_ids, f"governance: duplicate Issue Form ID {item_id}")
            issue_ids.add(item_id)

    issue_config = ROOT / ".github/ISSUE_TEMPLATE/config.yml"
    validator.require_contains(issue_config, "blank_issues_enabled: false", "governance")
    validator.require_contains(issue_config, "security/advisories/new", "governance")


def source_id_from_entry(path: Path, validator: Validator) -> str | None:
    text = path.read_text(encoding="utf-8")
    filename_id = path.stem
    title_match = re.search(r"^# .*· (SRC-[A-Z0-9]+-\d{3})$", text, re.MULTILINE)
    field_match = re.search(r"来源 ID(?:（Source ID）)?：`(SRC-[A-Z0-9]+-\d{3})`", text)
    validator.require(title_match is not None, f"sources: {path.relative_to(ROOT)} has no registry title ID")
    validator.require(field_match is not None, f"sources: {path.relative_to(ROOT)} has no Source ID field")
    if title_match:
        validator.require(title_match.group(1) == filename_id, f"sources: title ID does not match {path.name}")
    if field_match:
        validator.require(field_match.group(1) == filename_id, f"sources: Source ID field does not match {path.name}")

    required_sections = (
        ("## 身份（Identity）",),
        ("## 位置与版本（Location and Revision）",),
        ("## 权限评估（Authority Assessment）",),
        ("## 派生证据（Derived Evidence）", "## 派生证据"),
    )
    for alternatives in required_sections:
        validator.require(
            any(section in text for section in alternatives),
            f"sources: {path.relative_to(ROOT)} is missing section {alternatives[0]}",
        )
    if "`NOT PINNED`" in text or "NOT PINNED —" in text:
        validator.require(
            any(marker in text for marker in ("执行时", "必须固定", "重新核验")),
            f"sources: {path.relative_to(ROOT)} is unpinned without a pin/revalidation boundary",
        )
        validator.require("浮动" in text, f"sources: {path.relative_to(ROOT)} is unpinned without a floating-anchor label")
    return filename_id if title_match and field_match else None


def check_cycles_and_sources(validator: Validator, baseline: dict) -> None:
    cycles = baseline["cycles"]
    batch_documents = baseline["batch_documents"]
    validator.require([cycle["number"] for cycle in cycles] == list(range(1, 19)), "cycles: baseline numbers must be 1 through 18")
    validator.require(set(batch_documents) == {str(number) for number in range(1, 9)}, "cycles: Batch document mapping must cover Batch 1 through 8")
    expected_directories = {f"cycle-{number:02d}" for number in range(1, 19)}
    cycles_root = ROOT / "research/cycles"
    actual_directories = {path.name for path in cycles_root.iterdir() if path.is_dir() and path.name.startswith("cycle-")}
    validator.require(actual_directories == expected_directories, "cycles: workspace directories must be exactly cycle-01 through cycle-18")

    overview = (ROOT / "docs/00-研究计划总纲.md").read_text(encoding="utf-8")
    index = (cycles_root / "README.md").read_text(encoding="utf-8")
    global_source_ids: set[str] = set()
    global_experiment_ids: set[str] = set()

    for cycle in cycles:
        number = cycle["number"]
        number_text = f"{number:02d}"
        cycle_dir = cycles_root / f"cycle-{number_text}"
        note_path = cycle_dir / "research-note.md"
        experiments_path = cycle_dir / "experiments/README.md"
        evidence_dir = cycle_dir / "evidence"
        for path in (note_path, experiments_path):
            validator.require(path.is_file(), f"cycles: missing {path.relative_to(ROOT)}")
        validator.require(evidence_dir.is_dir(), f"cycles: missing {evidence_dir.relative_to(ROOT)}")
        if not (note_path.is_file() and experiments_path.is_file() and evidence_dir.is_dir()):
            continue

        note = note_path.read_text(encoding="utf-8")
        experiments = experiments_path.read_text(encoding="utf-8")
        expected_heading = f"# Cycle {number_text} 研究笔记（Research Note）· {cycle['name']}"
        validator.require(note.startswith(expected_heading), f"cycles: Cycle {number_text} heading/name differs from baseline")
        validator.require("状态（Status）：PLANNED · NOT EXECUTED" in note, f"cycles: Cycle {number_text} is not explicitly planned/not executed")
        validator.require(f"内容 Batch：{cycle['batch']}" in note, f"cycles: Cycle {number_text} Batch mapping differs from baseline")
        validator.require(cycle["name"] in overview, f"cycles: overview is missing Cycle {number_text} name")
        content_document = ROOT / batch_documents[str(cycle["batch"])]
        validator.require(content_document.is_file(), f"cycles: missing Batch {cycle['batch']} content document")
        if content_document.is_file():
            validator.require(
                cycle["name"] in content_document.read_text(encoding="utf-8"),
                f"cycles: Batch {cycle['batch']} content document is missing Cycle {number_text} name",
            )
        validator.require(
            f"[cycle-{number_text} · {cycle['name']}](cycle-{number_text}/research-note.md) — `PLANNED · NOT EXECUTED`" in index,
            f"cycles: index entry differs for Cycle {number_text}",
        )

        expected_experiments = set(cycle["experiments"])
        note_experiments = set(EXPERIMENT_ID_RE.findall(note))
        planned_experiments = set(EXPERIMENT_ID_RE.findall(experiments))
        validator.require(planned_experiments == expected_experiments, f"experiments: Cycle {number_text} IDs differ from baseline")
        validator.require(note_experiments <= expected_experiments, f"experiments: Cycle {number_text} note contains undeclared IDs")
        validator.require(bool(note_experiments), f"experiments: Cycle {number_text} note contains no planned Experiment ID")
        for experiment_id in expected_experiments:
            validator.require(experiment_id.startswith(f"EXP-C{number_text}-"), f"experiments: {experiment_id} is assigned to the wrong Cycle")
            validator.require(experiment_id not in global_experiment_ids, f"experiments: duplicate baseline ID {experiment_id}")
            global_experiment_ids.add(experiment_id)

        all_source_paths = sorted(evidence_dir.glob("SRC-*.md"))
        for path in all_source_paths:
            validator.require(
                SOURCE_FILENAME_RE.fullmatch(path.name) is not None,
                f"sources: malformed Source Registry filename {path.relative_to(ROOT)}",
            )
        source_paths = [path for path in all_source_paths if SOURCE_FILENAME_RE.fullmatch(path.name)]
        actual_sources = {path.stem for path in source_paths}
        expected_sources = set(cycle["sources"])
        validator.require(actual_sources == expected_sources, f"sources: Cycle {number_text} registry IDs differ from baseline")
        for path in source_paths:
            source_id = source_id_from_entry(path, validator)
            if source_id:
                validator.require(source_id not in global_source_ids, f"sources: duplicate Source ID {source_id}")
                global_source_ids.add(source_id)

    validator.require(not list(cycles_root.rglob("SRC-ZCODE-*.md")), "sources: superseded SRC-ZCODE entry exists in the active registry")


def check_not_started_boundary(validator: Validator, baseline: dict) -> None:
    state = baseline["content_state"]["research_execution"]
    validator.require(state in {"NOT_STARTED"}, f"state: unsupported research_execution value {state!r}")
    if state != "NOT_STARTED":
        return

    cycles_root = ROOT / "research/cycles"
    for experiments_dir in sorted(cycles_root.glob("cycle-*/experiments")):
        files = {path.name for path in experiments_dir.iterdir() if path.is_file()}
        validator.require(files == {"README.md"}, f"state: {experiments_dir.relative_to(ROOT)} contains an execution artifact")
    for number in range(15, 19):
        evidence_dir = cycles_root / f"cycle-{number:02d}/evidence"
        files = {path.name for path in evidence_dir.iterdir() if path.is_file()}
        validator.require(files == {"README.md"}, f"state: {evidence_dir.relative_to(ROOT)} contains a result artifact")
    for relative_dir in ("research/adr-candidates", "research/route-reviews"):
        files = {path.name for path in (ROOT / relative_dir).iterdir() if path.is_file()}
        validator.require(files == {"README.md"}, f"state: {relative_dir} contains a ratified artifact")

    forbidden_filenames = re.compile(r"^(EVD-|ENT-|ADR-CANDIDATE-\d|FINDING-|RUN-)")
    for path in (ROOT / "research").rglob("*"):
        if path.is_file():
            validator.require(not forbidden_filenames.match(path.name), f"state: unexpected execution artifact {path.relative_to(ROOT)}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--write-manifest",
        action="store_true",
        help="rewrite MANIFEST.txt from the current non-ignored repository files before validation",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    validator = Validator()
    baseline = load_baseline(validator)
    if baseline:
        check_manifest(validator, baseline, args.write_manifest)
        check_markdown_links(validator)
        check_program_contract(validator, baseline)
        check_public_governance(validator, baseline)
        check_cycles_and_sources(validator, baseline)
        check_not_started_boundary(validator, baseline)

    if validator.errors:
        print(f"Content integrity validation failed with {len(validator.errors)} error(s):", file=sys.stderr)
        for error in validator.errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    action = "updated and validated" if args.write_manifest else "validated"
    print(f"Content integrity {action}: {validator.checks} checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
