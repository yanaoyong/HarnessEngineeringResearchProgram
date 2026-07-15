# Cycle 13 实验工作区（Experiment Workspace）

> 状态（Status）：PREPARED · NOT EXECUTED

## `EXP-C13-01` · Multi-session Handoff Trace

- 类型：`EXPLORATORY`
- Stable Task：`T03 · Medium Change`
- 历史映射：`EXP-W11-01`

## Design

选择一个能从固定 clean baseline 分成 Intake / Scope → Research → Plan → Implement → Review 的连续 medium change，形成四个 transition。四种 mode 在运行前分别绑定一个 transition：

1. Host Resume / native continuation；
2. fresh session + 自由文本 prose summary；
3. fresh session + 结构化 handoff artifact；
4. fresh session + 现有 Changes artifact。

Mode assignment 在首个 episode 前冻结。phase 与 mode 天然混杂，因此本实验只定位信息损失，不比较 mode superiority。

## Session and episode semantics

- `execution episode`：一次连续 Agent 工作区间；四个 transition 都创建新的 episode。
- Resume mode：新 episode 恢复同一个 Host session identity；不得创建新 session，也不得额外注入 prose / structured / Changes artifact，除非它本来就是 Host resume Contract 的一部分。
- 其他三种 mode：新 episode 使用全新的 Host session identity，只提供该 mode 允许的 artifact 与任务入口。
- 每个 episode 记录脱敏 session identity、predecessor episode、continuity mode、实际 hydration inputs、Host / surface / Provider / Model / Configuration 与 session capability。
- Host 无法实现某 mode 时记为 `UNKNOWN / NOT EXECUTED`，不替换成另一机制。

## Structured handoff fields

Goal、Scope / Non-goal、Repository commit / dirty state、Decisions + rationale、Evidence / commands、Artifacts changed、Current failure、Open risks、Unfinished items、Next action、Human decisions、Freshness / revalidation trigger。

Changes artifact 保持其固定 project schema，不为了与 structured handoff 对齐而补字段；字段差异本身属于 observation。

## Observations

记录 missing critical fact、contradiction、stale fact、unsupported assumption、recovery time、duplicate work、evidence trace break、Human correction、Context input size 与 acceptance state。速度不能在缺少 completeness / correctness 时单独算改善。

## Result boundary

Result 只回答“在哪些 transition 观察到哪些信息损失或恢复机制”，不比较四个 mode 的优劣。任何 phase / mode 归因、episode trace 或 hydration input 不完整时，Result 为 `INCONCLUSIVE`。后续比较必须另建 matched-task、balanced-order experiment。

执行时另建 Experiment Record 和每个 execution episode 的 Run Metadata；本阶段不创建结果、`EVD-*` 或实现。
