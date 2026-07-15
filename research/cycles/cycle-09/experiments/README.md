# Cycle 09 实验工作区（Experiment Workspace）

> 状态（Status）：PREPARED · NOT EXECUTED

本目录为后续研究执行准备两个计划实验：

- `EXP-C09-01` · Four-host Semantic Capability Trace
- `EXP-C09-02` · Naive Artifact Port vs Portable Semantic Contract

## 共同门禁

任一 Host Run 开始前必须绑定 Host version、surface、platform、installation channel、官方 Contract anchor、Provider profile、endpoint type、Model ID / revision、脱敏 Configuration、repository commit、task instance、tool / permission profile、acceptance / review procedure 与 Human intervention policy。

Source authority 按 Host 分开处理：Claude Code 不以第三方实现填补未公开 Runtime；Codex Source claim 固定 `openai/codex` commit；ZCode Runtime Source Authority Gate 未通过时不创建 Source architecture claim；OpenCode Source / Behavior agreement 需要执行 artifact 到固定 commit 的可复查 provenance。surface parity 未验证时只研究实际运行 surface。

门禁未通过时，对应 stratum 保持 `PLANNED · NOT EXECUTED / UNKNOWN`，不填写 Result，也不改写为 `UNSUPPORTED`。

## `EXP-C09-01` · Four-host Semantic Capability Trace

- 类型：`EXPLORATORY`
- Outcome Mode：`OBSERVATION_ONLY`
- Stable Task：`T01 · Engineering Constraint`
- Task Instance：`T01-C09-LOCAL-HTTP-TIMEOUT`
- Fixture：在相同固定 commit 的隔离 repository 中，为已有本地 HTTP client 增加显式、非默认、可配置 timeout；不访问网络或真实服务。
- Acceptance：本地 fixture 覆盖字段缺省、合法配置、非法配置与 request construction，保存命令、exit code、diff 与 deterministic result。
- Host strata：Claude Code、Codex、ZCode、OpenCode 分别执行并使用独立 Run Metadata；每个 stratum 只绑定一个明确 surface。
- Trace：instruction / rule source、Skill discovery / activation state、actual tool set、read / edit / command request、permission owner / decision、Hook / lifecycle observation、task / session state、acceptance、artifact、human intervention 与 Unknown。
- Boundary：Provider / Model 无法保持相同时，只观察 semantic route 与 responsibility boundary，不比较 outcome quality、不归因 Host performance。

`EXP-C09-01` 只产生 capability question map 与 scoped observation，不裁决 `H-C09-01`，也不能把一次 trace 写成 capability support。完成记录使用 `COMPLETE / PARTIAL / INVALIDATED` Observation Outcome，Experiment Result 固定为 `NOT APPLICABLE · OBSERVATION ONLY`。

## `EXP-C09-02` · Naive Artifact Port vs Portable Semantic Contract

- 类型：`COMPARATIVE`
- Outcome Mode：`HYPOTHESIS_RESULT`
- Stable Task：`T02 · Semantic Review`
- 历史映射：`EXP-W07-01`
- Project Artifact Gate：选择一个已有、revision 可固定并具备 source-host Behavior baseline 的 myharness code-review 或 research-discovery capability。若不存在，保持 `NOT EXECUTED`；不得临时实现完整 capability 只为填表。
- T02：固定 patch、Agent-visible task、acceptance reference、evaluator-only oracle 与 output schema；oracle 至少含一个需语义推理问题和一个 deterministic defect，答案不得泄漏给 Agent。
- Baseline A：只做目标 Host 能加载所需的最小包装 / 路径调整与显眼 Tool 名替换，不预先提取 Portable Semantic Contract，也不故意制造无效 artifact。
- Variant B：保持 capability Intent / Procedure，先提取 Trigger、Preconditions、Required Context、Action Vocabulary、Evidence、Completion、Failure Route、Human Intervention 与 Limitations，再用 Host Adapter 映射 discovery / bootstrap、tool、permission、lifecycle、distribution、state、observability 与 degradation。
- Source / target derivation：从 `Claude Code / Codex / ZCode / OpenCode` 中绑定一个具备可复查 Behavior baseline 的 `source_host`，然后计算 `target_hosts = four_hosts - {source_host}`。默认 Claude 为 source 时，targets 才是 Codex、ZCode、OpenCode。Route Review 更换 source 时必须使旧 target plan 失效并重算 targets；source 与 target 不得重合，不得遗漏剩余主要 Host。source artifact 不属于四宿主时保持 `NOT EXECUTED` 并 Route Review，不引入第五个 Host。
- Target strata：`EXP-C09-02` 的 Result Unit 是 `HOST`，Stratum Key 是 `target_host`。在同一个 Experiment Record 中，重算后的每个 target Host 使用独立 stratum section，分别保存 A / B Run group、Result、限制与 scoped `EVD-*`；不得为同一 Experiment ID 创建相互冲突的单 Result 记录。
- Controlled Variables：同一目标 Host 内固定 task、Host version / surface、Provider profile、Model、Configuration、permission、source capability revision、acceptance / review 与 Human intervention。
- Replication：每个可执行目标 A / B 各至少两个 fresh task Run，顺序交错，从相同 clean baseline 与 Agent-visible input 开始。
- Observations：format load、discovery、activation、required context、procedure checkpoints、action / permission mapping、evidence citation、deterministic verification、completion、silent degradation、Host leakage、false positive / completion、Context / maintenance cost 与 human intervention。

每个 target stratum 必须在首个 Run 前冻结 Contract revision、Adapter revision 和主要裁决表。一个 replication block 包含从同一 clean baseline 和相同 Agent-visible input 开始的一个 A Run 与一个 B Run；第一个 block 的先后顺序预先决定，第二个 block 反转顺序：

- 主要 checkpoint：discovery、activation、required-context delivery、预声明 procedure checkpoints、evidence citation、deterministic verification、completion 和 degradation reporting，每项按 `PASS / FAIL / UNKNOWN` 记录。
- Critical failure：Host leakage、silent degradation 和 false completion，每类独立记录。
- Secondary trade-off：Context / maintenance cost 与 human intervention；不得在看到结果后用它们改写主要裁决方向。如使用 budget，threshold 必须预先固定。

| Result | 目标 Host 内的裁决规则 |
|---|---|
| `SUPPORT` | 两个顺序交错 replication block 中，B 相对 A 至少有一项预声明主要 checkpoint 持续改善或一类 critical failure 持续减少，没有新增主要退化 / critical failure，且差异可追溯到 porting method |
| `REJECT` | A / B 在全部预声明主要项上相同且 B 无方向性增益，或 B 在两个 block 中持续新增主要退化 / critical failure 而无主要改善；差异必须排除已知 confounder |
| `INCONCLUSIVE` | replication 方向不一致、主要指标出现未预声明互换、必需项为 `UNKNOWN`、trace 不完整或 confounder 无法分离 |

一个目标 Host 的 Result 不能替代另一个；至少两个目标 strata 完成前不形成 cross-host Hypothesis Result。不同 Provider / Model 条件下的结果不汇总为 Host 或 Model 排名。

cross-host Experiment Result 使用以下预注册聚合规则：至少两个 target strata 已完成时，两个或以上 `SUPPORT` 且没有 `REJECT` 才为 `SUPPORT`；两个或以上 `REJECT` 且没有 `SUPPORT` 才为 `REJECT`；其余已达到最小完成数的组合均为 `INCONCLUSIVE`。不足两个已完成 strata 时，Experiment-level Result 为 `NOT APPLICABLE — insufficient completed strata`，不得填写 `INCONCLUSIVE` 代替未执行。

`SUPPORT` 只是绑定 target Host / capability slice 下的方向性 Hypothesis Result，不自动确定 Mapping Disposition、四宿主 portability 或 S1–S4。

真实执行开始后，使用 [实验记录模板](../../../templates/experiment-record.template.md) 为每个 Experiment ID 创建一个 Experiment Record，并为每次执行保存独立 Run Metadata。内容生成阶段不得创建 Run、Adapter implementation、Result、`EVD-*` 或 Support Assessment。
