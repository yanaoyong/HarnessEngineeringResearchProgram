#!/usr/bin/env python3
"""Regression tests for semantic content-integrity guards."""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run(command: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=cwd, capture_output=True, text=True, check=False)


def temporary_repository() -> tuple[tempfile.TemporaryDirectory[str], Path]:
    temporary_directory = tempfile.TemporaryDirectory(prefix="content-validation-")
    repository = Path(temporary_directory.name) / "repository"
    shutil.copytree(
        ROOT,
        repository,
        ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc"),
    )
    initialized = run(["git", "init", "-q"], repository)
    if initialized.returncode != 0:
        raise RuntimeError(initialized.stderr)
    staged = run(["git", "add", "-A"], repository)
    if staged.returncode != 0:
        raise RuntimeError(staged.stderr)
    return temporary_directory, repository


def validate(repository: Path, write_manifest: bool = False) -> subprocess.CompletedProcess[str]:
    command = [sys.executable, "scripts/validate_content.py"]
    if write_manifest:
        command.append("--write-manifest")
    return run(command, repository)


def require_success(result: subprocess.CompletedProcess[str], label: str) -> None:
    if result.returncode != 0:
        raise AssertionError(f"{label} unexpectedly failed:\n{result.stdout}{result.stderr}")


def require_failure(result: subprocess.CompletedProcess[str], expected: str, label: str) -> None:
    output = result.stdout + result.stderr
    if result.returncode == 0:
        raise AssertionError(f"{label} unexpectedly passed")
    if expected not in output:
        raise AssertionError(f"{label} failed without expected diagnostic {expected!r}:\n{output}")


def test_missing_research_note_experiment() -> None:
    temporary_directory, repository = temporary_repository()
    try:
        require_success(validate(repository), "baseline copy")
        note = repository / "research/cycles/cycle-17/research-note.md"
        text = note.read_text(encoding="utf-8")
        if "EXP-C17-03" not in text:
            raise AssertionError("Cycle 17 fixture no longer contains EXP-C17-03")
        note.write_text(text.replace("EXP-C17-03", "OMITTED-C17-03"), encoding="utf-8")
        require_failure(
            validate(repository, write_manifest=True),
            "experiments: Cycle 17 Research Note IDs differ from baseline",
            "missing Research Note Experiment ID",
        )
    finally:
        temporary_directory.cleanup()


def test_support_assessment_before_execution() -> None:
    temporary_directory, repository = temporary_repository()
    try:
        require_success(validate(repository), "baseline copy")
        assessment = repository / "research/support-assessments/UNAUTHORIZED.md"
        assessment.write_text("# Unauthorized Support Assessment\n", encoding="utf-8")
        require_failure(
            validate(repository, write_manifest=True),
            "state: research/support-assessments contains an unauthorized assessment artifact",
            "Support Assessment before research execution",
        )
    finally:
        temporary_directory.cleanup()


def main() -> int:
    test_missing_research_note_experiment()
    test_support_assessment_before_execution()
    print("Content validation regression tests: 2 passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
