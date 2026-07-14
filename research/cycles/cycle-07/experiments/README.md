# Cycle 07 实验工作区（Experiment Workspace）

> 状态（Status）：PREPARED · NOT EXECUTED

本目录为后续实现预先准备。计划实验：

- `EXP-C07-01` · Contract → Configuration → Behavior Trace
- `EXP-C07-02` · Provider Profile Boundary Comparison

`EXP-C07-01` 使用 `T01-C07-LOCAL-RETRY-LIMIT-VALIDATION`：在固定 commit 的隔离 fixture repository 中为已有本地 configuration parser 补充 `retry_limit` 上界验证，只修改冻结的 parser source 与 test file，不改变公开 schema / error type，不访问网络；deterministic acceptance checks 覆盖负数、零、允许上界、超过上界与字段缺省。

`EXP-C07-02` 使用固定 T02 patch 与 acceptance reference。Evaluator-only oracle 记录需要推理的“重试状态在成功后未清零”与可由 schema check 确定检出的“新增配置字段未同步到 schema”两个预植入缺陷；oracle 及缺陷名称不得进入 Agent-visible task statement、Rule、context、acceptance reference 或 output schema。两个已授权 Provider profile 必须复用相同 ZCode version、platform、repository baseline、Agent-visible input、permission mode 与 Review procedure；优先固定相同 Model ID，每个 profile 至少执行两个顺序交错的 fresh task Run。观察必须分开记录 Host-side tool exposure / filtering policy 与 decision owner、actual exposed tool set、Provider / Model tool-calling capability 与实际 tool request / success；actual exposed tool set 变化不能单独反驳 Host boundary。若配对 Run 已完成但 Model ID、endpoint policy、quota、tool policy 或 configuration drift 仍无法分离，登记 confounder 并填写 `INCONCLUSIVE`，不得写成 Host invariant；若无法合规取得两个 profile，实验保持 `PLANNED · NOT EXECUTED`，不填写 Result。

真实执行开始后，使用 [实验记录模板](../../../templates/experiment-record.template.md) 创建独立 Experiment Record，并为每次执行保存独立 Run Metadata。每个 Run 必须绑定 product / Host version、platform、installation channel、Provider / endpoint type、Model ID、脱敏 configuration snapshot、Rule / Skill / Check / Adapter revision、controlled variables、known confounders、evidence 与 human intervention。

不得记录 API Key / token，不测试权限绕过，不访问真实业务服务或工作区外路径。内容生成阶段不得填写结果、创建 `EVD-*`、`ENT-*` 或 Support Assessment。
