# Cycle 12 研究笔记（Research Note）· Adaptive Workflow

> 状态（Status）：PLANNED · NOT EXECUTED
>
> 内容 Batch：7

[Cycle 正文](../../../docs/04-Harness-Engineering-Research-Themes.md) · [实验工作区](experiments/README.md) · [来源权限](../../source-authority.md)

## 1. 研究问题

如何让 workflow depth 随任务风险变化，同时保持 mandatory gate、escalation 与 acceptance 可审计？

## 2. 为什么与 myharness 有关

固定十阶段可能产生 ceremony，自由裁剪又可能静默跳过风险控制。myharness 需要区分可省略 artifact、不可省略 gate 与必须升级的人类决定。

## 3. 范围与退出条件

- 范围：一个低风险 T01 documentation task、两个 T03 medium-change tasks、完整 workflow 与 risk-routed variant；V4.1 Week 10 迁移。
- 范围外：修改 10 Stage、引入 BMAD / OpenSpec、生产任务自动路由。
- 退出条件：固定 risk rubric、route table、task parity、primary / secondary metrics；独立报告各 stratum。

当前退出条件未满足。

## 4. 心智模型 V0

Adaptive Workflow 是 `preflight + risk classification + mandatory gates + escalation + acceptance`，不是 Agent 自由跳阶段。

## 5. 证据登记

尚无 `EVD-*`。计划来源：

- [`SRC-HARNESS-014`](evidence/SRC-HARNESS-014.md)：BMAD Method 官方文档 Contract 锚点。
- [`SRC-HARNESS-007`](evidence/SRC-HARNESS-007.md)：BMAD Method 官方源码仓库锚点。
- 复用 Cycle 11 [`SRC-HARNESS-006`](../cycle-11/evidence/SRC-HARNESS-006.md)：OpenSpec；复用不提升 Evidence Class。

myharness 10 Stage 在固定 revision 前只是 Project Evidence 候选。

## 6. 参考模式

BMAD 的 planning tracks 用于追问“深度如何变化”；OpenSpec 用于追问 artifact 如何演进。二者都不直接成为 myharness route taxonomy。

## 7. 假设

`H-C12-01 · Risk-routed Workflow`：预注册 risk route 能减少 ceremony / Context，而不增加 escaped critical risk、rework 或 false completion。

## 8. 实验

- `EXP-C12-01`：`COMPARATIVE` · `T01 · Engineering Constraint` · Low-risk Documentation Workflow。
- `EXP-C12-02`：`COMPARATIVE` · `T03 · Medium Change` · Medium-change Workflow。
- 历史映射：`EXP-W10-01` → `EXP-C12-01`（README / documentation）+ `EXP-C12-02`（Hook / Plugin / architecture）
- Run Metadata：尚未创建
- 结果：尚未运行

## 9. 观察

无。

## 10. 矛盾证据与限制

- Task complexity 不等于 delivery risk。
- 三个 stratum 不能合并为统一胜率。
- 同一 task instance 重跑仍可能有 Provider cache、顺序或 evaluator learning effect；必须使用 fresh session、平衡顺序并记录 confounder。
- 少 artifact 不等于更高效，多 gate 不等于更安全。

## 11. 心智模型 V1

等待实验与证据。

## 12. 设计判断

待定。不改变 myharness workflow。

## 13. 开放问题

见 `OQ-012`。

## 14. 路线复盘触发条件

若 risk label 只能在结果发生后确定，或 task parity 无法通过，停止比较并复盘设计。
