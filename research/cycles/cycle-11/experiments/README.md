# Cycle 11 实验工作区（Experiment Workspace）

> 状态（Status）：PREPARED · NOT EXECUTED

## `EXP-C11-01` · Historical Change Convergence Review

- 类型：`COMPARATIVE`
- Stable Task：`T02 · Semantic Review`
- 历史映射：`EXP-W09-01`

### Artifact Gate

选择一个曾被怀疑 drift、但仍能固定完整 commit 与相关 artifacts 的历史 Change。packet 至少包含 Spec / requirement、Task、Diff / symbol、Test、CI snapshot、Summary / status 与时间边界。缺失项保留为 `UNKNOWN`，不得补写历史事实。

### Oracle construction

两名人工 evaluator 独立建立 `Requirement ↔ Task ↔ Diff / Symbol ↔ Test ↔ CI ↔ Summary` truth map，并按预注册规则裁决分歧。每条 edge 标为 deterministic、semantic 或 unavailable；Round A 不计 Agent run。

### Agent variants

- Round B：无额外结构的 convergence review。
- Round C：使用冻结 checklist 的 convergence review。
- B / C 使用同一个 T02 task instance、repository baseline、Agent-visible packet、output schema、Host / surface、Provider、Model、Configuration、tools、permission 与 budget；fresh session、禁止跨 Run 记忆。
- B / C 各执行 3 个 Run，组成 3 个 paired blocks。每个 block 从相同 clean baseline 开始；顺序在首个 Run 前冻结并平衡，例如 `B→C / C→B / B→C`，共 6 个 Agent Run。
- 可选 CodeGraph 为独立 `EXPLORATORY` / `OBSERVATION_ONLY` stratum，使用 `COMPLETE / PARTIAL / INVALIDATED` Observation Outcome，不进入 B / C 主裁决，也不填写独立 Hypothesis Result。

### Metrics and result

按 drift taxonomy 记录 known-edge recall、false positive、citation validity、deterministic / semantic classification、unsupported status claim 与 false completion。Context、时长、Human intervention 为 secondary。

- `SUPPORT`：至少 2/3 paired blocks 中 C 相对 B 改善至少一个主要项，且没有新增 critical failure。
- `REJECT`：3/3 blocks 均无主要增益，或至少 2/3 blocks 持续新增主要 regression / critical failure 而无主要改善。
- `INCONCLUSIVE`：其余结果、block 方向冲突、oracle 未决、trace 不全、Run 缺失或 confounder 未分离。

执行时使用模板创建 Experiment Record 与每次 Run Metadata。本阶段不创建 Run、Result、`EVD-*` 或实现。
