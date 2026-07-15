# Harness Engineering Research Program · Codex Instructions

## Current repository state

This repository is currently at:

* Program version: V4.2
* Current structure: 18 Cycle-based research cycles
* Frozen baseline: Batch 0 common protocol
* Completed content baseline: Batch 1–5, covering Cycle 1–8
* Current task: Generate Batch 6 only, covering Cycle 9

This task starts from the merged V4.2 Batch 5 baseline. V4.1 Week 7 remains the historical migration source for Cycle 9.

Do not apply or reproduce an existing external ZIP or patch. Generate Batch 6 by reading the repository, preserving the frozen Batch 0 protocol and completed Batch 1–5 decisions except where the repository owner explicitly changes them, and migrating the V4.1 Cross-host Harness Abstraction content directly.

## Required reading

Before proposing or making changes, read:

1. `README.md`
2. `CHANGELOG.md`
3. `docs/00-研究计划总纲.md`
4. `docs/01-Agent与Harness基础认知.md`
5. `docs/02-Coding-Agent-Host-Model.md`
6. `docs/03-Cross-host-Harness-Abstraction.md`
7. `docs/04-Harness-Engineering-Research-Themes.md`
8. `docs/05-myharness-Integration-Research.md`
9. `docs/06-Research-Infrastructure.md`
10. `docs/07-Reference-Project-Atlas.md`
11. `docs/08-V4.2-Batch0-Protocol.md`
12. `docs/09-V4.2-Glossary.md`
13. `research/README.md`
14. `research/task-suite.md`
15. `research/source-authority.md`
16. `research/support-levels.md`
17. all existing files under `research/templates/`

## V4.2 program decision

V4.2 contains 18 research Cycles rather than 16 Weeks.

The Cycle names and order are frozen:

1. Coding Agent 最小模型
2. Harness Primitive
3. Claude Code Context Lifecycle
4. Claude Code Extension & Control Surface
5. Codex Architecture & Customization
6. Codex Execution、Safety & State
7. ZCode Host Contract & Enterprise Reality
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
* ZCode: domestic model ecosystem and enterprise reality reference
* OpenCode: open-source, multi-provider, vendor-neutral Host reference

## ZCode evidence boundary

ZCode must be studied through:

* Official Contract
* Official product documentation
* Official release information
* Direct Behavior Evidence
* Local configuration
* Enterprise deployment facts

Do not create ZCode source-code architecture conclusions unless an official and verified Runtime source repository is identified.

Community reverse engineering, unofficial repositories, client fingerprints, and third-party patches may only create Open Questions. They cannot prove an official Contract or Architecture.

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
5. ZCode Source Authority Gate
6. Stable task suite T01–T03
7. Experiment run metadata
8. Host support levels S0–S4
9. Research workspace naming based on Cycle rather than Week
10. Migration boundary from V4.1 to V4.2

## Current Batch 6 scope

Batch 6 generates the Four-host Harness Abstraction content only:

1. Cycle 9 · Four-host Harness Abstraction
2. Cycle 9 Research Note in planned, not-executed state
3. Portable Semantic Contract、Host Adapter、Host-specific Capability and explicit degradation research boundaries
4. Planned Cross-host Source Registry entries with explicit authority and floating-anchor boundaries
5. Reuse of Cycle 3–8 Host sources without upgrading Source IDs into Evidence Claims
6. Experiment designs using `EXP-Cxx-yy` and T01–T03 without creating results
7. Cycle 9 workspace directories required for later implementation
8. V4.1 Week 7 / `EXP-W07-01` historical migration mapping
9. Explicit separation of Host、surface、Provider、endpoint / protocol、Model and Configuration effects

Workspace directories for the Cycles in the current content Batch may be prepared before experiment execution. For Batch 6, add only `cycle-09` with the planned `research-note.md`, `experiments/`, and `evidence/` structure. Do not create Cycle 10–18 directories.

Batch 6 content generation does not mean that experiments were run, Portable Semantic Contracts or Host Adapters were validated, Evidence Claims were established, four-host portability was proven, or Support Levels were achieved.

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

* repository commit
* Host and Host version
* Provider and endpoint type
* Model ID
* configuration snapshot
* Rule revision
* Skill revision
* Check revision
* Adapter revision
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

Existing `EXP-Wxx-yy` references remain historical until their corresponding content Batch is migrated.

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

The following files are the existing Batch 0 baseline, not the current Batch 6 generation target.

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

## Explicit non-goals

Do not:

* generate Cycle 10–18正文;
* implement Batch 7;
* claim that planned Batch 1, Batch 2, Batch 3, Batch 4, Batch 5 or Batch 6 experiments have been executed;
* create Run records, `EVD-*` conclusions, `ENT-*` facts, or Support Assessments before real execution;
* rewrite all V4.1 content files;
* create Cycle 10–18 directories;
* implement myharness features;
* implement or merge a complete myharness Host Adapter;
* implement an OpenCode Adapter or Plugin;
* promise a complete ZCode Plugin;
* add a fifth primary Host;
* create legal compliance conclusions;
* invent official project facts or source paths;
* commit or push unless explicitly instructed.

## Editing discipline

* Preserve useful V4.1 content as migration baseline.
* Clearly label V4.1 content that remains pending migration.
* Use native Markdown.
* Do not add trailing whitespace.
* Keep internal links valid.
* Do not silently redefine frozen terminology.
* Record unresolved contradictions as Open Questions.

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
git diff --check
git status --short
```

Also validate:

* all internal relative links;
* all 18 Cycle names appear in the V4.2 overview;
* Cycle 1–9正文 exists and Cycle 10–18正文 has not been generated;
* only `research/cycles/cycle-01` through `research/cycles/cycle-09` exist;
* Cycle 9 workspace directory contains `research-note.md`, `experiments/`, and `evidence/` preparation;
* Source anchors without a pinned commit are labeled as floating anchors to be verified at execution time;
* ZCode source conclusions were not invented;
* Host、surface、Provider、endpoint / protocol、Model and Configuration effects remain separated;
* Batch 6 files do not claim that a Portable Semantic Contract, Host Adapter, four-host portability or any S1–S4 result has been validated;
* all changed Markdown files have no trailing whitespace.

Do not commit or push.
