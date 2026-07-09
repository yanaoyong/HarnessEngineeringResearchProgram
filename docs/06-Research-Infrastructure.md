# PART VII · Research Infrastructure

> 贯穿全程使用的 Research Note、Evidence Model、Experiment Record、ADR Candidate、Open Questions、Route Review 与 Design Beliefs 模板。

[← 上一卷](05-myharness-Integration-Research.md) · [返回总览](../README.md) · [下一卷 →](07-Reference-Project-Atlas.md)

---

## 1. 统一 Research Note 模板

每个 Week 建议使用同一结构。重点不是篇幅，而是必须能看见：

```text
Mental Model V0
        ↓
Source / Behavior / Project Evidence
        ↓
Hypothesis
        ↓
Experiment
        ↓
Mental Model V1
        ↓
Design Judgment
```

模板：

```markdown
# Week XX Research Note

## 1. Research Question

我真正想回答什么？

## 2. Why It Matters to myharness

为什么这个问题与我的项目有关？

## 3. Mental Model V0

学习前，我认为机制是什么？

## 4. Source Evidence

从官方资料、规范或源码看到了什么？

## 5. Reference Pattern

优秀项目怎么解决？它解决的是否真是同一个问题？

## 6. Hypothesis

我现在形成什么可验证判断？

## 7. Experiment

如何用最小实践验证？

## 8. Observation

实际发生了什么？

## 9. Mental Model V1

我的认知发生什么变化？

## 10. Design Judgment

对 myharness 当前有什么判断？

## 11. Open Questions

哪些问题暂时不研究？
```

## 2. Evidence Model

| 证据类型 | 典型来源 | 它回答的问题 |
|---|---|---|
| Source Evidence | 官方文档、源码、公开规范、论文 | 系统被设计成什么？ |
| Behavior Evidence | Claude / Codex 行为实验、Session、Trace、Tool behavior | 系统实际上表现成什么？ |
| Project Evidence | myharness failure-record、A/B test、真实 Change、Review、CI | 这个问题在我的项目中真的存在吗？ |

> **重要判断：** 一个优秀开源项目采用某种 Pattern，只能构成 Reference Evidence；它不等于 myharness 必须采用。只有 Source / Behavior / Project Evidence 逐渐闭环，才值得进入 Architecture Decision。

### Evidence Strength 不是“引用数量”

建议同时记录：

```text
Direct / Indirect
Repeatable / One-off
Current / Stale
Host-specific / Cross-host
Supports / Contradicts
```

一个反例可以比十条同方向印象更有价值。

## 3. Experiment Record

建议 Experiment ID 使用：

```text
EXP-W01-01
EXP-W08-02
EXP-W16-01
```

模板：

```markdown
# EXP-WXX-YY

## Research Question

## Hypothesis

## Experiment Type

EXPLORATORY / COMPARATIVE / ABLATION

## Host / Model

## Task / Prompt

## Baseline

## Experimental Variant

## Controlled Variables

## Observed Evidence

## Unexpected Behavior

## Evidence Location

## Result

SUPPORT / REJECT / INCONCLUSIVE

## Mental Model Update

## Next Question
```

### 三类 Experiment Type

| Type | 目的 | 适合回答 |
|---|---|---|
| EXPLORATORY | 观察现象、发现变量、形成下一步假设 | “Context 到底怎么增长？” |
| COMPARATIVE | 在共同 baseline 下比较机制差异 | “Rule + Skill 与 Rule + Check 有何差异？” |
| ABLATION | 移除或逐层增加能力，观察某个 capability 的边际贡献 | “Changes 这一层真的增加价值吗？” |

不要为了让实验“像论文”而强行做所有组合。分类的目的只是提醒自己：**当前证据究竟能支持多强的结论。**

## 4. ADR Candidate Template

Week 14 的 ADR 是实验候选，不是已经接受的架构决策。

```markdown
# ADR-CANDIDATE-XXX · <Title>

## Status

PROPOSED / EXPERIMENT

## Context

## Observed Problem

## Current Evidence

## Hypothesis

## Experiment Design

## Success Signal

## Failure Signal

## Boundary

## Reversal Plan

## Result

SUPPORT / REJECT / INCONCLUSIVE

## Decision Update

ACCEPTED / REJECTED / REVISE / MORE EVIDENCE REQUIRED
```

核心原则：

> Implementation 完成不等于 ADR 正确；只有结果回答了原 Hypothesis，才有资格更新 Decision。

## 5. Open Questions / Research Backlog

旁支问题不是“不重要”，只是**当前不研究**。

建议统一记录在 `research/open-questions.md`。

字段：

```text
Question ID
Question
Discovered In
Why It Matters
Current Evidence
Blocks Current Research?
Priority
Candidate Phase
Status
```

示例：

```markdown
### OQ-007 · Subagent 的主要收益来自 specialization 还是 context isolation？

- Discovered In: Week 2
- Why It Matters: 影响 myharness 对 subagent 的使用边界
- Current Evidence: EXP-W02-01
- Blocks Current Research?: NO
- Priority: MEDIUM
- Candidate Phase: Week 11
- Status: BACKLOG
```

建议状态：

```text
BACKLOG
ACTIVE
ANSWERED
DROPPED
MERGED
```

## 6. Route Review

每 2–4 个研究循环做一次 Route Review。它不是进度汇报，而是检查：

> **当前路线是否仍然值得继续？**

模板：

```markdown
# Route Review · RR-YYYYMMDD

## Cycles Reviewed

## Questions Answered

## Mental Models Changed

## Hypotheses Supported

## Hypotheses Rejected

## Inconclusive Results

## New Open Questions

## Current Route Still Valid?

YES / PARTIAL / NO

## Projects to Add

## Projects to Remove

## Plan Changes

## Why the Route Changed

## Next Review Trigger
```

Route Review 可以得到：

```text
继续原路线
调整项目
交换 Week 顺序
延长当前循环
提前借用后续方法
删除一个研究问题
```

但必须记录“为什么改”。

## 7. myharness Design Beliefs Template

Design Beliefs 不是 Rules，也不是永久真理。

```markdown
# B-XXX · <Short Statement>

## Statement

当前相信的设计原则。

## Why I Believe It

为什么形成这个判断？

## Evidence

对应 Experiment / Failure / A-B Test / Source。

## Counterexample

什么现象反驳或限制它？

## Boundary

在哪些条件下适用？

## Confidence

HIGH / MEDIUM / LOW

## Implication

它对 myharness 设计意味着什么？
```

示例（仅示意，不是预设结论）：

```text
B-001

Statement
Deterministic engineering constraints should prefer enforcement over instruction.

Evidence
EXP-W04-01
failure-record-002

Counterexample
Semantic architecture rules cannot be completely enforced deterministically.

Boundary
Applicable to machine-checkable constraints.

Confidence
HIGH

Implication
Rule explains why. Hook / Test verifies observable violation.
```

## 8. Research Workspace

本仓库使用轻量工作区：

```text
research/
├── README.md
├── open-questions.md
├── cycles/
│   └── README.md
├── route-reviews/
│   └── README.md
├── adr-candidates/
│   └── README.md
├── templates/
│   ├── research-note.template.md
│   ├── experiment-record.template.md
│   ├── adr-candidate.template.md
│   └── route-review.template.md
└── design-beliefs.md
```

不要提前创建 `week-01` 到 `week-16` 的 16 个空目录。

开始一个研究循环时再创建：

```text
research/cycles/week-01/
├── research-note.md
├── experiments/
└── evidence/
```

让研究工作区随着真实研究自然生长。

---

## 路线调整说明

本卷是研究基础设施，不是额外流程负担。模板字段可以根据实际研究删减；如果记录成本开始高于证据价值，应在下一次 Route Review 中主动简化。
