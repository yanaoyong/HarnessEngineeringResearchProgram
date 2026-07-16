# Harness Engineering Research Program · Codex Instructions

## Current repository state

This repository is currently at:

* Program version: V4.3
* Current structure: 18 Cycle-based research cycles
* Frozen baseline: V4.2 Batch 0 common protocol plus the V4.3 Qwen Code Host-set Amendment
* Completed content baseline: Batch 1–8, covering Cycle 1–18
* Current default state: Batch 1–8 content generation is complete; no content Batch or research execution is active

The repository is based on the merged V4.2 Batch 8 baseline plus the owner-approved V4.3 replacement of ZCode with Qwen Code. V4.1 Week 1–16 have been migrated and remain historical mapping sources only.

Do not regenerate a completed content Batch or apply an external ZIP or patch as a substitute for repository review. Preserve the V4.2 Batch 0 protocol as amended by `docs/10-V4.3-Qwen-Code-Host-Amendment.md` and the completed Batch 1–8 decisions except where the repository owner explicitly authorizes a recorded correction or a later research-execution artifact.

## Required reading

Before proposing or making changes, read:

1. `README.md`
2. `CONTRIBUTING.md`
3. `GOVERNANCE.md`
4. `CHANGELOG.md`
5. `docs/README.md`
6. `docs/00-研究计划总纲.md`
7. `docs/01-Agent与Harness基础认知.md`
8. `docs/02-Coding-Agent-Host-Model.md`
9. `docs/03-Cross-host-Harness-Abstraction.md`
10. `docs/04-Harness-Engineering-Research-Themes.md`
11. `docs/05-myharness-Integration-Research.md`
12. `docs/06-Research-Infrastructure.md`
13. `docs/07-Reference-Project-Atlas.md`
14. `docs/08-V4.2-Batch0-Protocol.md`
15. `docs/09-V4.2-Glossary.md`
16. `docs/10-V4.3-Qwen-Code-Host-Amendment.md`
17. `research/README.md`
18. `research/task-suite.md`
19. `research/source-authority.md`
20. `research/support-levels.md`
21. all existing files under `research/templates/`

## V4.3 program decision

V4.3 retains the 18 research Cycles introduced by V4.2 and replaces only the ZCode primary Host with Qwen Code.

The Cycle names and order are frozen:

1. Coding Agent 最小模型
2. Harness Primitive
3. Claude Code Context Lifecycle
4. Claude Code Extension & Control Surface
5. Codex Architecture & Customization
6. Codex Execution、Safety & State
7. Qwen Code Host Architecture & Enterprise Reality
8. OpenCode Host Architecture & Model Portability
9. Four-host Harness Abstraction
10. Skill Behavior & Evaluation
11. Change Contract & Convergence
12. Adaptive Workflow
13. Context Lifecycle & Session Handoff
14. Knowledge Ratification & Harness Minimalism
15. Read-only Architecture Audit
16. Hypothesis & ADR Candidate
17. Minimal Implementation Experiment
18. Acceptance、Ablation & Design Beliefs

## Four-host research roles

* Claude Code: mature Harness best-practice reference
* Codex: advanced open-source implementation reference
* Qwen Code: domestic open-source coding-agent, Qwen ecosystem, and enterprise deployment reality reference
* OpenCode: open-source, multi-provider, vendor-neutral Host reference

## Qwen Code evidence boundary

Qwen Code may be studied through:

* Official Contract
* Official product documentation
* Verified Official Source
* Official release information
* Direct Behavior Evidence
* Local configuration
* Enterprise deployment facts

`QwenLM/qwen-code` is the verified official source repository, but Source Evidence still requires a pinned full commit, bounded source paths, and artifact-to-source provenance for any Behavior agreement claim. A floating default branch, package version, compatible protocol, or selectable Model cannot by itself prove deployed architecture or portability.

## OpenCode evidence boundary

OpenCode may use:

* Official Contract
* Official Source
* Direct Behavior
* Project Evidence

Host effects must be separated from Provider and Model effects.

## Frozen Batch 0 baseline

Batch 0 froze the common protocol used by Batch 1 and later content Batches.

It must define:

1. Cycle 1–18 names and phases
2. Batch 1–8 boundaries
3. Common terminology
4. Evidence classification
5. Qwen Code Official Source Verification and artifact-to-source provenance
6. Stable task suite T01–T03
7. Experiment run metadata
8. Host support levels S0–S4
9. Research workspace naming based on Cycle rather than Week
10. Migration boundary from V4.1 to V4.2 and the V4.3 Host-set amendment

## Completed Batch 8 scope

Batch 8 generated the myharness Integration Research content only:

1. Cycle 15 · Read-only Architecture Audit
2. Cycle 16 · Hypothesis & ADR Candidate
3. Cycle 17 · Minimal Implementation Experiment
4. Cycle 18 · Acceptance、Ablation & Design Beliefs
5. Cycle 15–18 Research Notes in planned, not-executed state
6. Evidence preparation boundaries without creating new Source or Evidence Claims
7. Reuse of earlier Cycle sources without upgrading Source IDs into Evidence Claims
8. Experiment designs using `EXP-Cxx-yy` and T01–T03 without creating results
9. V4.1 Week 13–16 / `EXP-W13-01` through `EXP-W16-01` historical migration mappings
10. Explicit separation of Host、surface、Provider、endpoint / protocol、Model and Configuration effects
11. Explicit separation of Finding、Hypothesis、ADR Candidate、implementation、acceptance result and Design Belief

Batch 8 prepared only `cycle-15` through `cycle-18` with planned `research-note.md`, `experiments/`, and `evidence/` structure. All Cycle 1–18 workspaces now exist; do not create Cycle 19 or later directories without a new program decision.

Batch 8 content generation does not mean that an audit was run, Findings or ADR Candidates were created, an implementation was built or merged, experiments or ablations were executed, Design Beliefs were ratified, Evidence Claims were established, or Support Levels were achieved.

## Batch 0 required terminology

Define and distinguish:

* Agent
* Coding Agent Host
* Harness
* Model
* Provider
* Configuration
* Tool
* Instruction
* Rule
* Skill
* Hook
* Plugin
* Portable Semantic Contract
* Host Adapter
* Provider Profile
* Provider-dependent Behavior
* Host-specific Capability
* Unsupported / Unknown
* Contract Evidence
* Source Evidence
* Behavior Evidence
* Project Evidence
* Enterprise Fact
* Community Claim
* Mental Model
* Hypothesis
* Exit Criteria
* Route Review
* Support Level

## Stable task suite

Batch 0 must define:

* `T01 · Engineering Constraint`
* `T02 · Semantic Review`
* `T03 · Medium Change`

The task suite is for directional comparison, not public model benchmarking.

## Experiment metadata

Experiment records must separate:

* Program version, base protocol schema, Research Program commit, and applied amendments
* repository commit
* Host and Host version
* Provider and endpoint type
* Model ID
* configuration snapshot
* Rule revision
* Skill revision
* Check revision
* Adapter revision
* Harness-under-test cell and revision, when separate from the task fixture
* implementation artifact IDs, when applicable
* controlled variables
* known confounders
* evidence
* human intervention

New experiment IDs use:

```text
EXP-C01-01
EXP-C08-02
EXP-C18-01
```

All corresponding content Batches have been migrated. Existing `EXP-Wxx-yy` references remain historical mapping IDs and must not be reused for new research artifacts.

## Host support levels

Define:

* S0 · Not Assessed
* S1 · Contract Mapped
* S2 · Behavior Verified
* S3 · Operationally Verified
* S4 · Enterprise Profile Verified

Required distinctions:

* S1 does not mean full support.
* S2 does not mean production ready.
* S4 does not mean universal legal compliance.
* Every support result must bind Host version, Provider profile, model, evidence IDs, known limitations, and verification date.

## Frozen Batch 0 outputs

The following files are the historical Batch 0 output set. The repository currently has no active content-generation Batch.

Expected new files:

```text
docs/08-V4.2-Batch0-Protocol.md
docs/09-V4.2-Glossary.md

research/task-suite.md
research/source-authority.md
research/support-levels.md

research/templates/run-metadata.template.yaml
research/templates/source-registry.template.md
research/templates/host-profile.template.md
research/templates/provider-profile.template.md
research/templates/enterprise-readiness-fact-sheet.template.md
```

Expected updated files:

```text
README.md
CHANGELOG.md
MANIFEST.txt
docs/00-研究计划总纲.md
docs/06-Research-Infrastructure.md
research/README.md
research/cycles/README.md
research/open-questions.md
research/templates/research-note.template.md
research/templates/experiment-record.template.md
```

The final file list may vary only when justified by the existing repository structure.

V4.3 later added `docs/10-V4.3-Qwen-Code-Host-Amendment.md`; it is not a Batch 0 output.

## Explicit non-goals

Do not:

* change the frozen Cycle 1–18 names, order or Batch boundaries;
* claim that planned Batch 1 through Batch 8 experiments have been executed;
* create Run records, `EVD-*` conclusions, `ENT-*` facts, or Support Assessments before real execution;
* create actual architecture Findings, ADR Candidates, implementation artifacts, Decision Updates, Design Beliefs or Route Review results during content generation;
* create Cycle 19 or later directories;
* rewrite all V4.1 historical material outside an explicitly authorized maintenance or research-execution scope;
* implement myharness features;
* implement or merge a complete myharness Host Adapter;
* implement an OpenCode Adapter or Plugin;
* promise or implement a complete Qwen Code Adapter;
* add a fifth primary Host;
* create legal compliance conclusions;
* invent official project facts or source paths;
* commit or push unless explicitly instructed.

## Editing discipline

* Preserve useful V4.1 content as migration baseline.
* Clearly label retained V4.1 content as historical mapping material; Week 1–16 content migration is complete.
* Use native Markdown.
* Do not add trailing whitespace.
* Keep internal links valid.
* Do not silently redefine frozen terminology.
* Record unresolved contradictions as Open Questions.

## Public repository governance

* Route content defects and research execution proposals through the structured Issue Forms when creating GitHub Issues.
* Treat security, credential, workflow injection and privacy reports as private; follow `SECURITY.md` and never ask reporters to post secrets publicly.
* Repository owner approval is required for governance, protocol, execution-authority and license changes.
* The repository currently has no project-level `LICENSE`. Do not add or infer a license without an explicit owner decision.
* `CODEOWNERS` requests review but does not prove that branch protection or a ruleset is enabled.
* Keep `CONTRIBUTING.md`, `GOVERNANCE.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, navigation and GitHub templates aligned with the effective V4.3 protocol.

## 语言与双语术语（Language and Bilingual Terminology）

* 中文是推荐的默认表达语言，不是强制要求。文档正文、解释、标题、表格标签、状态描述和研究结论在中文能够自然、准确表达时，优先使用中文。
* 当英文更准确、更符合官方命名、行业惯例、技术语境或互操作要求时，应当使用英文，不得为了形式上的中文化牺牲准确性和可复查性。
* 官方术语、规范概念、模式字段、状态或来源标题需要使用英文时，在有助于中文读者理解且不会造成冗余的位置提供中英文对照，例如 `心智模型（Mental Model）`、`退出条件（Exit Criteria）`。无需对代码、命令、路径和重复出现的同一术语机械添加中文。
* 翻译会改变或模糊含义时，必须原样保留规范英文标识符和字面量，包括文件路径、命令、代码、应用程序接口（API）名称、配置键、模式字段、`EXP-C01-01`、`EVD-*` 等 ID，以及冻结的专有名称。
* 同一术语首次提供中英文对照后，后续应一致使用已经确立的中文译名。优先使用 `docs/09-V4.2-Glossary.md` 已冻结的译名，不得静默引入相互竞争的翻译。
* 表格或模板因互操作性必须保留英文字段名时，应补充中文说明或双语标签，不得删除规范英文名称。
* 引用英文来源时，应保留官方标题，并在需要时提供中文说明或摘要。不得使用可能被误认为官方标题或逐字引文的自行翻译文本。
* 不得仅为执行本语言规范而重写保留的 V4.1 历史正文。应在对应内容 Batch 迁移时，或文件因其他原因进入当前范围时应用本规范。

## Required validation

Before reporting completion, run:

```bash
python3 scripts/validate_content.py
python3 scripts/test_content_validation.py
git diff --check
git status --short
```

`validation/content-baseline.json` 是当前 V4.3 内容完整性基线。只有在 repository owner 明确批准 Cycle、Batch、Source Registry、Experiment plan 或执行状态变化时，才更新该文件。内容文件清单或字节数发生预期变化后，运行 `python3 scripts/validate_content.py --write-manifest`，并审查 `MANIFEST.txt` diff；不得只为消除 CI 失败而放宽基线。

Also validate:

* all internal relative links;
* all 18 Cycle names appear in the V4.3 overview;
* Cycle 1–18正文 exists and remains planned, not executed;
* only `research/cycles/cycle-01` through `research/cycles/cycle-18` exist;
* Cycle 15–18 workspace directories contain `research-note.md`, `experiments/`, and `evidence/` preparation;
* Source anchors without a pinned commit are labeled as floating anchors to be verified at execution time;
* no revision-bound Qwen Code Source claim exists unless it is pinned to a verified official revision and supported by the required artifact provenance;
* Host、surface、Provider、endpoint / protocol、Model and Configuration effects remain separated;
* Batch 8 files do not claim that an audit, Finding, ADR Candidate, implementation, acceptance result, Design Belief, Route Review or any S1–S4 result has been completed or validated;
* `research/support-assessments/` contains only its README while `research_execution` is `NOT_STARTED`;
* all changed Markdown files have no trailing whitespace.
