# Cycle 07 实验工作区（Experiment Workspace）

> 状态（Status）：PREPARED · NOT EXECUTED

本目录为 Qwen Code Host 的两个计划实验准备空间，不包含 Run、Result 或 `EVD-*`。

## `EXP-C07-01` · Contract → Source → Configuration → Behavior Trace

- 类型：`EXPLORATORY`
- Outcome Mode：`OBSERVATION_ONLY`
- Stable Task：`T01 · Engineering Constraint`
- Task Instance：`T01-C07-LOCAL-RETRY-LIMIT-VALIDATION`
- Fixture：在固定 commit 的隔离 repository 中，为已有 local configuration parser 补充 `retry_limit` 上界验证；只修改冻结的 parser / test，不访问网络或工作区外路径。
- Acceptance：覆盖负数、零、允许上界、超过上界与字段缺省；保存命令、exit code、diff 与 deterministic result。
- Source gate：固定 `QwenLM/qwen-code` 完整 commit，记录 capability question、path、search term、stop point；通过 official release / package / build metadata 将执行 artifact 映射到 source revision。映射缺失时 Source / Behavior agreement 为 `UNKNOWN`。
- Trace：Qwen Code version / surface、platform、installation channel、`QWEN.md` / memory、approval / sandbox、Hook / Skill / Subagent / Extension state、Provider / endpoint / protocol、Model、脱敏 Configuration、actual tool set / request / result、Review、artifact 与 Human intervention。
- Result boundary：执行后只记录 `COMPLETE / PARTIAL / INVALIDATED` Observation Outcome；Experiment Result 为 `NOT APPLICABLE · OBSERVATION ONLY`。

## `EXP-C07-02` · Provider Profile Boundary Comparison

- 类型：`COMPARATIVE`
- Outcome Mode：`HYPOTHESIS_RESULT`
- Stable Task：`T02 · Semantic Review`
- T02：固定 patch、Agent-visible task、acceptance reference、evaluator-only oracle 与 output schema；oracle 至少含一个 semantic defect 和一个 deterministic defect，答案不得泄漏。
- Baseline A / Variant B：两个已授权 Provider profile；必须核验相同 Model identity / revision、tool-calling、context / output 与 task compatibility，只改变 Provider / endpoint route。
- Controlled Variables：Qwen Code version / surface、platform、source commit / artifact provenance、repository baseline、task、instruction / memory、tool / permission / sandbox、review procedure 与 Human intervention。
- Replication：A / B 各至少两个 fresh-task Run，顺序交错，从相同 clean baseline 与输入开始。
- Comparability gate：Model identity、protocol、limit、quota、routing 或 policy 不能保持可比时保持 `PLANNED · NOT EXECUTED`；不得用 Provider A + Model A 对 Provider B + Model B 裁决 Host invariant。
- Observations：configuration resolution、Host-owned tool / approval / sandbox route、provider transform / protocol error、actual tool request / result、issue detection、evidence quality、false positive、retry、Review / artifact route 与 Human intervention。
- Result vocabulary：`SUPPORT / REJECT / INCONCLUSIVE`。只有配对 Run 已完成但已登记 confounder 仍不可分时才使用 `INCONCLUSIVE`。

## 共同边界

- 每次执行使用独立 Run Metadata，绑定 task-fixture commit、Qwen Code version / surface、official source commit、artifact provenance、Provider、endpoint / protocol、Model、Configuration 与 revision fields。
- 不记录 secret、token、private endpoint value 或真实业务数据。
- 不测试 bypass，不把任务完成、工具调用成功、协议兼容或 Model 可选写成 portability / enterprise readiness。
- 内容准备阶段不创建 Experiment Record、Run、Result、`ENT-*`、`EVD-*` 或 Support Assessment。
