# Changelog

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
