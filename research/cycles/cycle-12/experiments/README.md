# Cycle 12 实验工作区（Experiment Workspace）

> 状态（Status）：PREPARED · NOT EXECUTED

V4.1 `EXP-W10-01` 被拆成一个低风险 T01 实验和一个中等变更 T03 实验，避免把 README 小改静默重定义为 T03。两个实验分别创建 Experiment Record，并按 task instance 独立报告。

## 共同 Risk Route

- Baseline A：固定 revision 的完整 myharness 10 Stage。
- Variant B：执行前由冻结 risk rubric 选择 required artifacts、mandatory gates、Human checkpoints 与 escalation；Agent 不能在执行中自行删减。
- Risk dimensions：blast radius、reversibility、security / data boundary、interface / compatibility、testability、unknowns 与 coordination cost。未知高影响项必须升级，不能默认低风险。
- 每个 A / B pair 固定 Host / surface、Provider、endpoint、Model、Configuration、tools、permission、budget、acceptance 与 Human intervention policy。
- 每个 variant 对同一 task instance 各执行 3 个 fresh-session Run，组成 3 个 paired blocks。每个 Run 从完全相同的 clean baseline 和 Agent-visible input 开始；顺序预先平衡并冻结。

## `EXP-C12-01` · Low-risk Documentation Workflow

- 类型：`COMPARATIVE`
- Stable Task：`T01 · Engineering Constraint`
- 历史映射：`EXP-W10-01` 的 README / 文档措辞部分

冻结一个小型、可逆的 README / documentation task instance，包含明确工程约束与 deterministic acceptance，例如术语一致性、内部链接或 schema-generated snippet 不得漂移。A / B 对完全相同的 task instance 与 baseline 执行。

## `EXP-C12-02` · Medium-change Workflow

- 类型：`COMPARATIVE`
- Stable Task：`T03 · Medium Change`
- 历史映射：`EXP-W10-01` 的 Hook Bug 与 Plugin / Architecture 部分

冻结两个独立 T03 task instances：一个普通 Hook bug，一个受控的 Plugin / architecture boundary change。每个 instance 都必须跨多个相互依赖步骤或文件、具备明确 acceptance、可逆 baseline，且不能扩大为项目重构。每个 instance 内 A / B 使用完全相同的 task 和 baseline；`EXP-C12-02` 的 Result Unit 是 `TASK_INSTANCE`，Stratum Key 是 `task_instance_id`，两个 instance 的 Result 不互相替代。

## Metrics and result

- Primary：escaped critical risk、acceptance failure、rework、false completion。
- Secondary：elapsed time、artifact count、Context cost、Human checkpoints、ceremony steps。

每个 task instance 独立裁决：

- `SUPPORT`：至少 2/3 paired blocks 中 B 不恶化任何 primary 指标，并持续降低至少一个预注册 secondary cost；不得新增 critical failure。
- `REJECT`：至少 2/3 paired blocks 中 B 增加 primary failure / critical failure，或 3/3 blocks 均无 primary 改善且无 secondary cost 降低。
- `INCONCLUSIVE`：其余结果、block 方向冲突、Run 缺失、risk route 泄漏或 confounder 未分离。

不同 task instance 与 T01 / T03 Result 不汇总为统一 workflow 胜率。不得把结果写成 Light / Standard / Full 已验证，也不得直接修改 myharness。执行时另建 Experiment Record、Run Metadata 与证据。

`EXP-C12-01` 使用 Experiment-level Result。`EXP-C12-02` 在一个 Experiment Record 中为两个 `task_instance_id` 分别建立 Stratum Result；由于两类任务刻意代表不同风险形状且没有预注册聚合语义，Experiment-level Result 写为 `NOT APPLICABLE — see task-instance Stratum Results`，不得用平均值或多数票生成统一结论。
