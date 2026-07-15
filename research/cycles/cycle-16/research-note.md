# Cycle 16 研究笔记（Research Note）· Hypothesis & ADR Candidate

> 状态（Status）：PLANNED · NOT EXECUTED
>
> 内容 Batch：8

[Cycle 正文](../../../docs/05-myharness-Integration-Research.md) · [实验工作区](experiments/README.md) · [证据准备](evidence/README.md) · [ADR Candidate 模板](../../templates/adr-candidate.template.md)

## 1. 研究问题

哪些经证据约束的架构假设值得进入可逆实验，哪些应进入 Backlog、Open Question 或保持现状？

## 2. 为什么与 myharness 有关

未经选择门禁的 Finding 容易膨胀为 feature list。Cycle 16 要把证据强度、价值、成本、可移植性与可逆性放进同一可复查过程，同时保留合理分歧。

## 3. 范围与退出条件

- 范围：真实 Cycle 15 合格 Finding、八维评分、两个 independent T03 portfolio Run、至多三个 `PROPOSED` 候选；V4.1 Week 14 迁移。
- 范围外：接受 ADR、实现功能、创建空候选补足 Top3、以总分替代 owner decision。
- 退出条件：候选可追溯、可证伪、可逆，排序分歧和 Backlog 理由显式记录。

当前退出条件未满足；Cycle 15 尚未执行，因此当前没有候选输入。

## 4. 心智模型 V0

ADR Candidate 是 `Finding → Hypothesis → minimal experiment → success / failure / reversal` 的实验合同，不是架构决定。

## 5. 证据登记

尚无 `EVD-*`。Cycle 16 只接受未来 Cycle 15 scoped `EVD-*` 所绑定的 Project Artifact / Run / evaluator IDs，或明确记录的 evidence gap；Reference Pattern、评分或 Agent agreement 都不能独立创建证据。

## 6. 参考模式

复用 [ADR Candidate 模板](../../templates/adr-candidate.template.md) 与 V4.1 八维评分，但在执行前冻结成本方向、权重、准入阈值和 evaluator procedure。

## 7. 假设

`H-C16-01 · Traceable Candidate Selection`：资格门禁、八维评分与 reversal contract 能让两个独立 portfolio 保持证据链并暴露排序分歧，而不是把偏好包装成决策。

## 8. 实验

- 实验 ID：`EXP-C16-01`
- 类型：`EXPLORATORY`
- Stable Task：`T03 · Medium Change`
- 历史映射：`EXP-W14-01` → `EXP-C16-01`
- Run Metadata：尚未创建
- 结果：尚未运行

## 9. 观察

无。

## 10. 矛盾证据与限制

- 分数有伪精确风险，且不同评分者可能理解成本方向不同。
- 两个 Run 选出同一候选不证明候选正确；不同也不自动表示协议失败。
- Evidence Strength 取决于 Cycle 15 的 artifact authority 与覆盖范围。
- Cross-host Portability 未经 Cycle 9 / Host-specific Behavior Evidence 不能得高置信评分。

## 11. 心智模型 V1

等待实验与证据。

## 12. 设计判断

待定。本 Batch 不创建实际 `ADR-*` 文件。

## 13. 开放问题

见 `OQ-015` 与 `OQ-016`。

## 14. 路线复盘触发条件

若评分对候选排序的影响大于 Evidence gate，或合格 Finding 无法写成可证伪且可逆的实验，停止选 Top3 并复盘候选协议。
