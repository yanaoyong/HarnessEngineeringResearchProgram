# Cycle 08 实验工作区（Experiment Workspace）

> 状态（Status）：PREPARED · NOT EXECUTED

本目录为后续实现预先准备。计划实验：

- `EXP-C08-01` · Contract → Source → Behavior Architecture Trace
- `EXP-C08-02` · Provider Portability Comparison
- `EXP-C08-03` · Model Portability Comparison

`EXP-C08-01` 使用 `OBSERVATION_ONLY`，Experiment Result 为 `NOT APPLICABLE · OBSERVATION ONLY`；`EXP-C08-02` 与 `EXP-C08-03` 使用 `HYPOTHESIS_RESULT`。

`EXP-C08-01` 使用 `T03-C08-LOCAL-RETRY-BUDGET`：在固定 commit 的隔离 fixture repository 中为已有本地 job runner 增加可配置 retry budget，修改 config type / parser、validation、runtime use、tests 与用户文档；acceptance checks 覆盖字段缺省、合法 / 非法边界、runtime 停止条件与文档示例。Trace 必须绑定 OpenCode version / surface / platform、官方页面版本、固定 `anomalyco/opencode` source commit、configuration precedence、instruction source、agent、tool / permission、extension state、Provider profile、Model、session / task state、Review、artifact 与 human intervention。源码只追真实触及的 capability，并记录 path、search term、stop point 与 Unknown。

在解释 `EXP-C08-01` 的 Source / Behavior agreement 前，必须通过官方 release / tag provenance、package / binary build metadata 或其他可复查官方材料，把实际执行的 OpenCode artifact 映射到固定 source commit。只有 commit pinned 但映射缺失时，Source 与 Behavior 分开记录，agreement 保持 `UNKNOWN`，且 Cycle 8 相关 Exit Criteria 未满足。

`EXP-C08-02` 与 `EXP-C08-03` 复用同一固定 T02 patch 与 evaluator-only oracle，但使用独立 Experiment Record、Result 与 scoped `EVD-*`。Agent-visible task 强制先用 read tool 检查预先登记的 implementation、schema 与 test 文件，再运行 fixture 内固定的本地 `./scripts/check-review-fixture`。该 exact command 在共同 permission profile 中设置为 `ask`，每个 Run 由相同 `approve once` Human intervention 处理；命令不访问网络、secret 或工作区外路径。该 procedure 确保 tool request、permission prompt / decision、command result 与 Review artifact 都有可观察记录，同时不向 Agent 暴露 evaluator-only defect name。

`EXP-C08-02` 只比较两个已授权 Provider profile / endpoint route，并固定同一 Model ID / revision、model options 与 capability preflight。`EXP-C08-03` 只比较两个 Model ID / revision，并固定同一 Provider profile、endpoint type、authentication category 与 routing。每个 Experiment 的 A / B 各至少两个顺序交错的 fresh task Run，并从相同 clean baseline 与 Agent-visible input 开始。Provider 与 Model 同时变化的两格不能形成 portability conclusion。

comparability gate 未通过时，对应 Experiment 保持 `PLANNED · NOT EXECUTED`，不填写 Result；只有配对 Run 已真实完成但已登记 confounder 仍无法分离时才填写 `INCONCLUSIVE`。任一 Experiment 未执行时，Cycle 8 Exit Criteria 未满足。config parsed、model listed、provider accepted、tool schema sent、tool requested、tool succeeded、review artifact 与 task completion 必须分别记录。

真实执行开始后，使用 [实验记录模板](../../../templates/experiment-record.template.md) 创建独立 Experiment Record，并为每次执行保存独立 Run Metadata。每个 Run 必须绑定 repository commit、OpenCode version / surface / platform、官方 source commit、Provider / endpoint type、Model ID / revision、脱敏 Configuration、Rule / Skill / Check / Adapter revision、controlled variables、known confounders、evidence 与 human intervention。

不得记录 API Key / token，不访问真实业务服务或工作区外路径，不运行破坏性操作。内容生成阶段不得填写结果、创建 `EVD-*` 或 Support Assessment。
