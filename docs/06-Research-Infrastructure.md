# PART VII · Research Infrastructure

> 贯穿全程使用的 Research Note、Evidence Model、Experiment Record 与 Design Beliefs 模板。

[← 上一卷](05-myharness-Integration-Research.md) · [返回总览](../README.md) · [下一卷 →](07-Reference-Project-Atlas.md)

---

## 统一 Research Note 模板

每个 Week 建议使用同一结构，重点不是篇幅，而是必须能看见 V0 → Evidence → Experiment → V1 的认知变化。

\# Week XX Research Note

\## 1. Research Question
我真正想回答什么？

\## 2. Why It Matters to myharness
为什么这个问题与我的项目有关？

\## 3. Mental Model V0
学习前，我认为机制是什么？

\## 4. Source Evidence
从官方资料或源码看到了什么？

\## 5. Reference Pattern
优秀项目怎么解决？

\## 6. Hypothesis
我现在形成什么可验证判断？

\## 7. Experiment
如何用最小实践验证？

\## 8. Observation
实际发生了什么？

\## 9. Mental Model V1
我的认知发生什么变化？

\## 10. Design Judgment
对 myharness 当前有什么判断？

\## 11. Open Questions
哪些问题暂时不研究？

## 三类证据

| **证据类型**      | **典型来源**                                                | **它回答的问题**                 |
|-------------------|-------------------------------------------------------------|----------------------------------|
| Source Evidence   | 官方文档、源码、公开规范、论文                              | 系统被设计成什么？               |
| Behavior Evidence | Claude / Codex 行为实验、Session、Trace、Tool behavior      | 系统实际上表现成什么？           |
| Project Evidence  | myharness failure-record、A/B test、真实 Change、Review、CI | 这个问题在我的项目中真的存在吗？ |

| **重要判断：** 一个优秀开源项目采用某种 Pattern，只能构成 Reference Evidence；它不等于 myharness 必须采用。只有 Source / Behavior / Project Evidence 逐渐闭环，才值得进入 Architecture Decision。 |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Experiment Record 最小字段

Experiment ID
Research Question
Hypothesis
Host / Model
Task / Prompt
Baseline
Experimental Variant
Controlled Variables
Observed Evidence
Unexpected Behavior
Result: SUPPORT / REJECT / INCONCLUSIVE
Mental Model Update
Next Question

## myharness Design Beliefs v1 模板

Belief ID

Statement
当前相信的设计原则。

Why I Believe It
为什么形成这个判断？

Evidence
对应 Experiment / Failure / A-B Test / Source。

Counterexample
什么现象反驳或限制它？

Boundary
在哪些条件下适用？

Confidence
HIGH / MEDIUM / LOW

Implication
它对 myharness 设计意味着什么？

## 示例（仅示意，不是预设结论）

B-001

Statement
Deterministic engineering constraints should prefer enforcement over instruction.

Why I Believe It
Instruction-only experiments showed ...

Evidence
EXP-W04-02
failure-record-002

Counterexample
Semantic architecture rules cannot be completely enforced deterministically.

Boundary
Applicable to machine-checkable constraints.

Confidence
HIGH

Implication
Rule explains why. Hook / Test verifies observable violation.


---

## 路线调整说明

本卷是研究导航，不是冻结的教学脚本。执行到对应研究循环前，应先刷新相关官方文档、默认分支与 Changelog；若项目目录或能力名称发生变化，继续追踪本卷定义的研究问题与 Capability，而不是机械寻找旧路径。
