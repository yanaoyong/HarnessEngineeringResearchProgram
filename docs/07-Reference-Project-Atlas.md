# PART VIII · Reference Project Atlas

> 按研究问题使用的项目与官方资料图谱。Batch 1–2 active overlay 已刷新；其余 V4.1 rows 等待对应内容 Batch 迁移。项目是 Reference，不是课程主线。

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

## Batch 1–2 当前图谱（Active Atlas）

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

上述入口、官方页面和默认分支目录只是计划执行时核验的浮动锚点，Atlas 只提供定位，不证明当前 revision 的源码事实或实际 Host behavior。形成 Evidence 时必须重新核验并登记 Source ID、Host version / commit、scope、访问日期与限制。

## V4.1 Legacy Atlas · Pending Migration

下表保持 V4.1 `Relevant Week` 语义，供 Batch 3–8 迁移及 historical mapping 复查。Batch 2 不借 Atlas 更新提前生成 Cycle 5–18 正文；其中 Week 3–4 rows 只保留迁移历史。

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
- OpenAI Codex · Docs — https://developers.openai.com/codex
- OpenAI Codex · Customization — https://developers.openai.com/codex/concepts/customization
- openai/codex — https://github.com/openai/codex
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
- github/spec-kit — https://github.com/github/spec-kit
- Fission-AI/OpenSpec — https://github.com/Fission-AI/OpenSpec
- BMAD Method — https://github.com/bmad-code-org/BMAD-METHOD
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
