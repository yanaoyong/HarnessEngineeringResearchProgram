# PART VIII · Reference Project Atlas

> 按研究问题使用的项目与官方资料图谱。Batch 1–7 active overlay 已刷新；V4.1 Week 13–16 rows 等待 Batch 8 迁移。项目是 Reference，不是课程主线。

[← 上一卷](06-Research-Infrastructure.md) · [返回总览](../README.md)

---

## 如何使用 Atlas

先有 Research Question，再打开项目。

```text
Research Question
        ↓
Find Research Role
        ↓
Open Primary Anchor
        ↓
Read to Planned Depth
        ↓
Stop at Do-Not-Study Boundary
```

当项目默认分支、目录或术语发生变化时，优先追 Capability 与研究问题，不机械寻找旧路径。

## Batch 1–7 当前图谱（Active Atlas）

| 项目 / 来源 | 研究角色（Research Role） | 核心问题 | 深度 | 相关 Cycle | 当前锚点 | 权限 / 停止边界 |
|---|---|---|---|---|---|---|
| SWE-agent/minimal-agent-tutorial | 最小 Agent 教学基线 | Coding Agent 最少需要什么？ | L3 | C01 | `docs/index.md` + 完整最小实现 | 只证明绑定 revision 的教学实现；不研究 benchmark infrastructure |
| SWE-agent/mini-swe-agent | 最小脚手架对照（Minimal Scaffold Contrast） | Agent Core 扩大后增加哪些结构？ | L3 定向 | C01 | 浮动 `main`：`src/minisweagent/{agents,environments,models,run}` | 计划执行时重新核验并固定 commit；不研究 deployment 与 benchmark ranking |
| SWE-agent ACI paper | 接口理论（Interface Theory） | 接口设计如何影响 Agent 行为？ | L1 理论 | C01 | arXiv:2405.15793v3 | 不证明任何商业 Host 的当前实现或 Support Level |
| shareAI-lab/learn-claude-code | Harness Primitive 教学重实现 | Primitive 为什么存在，职责是否可互换？ | L3 | C02 | `s01`、`s03`–`s07`；`s02`、`s08` 快读 | 不是 Claude Code 官方源码；不得推导官方 Runtime architecture、event 或 Contract |
| Claude Code official docs · Context / Sessions / Memory | Claude Code Host Contract | Context 如何装载、增长、压缩和恢复？ | L2 定向 | C03 | `context-window`、`sessions`、`memory`、`how-claude-code-works` | 浮动官方页面；执行时绑定 Host version；不证明本地 Behavior 或未公开 Runtime architecture |
| shareAI-lab/learn-claude-code | Context lifecycle 教学模型 | compact、memory、system prompt 与 task state 如何在教学实现中协作？ | L3 定向 | C03 | 按 capability 定位 current track；执行时固定 commit | current / legacy track 会变化；只证明绑定 revision 的教学实现，不证明 Claude Code Runtime |
| HumanLayer Advanced Context Engineering | Context strategy 方法参考 | 如何解释 context trajectory 与 intentional compaction？ | L2 method | C03 | 浮动 `main`：`ace-fca.md` | Community Reference；先观察后解释，不能证明 Host Contract / Behavior |
| Claude Code official docs · Extend Claude Code | Extension surface Contract | CLAUDE.md、Skill、Hook、Subagent、MCP、Plugin 的职责与加载边界是什么？ | L2 定向 | C04 | `features-overview` → Memory / Hooks / Subagents / Plugins 专项页 | 浮动官方页面；Contract 不等于配置已加载或 capability 有效 |
| myharness Claude extension artifacts | 项目只读映射对象 | 现有 Rule、Skill、Hook、Check 与 Plugin distribution 是否职责重叠？ | Project mapping | C04 | 执行时按当前仓库 capability 重新定位 | 文件存在不等于 Project / Behavior Evidence；Batch 2 不修改实现 |
| Codex official docs · Customization / AGENTS.md / Skills / Plugins | Codex customization Contract | 项目指导、Skill progressive disclosure 与 Plugin distribution 如何分工？ | L2 定向 | C05 | Customization overview → AGENTS.md / Build skills / Build plugins | 浮动官方页面；执行时绑定 Codex version / surface；不证明本地加载或内部实现 |
| Codex official docs · MCP / Subagents / Hooks / Config | Codex extension boundary | external tool、delegation、lifecycle 与 configuration 如何进入 architecture map？ | L2 定向 | C05–C06 | 从当前官方导航按 capability 重新定位 | 页面与导航会变化；Contract 不等于 capability 已启用或 behavior 已验证 |
| openai/codex | Codex verified Official Source 候选 | 特定 revision 如何实现 customization、execution、policy、sandbox、hook 与 state boundary？ | L3 targeted | C05–C06 | 浮动默认分支；执行时先固定 commit，再按 capability 建 Repository Map | 当前 `NOT PINNED`；不得沿用旧 crate / path，也不得把 Source 当成当前安装 Behavior |
| Codex official docs · Rules / Sandbox / Agent approvals & security | Codex execution / safety Contract | technical boundary、approval 与 command policy 如何分工？ | L2 定向 | C06 | Rules、Sandbox、Agent approvals & security | 浮动官方页面；绑定 Host version / surface / platform；不形成安全保证或合规结论 |
| myharness pre-execution artifacts | 项目只读映射对象 | guard 是否重复 Host policy，或提供 Host 无法表达的项目语义？ | Project mapping | C06 | 执行时按当前仓库 capability 重新定位 | 文件存在不等于已触发、有效或需要保留；Batch 3 不修改实现 |
| ZCode 用户协议、Agent 与安全操作确认官方文档 | ZCode product / Host Contract | 产品身份、Agent / workspace、permission 与 Review 的公开责任边界是什么？ | L1–L2 定向 | C07 | `terms`、`agent-framework`、`safety-confirm` | 浮动官方页面；绑定 Host version / platform；不证明 Behavior、Runtime source 或 enterprise readiness |
| ZCode 连接模型与远程开发官方文档 | Provider / Model / execution boundary Contract | Provider、endpoint、Model、authentication 与 execution location 如何同 Host surface 分离？ | L2 定向 | C07 | `configuration`、`remote-development` | 协议兼容不等于 Model portability；remote surface 不等于私有化、隔离或组织批准 |
| ZCode 隐私政策、Changelog 与反馈支持文档 | Enterprise fact question anchors | 数据、版本、日志、支持与运维需要验证哪些 deployment fact？ | L1 定向 | C07 | `privacy`、`changelog`、`feedback` | policy / release / support 页面不能替代 `ENT-*`、SLA、审计、数据驻留或法律审查 |
| OpenCode official docs · Config / Rules / Agents / Tools / Permissions | OpenCode Host Contract | config、instruction、agent、tool、permission 与 extension surface 如何分工？ | L2 定向 | C08 | `config`、`rules`、`agents`、`tools`、`permissions`、`skills`、`plugins`、`mcp-servers` | 浮动官方页面；绑定 Host version / surface / platform；Contract 不等于配置已加载或 Behavior 已验证 |
| OpenCode official docs · Providers / Models | Provider / Model boundary Contract | Provider adapter、endpoint / protocol、Model identity / option 与 Host semantic 如何分离？ | L2 定向 | C08 | `providers`、`models` | Provider / Model 可配置、可选或协议兼容不等于 portability；列表与推荐会变化 |
| anomalyco/opencode | OpenCode verified Official Source 候选 | 特定 revision 如何实现 config、session / agent、tool / permission、provider / model 与 extension boundary？ | L3 targeted | C08 | 浮动默认开发分支；执行时先固定完整 commit，再按 capability 建 Repository Map | 当前 `NOT PINNED`；不沿用当前 package / path，不把 Source 当成安装 Behavior 或 portability 结论 |
| Agent Skills official docs | Cross-product Skill format / lifecycle Contract | `SKILL.md` format、progressive disclosure 与 client integration 能提供哪些公共语义，哪些仍由 Host 决定？ | L2 定向 | C09 | Overview、Specification、Adding skills support | 格式和 guidance 不证明任一 Host 当前版本兼容、已加载或行为等价；normative format 与 implementor recommendation 分开 |
| obra/superpowers porting guide | Cross-harness porting Reference Pattern | shared skill body、tool mapping、bootstrap、capability gate、degradation 与 definition of done 如何分层？ | L3 定向 | C09 | 浮动 `main`：`docs/porting-to-a-new-harness.md` + 相关 live integration | 项目自身方法不是四个 Host 的官方 Contract；执行时固定 commit，文档与 code 冲突时分别记录，不复制完整 implementation |
| mifunedev/openharness | Reference role drift contrast | V4.1 shared primitive anchor 是否仍回答 Cycle 9 portability 问题？ | L1 范围核验 | C09 | 浮动 `main`：current README / canonical repository | 当前公开定位主要是 Docker sandbox / long-lived workspace；旧 `.oh` path 只作历史线索，不作为 portability Evidence 或第五 Host |
| Agent Skills · Skill creation guidance | Skill discovery / output evaluation Contract | description、trigger eval 与 output eval 如何分开？ | L2 定向 | C10 | `optimizing-descriptions`、`evaluating-skills` | 浮动官方页面；guidance 不证明任一 Host 的 actual Discovery、Activation 或 Skill outcome |
| obra/superpowers | Skill behavior-contract Reference Pattern | procedure、verification、failure route 与 Skill test 如何组合？ | L3 定向 | C10 | 浮动 `main`：`skills/writing-skills/`、`skills/verification-before-completion/` | 执行时固定 commit；项目自身规范不证明 myharness 或四宿主 behavior |
| shareAI-lab/learn-claude-code | Skill loading 教学对照 | 教学 Harness 如何表达 loading / progressive capability？ | L2 定向 | C10 | 浮动默认分支：按 current track 重新定位 | 不是 Claude Code 官方 Runtime；不得形成官方 Contract / Architecture claim |
| GitHub Spec Kit | Change artifact convergence reference | Spec、Plan、Task、Implementation 与 cross-artifact analysis 如何关联？ | L2 定向 | C11 | 浮动官方 docs + `github/spec-kit` 默认分支 | Contract docs 与 Source repository 分开登记；源码执行时固定 commit，不沿用未核验旧命令名 |
| Fission-AI/OpenSpec | Evolvable Change artifact reference | Change schema / artifact 如何随实现演进？ | L2 定向 | C11–C12 | 浮动默认分支：docs、schemas、instructions / templates | 不证明 myharness Change truth，也不把 flexible workflow 等同于无 Gate |
| BMAD Method | Adaptive workflow reference | planning depth / track 如何随 project need 变化？ | L2 定向 | C12 | 浮动官方 docs + `bmad-code-org/BMAD-METHOD` 默认分支 | Contract docs 与 Source repository 分开登记；不直接复制 track / story-count taxonomy |
| HumanLayer Advanced Context Engineering | Intentional compaction method reference | trajectory 如何压缩为可继续工作的 artifact？ | L2 method | C13 | 浮动 `main`：`ace-fca.md` | Community Reference；作者案例不证明 Host Contract、普遍 productivity 或最佳 handoff |
| snarktank/ralph | Fresh-context persistent-artifact contrast | PRD、progress 与 fresh iteration 如何交接任务状态？ | L2 定向 | C13 | 浮动 `main`：README、prompt / CLAUDE、PRD / progress artifacts | 固定 revision 后只解释该项目；不能证明 fresh context 优于 resume |
| buildermethods/agent-os | Knowledge-to-standard reference | standards 如何被发现、部署与索引？ | L2 定向 | C14 | 浮动默认分支：Discover / Deploy / Shape / Index capabilities | 不证明发现准确、值得永久化或维护成本可接受；不研究安装脚本 |
| SWE-agent/mini-swe-agent + ACI paper | Minimal scaffold / interface theory contrast | interface value、scaffold size 与 permanent Harness 如何区分？ | L1–L2 定向 | C14 | mini-swe-agent 浮动 `main` + arXiv:2405.15793v3 | 不使用 benchmark 排名裁决 minimalism；论文受 OQ-003 taxonomy boundary 约束 |

上述入口、官方页面和默认分支目录只是计划执行时核验的浮动锚点，Atlas 只提供定位，不证明当前 revision 的源码事实或实际 Host behavior。形成 Evidence 时必须重新核验并登记 Source ID、Host version / commit、scope、访问日期与限制。

## V4.1 Legacy Atlas · Historical Mapping / Batch 8 Pending

下表保持 V4.1 `Relevant Week` 语义，供 historical mapping 与 Batch 8 迁移复查。Week 1–12 rows 只保留迁移历史，Cycle 7–8 没有 V4.1 row；Batch 7 已在 active overlay 中刷新 Week 8–12 主锚点，不修改此历史表。只有 Week 13–16 相关语义仍待 Batch 8 迁移。

| Project / Source | Research Role | Primary Question | Depth | Relevant Week | Primary Anchor | Do Not Study |
|---|---|---|---|---|---|---|
| SWE-agent/minimal-agent-tutorial | Agent baseline | Coding Agent 最少需要什么？ | L3 | 1 | `docs/index.md` + minimal implementation | Benchmark infrastructure |
| SWE-agent/mini-swe-agent | Minimal scaffold contrast | Agent Core 扩大后增加了哪些结构？ | L3 | 1 / 12 | Agent / Environment / Model / Run | SWE-bench deployment |
| shareAI-lab/learn-claude-code | Teaching reconstruction | Harness Primitive 为什么存在？ | L3 | 2 / 3 / 8 | 对应 `sXX_*` 教学章节 | 当成 Claude 官方源码 |
| Claude Code official docs | Host contract | Claude Context 与 extension surfaces 如何工作？ | L2 | 3 / 4 / 11 | Context / Memory / Skills / Hooks / Subagents / MCP / Plugins docs | 无研究问题时通读全部功能 |
| HumanLayer ACE | Context strategy | 如何管理 context trajectory 与 intentional compaction？ | L2 | 3 / 11 | `ace-fca.md` | 当成 Claude 内部实现说明 |
| OpenAI Codex docs | Host contract | Codex customization / execution 的稳定 Surface 是什么？ | L2 | 5 / 6 / 7 | Customization / Permissions / Rules / Hooks / Sandboxing docs | 只看二手介绍 |
| openai/codex | Host source | Codex 如何实现 Harness 相关 capability boundary？ | L3 targeted | 5 / 6 | `codex-rs/Cargo.toml` → related crate | TUI、网络客户端、无关 infra |
| Agent Skills | Cross-product skill contract | Skill 哪些部分能跨产品复用？ | L2 | 7 / 8 | SKILL.md format + progressive disclosure | 把格式相同等同于行为相同 |
| obra/superpowers | Skill behavior + harness porting | Skill 如何塑造行为？一个 Harness port 为什么成立？ | L3 | 7 / 8 | `docs/porting-to-a-new-harness.md`；selected skills | 无问题时漫游所有 skills |
| mifunedev/openharness | Shared primitive distribution | Shared primitive pack 与 provider surface 如何分层？ | L1 | 7 | README + `.oh/docs/oh-directory-layout.md` | 完整学习其全部 control plane |
| github/spec-kit | Artifact convergence | Change 如何保持 artifact truth 与 convergence？ | L2 | 9 | README / quickstart / evolving specs / converge / analyze | CLI internals |
| Fission-AI/OpenSpec | Flexible change artifacts | Change artifact 如何演进而不依赖 rigid phase gates？ | L1 | 9 / 10 | README + spec-driven schema | 安装与 CLI 实现细节 |
| BMAD Method | Adaptive workflow | Workflow depth 如何随 complexity / risk 调整？ | L2 | 10 | 当前 README + official docs；按 Capability 搜索 current source | Party Mode、所有 Persona |
| snarktank/ralph | Fresh-context handoff contrast | Fresh context 如何靠持久化 artifact 延续工作？ | L1 | 11 | README / workflow / prompt / PRD artifacts | UI 与外围工具 |
| buildermethods/agent-os | Knowledge → standards | 发现如何变成可部署、可索引的标准？ | L2 | 12 | Discover / Deploy / Shape / Index capabilities | 安装脚本 |
| SWE-agent ACI paper | Interface theory | Agent-computer interface 为什么影响行为？ | L1 theory | 1 / 12 / 16 | ACI thesis and experiments | 复刻完整 benchmark |

## Primary Links

- Agent Skills — https://agentskills.io/home
- Agent Skills · Specification — https://agentskills.io/specification
- Agent Skills · Adding skills support — https://agentskills.io/client-implementation/adding-skills-support
- Agent Skills · Optimizing skill descriptions — https://agentskills.io/skill-creation/optimizing-descriptions
- Agent Skills · Evaluating skill output quality — https://agentskills.io/skill-creation/evaluating-skills
- OpenAI Codex · Docs — https://learn.chatgpt.com/docs
- OpenAI Codex · Customization — https://learn.chatgpt.com/docs/customization/overview
- OpenAI Codex · AGENTS.md — https://learn.chatgpt.com/docs/agent-configuration/agents-md
- OpenAI Codex · Build skills — https://learn.chatgpt.com/docs/build-skills
- OpenAI Codex · Build plugins — https://learn.chatgpt.com/docs/build-plugins
- OpenAI Codex · Rules — https://learn.chatgpt.com/docs/agent-configuration/rules
- OpenAI Codex · Hooks — https://learn.chatgpt.com/docs/hooks
- OpenAI Codex · Sandbox — https://learn.chatgpt.com/docs/sandboxing
- OpenAI Codex · Agent approvals & security — https://learn.chatgpt.com/docs/agent-approvals-security
- openai/codex — https://github.com/openai/codex
- ZCode · 用户协议 — https://zcode.z.ai/cn/terms
- ZCode · Agent — https://zcode.z.ai/cn/docs/agent-framework
- ZCode · Agent interaction / AGENTS.md — https://zcode.z.ai/cn/docs/agents
- ZCode · 连接模型与套餐 — https://zcode.z.ai/cn/docs/configuration
- ZCode · 安全操作确认 — https://zcode.z.ai/cn/docs/safety-confirm
- ZCode · 远程开发 — https://zcode.z.ai/cn/docs/remote-development
- ZCode · 隐私政策 — https://zcode.z.ai/cn/privacy
- ZCode · 版本发布与更新 — https://zcode.z.ai/cn/changelog
- ZCode · 用户反馈与支持 — https://zcode.z.ai/cn/docs/feedback
- OpenCode · Intro — https://opencode.ai/docs/
- OpenCode · Config — https://opencode.ai/docs/config/
- OpenCode · Providers — https://opencode.ai/docs/providers/
- OpenCode · Models — https://opencode.ai/docs/models/
- OpenCode · Rules — https://opencode.ai/docs/rules/
- OpenCode · Agents — https://opencode.ai/docs/agents/
- OpenCode · Tools — https://opencode.ai/docs/tools/
- OpenCode · Permissions — https://opencode.ai/docs/permissions/
- OpenCode · Agent Skills — https://opencode.ai/docs/skills/
- OpenCode · Plugins — https://opencode.ai/docs/plugins/
- OpenCode · MCP servers — https://opencode.ai/docs/mcp-servers/
- anomalyco/opencode — https://github.com/anomalyco/opencode
- Claude Code · Context Window — https://code.claude.com/docs/en/context-window
- Claude Code · How Claude Code Works — https://code.claude.com/docs/en/how-claude-code-works
- Claude Code · Sessions — https://code.claude.com/docs/en/sessions
- Claude Code · Memory / CLAUDE.md — https://code.claude.com/docs/en/memory
- Claude Code · Extend Claude Code — https://code.claude.com/docs/en/features-overview
- Claude Code · Hooks — https://code.claude.com/docs/en/hooks
- Claude Code · Subagents — https://code.claude.com/docs/en/sub-agents
- Claude Code · Plugins — https://code.claude.com/docs/en/plugins
- SWE-agent/minimal-agent-tutorial — https://github.com/SWE-agent/minimal-agent-tutorial
- SWE-agent/mini-swe-agent — https://github.com/SWE-agent/mini-swe-agent
- shareAI-lab/learn-claude-code — https://github.com/shareAI-lab/learn-claude-code
- HumanLayer Advanced Context Engineering — https://github.com/humanlayer/advanced-context-engineering-for-coding-agents
- obra/superpowers — https://github.com/obra/superpowers
- obra/superpowers · Porting to a new harness — https://github.com/obra/superpowers/blob/main/docs/porting-to-a-new-harness.md
- github/spec-kit — https://github.com/github/spec-kit
- GitHub Spec Kit · Documentation — https://github.github.com/spec-kit/index.html
- Fission-AI/OpenSpec — https://github.com/Fission-AI/OpenSpec
- BMAD Method — https://github.com/bmad-code-org/BMAD-METHOD
- BMAD Method · Getting Started — https://docs.bmad-method.org/tutorials/getting-started/
- buildermethods/agent-os — https://github.com/buildermethods/agent-os
- mifunedev/openharness — https://github.com/mifunedev/openharness
- snarktank/ralph — https://github.com/snarktank/ralph
- SWE-agent ACI paper — https://arxiv.org/abs/2405.15793

## Atlas Maintenance Rule

每次 Route Review 允许：

```text
Add Project
Remove Project
Change Reading Depth
Change Relevant Week
Replace Primary Anchor
Tighten Do-Not-Study Boundary
```

Atlas 的目标不是积累 100 个项目，而是保持：

> **当前研究问题有高质量参照，且阅读边界清楚。**

---

## 路线调整说明

执行到对应研究循环前，应刷新官方资料、默认分支与 Changelog。若项目发生大版本变化，以 Research Role 与 Primary Question 为主线重新定位，不让旧目录路径绑架研究路线。
