# Cycle 11 研究笔记（Research Note）· Change Contract & Convergence

> 状态（Status）：PLANNED · NOT EXECUTED
>
> 内容 Batch：7

[Cycle 正文](../../../docs/04-Harness-Engineering-Research-Themes.md) · [实验工作区](experiments/README.md) · [来源权限](../../source-authority.md)

## 1. 研究问题

Change Artifact 如何避免与 Spec、Task、Diff、Test、CI 和 Summary 的真实状态漂移？

## 2. 为什么与 myharness 有关

Changes 只有在执行中能约束工作、关闭后能支持复查时才有价值。目录与状态字段存在不能证明实现完成，也不能证明 Summary 没有“撒谎”。

## 3. 范围与退出条件

- 范围：一个冻结历史 Change、人工 truth map、无结构 Agent review 与显式 checklist 对照；V4.1 Week 9 迁移。
- 范围外：实现 `harness converge`、引入 CodeGraph 主流程、批量修复历史 Change。
- 退出条件：固定 artifact packet、oracle、drift taxonomy、评分规则；完成 B / C replication；形成 responsibility judgment。

当前退出条件未满足。

## 4. 心智模型 V0

Change truth 是跨 Artifact edge 的可验证关系，不是单个文件的状态。确定性 edge 与语义 edge 需要不同 verifier。

## 5. 证据登记

尚无 `EVD-*`。计划来源：

- [`SRC-HARNESS-005`](evidence/SRC-HARNESS-005.md)：GitHub Spec Kit 官方文档 Contract 锚点。
- [`SRC-HARNESS-013`](evidence/SRC-HARNESS-013.md)：GitHub Spec Kit 官方源码仓库锚点。
- [`SRC-HARNESS-006`](evidence/SRC-HARNESS-006.md)：Fission-AI/OpenSpec 官方仓库锚点。

myharness historical Change 只有在执行时固定 commit、artifact 与 authority 后才可能产生 Project Evidence。

## 6. 参考模式

使用 `Requirement ↔ Task ↔ Diff / Symbol ↔ Test ↔ CI ↔ Summary` truth map；Spec Kit / OpenSpec 只提供 artifact workflow 参考，不证明 myharness 一致。

## 7. 假设

`H-C11-01 · Explicit Convergence Contract`：显式 checklist 相比无结构 review，提高预声明 drift edge 的召回和引用可追溯性，但可能增加误报和成本。

## 8. 实验

- 实验 ID：`EXP-C11-01`
- 类型：`COMPARATIVE`
- Stable Task：`T02 · Semantic Review`
- 历史映射：`EXP-W09-01` → `EXP-C11-01`
- Run Metadata：尚未创建
- 结果：尚未运行

## 9. 观察

无。

## 10. 矛盾证据与限制

- 人工 truth map 也可能错误，必须双人复核并记录分歧。
- Round A 是 oracle construction，不是与 Agent 等价的 variant。
- CodeGraph 若加入会引入额外变量，只能单独探索。
- 历史 artifact 的缺失可能来自 retention policy，而非执行失败。

## 11. 心智模型 V1

等待实验与证据。

## 12. 设计判断

待定。不实现 myharness Convergence capability。

## 13. 开放问题

见 `OQ-011`。

## 14. 路线复盘触发条件

如果无法建立可复查 oracle，或主要 drift 只存在于仓库外系统，则先复盘 evidence scope。
