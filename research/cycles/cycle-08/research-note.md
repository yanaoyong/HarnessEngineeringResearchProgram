# Cycle 08 研究笔记（Research Note）· OpenCode Host Architecture & Model Portability

> 状态（Status）：PLANNED · NOT EXECUTED
>
> 内容 Batch：5

[Cycle 正文](../../../docs/02-Coding-Agent-Host-Model.md) · [研究工作区](../../README.md) · [来源权限（Source Authority）](../../source-authority.md)

## 1. 研究问题（Research Question）

在绑定 OpenCode 版本与官方源码 revision 后，哪些 Agent、Context、Tool、Permission 与 extension 语义由 Host 保持，哪些行为依赖 Provider adapter、endpoint / protocol、Model 与 Configuration，从而使“Model portability”成立、失败或保持 Unknown？

## 2. 为什么与 myharness 有关

OpenCode 是 open-source、multi-provider、vendor-neutral Host reference。myharness 需要知道可移植的是行为语义、Host Adapter 还是只在某个 Provider / Model profile 下成立的结果，不能把配置可解析、模型可选择、工具可见或单次任务完成合并成 portability。

## 3. 研究范围与退出条件（Scope and Exit Criteria）

- 范围（Scope）：官方 Contract；固定 revision 的 Official Source；Config、Rule / Instruction、Agent、Tool、Permission、Skill、Plugin、MCP、Session；Provider adapter、endpoint / protocol、Model capability / option；绑定版本的无破坏性 Direct Behavior 与 Project artifact。
- 范围外（Out of Scope）：浮动分支架构结论、双变量 portability comparison、公开 Model benchmark、企业结论、OpenCode Adapter / Plugin、Cycle 9 abstraction 或 myharness 实现。
- 退出条件（Exit Criteria）：绑定 OpenCode version / surface / platform；通过可复查官方 provenance 将实际执行的 OpenCode artifact 映射到 `anomalyco/opencode` 完整 commit；完成 Contract / Source / Behavior map；真实执行 `EXP-C08-01`；分别完成 `EXP-C08-02` Provider contrast 与 `EXP-C08-03` Model contrast；分离 Host / Provider / endpoint / Model / Configuration effects；为两个对照分别登记 Result 与 scoped `EVD-*`；形成 Mental Model V1。

当前 Exit Criteria 未满足。

## 4. 心智模型 V0（Mental Model V0）

```text
Official Contract + Host Version / Surface
        ↓
Pinned Official Source + Capability Map
        ↓
Host Runtime：Config · Session · Agent · Tool · Permission · Extension
        ↓
Provider Adapter + Endpoint / Protocol + Routing
        ↓
Model ID / Revision + Capability + Options
        ↓
Direct Behavior + Project Artifact
```

这是待验证责任模型，不构成 OpenCode architecture、Model portability、Support Level 或企业结论。

## 5. 证据登记（Evidence Registry）

尚未登记 `EVD-*`。Batch 5 内容生成只登记计划来源，不创建 Contract claim、Source claim、Behavior claim、Project Evidence claim 或 Support Assessment。

### 已登记来源制品（Registered Source Artifacts）

- [`SRC-OPENCODE-001`](evidence/SRC-OPENCODE-001.md)：OpenCode Intro；官方身份、surface 与安装入口。
- [`SRC-OPENCODE-002`](evidence/SRC-OPENCODE-002.md)：Config；配置格式、位置、precedence 与 schema。
- [`SRC-OPENCODE-003`](evidence/SRC-OPENCODE-003.md)：Providers；Provider、authentication、endpoint 与 adapter 配置。
- [`SRC-OPENCODE-004`](evidence/SRC-OPENCODE-004.md)：Models；`provider/model` identity、selection、options 与 capability questions。
- [`SRC-OPENCODE-005`](evidence/SRC-OPENCODE-005.md)：Rules；`AGENTS.md`、instruction source 与 precedence。
- [`SRC-OPENCODE-006`](evidence/SRC-OPENCODE-006.md)：Agents；agent mode、Model、Tool 与 Permission configuration。
- [`SRC-OPENCODE-007`](evidence/SRC-OPENCODE-007.md)：Tools；built-in / custom / MCP tool 与 permission surface。
- [`SRC-OPENCODE-008`](evidence/SRC-OPENCODE-008.md)：Agent Skills；Skill discovery、on-demand load 与 permission。
- [`SRC-OPENCODE-009`](evidence/SRC-OPENCODE-009.md)：Plugins；project / global / package load 与 event / tool extension。
- [`SRC-OPENCODE-010`](evidence/SRC-OPENCODE-010.md)：MCP servers；local / remote server、tool exposure 与 configuration。
- [`SRC-OPENCODE-011`](evidence/SRC-OPENCODE-011.md)：`anomalyco/opencode` 官方源码仓库浮动锚点。
- [`SRC-OPENCODE-012`](evidence/SRC-OPENCODE-012.md)：Permissions；action、rule matching、default、approval 与 per-agent override Contract。

所有页面和源码默认分支都是浮动锚点。执行时必须重新核验访问日期与 Host release；源码必须固定完整 commit、重新定位 source path 并限定 claim scope。

### 契约证据（Contract Evidence）

尚未登记。

### 源码证据（Source Evidence）

尚未登记。`SRC-OPENCODE-011` 的仓库身份已核验，但 commit 为 `NOT PINNED`；固定 revision 前不能派生可复现 Source Evidence。

### 行为证据（Behavior Evidence）

尚未登记。

### 项目证据（Project Evidence）

尚未登记。实验 fixture 与 myharness artifacts 只在执行时按 scope 登记。

### 企业事实（Enterprise Fact）

不在 Cycle 8 当前范围内登记。

### 社区主张（Community Claims）

尚未登记。第三方 Provider adapter、Plugin、patch、架构分析或行为报告只能形成 Open Question，不能替代官方 Contract / Source 或 Direct Behavior。

## 6. 参考模式（Reference Pattern）

使用 `Official Contract → pinned Official Source → Host Runtime → Provider Adapter / endpoint → Model → Direct Behavior` 证据链。每层记录 owner、revision、scope、可支持判断、不可支持判断与 Unknown；portability 必须通过单变量 comparability gate，而不是由配置格式或任务最终成功推导。

## 7. 假设（Hypothesis）

`H-C08-01 · Provider Portability`：在相同 OpenCode version / surface、repository baseline、instruction、tool / permission profile、Model ID / revision、model options 与 T02 instance 下，只切换通过 comparability gate 的 Provider profile / endpoint route，应保持 Host-owned config resolution、instruction source、permission decision owner、Review / artifact route 与 task contract；provider transform、protocol acceptance、tool request / arguments、retry 与 completion path 可以不同。

`H-C08-02 · Model Portability`：在相同 OpenCode version / surface、Provider profile / endpoint / routing、repository baseline、instruction、tool / permission profile 与 T02 instance 下，只切换通过 capability preflight 的 Model ID / revision，应保持相同 Host-owned route 与 task contract；tool use、reasoning、issue detection、evidence quality、false positive、retry 与 completion path 可以不同。

两个 Hypothesis 分别由 `EXP-C08-02` 与 `EXP-C08-03` 裁决。comparability gate 未通过时，对应 Experiment 保持 `NOT EXECUTED`；只有配对 Run 已完成但已登记 confounder 仍无法分离时才使用 `INCONCLUSIVE`。

## 8. 实验（Experiment）

- `EXP-C08-01`：`EXPLORATORY` · `OBSERVATION_ONLY` · `T03 · Medium Change` · Contract → Source → Behavior Architecture Trace。
- T03 instance：`T03-C08-LOCAL-RETRY-BUDGET`。在固定 commit 的隔离 fixture repository 中，为已有本地 job runner 增加可配置 retry budget，修改 config type / parser、validation、runtime use、tests 与用户文档；不访问网络或真实服务。
- T03 acceptance：覆盖字段缺省、合法边界、非法边界、runtime 停止条件与文档示例；保存本地命令、exit code、diff 与 artifact convergence check。
- T03 trace：绑定 OpenCode version / surface / platform、官方页面版本、固定 source commit、configuration precedence、instruction source、agent、tool / permission、extension state、Provider profile、Model、session / task state、Review、artifact 与 human intervention。
- T03 provenance gate：只有通过官方 release / tag provenance、package / binary build metadata 或其他可复查官方材料，把实际执行的 OpenCode artifact 映射到固定 source commit，才可解释 Source / Behavior agreement；映射缺失时 agreement 保持 `UNKNOWN`，且相关 Exit Criteria 未满足。
- `EXP-C08-02`：`COMPARATIVE` · `T02 · Semantic Review` · Provider Portability Comparison。
- T02 instance：对固定 commit 中含 acceptance reference 的有限 patch 作审查。Evaluator-only oracle 记录语义缺陷“重试预算在成功后仍被后续任务复用”与 deterministic defect“新增配置字段未加入边界验证”；oracle 及缺陷名称不得进入 Agent-visible task statement、Rule、context、acceptance reference 或 output schema。
- 强制 Evidence procedure：Agent-visible task 要求先用 read tool 检查预先登记的 implementation、schema 与 test 文件，再运行 fixture 内固定的本地 `./scripts/check-review-fixture`。该 exact command 在共同 permission profile 中设置为 `ask`，每个 Run 由相同 `approve once` Human intervention 处理；命令不访问网络、secret 或工作区外路径。
- Provider contrast：固定同一 Model ID / revision、model options 与 capability preflight，只改变两个已授权 Provider profile / endpoint route；A / B 各至少两个顺序交错的 fresh task Run。
- `EXP-C08-03`：`COMPARATIVE` · `T02 · Semantic Review` · Model Portability Comparison。
- T02 instance 与 Evidence procedure：完全复用 `EXP-C08-02` 的 patch、Agent-visible input、oracle、read file set、local check 与 permission procedure。
- Model contrast：固定同一 Provider profile、endpoint type、authentication category 与 routing，只改变两个通过 tool calling、context / output 与 task compatibility preflight 的 Model ID / revision；A / B 各至少两个顺序交错的 fresh task Run。
- 禁止比较：Provider 与 Model 同时变化的任意两格不能形成 portability conclusion；`EXP-C08-02` 与 `EXP-C08-03` 分别填写 Result 与 scoped `EVD-*`，不得互相替代。
- 安全边界（Safety Boundary）：不记录 API Key / token，不访问真实业务服务或工作区外路径，不运行破坏性操作。
- 运行元数据（Run Metadata）：尚未创建。
- Outcome / Result：均尚未运行；`EXP-C08-01` 执行后记录 Observation Outcome，Experiment Result 为 `NOT APPLICABLE · OBSERVATION ONLY`；`EXP-C08-02/03` 才填写 Hypothesis Result。
- 历史映射（Legacy Mapping）：无；Cycle 8 是 V4.2 新增 Cycle。

## 9. 观察（Observation）

无。研究执行尚未开始。

## 10. 矛盾证据与限制（Contradictory Evidence and Limitations）

- 官方页面是浮动 Contract anchor，不证明本地配置已加载、Behavior 已验证或所有 surface 等价。
- 官方源码仓库的默认开发分支会变化；固定 commit 前不得形成可复现 Source Evidence。
- Source implementation 不自动证明安装版本采用、配置启用、未来 Contract 或所有 Provider / Model 组合行为。
- Provider、endpoint / protocol、authentication、routing、quota、Model revision、tool capability、context / output limit 与 options 都可能污染 portability comparison。
- config parsed、model listed、provider accepted、tool schema sent、tool requested、tool succeeded、review produced 与 task completed 是不同 observation。
- 如果 comparability gate 无法满足，对应 Experiment 保持 `PLANNED · NOT EXECUTED`，不得填写 Result；只有真实配对 Run 完成但 Evidence 仍不足以分离 effect 时才填写 `INCONCLUSIVE`。任一 portability Experiment 未执行时，Cycle 8 Exit Criteria 未满足。

## 11. 心智模型 V1（Mental Model V1）

等待实验与证据。

## 12. 设计判断（Design Judgment）

待定。不实现 OpenCode Adapter / Plugin，不分配任何 OpenCode 支持等级，不形成 Model benchmark、普遍 portability 或 enterprise conclusion。

## 13. 开放问题（Open Questions）

source revision、surface parity 与 Provider / Model comparability 由 [Open Questions](../../open-questions.md) 跟踪。跨 Host portable semantic contract 转交 Cycle 9。

## 14. 路线复盘触发条件（Route Review Trigger）

Cycle 8 Exit Criteria 满足后创建 Batch 5 Route Review；若固定 Source 与 Contract 显著冲突，或 Direct Behavior 推翻 Host / Provider / Model 分层，则提前触发并记录原因。
