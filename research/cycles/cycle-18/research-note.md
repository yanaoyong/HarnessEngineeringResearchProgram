# Cycle 18 研究笔记（Research Note）· Acceptance、Ablation & Design Beliefs

> 状态（Status）：PLANNED · NOT EXECUTED
>
> 内容 Batch：8

[Cycle 正文](../../../docs/05-myharness-Integration-Research.md) · [实验工作区](experiments/README.md) · [证据准备](evidence/README.md) · [Design Beliefs](../../design-beliefs.md)

## 1. 研究问题

哪些实验性 Harness capability 在绑定条件下带来可接受的边际价值，哪些应拒绝、修订或要求更多证据？

## 2. 为什么与 myharness 有关

功能是否运行与是否值得长期保留是两个问题。最终裁决必须同时看到结果、过程、治理、上下文和维护成本，并把结论限制在真实执行条件内。

## 3. 范围与退出条件

- 范围：通过 Cycle 17 gate 的 variants、candidate × Host 独立 Experiment Records、每个 record 的 3 个固定 T03 tasks / Applicability Matrix、候选级 Decision Update 与有边界的 Design Belief；V4.1 Week 16 迁移。
- 范围外：强制全因子矩阵、公开 benchmark、统计显著性、跨 Host / Model 普遍结论、生产就绪或法律合规判断。
- 退出条件：每个 eligible candidate / Host record 的 activation-positive / non-trigger tasks 和 cells 完整运行，五类指标分开，critical failure 不被均值掩盖，结论可追溯到 `EVD-*`。

当前退出条件未满足；Cycle 17 尚未执行。

## 4. 心智模型 V0

Acceptance 是 evidence gate，不是 feature vote；Ablation 解释边际贡献，Design Belief 记录有反例、有边界且可撤销的当前判断。

## 5. 证据登记

尚无 `EVD-*`。可复用 Cycle 14 的 `SRC-HARNESS-012` 作为 interface theory 背景，但不升级为 myharness Result。当前 `research/design-beliefs.md` 仍只有模板；没有真实 Run 前不得新增 belief 或更新 ADR Decision。

## 6. 参考模式

复用 V4.1 B0 / A0 / experimental variant 与 Outcome / Process / Governance / Context / Cost 五维框架；矩阵只纳入通过前置门禁且能保持解释性的 cell。

## 7. 假设

`H-C18-<candidate>-<host> · Evidence-gated Marginal Value`：一个 candidate / Host stratum 的最小信息量矩阵能在包含 activation-positive 和 non-trigger control 的固定 T03 tasks 上暴露候选边际取舍，并支持 scoped Decision Update；不能证明普遍优越性。

## 8. 实验

- 实验 ID：`EXP-C18-01..12` candidate × Host family；每个已启用 ID 只有一个 candidate、Host / surface、Hypothesis 与 Result
- 类型：`ABLATION`
- Stable Task：`T03 · Medium Change`
- 历史映射：`EXP-W16-01` → `EXP-C18-01..12`
- Run Metadata：尚未创建
- 结果：尚未运行

## 9. 观察

无。

## 10. 矛盾证据与限制

- 候选通过 Cycle 17 不保证在不同 task 上仍有收益。
- Native Host、Current myharness 与 variant 的可用 surface 可能不同；不满足 parity 时不得比较。
- 三个 task 的小样本只能形成方向性证据。
- positive task 未激活 candidate 与 candidate 已激活但无收益是不同结果；缺少 activation trace 时不得裁决边际价值。
- Context 与 maintenance cost 的单位可能不同，不能用单一总分遮蔽 critical failure。

## 11. 心智模型 V1

等待实验与证据。

## 12. 设计判断

待定。ADR Decision 与 Design Belief 均未产生。

## 13. 开放问题

见 `OQ-017` 与 `OQ-018`。

## 14. 路线复盘触发条件

真实完成 Cycle 18 后执行最终 Route Review；若任一 candidate / Host record 的 matrix parity、Applicability Matrix、activation signal 或 evidence trace 不成立，则该 record 保持 `INCONCLUSIVE`，不得为了结束 Program 强行接受候选。
