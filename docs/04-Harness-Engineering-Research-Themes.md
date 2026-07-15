# PART V · Harness Engineering Research Themes

> V4.2 Batch 7 · Cycle 10–14 正文迁移。状态：`PLANNED · NOT EXECUTED`。

[← 上一卷](03-Cross-host-Harness-Abstraction.md) · [返回总览](../README.md) · [下一卷 →](05-myharness-Integration-Research.md)

---

## Batch 7 研究边界

Batch 7 把 V4.1 Week 8–12 迁移为五个 Cycle，研究 Skill 行为、Change 收敛、自适应工作流、上下文交接与知识固化。生成正文和工作区不表示实验已经执行，也不表示任何设计已经进入 myharness。

共同边界：

- 新实验使用 `EXP-Cxx-yy` 与稳定任务套件 T01–T03；V4.1 `EXP-Wxx-yy` 只保留历史映射。
- Source Registry 只登记计划来源；`SRC-*` 不是 `EVD-*`，默认分支锚点必须在执行时固定完整 commit。
- Host、surface、Provider、endpoint / protocol、Model 与 Configuration 效应分别记录；不同条件的结果不得汇总成 Host 或 Model 排名。
- Skill 被发现、被激活、步骤被执行、产出通过验收与任务成功是不同事件。
- Artifact 存在、流程完成、事实一致与结果正确是不同命题。
- 本 Batch 不创建 Run、`EVD-*`、`ENT-*`、Support Assessment、ADR 或 Route Review，不实现 Cycle 15–18。

## Cycle 10 · Skill Behavior & Evaluation

> 历史来源：V4.1 Week 8 · `EXP-W08-01`

### 核心研究问题

> 什么样的 Skill 能在绑定 Host、Model 与任务条件下改变可观察行为，而不只是改善描述或写作质量？

### 责任模型

```text
Discovery → Activation → Execution → Evidence → Outcome
    │           │            │           │          │
description   Host route   procedure   verifier   acceptance
```

五个阶段必须分别观测。Description 只直接控制候选发现信号；Skill 正文不能独立证明自身已被遵循，确定性约束仍需要外部 Check / Test。

### 计划来源

| 来源 | 研究角色 | 当前边界 |
|---|---|---|
| Agent Skills · Optimizing skill descriptions | Discovery / trigger 评测 Contract | 官方浮动页面；不证明任一 Host 的实际触发行为 |
| Agent Skills · Evaluating skill output quality | testcase、grader、baseline / variant 方法 | 官方 guidance；不产生本项目结果 |
| obra/superpowers | Behavior-contract 与 verification 参考实现 | 默认分支浮动；只解释固定 revision 的项目设计 |
| learn-claude-code | Skill loading 教学对照 | 不是 Claude Code 官方源码 |

来源条目见 [Cycle 10 Research Note](../research/cycles/cycle-10/research-note.md)。

### 假设与实验

`H-C10-01 · Description Discovery`：在同一 Host / surface、Provider、Model、Configuration 和 T02-shaped query corpus 下，V1→V2 只改变 name / description / applicability，可以方向性改变 Discovery / Activation 的正确路由。

`H-C10-02 · Activated Behavior Contract`：在 Skill 已显式加载、name / description 相同的条件下，V2→V3 只改变 Trigger、Preconditions、Required Context、Procedure、Evidence Required、Completion Criteria 与 Failure Route bundle，可以方向性改变 Execution / Evidence。

V4.1 `EXP-W08-01` 拆分为两个独立 `T02 · Semantic Review` 实验：

1. `EXP-C10-01` · Skill Discovery and Activation：24 个 T02-shaped packets 按 label 分层为 train / validation；V1 / V2 在 12 个 validation packets 上各做 3 次 fresh-session Run，只解释 description bundle。
2. `EXP-C10-02` · Activated Skill Behavior Contract：显式加载相同 Skill identity，对 3 个固定 T02 instances 的 V2 / V3 各做 3 次 Run，只解释 behavior-contract bundle。

主要观测为漏触发、误触发、步骤遵循、证据可追溯性、确定性缺陷检出、语义缺陷检出、false completion、Context cost 与 Human intervention。小样本只形成绑定条件下的方向性结果。

### 退出条件

- 冻结 Skill revisions、query split、T02 oracle、grader 与裁决阈值。
- 分开报告 Discovery、Activation、Execution、Evidence 与 Outcome。
- 完成 `EXP-C10-01` 的 72 个 validation Run 与 `EXP-C10-02` 的 18 个 activated Run，且结果绑定完整 Run Metadata；Run 缺失时保持 `INCONCLUSIVE`。
- 形成 Mental Model V1；不因 Skill 有效就推导跨 Host portability 或 S1–S4。

完整计划见 [Cycle 10 实验工作区](../research/cycles/cycle-10/experiments/README.md)。

## Cycle 11 · Change Contract & Convergence

> 历史来源：V4.1 Week 9 · `EXP-W09-01`

### 核心研究问题

> Change Artifact 如何在执行中保持约束，并在关闭后可复查地反映 Spec、Task、Code、Test、CI 与 Summary 的真实关系？

### Change Truth Model V0

```text
Requirement ↔ Task ↔ Diff / File / Symbol ↔ Test ↔ CI ↔ Summary
       semantic edges                deterministic edges
```

Artifact 存在不等于完整，完整不等于内部一致，内部一致不等于与代码或结果一致。确定性关系和语义判断必须分开，人工 truth map 是 evaluator reference，不是一个可与 Agent 回合并列的实验 variant。

### 计划来源

| 来源 | 研究角色 | 当前边界 |
|---|---|---|
| GitHub Spec Kit | Spec → Plan → Tasks → Implement 与 cross-artifact analysis 参考 | 官方文档 Contract 与源码仓库分开登记；旧命令名不作 Contract，源码执行时固定 commit |
| Fission-AI/OpenSpec | 可演进 Change artifacts 与 schema 参考 | 默认分支浮动；不证明 myharness Change truth |
| myharness historical Changes | Project Evidence 候选 | 执行时固定 commit；目录存在不等于状态真实 |

### 假设与实验

`H-C11-01 · Explicit Convergence Contract`：对一个冻结的历史 Change 与同一 T02 oracle，相比不给结构的 Agent review，显式 Convergence Checklist 会提高已知 drift edge 的召回和引用可追溯性，同时可能增加误报、Context 与审查时间。

`EXP-C11-01` 使用 `T02 · Semantic Review`：

- Round A：两名人工评审者先建立并裁决 truth map，只作为 evaluator-only oracle。
- Round B：Agent 在不知道 oracle 的情况下做无结构收敛检查。
- Round C：同一绑定条件下，Agent 使用冻结的 Convergence Checklist；fresh session、相同可见输入、顺序交错。
- 可选 CodeGraph 只能作为独立 exploratory stratum，不能混入 B / C 主裁决。

主要指标按 drift taxonomy 分层报告 recall、false positive、evidence citation、semantic / deterministic classification、false completion 与 Human intervention。不得因 Checklist 文件存在就宣称 Change 已收敛。

### 退出条件

- 固定历史 Change commit、artifact packet、oracle、drift taxonomy 与评分规则。
- 把确定性 defect 与语义 defect 分开裁决。
- 完成 3 个 B / C paired blocks（共 6 个 Agent Run）并保存 Run Metadata；人工 Round A 不计 Agent run。
- 明确 Convergence 应由 Skill、Check、Hook、CLI 还是 Acceptance 承担；不在本 Cycle 实现功能。

完整计划见 [Cycle 11 实验工作区](../research/cycles/cycle-11/experiments/README.md)。

## Cycle 12 · Adaptive Workflow

> 历史来源：V4.1 Week 10 · `EXP-W10-01`

### 核心研究问题

> 如何让 workflow depth 随任务风险变化，同时避免把“自适应”退化为 Agent 自行省略 Gate？

### Risk-routing Model V0

```text
Task facts → deterministic preflight → risk classification
                                      ↓
                    required artifacts / gates / escalation
                                      ↓
                              acceptance + audit
```

Task complexity、delivery risk 与 ceremony cost 分开。Workflow route 由冻结 rubric 选择；Mandatory Gate、未知项升级与 Human checkpoint 不能由执行中的 Agent 静默取消。

### 计划来源

| 来源 | 研究角色 | 当前边界 |
|---|---|---|
| BMAD Method | 多 planning track 与阶段化 workflow 参考 | 官方文档 Contract 与源码仓库分开登记；不直接复制 track 名或 story count |
| OpenSpec | artifact-driven、可演进 workflow 对照 | 复用 Cycle 11 来源；不等于无 Gate |
| myharness 10 Stage | Project Evidence 候选 | 执行时固定 revision；流程存在不证明每一步有价值 |

### 假设与实验

`H-C12-01 · Risk-routed Workflow`：对一个低风险 T01 documentation task 与两个 T03 medium-change tasks，相比完整十阶段 baseline，由执行前冻结的 risk rubric 选择 required artifacts、mandatory gates 与 escalation 的 variant，能减少 ceremony / Context cost，而不增加 escaped risk、rework 或 false completion。

- `EXP-C12-01`：`T01 · Engineering Constraint`，使用同一个小型 README / documentation task instance 比较完整 workflow 与 risk route。
- `EXP-C12-02`：`T03 · Medium Change`，分别使用同一个 Hook bug instance 与同一个受控 Plugin / architecture instance 做 A / B 比较。
- 每个 instance 的 A / B 各执行 3 个 fresh-session Run、组成 3 个 paired blocks；禁止用“acceptance-equivalent matched task”替代同一 task instance。

主要指标是 escaped critical risk、acceptance failure、rework 与 false completion；流程时间、artifact 数量、Context 与 Human checkpoints 是 secondary trade-off。若 task parity、risk label 或 Host / Model 条件无法固定，结果必须为 `INCONCLUSIVE`。

### 退出条件

- 冻结 risk dimensions、route table、mandatory gates、escalation、task instance 与 baseline。
- 在看到结果前指定 primary risk 与 secondary cost 指标。
- 每个 task stratum 独立报告，不能把不同难度汇总为统一 workflow 胜率。
- 形成是否值得进入 Cycle 16 Hypothesis / ADR Candidate 的问题；不在本 Cycle 修改 myharness 10 Stage。

完整计划见 [Cycle 12 实验工作区](../research/cycles/cycle-12/experiments/README.md)。

## Cycle 13 · Context Lifecycle & Session Handoff

> 历史来源：V4.1 Week 11 · `EXP-W11-01`

### 核心研究问题

> 多 Session 的任务如何保留目标、决定、证据、未完成状态与失败路线，而不携带全部历史噪声？

### Handoff Model V0

```text
live context ──ratify──> durable handoff artifact ──hydrate──> next session
     │                         │                         │
trajectory noise       goal / decisions / evidence    verify freshness
```

Host 的 resume / compaction 是 session capability；结构化 handoff 是 Project artifact；Changes 是 task-state artifact。三者可以组合，但不能因都“保存上下文”就视为等价。

### 计划来源

| 来源 | 研究角色 | 当前边界 |
|---|---|---|
| HumanLayer Advanced Context Engineering | intentional compaction 与 research / plan / implement 方法参考 | Community Reference；不证明 Host Contract 或普遍效果 |
| snarktank/ralph | fresh-context + persistent PRD / progress artifact 对照 | 固定 revision 后只解释该项目 |
| Cycle 3–6 Host sources | Claude Code / Codex session Contract 候选 | 复用 Source ID，不提升为 Evidence；不假设 surface parity |

### 假设与实验

`H-C13-01 · Structured Handoff Observability`：对一个连续 T03 task，结构化交接字段能暴露目标、已作决定、证据、当前状态、未完成项、风险与恢复动作的遗漏位置；但单个任务在不同 transition 使用不同 mode 时，只能形成 exploratory observation，不能裁决哪种 handoff mode 更优。

`EXP-C13-01` 使用 `T03 · Medium Change`，将同一任务分为 Intake / Scope → Research → Plan → Implement → Review 五个 phase。四个 transition 预先分别绑定 Host Resume、fresh-session prose summary、fresh-session structured handoff 与 fresh-session Changes artifact，并记录 hydration 时的遗漏、冲突、过期信息、恢复时间、重复工作、Human correction 与 evidence trace。Resume 恢复同一 Host session identity；其余 mode 创建新 session。分配顺序在运行前冻结。

该设计不做 mode superiority claim；若后续需要比较，必须另建匹配任务、平衡顺序和 fresh-session 的 comparative experiment。

### 退出条件

- 固定 phase boundary、handoff schema、transition assignment 与 observation rubric。
- 每个 transition 绑定 Host / surface / Provider / Model / Configuration 与 session capability。
- 区分 Host resume、summary artifact、Change state 与永久 Project Knowledge。
- 只形成 exploratory Mental Model V1；不将单一任务结果写成普遍最佳实践。

完整计划见 [Cycle 13 实验工作区](../research/cycles/cycle-13/experiments/README.md)。

## Cycle 14 · Knowledge Ratification & Harness Minimalism

> 历史来源：V4.1 Week 12 · `EXP-W12-01`

### 核心研究问题

> Agent 发现的事实何时值得固化为 Rule、Skill、Hook、Test、Wiki 或 Change template，何时应选择 Nothing？

### Ratification Model V0

```text
observation → authority / recurrence / scope / determinism check
            → value − context cost − maintenance − portability risk
            → Rule | Skill | Hook | Test | Wiki | Change Template | Nothing
```

严重但一次性的事件不自动成为永久 Rule；可确定验证的约束优先进入 Test / Check；复杂行为指导才可能进入 Skill。“Nothing”是有效结论，不是遗漏。

### 计划来源

| 来源 | 研究角色 | 当前边界 |
|---|---|---|
| buildermethods/agent-os | Discover / deploy / index standards 的项目参考 | 默认分支浮动；不证明标准准确或维护成本可接受 |
| SWE-agent/mini-swe-agent | minimal scaffold 对照 | 只解释固定 revision；不以 benchmark 排名裁决 minimalism |
| SWE-agent ACI paper | interface-design 理论背景 | 按 OQ-003 保守登记；不证明 Host implementation 或 myharness 决策 |
| myharness failure / improvement records | Project Evidence 候选 | 只有固定 artifact、revision 与 authority 后才能用于实验 |

### 假设与实验

`H-C14-01 · Evidence-gated Ratification`：对冻结的十个历史 failure / improvement packets，显式 authority、recurrence、scope、determinism、expected value、Context cost、maintenance 与 portability rubric，能使候选治理位置及 `Nothing` 决策更可复查；它不能仅凭 retrospective classification 证明未来缺陷会减少。

`EXP-C14-01` 使用 `T02 · Semantic Review`。十个正式 packet 必须各自包含有限 Change / diff、一个语义问题和一个 deterministic check；不满足 T02 Contract 的历史记录进入 exclusion log。每个 packet 执行两个相同绑定条件下的 independent Agent reviewer Run；两名人工 evaluator 预先建立允许 disagreement 的 evaluator-only reference，不计 Agent Run。Agent reviewer 分类 One-off / Recurring、Host / Model / Project Knowledge / Process / Deterministic Constraint，再选择目标治理位置并给出引用。

主要观察为 authority gap、分类一致性、unsupported ratification、deterministic-to-semantic mismatch、重复 / 冲突规则、Context / maintenance cost 与 `Nothing` 的理由质量。

### 退出条件

- 固定十个 packet、采样时间窗、ratification rubric 与 evaluator-only reference。
- 每个候选都记录 authority、scope、owner、revalidation trigger 与 removal condition。
- 不把一次 retrospective review 写成 future reliability 或 Harness minimality 证明。
- 只形成进入 Cycle 15 audit / Cycle 16 Hypothesis 的候选，不直接修改 myharness。

完整计划见 [Cycle 14 实验工作区](../research/cycles/cycle-14/experiments/README.md)。

## V4.1 历史迁移映射

| V4.1 | V4.2 | 新实验 | 状态 |
|---|---|---|---|
| Week 8 · Skill Behavior & Evaluation | Cycle 10 | `EXP-W08-01` → `EXP-C10-01` + `EXP-C10-02` | `PLANNED · NOT EXECUTED` |
| Week 9 · Change Contract & Convergence | Cycle 11 | `EXP-W09-01` → `EXP-C11-01` | `PLANNED · NOT EXECUTED` |
| Week 10 · Adaptive Workflow | Cycle 12 | `EXP-W10-01` → `EXP-C12-01` + `EXP-C12-02` | `PLANNED · NOT EXECUTED` |
| Week 11 · Context Lifecycle & Session Handoff | Cycle 13 | `EXP-W11-01` → `EXP-C13-01` | `PLANNED · NOT EXECUTED` |
| Week 12 · Knowledge Ratification & Harness Minimalism | Cycle 14 | `EXP-W12-01` → `EXP-C14-01` | `PLANNED · NOT EXECUTED` |

历史 ID 只表示研究意图的迁移关系，不表示旧实验已执行，也不能与新 ID 同时创建两份结果。

## Batch 7 完成边界

Batch 7 完成仅表示 Cycle 10–14 的正文、计划实验、来源登记与工作区已准备。Cycle 15–18 正文、目录、实验与结论属于 Batch 8；任何 Route Review、ADR Candidate、实现、Run、Evidence Claim 或 Support Level 都需要后续真实研究。
