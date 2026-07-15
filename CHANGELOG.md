# Changelog

## V4.2 Post-Batch 8 content review corrections · 2026-07-15

本轮只修复 Batch 0–8 内容审查发现的协议与溯源问题，不执行研究、不创建 Result、`EVD-*`、实现或 Support Assessment。

### Changed

- 将仓库级任务说明从“生成 Batch 8”更新为 Batch 1–8 / Cycle 1–18 内容已完成，避免后续重复迁移。
- 以 Batch 0 审查后澄清的方式分离 Run outcome 与 Experiment Result：Run 不再填写 `SUPPORT / REJECT / INCONCLUSIVE`。
- 为 Experiment Record 增加 Result cardinality、stratum result 与 aggregation rule；Cycle 9 使用 `HOST` / `target_host`，Cycle 12 使用 `TASK_INSTANCE` / `task_instance_id`。
- 为 `EXPLORATORY` 增加独立 Outcome Mode；observation-only trace 使用 `COMPLETE / PARTIAL / INVALIDATED`，不再被迫填写 Hypothesis Result。
- 为 Run Metadata 增加 Harness-under-test cell、H0 / H1 revision、implementation artifact 与 task-fixture relationship，支持 Cycle 17/18 的 B0 / A0 / A1 溯源。
- 明确 Cycle 14 内容生成阶段不创建 `EVD-*`，但真实执行后任何进入后续 Cycle 的可复用 claim 都必须派生 scoped `EVD-*`。
- 将重复登记的 learn-claude-code、Superpowers、ACE、mini-swe-agent 与 SWE-agent ACI paper 归一到最早稳定 Source ID，并移除六个未派生 Evidence 的重复条目。

### Boundaries

- 不改变 18 个 Cycle 的冻结名称、顺序、Batch 边界或历史实验映射。
- 不声称任何计划实验已经执行，也不改变任何 Host 的 Support Level。

## V4.2 Batch 8 · 2026-07-15

Batch 8 将 V4.1 Week 13–16 迁移为 Cycle 15–18「myharness Integration Research」正文与计划态 Research Note。18 个 Cycle 的内容生成已经完成，但研究执行尚未开始；没有 Run、`EVD-*`、架构 Finding、ADR Candidate、实现、Design Belief、Route Review 结果或 Support Assessment。

### Added

- 新增 Cycle 15–18：Read-only Architecture Audit、Hypothesis & ADR Candidate、Minimal Implementation Experiment、Acceptance、Ablation & Design Beliefs。
- 新增 `cycle-15` 至 `cycle-18` 的计划工作区；evidence 目录只包含准备边界，不创建新的 `SRC-*` 或 `EVD-*`。
- 新增 `EXP-C15-01`、`EXP-C16-01`、`EXP-C17-01..03` candidate family 与 `EXP-C18-01..12` candidate × Host family 计划设计，并保留 `EXP-W13-01` 至 `EXP-W16-01` historical mapping。
- 新增 `OQ-015..018`，跟踪 audit packet authority、candidate score stability、minimal implementation isolation 与 ablation matrix parity。

### Changed

- 将只读审计收敛为覆盖八个维度和全部 artifact families 的 Coverage Matrix、8 个 T02 packets / 16 个 Agent Run；`No Finding` 必须通过 evaluator critical-issue gate，禁止从旧路径缺失直接推导 capability 缺失。
- 将 Cycle 16 的 Top3 改为“至多三个”合格候选；评分只暴露取舍，Evidence / Reversibility gate 优先，候选状态保持 `PROPOSED`。
- 将 Cycle 17 拆成 one-time H1 build 与候选级独立 A0 / A1 T03 task Runs；Run 使用共同 task-fixture baseline，H0 / H1 Harness revisions 单独绑定，并保留隔离 worktree 与实际 rollback verification。
- 将 Cycle 18 拆成 candidate × Host 独立 Experiment Records，每个记录只有一个 Hypothesis / Result；加入 2 个 activation-positive tasks、1 个 non-trigger control 与 Applicability Matrix。
- 明确 Batch 8 内容生成不创建 `EVD-*`，但 Cycle 15 真实执行后必须为复用 Finding / No Finding claim 派生 scoped `EVD-*`，供 Cycle 16 使用。
- 收紧 ADR Candidate、Route Review 与 Design Beliefs 目录门禁，明确内容生成阶段没有实际条目。
- 刷新总览、Research Infrastructure、Workspace、Cycle index 与 Atlas，使计划态内容基线推进到 Batch 1–8 / Cycle 1–18。

### Boundaries

- 不执行 myharness 审计，不创建实际 Finding、ADR Candidate、implementation diff、Run、Decision Update 或 Design Belief。
- 不实现或合并 myharness feature / Host Adapter，不把实现完成、测试通过或小样本结果写成普遍架构结论。
- 内容生成不满足 Cycle 15–18 Exit Criteria，也不表示 V4.2 研究执行完成或任一 Host 达到 S1–S4。

## V4.2 Batch 7 · 2026-07-15

Batch 7 将 V4.1 Week 8–12 迁移为 Cycle 10–14「Harness Engineering Research Themes」正文与计划态 Research Note。研究执行尚未开始；没有 Run、`EVD-*`、Design Judgment、ADR、实现或 Support Assessment。

### Added

- 新增 Cycle 10–14：Skill Behavior & Evaluation、Change Contract & Convergence、Adaptive Workflow、Context Lifecycle & Session Handoff、Knowledge Ratification & Harness Minimalism。
- 新增 `cycle-10` 至 `cycle-14` 的计划工作区，以及 `SRC-HARNESS-001..014` 来源登记。
- 新增 `EXP-C10-01/02`、`EXP-C11-01`、`EXP-C12-01/02`、`EXP-C13-01` 与 `EXP-C14-01` 计划设计，使用 T01–T03，并保留 `EXP-W08-01` 至 `EXP-W12-01` historical mapping。
- 新增 `OQ-010..014`，跟踪 Skill observability、Change oracle、risk classifier、handoff comparability 与 ratification threshold。

### Changed

- 把 Skill Discovery、Activation、Execution、Evidence 与 Outcome 分开，V1→V2 与 V2→V3 分别解释 description bundle 与 behavior-contract bundle。
- 把人工 Change truth map 定位为 evaluator-only oracle，不作为 Agent variant；CodeGraph 只允许独立 exploratory stratum。
- 把 Adaptive Workflow 定义为预注册 risk route、mandatory gate 与 escalation，而不是 Agent 自由跳阶段。
- 将单任务 handoff 设计收敛为 exploratory trace，明确禁止 mode superiority claim。
- 将 knowledge ratification 与 future reliability 分开，允许 `Nothing`，并要求 owner、revalidation trigger 与 removal condition。
- 将 Cycle 10 拆成 Discovery / Activation 与显式激活后的 Behavior 两个实验，并冻结 query split、最低 Run 数与 Result threshold。
- 将 Cycle 12 的低风险 README task 恢复为 T01，Hook / Plugin medium changes 保持 T03；所有 A / B 使用同一 task instance。
- 恢复 Cycle 13 的 Resume、prose summary、structured handoff 与 Changes artifact 四种独立 mode，并区分 Host session identity 与 execution episode。
- 使 Cycle 14 的十个正式 packet 全部满足 T02 Contract，明确 Agent reviewer 与人工 evaluator-only reference 的责任。
- 将 Spec Kit、BMAD 的官方文档 Contract 与源码 Source 分成独立 Source Registry entries；ACI 论文固定到 arXiv v3 URL。
- 刷新 Reference Project Atlas 的 Batch 7 active overlay；所有默认分支保持浮动、执行时固定 commit。

### Boundaries

- 不生成 Cycle 15–18 正文或目录，不实现 Batch 8。
- 不修改 myharness Skill、Change、workflow、handoff、memory 或 standards 实现。
- 内容生成不满足 Cycle 10–14 Exit Criteria，不产生 Route Review、ADR Candidate 或 S1–S4。

## V4.2 Batch 6 · 2026-07-15

Batch 6 将 V4.1 Week 7 迁移为 Cycle 9「Four-host Harness Abstraction」正文与计划态 Research Note。研究执行尚未开始；没有 Run、`EVD-*`、Adapter implementation、portability result 或 Support Assessment。

### Added

- 建立 `Portable Semantic Contract → Capability Requirement → Host Adapter → Bound Host / Provider / Model / Configuration → Direct Behavior / Project Artifact` 工作模型。
- 定义 `DIRECT / ADAPTED / DEGRADED / HOST_SPECIFIC / UNSUPPORTED / UNKNOWN` 局部 Mapping Disposition，并明确它不替代 S0–S4 Support Level。
- 设计 `EXP-C09-01` T01 Four-host Semantic Capability Trace；四个 Host 分别绑定 version / surface / Provider / Model / Configuration 与独立 Run Metadata。
- 将 V4.1 `EXP-W07-01` 迁移为 `EXP-C09-02` T02 Naive Artifact Port vs Portable Semantic Contract；在默认 Claude source baseline 下，Codex、ZCode、OpenCode 目标 strata 分别建立 A / B Run group、Result 与 scoped Evidence，不互相替代。
- 为 `EXP-C09-02` 预注册 checkpoint / critical-failure 裁决表、replication block 配对规则与 `SUPPORT / REJECT / INCONCLUSIVE` 条件；source Host 变更时按 `target_hosts = four_hosts - {source_host}` 重算目标。
- 新增 Cross-host Evidence Readiness Gate，保留 Claude Code、Codex、ZCode 与 OpenCode 不同 Source Authority；未通过 Gate 的 Host 使用 `NOT EXECUTED / UNKNOWN`，不伪装为 `UNSUPPORTED`。
- 新增 `cycle-09` 计划工作区与 `SRC-CROSSHOST-001..005`，登记 Agent Skills Overview / Specification / client implementor guide、Superpowers porting guide 与 Open Harness current repository 浮动锚点。

### Changed

- 更新 README、总纲、Research Infrastructure、Workspace、Cycle index 与 Atlas，使内容基线推进到 Batch 1–6 / Cycle 1–9。
- 将 Agent Skills format compatibility、Host discovery / activation、procedure execution、Evidence 与 Completion 分开；文件、目录、Tool 名或 Plugin packaging 相同不等于 semantic portability。
- 刷新 V4.1 OpenHarness 锚点：当前 README 主要定位为 Docker sandbox / long-lived workspace，因此旧 `.oh` primitive / provider surface 只保留为历史迁移线索，不再作为 Cycle 9 主锚点。
- 新增四宿主 target comparability Open Question，并继续保留 Codex / OpenCode surface parity、OpenCode provenance 与 Provider / Model comparability 边界。

### Validation Boundary

- 内容生成不满足 Cycle 9 Exit Criteria，不创建 Route Review 结果，也不表示任一 Host 或 capability 已达到 S1–S4。
- 不运行四个 Host，不实现或合并 myharness Adapter，不形成跨四宿主普遍可移植性、公开模型排名、企业或法律结论。
- 不生成 Cycle 10–18 正文，不实现 Batch 7。

## V4.2 Batch 5 · 2026-07-14

Batch 5 生成 OpenCode Host 的 Cycle 8 正文与计划态 Research Note。研究执行尚未开始；没有 Run、`EVD-*`、实验结果、已固定 Source Evidence、Model portability conclusion 或 Support Assessment。

### Added

- 新增 Cycle 8「OpenCode Host Architecture & Model Portability」；该 Cycle 是 V4.2 新内容，没有 V4.1 Week / `EXP-Wxx-yy` 迁移对象。
- 建立 Official Contract → pinned Official Source → Host Runtime → Provider Adapter / endpoint protocol → Model → Direct Behavior 工作模型，要求 Host、Provider、endpoint / protocol、Model 与 Configuration effects 分开记录。
- 设计 `EXP-C08-01` T03 Contract → Source → Behavior architecture trace；执行时必须固定 `anomalyco/opencode` 完整 commit，并通过官方 provenance 或可复查 build metadata 将实际执行 artifact 映射到该 commit，再按 capability 重新定位 source path。
- 分别设计 `EXP-C08-02` T02 Provider Portability Comparison 与 `EXP-C08-03` T02 Model Portability Comparison；两者使用独立 Experiment Record、Result 与 scoped Evidence，缺少可比 profile 时保持 `NOT EXECUTED`，不得用不同 Provider 与不同 Model 同时变化的两格比较声称 portability。
- 为 T02 对照加入受控 tool / permission observation：固定 read file set 与本地检查命令，将 exact command 设为 `ask`，各 Run 使用相同 `approve once` Human intervention。
- 新增 `cycle-08` 计划工作区、实验说明与 `SRC-OPENCODE-001..012`，登记 Intro、Config、Providers、Models、Rules、Agents、Tools、Permissions、Skills、Plugins、MCP 与官方源码仓库浮动锚点。

### Changed

- 更新总览、研究计划、Research Infrastructure、Workspace、Cycle index 与 Atlas，使内容基线推进到 Batch 1–5 / Cycle 1–8。
- 更新仓库级任务说明，使当前生成范围收敛为 Batch 5 / Cycle 8，禁止创建 Cycle 9–18 目录与正文。
- 新增 OpenCode artifact-to-source provenance、surface parity 与 Provider / Model 可比性 Open Questions；官方文档和浮动默认分支不被当成已执行 Evidence。

### Validation Boundary

- 内容生成不满足 Cycle 8 Exit Criteria，不创建 Route Review 结果，也不表示 OpenCode 已达到 S1–S4。
- 不实现 OpenCode Adapter / Plugin，不运行 OpenCode，不记录 credential，不形成跨 Provider / Model 普遍可移植性、性能排名、安全保证或企业结论。
- 不生成 Cycle 9–18 正文，不实现 Batch 6。

## V4.2 Batch 4 · 2026-07-14

Batch 4 生成 ZCode Host 的 Cycle 7 正文与计划态 Research Note。研究执行尚未开始；没有 Run、`EVD-*`、`ENT-*`、实验结果、Runtime Source Evidence、Support Assessment 或法律合规结论。

### Added

- 新增 Cycle 7「ZCode Host Contract & Enterprise Reality」；该 Cycle 是 V4.2 新内容，没有 V4.1 Week / `EXP-Wxx-yy` 迁移对象。
- 建立 Product identity → Contract → Provider Profile → Local Configuration → Direct Behavior → Enterprise Fact 工作模型，要求 Host、Provider、endpoint、Model、Configuration 与 deployment effect 分开记录。
- 明确记录 ZCode Agent / desktop and remote Runtime Source Authority Gate 为 `NOT VERIFIED`，repository / revision 保持 `Unknown`；官方产品文档不被升级为 Runtime Source Evidence。
- 设计 `EXP-C07-01` T01 Contract → Configuration → Behavior trace，使用本地、可逆的 `retry_limit` parser fixture 和脱敏配置快照。
- 设计 `EXP-C07-02` T02 Provider Profile comparison，固定 patch、task、Host、permission 与 Review procedure，要求两个 profile 的 fresh-task 重复 Run；只有已执行的配对 Run 仍无法分离 Model / endpoint policy / quota confounder 时才使用 `INCONCLUSIVE`，无法取得授权 profile 时保持 `NOT EXECUTED`。
- 新增 `cycle-07` 计划工作区、实验说明与 `SRC-ZCODE-001..009`，登记用户协议、Agent、`AGENTS.md` 项目指令、模型连接、安全确认、远程开发、隐私、Changelog 与反馈支持官方浮动锚点。
- 定义 installation、identity、Provider / network、data、logging、upgrade、remote execution、support 与 procurement 的 Enterprise Reality 检查面；没有组织证据时保持 `Unknown`。

### Changed

- 更新总览、研究计划、Research Infrastructure、Workspace、Cycle index 与 Atlas，使内容基线推进到 Batch 1–4 / Cycle 1–7。
- 更新 OQ-001：已登记官方产品与 Contract 入口，但仍未发现由官方入口指认且满足五项 Gate criteria 的 Runtime source repository。
- 更新仓库级任务说明，使当前生成范围收敛为 Batch 4 / Cycle 7，禁止创建 Cycle 8–18 目录与正文。
- 根据 Batch 4 审查，将 Tool 观察拆成 Host-side exposure / filtering policy、actual exposed tool set、Provider / Model tool-calling capability 与实际 request / success，并把 T02 缺陷答案隔离为 evaluator-only oracle。

### Validation Boundary

- 内容生成不满足 Cycle 7 Exit Criteria，不创建 Route Review 结果，也不表示 ZCode 已达到 S1–S4。
- 不实现 ZCode Plugin / Adapter，不运行 ZCode，不测试权限绕过，不记录 credential，不形成 private deployment、SLA、数据驻留、安全保证或通用法律合规结论。
- 不生成 Cycle 8–18 正文，不实现 Batch 5。

## V4.2 Batch 3 · 2026-07-14

Batch 3 生成 Codex Host 的 Cycle 5–6 正文与计划态 Research Note。研究执行尚未开始；没有 Run、`EVD-*`、实验结果、已验证 Runtime architecture 或 Support Assessment。

### Codex Host 内容（Host Content）

- 将 V4.1 Week 5–6 迁移为 Cycle 5「Codex Architecture & Customization」与 Cycle 6「Codex Execution、Safety & State」。
- 为两个 Cycle 增加单一核心 Research Question、scope、Mental Model V0、可证伪 Hypothesis、Exit Criteria 与 Route Review trigger。
- 将 `EXP-W05-01` 拆分为 `EXP-C05-01` Contract → Source → Behavior architecture trace、`EXP-C05-02` Skill description、`EXP-C05-03` AGENTS hierarchy 与 `EXP-C05-04` Plugin distribution / load 四项设计，完整保留 V4.1 Week 5 的迁移覆盖。
- 将 `EXP-W06-01` 拆分为 `EXP-C06-01` 无破坏性 execution / state trace 与 `EXP-C06-02` Host hard-deny / Harness guard shadowing 配对对照。
- 将实验分别对齐 `T03 · Medium Change`、`T02 · Semantic Review` 与 `T01 · Engineering Constraint`，要求每个 Run / variant 使用独立 Run Metadata。
- 根据 Batch 3 审查，为 Cycle 6 固定真实的小型可逆 T01 修改、deterministic acceptance checks、隔离 marker effect、决策顺序分类、统一 recovery profile 与强制 fresh-run State checkpoint；只观察到一个 deny 时不得声称 Double Block。

### 来源权限（Source Authority）

- 登记当前 Codex Customization、AGENTS.md、Skills、Plugins、Rules、Hooks、Sandbox、Agent approvals & security 与 Config basics 的计划态官方 Contract 锚点。
- 将所有官方页面标记为执行时绑定 Codex version / surface / platform 并重新核验的浮动锚点；文档存在不等于本地配置已加载或 Behavior 已验证。
- 将 `openai/codex` 登记为官方 Source 仓库浮动锚点，但 commit 明确标记为 `NOT PINNED`；执行时固定完整 commit、重新定位 source path 与 claim scope 后才能派生 Source Evidence。
- 明确 Contract、Source 与 Behavior 必须分开登记；源码存在不证明当前安装版本采用、启用或公开承诺该实现。

### 研究工作区（Research Workspace）

- 新增 `cycle-05` 与 `cycle-06` 的非空计划态 Research Note。
- 为两个 Cycle 准备 `experiments/` 与 `evidence/`，只登记 Source artifact，不创建 Experiment Record、Run record 或 `EVD-*`。
- 明确内容生成不满足 Exit Criteria，不创建 Route Review 结果，也不表示 Codex 已达到 S1–S4。

### 非目标（Non-goals）

- 不生成 Cycle 7–18 正文，不实现 Batch 4。
- 不执行 Codex 实验，不形成未绑定 revision / version 的 architecture、Behavior 或安全结论。
- 不修改 myharness guard / Plugin，不实现 Adapter，也不运行危险或破坏性安全场景；Plugin 实验只能复用无需修改的既有 capability，否则保持 `NOT EXECUTED`。

## V4.2 Batch 2 · 2026-07-14

Batch 2 生成 Claude Code Host 的 Cycle 3–4 正文与计划态 Research Note。研究执行尚未开始；没有 Run、`EVD-*`、实验结果或 Support Assessment。

### Claude Code Host 内容（Host Content）

- 将 V4.1 Week 3–4 迁移为 Cycle 3「Claude Code Context Lifecycle」与 Cycle 4「Claude Code Extension & Control Surface」。
- 为两个 Cycle 增加单一核心 Research Question、scope、Mental Model V0、可证伪 Hypothesis、Exit Criteria 与 Route Review trigger。
- 将 `EXP-W03-01`、`EXP-W04-01` 保留为 historical plan mapping；新设计使用 `EXP-C03-01`、`EXP-C03-02` 与 `EXP-C04-01`。
- 将 Context trace 对齐 `T03 · Medium Change`，将 Rule / Skill / Check 对照对齐 `T01 · Engineering Constraint`，并要求所有 variant 使用独立 Run Metadata。
- 根据 Batch 2 审查，将 Cycle 3 拆分为探索性 lifecycle trace 与必做的受控 `/compact` 对照；将 Cycle 4 收敛为各 variant 共用的 timeout-only acceptance contract，把 fallback / degradation 保留为 Open Question。
- 在 `docs/02` 中继续保留 V4.1 Week 5–6，明确标记为 Batch 3 待迁移 historical baseline，未生成 Cycle 5–6 正文。

### 来源权限（Source Authority）

- 登记 Claude Code Context、Sessions、Memory、How Claude Code Works、Extension Overview、Hooks、Subagents 与 Plugins 的计划态官方 Contract 锚点。
- 将所有官方页面标记为执行时绑定 Host version 并重新核验的浮动锚点；文档存在不等于本地 Behavior 已验证。
- 更新 `learn-claude-code` 的 current / legacy track 风险，要求按 capability 重新定位并在执行时固定 commit；教学实现不能证明 Claude Code Runtime architecture。
- 将 HumanLayer ACE 限定为 Community Reference，只能形成 Reference Pattern / Open Question，不能证明 Claude Code Contract 或 Behavior。

### 研究工作区（Research Workspace）

- 新增 `cycle-03` 与 `cycle-04` 的非空计划态 Research Note。
- 为两个 Cycle 准备 `experiments/` 与 `evidence/`，只登记 Source artifact，不创建 Experiment Record、Run record 或 `EVD-*`。
- 明确内容生成不满足 Exit Criteria，不创建 Route Review 结果，也不表示 Claude Code 已达到 S1–S4。

### 非目标（Non-goals）

- 不生成 Cycle 5–18 正文，不实现 Batch 3。
- 不执行 Claude Code 实验，不形成未公开 Runtime architecture 或 Behavior 结论。
- 不修改 myharness feature，不实现 Adapter、OpenCode Adapter 或 ZCode Plugin。

## V4.2 Batch 1 · 2026-07-14

Batch 1 生成 Foundation 的 Cycle 1–2 正文与计划态 Research Note。研究执行尚未开始；没有 Run、Evidence claim、实验结果或 Support Assessment。

### 基础内容（Foundation Content）

- 将 V4.1 Week 1–2 迁移为 Cycle 1「Coding Agent 最小模型」与 Cycle 2「Harness Primitive」。
- 为每个 Cycle 增加单一核心 Research Question、scope、Mental Model V0、可证伪 Hypothesis、Exit Criteria 与 Route Review trigger。
- 将 V4.1 `EXP-W01-01`、`EXP-W02-01` 保留为 historical plan mapping；新设计使用 `EXP-C01-01`、`EXP-C02-01`、`EXP-C02-02`。
- 将实验映射到 T01–T03，并拆分 V4.1 Cycle 2 多变量设计，避免 Task State 与 Subagent Boundary 同时变化。

### 来源权限（Source Authority）

- 登记 SWE-agent minimal tutorial、mini-swe-agent、SWE-agent ACI paper 与 learn-claude-code 的计划态浮动锚点；执行时重新核验并固定 commit。
- 要求真正执行时固定 repository commit，不把浮动默认分支当成可复现 Source Evidence。
- 明确 learn-claude-code 是教学重实现，不能证明 Claude Code 官方 Runtime architecture、lifecycle event 或 Contract。

### 研究工作区（Research Workspace）

- 新增 `cycle-01` 与 `cycle-02` 的非空计划态 Research Note。
- 为 `cycle-01` 与 `cycle-02` 预先准备 `experiments/` 与 `evidence/` 工作区，供后续实现；不创建 Cycle 3–18 workspace。
- 根据 repository owner 决定澄清工作区规则：当前内容 Batch 可以在实验执行前准备对应 Cycle 目录，但目录存在不表示实验已执行。
- 明确区分内容生成与研究执行；所有 Evidence、结果和 Design Judgment 保持 pending。

### 非目标（Non-goals）

- 不生成 Cycle 3–18 正文，不实现 Batch 2。
- 不执行 T01–T03，不伪造 Run、`EVD-*` 或 S1–S4。
- 不实现 myharness feature、OpenCode Adapter、ZCode Plugin 或其他 Host Adapter。

## V4.2 Batch 0 · 2026-07-14

V4.2 Batch 0 只冻结公共研究协议。Batch 1 与 Cycle 1–18 正文尚未生成。

### Program Protocol

- 将 Program 从 16 Week 调整为 18 Cycle，并冻结 Cycle 名称、顺序、8 个 Phase 与 Batch 1–8 边界。
- 增加 ZCode 与 OpenCode 研究角色，将原 Week 7 之后内容顺延到 Cycle 9–18。
- 保留 V4.1 内容文件和 `EXP-Wxx-yy` 作为后续内容 Batch 的迁移基线。

### Evidence and Evaluation

- 冻结公共术语以及 Contract、Source、Behavior、Project、Enterprise、Community 六类来源。
- 增加 ZCode Source Authority Gate；未验证官方 Runtime source 时禁止源码架构结论。
- 增加 `T01 · Engineering Constraint`、`T02 · Semantic Review`、`T03 · Medium Change`。
- 新实验使用 `EXP-Cxx-yy`，Run Metadata 分离 Host、Provider、Model、配置、revision、confounder、Evidence 与人工干预。
- 增加 S0–S4 Host Support Levels，且不预设任何 Host 已达到 S1–S4。

### Research Workspace

- 新研究工作区使用 `cycle-xx/`，但不预创建 Cycle 目录。
- 增加 Source Registry、Host Profile、Provider Profile 与 Enterprise Readiness Fact Sheet 模板。

### Non-goals

- 不生成 Cycle 正文，不实现 Batch 1、myharness feature、OpenCode Adapter 或 ZCode Plugin。
- 不创建法律合规结论，不提交或推送。

## V4.1 · 2026-07-09

V4.1 是文档工程与研究基础设施修订，不改变 Week 1–16 的核心研究主题和顺序。

### Documentation Engineering

- 清理 16 个 Week 的 Word / Pandoc HTML 核心问题表格，改为原生 Markdown。
- 每个 Week 的实践增加 `EXP-Wxx-01` Experiment ID。
- 每个 Experiment 标注 `EXPLORATORY / COMPARATIVE / ABLATION`。
- 将跨 Week 的全局步骤编号改为 Week 内局部编号。
- Week 4 比较实验改为共享 Rule baseline，减少多变量混杂。
- Week 11 明确 Handoff Modes 为 exploratory qualitative evidence。

### Research Infrastructure

- 补充 ADR Candidate Template。
- 补充 Open Questions / Research Backlog。
- 补充每 2–4 个研究循环一次的 Route Review。
- 增加轻量 `research/` 工作区与可复制模板。
- 不预创建 16 个空 Week 目录，按真实研究自然生长。

### Research Navigation

- Week 7 将 `Superpowers docs/porting-to-a-new-harness.md` 升级为 L3 主锚点。
- Week 7 从“看多宿主目录表面”升级为研究 port invariants、tool mapping、bootstrap、supportability 与 definition of done。
- BMAD 与 Agent OS 改为 Capability-first 动态源码定位，不把当前目录写成永久 Contract。
- Reference Project Atlas 从 Link Index 升级为 Research Role / Primary Question / Depth / Week / Primary Anchor / Do Not Study 图谱。
- Week 16 移除模糊的“过程评测资料”占位，复用前 15 周积累的过程证据。

### Non-goals

- 不增加新的 Week。
- 不调整 16 周主题顺序。
- 不新增大规模 Eval / Observability 学习专题。
- 不借 V4.1 重构 myharness。
