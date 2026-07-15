# Cycle 10 实验工作区（Experiment Workspace）

> 状态（Status）：PREPARED · NOT EXECUTED

V4.1 `EXP-W08-01` 被拆分为两个实验：先研究 Discovery / Activation，再在显式激活条件下研究 Execution / Evidence。两个实验分别创建 Experiment Record，不共享 Result。

## 共同门禁

- 选择一个已有、revision 可固定、能在绑定 Host 上观察 discovery / activation 的 myharness semantic-review Skill；否则保持 `NOT EXECUTED`。
- 固定 Host version / surface、Provider profile、endpoint、Model、Configuration、permission、grader、Human intervention policy 与所有非 Skill revisions。
- 每个 Run 使用 fresh session、相同 repository baseline 与独立 Run Metadata；禁止跨 Run 记忆。

## `EXP-C10-01` · Skill Discovery and Activation

- 类型：`COMPARATIVE`
- Stable Task：`T02 · Semantic Review`
- 历史映射：`EXP-W08-01` 的 Discovery / Trigger 部分

### Variants

- V1：当前 Skill revision。
- V2：只修改 name / description / applicability；正文与 verifier 不变。

### Query corpus

- 冻结 24 个 T02-shaped query packets，按 label 分为 8 个 should-trigger、8 个 near-miss 和 8 个 should-not-trigger。
- 每个 packet 都包含有限 Change / diff、足够但不泄漏答案的上下文、至少一个语义问题和一个 deterministic check；label 只表示该 packet 是否属于所选 Skill 的 scope。
- 按 label 分层后固定 12 个 train 与 12 个 validation packets。只有 train 可用于调整 V2；validation 在最终 revision 冻结前不可查看结果。
- 每个 validation packet 对 V1 / V2 各执行 3 个 fresh-session Run，顺序在首个 Run 前平衡并冻结，共 72 个 validation Run。

### Observations and result

Host trace 必须能区分 discovered、loaded / activated 与 not activated；不可观察状态记为 `UNKNOWN`。每个 packet 以 3 次 Run 中至少 2 次正确路由为 packet pass，分别报告三类 label 的 raw pass count、false negative 与 false positive，不包装为统计显著性。

- `SUPPORT`：V2 在 12 个 validation packets 上比 V1 至少多通过 3 个，且任一 label stratum 不新增超过 1 个 regression。
- `REJECT`：V2 没有净增加 packet pass，或任一 label stratum 新增至少 3 个 regression。
- `INCONCLUSIVE`：其余结果、关键状态 `UNKNOWN`、Run 缺失、revision 泄漏或 confounder 未分离。

`EXP-C10-01` 只解释 description / applicability bundle 对 Discovery / Activation 的方向性影响，不评价 Skill 正文质量。

## `EXP-C10-02` · Activated Skill Behavior Contract

- 类型：`COMPARATIVE`
- Stable Task：`T02 · Semantic Review`
- 历史映射：`EXP-W08-01` 的 Execution / Evidence 部分

### Variants

- V2：`EXP-C10-01` 冻结后的 description revision，保留当前正文。
- V3：保持 V2 name / description / applicability 完全相同，正文增加 Trigger、Preconditions、Required Context、Procedure、Evidence Required、Completion Criteria 与 Failure Route；外部 verifier 不变。

### Activation control and task instances

- Host 必须支持显式调用或可复查的强制加载路径；每个 Run 在任务开始前确认同一 Skill revision 已加载。无法强制并观察激活的 Host stratum 保持 `NOT EXECUTED`。
- 冻结 3 个 T02 task instances；每个 instance 的 V2 / V3 使用完全相同的 task、diff、baseline、Agent-visible request、evaluator-only oracle、output schema 与 deterministic verifier。
- 每个 instance 对 V2 / V3 各执行 3 个 fresh-session Run。三个 paired blocks 的顺序在首个 Run 前冻结并平衡，共 18 个 Run。

### Observations and result

主要指标为 procedure checkpoint pass、evidence citation validity、deterministic / semantic defect recall 与 false completion。Context、时长和 Human intervention 为 secondary。每个 task instance 包含 3 个 paired blocks，并先形成 task-level direction：至少 2/3 blocks 改善且无新增主要 regression 为 task-level support；至少 2/3 blocks 无主要改善或持续新增 regression / false completion 为 task-level reject；其余为 task-level inconclusive。

- `SUPPORT`：至少 2/3 task instances 为 task-level support，且没有 task-level reject。
- `REJECT`：至少 2/3 task instances 为 task-level reject，且没有 task-level support。
- `INCONCLUSIVE`：其余结果、激活状态不一致、task / revision 泄漏、方向冲突或 confounder 未分离。

`EXP-C10-02` 只解释 behavior-contract bundle，不能归因单个字段，也不能与 `EXP-C10-01` 合并成一个 Result。

执行时使用 experiment-record 与 run-metadata 模板；本目录不创建 Run、Result 或 `EVD-*`。
