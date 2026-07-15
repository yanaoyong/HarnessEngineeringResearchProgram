# Cycle 10 研究笔记（Research Note）· Skill Behavior & Evaluation

> 状态（Status）：PLANNED · NOT EXECUTED
>
> 内容 Batch：7

[Cycle 正文](../../../docs/04-Harness-Engineering-Research-Themes.md) · [实验工作区](experiments/README.md) · [来源权限](../../source-authority.md)

## 1. 研究问题（Research Question）

什么样的 Skill 能在绑定 Host、surface、Provider、Model 与任务条件下改变 Discovery、Execution、Evidence 和 Outcome，而不只是改善文字？

## 2. 为什么与 myharness 有关

myharness 现有 Skill 可能同时承担触发说明、SOP、证据要求和完成判断。若不分阶段测量，漏触发会被误诊为正文问题，外部 verifier 的作用也会被错误归给 Skill。

## 3. 范围与退出条件（Scope and Exit Criteria）

- 范围：单个 semantic-review Skill 的 V1 / V2 / V3 计划比较；Discovery / Activation 与显式激活后的 Execution / Evidence 分成两个实验；V4.1 Week 8 迁移。
- 范围外：批量改写 Skills、跨 Host portability、公开 benchmark、Skill distribution、myharness 实现。
- 退出条件：固定 revisions、query split、T02 oracle、grader 与阈值；完成 fresh-session replication；形成 Mental Model V1。

当前退出条件未满足。

## 4. 心智模型 V0（Mental Model V0）

`Skill effect = discovery effect + procedure effect + evidence effect + interaction with Host / Model / task`。这是待验证分解，不是因果结论。

## 5. 证据登记（Evidence Registry）

尚无 `EVD-*`。计划来源：

- [`SRC-HARNESS-001`](evidence/SRC-HARNESS-001.md)：Agent Skills · Optimizing skill descriptions。
- [`SRC-HARNESS-002`](evidence/SRC-HARNESS-002.md)：Agent Skills · Evaluating skill output quality。
- [`SRC-HARNESS-003`](evidence/SRC-HARNESS-003.md)：obra/superpowers 浮动源码锚点。
- [`SRC-HARNESS-004`](evidence/SRC-HARNESS-004.md)：learn-claude-code 浮动源码锚点。

Source artifact 不等于 Evidence Claim；默认分支执行时必须固定 commit。Contract、Source、Behavior、Project、Enterprise 各栏均尚无证据。

## 6. 参考模式（Reference Pattern）

Agent Skills 的 trigger / output evaluation guidance 与 Superpowers 的 behavior-contract pattern 用来提出问题，不作为 myharness 或任一 Host 已有效的证明。

## 7. 假设（Hypothesis）

`H-C10-01 · Description Discovery`：在 T02-shaped validation corpus 中，V1→V2 只改变 name / description / applicability，可以方向性改变 Discovery / Activation 的正确路由。

`H-C10-02 · Activated Behavior Contract`：在 Skill 已显式加载、name / description 相同的条件下，V2→V3 只改变 behavior-contract bundle，可以方向性改变 Execution / Evidence。

## 8. 实验（Experiment）

- `EXP-C10-01`：`COMPARATIVE` · `T02 · Semantic Review` · Skill Discovery and Activation。
- `EXP-C10-02`：`COMPARATIVE` · `T02 · Semantic Review` · Activated Skill Behavior Contract。
- 历史映射：`EXP-W08-01` → `EXP-C10-01`（Discovery）+ `EXP-C10-02`（Execution / Evidence）
- Run Metadata：尚未创建
- 结果：尚未运行

完整设计见 [实验工作区](experiments/README.md)。

## 9. 观察（Observation）

无。来源刷新不构成实验观察。

## 10. 矛盾证据与限制

- discovery、activation、execution、evidence 和 outcome 不可互相替代；`EXP-C10-02` 无法显式加载 Skill 时不得执行。
- Model nondeterminism、Host skill routing、session history 和 task difficulty 都可能污染比较。
- V3 同时增加多个 contract field，只能解释为 contract bundle，不能归因某个字段。
- 小样本结果不得外推到其他 Skill、Host、Provider 或 Model。

## 11. 心智模型 V1（Mental Model V1）

等待实验与证据。

## 12. 设计判断（Design Judgment）

待定。本 Cycle 不修改 myharness Skill schema。

## 13. 开放问题（Open Questions）

见 `OQ-004` 与 `OQ-010`。

## 14. 路线复盘触发条件（Route Review Trigger）

若 Host 无法可靠观测 discovery / activation，或 deterministic verifier 主导全部结果，先记录限制并复盘测量模型。
