# Cycle 14 研究笔记（Research Note）· Knowledge Ratification & Harness Minimalism

> 状态（Status）：PLANNED · NOT EXECUTED
>
> 内容 Batch：7

[Cycle 正文](../../../docs/04-Harness-Engineering-Research-Themes.md) · [实验工作区](experiments/README.md) · [来源权限](../../source-authority.md)

## 1. 研究问题

Agent 发现的事实何时值得固化为 Harness，何时应选择更小的治理位置或 Nothing？

## 2. 为什么与 myharness 有关

每次失败都增加 Rule 会制造 Context、冲突与维护债务；什么都不记录又会重复踩坑。Ratification 需要 authority、recurrence、scope、determinism、价值与成本边界。

## 3. 范围与退出条件

- 范围：十个满足 T02 Contract 的历史 failure / improvement Change packets、每个两个独立 Agent reviewer Run 与人工 evaluator-only reference；V4.1 Week 12 迁移。
- 范围外：立即写 Rule / Skill / Hook、证明未来可靠性、Cycle 15 audit 或 Cycle 16 ADR。
- 退出条件：固定 packet、time window、rubric、reviewers 与 removal fields；形成候选而非实现。

当前退出条件未满足。

## 4. 心智模型 V0

Ratification 是证据与成本门禁：`recurring value - context - maintenance - portability risk`，目标可为 Rule / Skill / Hook / Test / Wiki / Change Template / Nothing。

## 5. 证据登记

尚无 `EVD-*`。计划来源：

- [`SRC-HARNESS-010`](evidence/SRC-HARNESS-010.md)：buildermethods/agent-os。
- 复用 Cycle 1 [`SRC-FOUNDATION-002`](../cycle-01/evidence/SRC-FOUNDATION-002.md)：SWE-agent/mini-swe-agent。
- 复用 Cycle 1 [`SRC-FOUNDATION-003`](../cycle-01/evidence/SRC-FOUNDATION-003.md)：SWE-agent ACI paper；受 `OQ-003` 限制。

myharness failure / improvement record 只有在固定 artifact 与 authority 后才可能产生 Project Evidence。真实执行后，任何进入 Cycle 15/16 的可复用 ratification claim 都必须派生 scoped `EVD-*`；候选列表本身不能替代 Evidence Claim。

## 6. 参考模式

Agent OS 提供 standards discovery / deployment 参考；mini-swe-agent 与 ACI 提醒 interface value 与 scaffold size 是不同问题。它们不决定 myharness 应固化什么。

## 7. 假设

`H-C14-01 · Evidence-gated Ratification`：对满足 T02 的固定 Change packets，显式 rubric 能让 Agent reviewer 的治理位置和 Nothing 决策更可复查，但 retrospective classification 不能证明未来缺陷下降。

## 8. 实验

- 实验 ID：`EXP-C14-01`
- 类型：`EXPLORATORY`
- Stable Task：`T02 · Semantic Review`
- 历史映射：`EXP-W12-01` → `EXP-C14-01`
- Run Metadata：尚未创建
- 结果：尚未运行

## 9. 观察

无。

## 10. 矛盾证据与限制

- historical packet availability 会产生幸存者偏差。
- 不能满足一个语义问题和一个 deterministic check 的历史记录必须从正式 T02 dataset 排除，不得以 `UNKNOWN` 补齐。
- recurrence 与 severity 不等价；后验复发不能证明候选机制有效。
- Rule、Skill、Hook、Test、Wiki 的 Context / maintenance 成本单位不同。
- Model behavior 不能在未分离 Host / Provider / Configuration 时归因。

## 11. 心智模型 V1

等待实验与证据。

## 12. 设计判断

待定。所有输出只进入 Cycle 15 / 16 候选列表。

## 13. 开放问题

见 `OQ-003` 与 `OQ-014`。

## 14. 路线复盘触发条件

若十个 packet 无法满足 authority / revision gate，或 reviewer 无法区分事实与解释，停止分类并复盘数据集。
