# Cycle 18 实验工作区（Experiment Workspace）

> 状态（Status）：PREPARED · NOT EXECUTED

## Candidate × Host experiment family

每个 Experiment Record 只绑定一个 candidate、一个 Host / surface stratum、一个 Hypothesis 与一个 Result。V4.1 `EXP-W16-01` 迁移为以下计划 family：

| Cycle 16 rank | Claude Code | Codex | ZCode | OpenCode |
|---|---|---|---|---|
| Rank 1 | `EXP-C18-01` | `EXP-C18-02` | `EXP-C18-03` | `EXP-C18-04` |
| Rank 2 | `EXP-C18-05` | `EXP-C18-06` | `EXP-C18-07` | `EXP-C18-08` |
| Rank 3 | `EXP-C18-09` | `EXP-C18-10` | `EXP-C18-11` | `EXP-C18-12` |

编号预留不表示 candidate 或 Host stratum 已通过门禁。只有对应组合可执行时才创建 Experiment Record；未入选 candidate、不可用 Host 或 surface parity 不成立时保持 `PLANNED · NOT EXECUTED`，不创建空 Result。

每个已启用实验：

- 类型：`ABLATION`
- Stable Task：`T03 · Medium Change`
- Hypothesis：`H-C18-<candidate>-<host> · Evidence-gated Marginal Value`

## Eligibility and record boundary

只有 Cycle 17 中具有完整 paired Result、可用 H1 implementation artifact、rollback evidence 和可分离 confounder 的 candidate 才能进入某个 Host stratum。每个 record 在执行前冻结：

- candidate ID、ADR Candidate revision、required target Host set、Host / surface 与 Host version；
- `B0 · Native Host`、`A0 · Current myharness` 与 `A1 · One frozen candidate variant`；
- Provider、endpoint / protocol、Model、Configuration、permission、tool profile 与 Human intervention policy；
- 3 个 T03 task instances、Applicability Matrix、primary / secondary metrics、critical failure、Decision threshold 与缺失 cell 处理。

不同 candidate 或 Host stratum 使用不同 Experiment Record、Run group、Result 与 scoped `EVD-*`。跨 candidate stack 必须另建实验，不能塞进任一 family record。

## Applicability and activation gate

三个 T03 task instances 至少包含：

- 2 个 `ACTIVATION_POSITIVE` tasks：根据 candidate Contract 预期 A1 发生 Discovery / Activation / Execution，并具有不依赖最终任务成功的 verifier；
- 1 个 `NON_TRIGGER_CONTROL` task：候选机制不应激活，用于观察 false activation 与无关 Context / Cost。

Applicability Matrix 为每个 task 记录 task-fixture commit、candidate applicability、expected Discovery / Activation / Execution signal、verifier、B0 / A0 expected behavior 与 known confounders。若 Host surface 无法观察所需 activation signal，或 positive task 无法在 preflight 中证明 candidate 可用，该 record 保持 `NOT EXECUTED`。

正式 Run 中：

- activation-positive task 的 A1 未激活时，记录 activation / implementation failure，不能解释成“候选已激活但无边际价值”；
- non-trigger control 的 A1 意外激活时，记录 false activation；
- activation trace、task outcome 与 cost metrics 分开登记。

## Smallest informative matrix

每个 record 默认只比较 B0、A0、A1。只有同一个 candidate 内存在预注册 component Hypothesis 且保持单变量解释时，才增加 Rules-only / Rules+Skills / Rules+Skills+Changes 等内部消融 cell。

每个 eligible cell 对 3 个 task 各执行 3 个 fresh-session Run，总数为：

```text
eligible cells × 3 tasks × 3 repetitions
```

每个 Run 有独立 metadata；顺序、cache / session policy 与 task reset procedure 在运行前冻结。

## Metrics and critical failures

- Outcome：Task Success、First-pass Acceptance、Tests。
- Process：Rework、False Completion、Blind Retry、Missed Verification、Unrelated Change。
- Governance：Rule Violation、Human Intervention、Gate Trigger。
- Context：Consumption、Repeated Reads、Recovery。
- Cost：Harness complexity、Maintenance、Cross-host duplication。

安全、正确性、rollback、activation observability 或 evidence integrity critical failure 单独裁决，不被平均 Context / Cost 优势抵消。不同 record 不计算合并胜率、公开 Model 排名或统计显著性。

## Result、ADR and Design Belief gate

- 每个 record 使用自己的预注册 Hypothesis 和 threshold 形成一个 `SUPPORT / REJECT / INCONCLUSIVE`；缺失 Run、activation signal、不可比 baseline 或未分离 confounder 时保持 `INCONCLUSIVE`。
- Candidate ADR 在运行前声明 required target Host set；集合内任一必需 record 缺失时，不能形成无边界 `ACCEPTED`，只能保留 `MORE EVIDENCE REQUIRED` 或 scoped decision。
- ADR Candidate 只有引用真实 scoped `EVD-*` 后才能更新为 `ACCEPTED / REJECTED / REVISE / MORE EVIDENCE REQUIRED`。
- Design Belief 必须包含 Evidence、Counterexample、Boundary、Confidence 与撤销条件；没有合格结论时保持 `No Change`。
- 实验分支是否合并是 Cycle 18 证据之后的独立 owner 决策，不由内容生成或 `SUPPORT` 自动触发。

当前没有 Experiment Record、matrix cell、Run、Result、ADR Decision、Design Belief、Route Review 或 Support Level。
