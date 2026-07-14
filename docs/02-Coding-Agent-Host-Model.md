# PART III · V4.2 Coding Agent Host Model

> Claude Code Host · Batch 2 · Cycle 3–4 正文已生成；研究执行与实验结果尚未开始。V4.1 Week 5–6 继续作为 Batch 3 的历史迁移源。

[← 上一卷](01-Agent与Harness基础认知.md) · [返回总览](../README.md) · [下一卷 →](03-Cross-host-Harness-Abstraction.md)

---

## Batch 2 边界（Boundary）

Batch 2 只生成 Claude Code Host 的两个 Cycle：

1. Cycle 3 · Claude Code Context Lifecycle
2. Cycle 4 · Claude Code Extension & Control Surface

本 Batch 将 V4.1 Week 3–4 迁移为计划态 V4.2 正文，并对齐 Contract / Behavior 权限、T01–T03、`EXP-Cxx-yy` 与 Run Metadata。它不执行 Claude Code，不产生 `EVD-*`、Support Assessment 或 Host architecture 结论，不实现 myharness feature，也不迁移 V4.1 Week 5–6。

V4.1 Week 3–4 原文可在基线提交 `f2b3961cbe125f846818d11a8892fe3c34f2751f` 中复查。旧 `EXP-W03-01` 与 `EXP-W04-01` 只作为历史计划 ID 保留。

## Claude Code Host 工作模型（Working Model）

```text
Session 输入与持久指令
  ↓
Context 装载与增长
  ↓
Agent / Tool interaction trajectory
  ↓
Compaction、Clear、Resume 或 Session boundary
  ↓
保留、重载、摘要或丢失的信息

Extension / Control Surface：
CLAUDE.md / Rules · Skill · Hook · Subagent · MCP · Plugin
```

该图是 `Mental Model V0`，不是 Claude Code 官方 Runtime architecture。官方文档只用于映射公开 Contract；第三方教学实现和 context engineering 方法只能作为绑定 revision 的教学 Source 或 Community Reference；真实发生的 lifecycle behavior 必须通过绑定 Host、Provider、Model 与配置的 Direct Behavior Evidence 观察。

---

## Cycle 3 · Claude Code Context Lifecycle

> Claude Code Host · V4.1 映射：Week 3

### 核心研究问题

> **在绑定 Claude Code 版本与运行条件下，一个工程任务的 Context 如何装载、增长、压缩与恢复，哪些连续性来自 Host lifecycle，哪些必须由外部 Artifact 承担？**

### 为什么与 myharness 有关

如果把 Conversation History、Session State、CLAUDE.md、Auto Memory、Task State、Change Artifact 与 Summary 都统称为 Memory，myharness 就可能重复 Host 能力、永久保存短期噪声，或误以为 Session resume 自动保留了任务继续所需的全部决策。Cycle 3 先建立可观察的 lifecycle map，不提前设计 Cycle 13 的跨 Session Handoff 策略。

### 研究范围（Scope）

本 Cycle 只研究：

- Claude Code 官方 Contract 中的 context window、session、compaction、resume 与 memory surface；
- Context 的主要组成、增长来源与高噪声 tool output；
- compact / resume 前后，事实、决策、文件定位、任务状态和下一步 trajectory 的可观察变化；
- Host lifecycle mechanism 与 Harness-owned Artifact 的边界假设。

本 Cycle 不研究：

- Anthropic 未公开的 Runtime architecture、内部 prompt 或实现路径；
- Provider / Model 排名、统计 benchmark 或大规模 observability platform；
- 完整 Session Handoff schema、长期 Knowledge ratification 或 myharness 实现；
- 把第三方教学重实现或 ACE 方法论当成 Claude Code 官方行为。

### 主线研究对象与权限边界（Authority Boundary）

| 研究对象（Research Object） | 计划深度 | Cycle 3 用途 | 权限边界（Authority Boundary） |
|---|---|---|---|
| Claude Code official docs：Context Window、Sessions、Memory、How Claude Code Works | L2 定向 | 映射公开的 Context、compaction、resume 与持久指令 Contract | 浮动官方文档锚点；执行时绑定 Host version、重新核验页面与访问日期；不能证明未公开 Runtime architecture |
| [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | L3 teaching model | 拆解 context compact、memory、system prompt、error recovery 与 task system 的教学机制 | 教学重实现不是 Anthropic 官方源码；目录是浮动锚点，执行时固定 commit |
| [HumanLayer Advanced Context Engineering](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents) | L2 method reference | 在 Direct Behavior observation 后解释 context trajectory 与 intentional compaction | Community Reference 只能形成 Reference Pattern / Open Question，不能证明 Claude Code Contract 或行为 |

本表登记计划来源，不产生 Contract Evidence claim 或 Source Evidence claim。官方页面和默认分支均须在执行时重新验证；未固定 commit 的仓库锚点明确视为 floating anchor。

### 问题驱动的阅读路线（Question-driven Reading Route）

1. 先读官方 `How Claude Code works` 与 `Explore the context window`，列出 Contract 声明与待行为验证项。
2. 再读 `Manage sessions` 与 `How Claude remembers your project`，区分 session transcript、resume、CLAUDE.md、rules 与 auto memory。
3. 在 `learn-claude-code` 当前 revision 中按 capability 重新定位 `context compact`、`memory`、`system prompt`、`error recovery` 与 `task system`；不要依赖 V4.1 的章节编号永久不变。
4. 先记录 Claude Code 的直接 observation，再读 ACE 的 `ace-fca.md`；方法论只用于提出解释和反例。
5. 遇到官方 Contract、教学实现与 Behavior 不一致时分别记录，不用一个来源覆盖另一个来源。

阅读和观察时只追：

- 当前 Context 包含什么，哪些项目在 Session start、按需调用或 tool result 后进入？
- Context growth 主要来自哪些 interaction，哪些输出对下一步是低价值噪声？
- `/compact`、`/clear`、resume 与新 Session 的语义是否相同？
- 哪些信息由 Host 重新装载，哪些只存在于 conversation，哪些由外部 Artifact 保持？
- trajectory 断裂时能否定位到 lost decision、stale state、missing evidence 或 repeated discovery？

### 心智模型 V0（Mental Model V0）

- Context 是一次请求可见信息的集合，不等于 Session 的全部持久化记录。
- Session persistence、Context compaction 与跨 Session memory 是不同机制，不能因都“保留信息”而合并。
- CLAUDE.md / Rules、Auto Memory、loaded Skill、Task / Change Artifact 与 conversation summary 具有不同 owner、load timing、scope 和 freshness。
- Tool output 可能提高局部可观察性，也可能消耗 Context 并降低后续 trajectory 质量。
- Resume 能否继续任务必须通过 Behavior Evidence 观察，不能仅由 transcript 存在或官方功能名推出。

以上是待验证模型，不是 Claude Code lifecycle 结论。

### 假设（Hypothesis）

> **H-C03-01:** 在绑定相同 Claude Code、Provider、Model、Configuration 与 T03 task instance 的条件下，经过一次受控 `/compact` 后，只存在于 conversation 的关键决策比写入并显式重载自临时实验 Artifact 的同类决策更容易出现重复定位、决策遗失或顺序漂移；Artifact variant 会增加维护、过期与 Context 成本。

支持信号：相同任务检查点上，能够把恢复差异追溯到信息位置和 lifecycle transition，且外部 Artifact variant 减少 repeated discovery 或 lost decision。

反驳信号：conversation-only baseline 在相同边界下同样稳定，或 Artifact 因过期、误导、装载失败而没有方向性增益。

不确定信号：无法确认两次 Run 的 `/compact` 边界、Host / Model / task state 是否可比，Artifact 没有按设计重载，或 Provider / Model effect 与 Host lifecycle effect 无法分离。

### 计划实验（Planned Experiments）

#### `EXP-C03-01` · Context Lifecycle Trace

- 实验类型（Experiment Type）：`EXPLORATORY`
- 稳定任务（Stable Task）：`T03 · Medium Change`
- 历史映射（Legacy Mapping）：`EXP-W03-01`（仅为历史计划）
- 观察设计（Observation Design）：在 Session start、初步定位、高文件读取、高日志输出、compact 前后、resume 前后设置 checkpoint；每个 checkpoint 记录当前目标、关键决策、已读文件、下一步、重复读取、Context command output 与 human intervention
- 受控变量（Controlled Variables）：repository commit、task instance、Host/version、Provider profile、Model、configuration snapshot、Rule/Skill/Check/Adapter revision
- 主要观察项（Primary Observations）：context growth source、repeated reads、lost decision、sequence drift、compact / resume continuity、recovery cost、stale artifact、human intervention
- 解释边界（Interpretation Boundary）：本实验只定位候选 lifecycle transition 与 confounder，不单独支持或反驳 `H-C03-01`

#### `EXP-C03-02` · Controlled Compaction Recovery Comparison

- 实验类型（Experiment Type）：`COMPARATIVE`
- 稳定任务（Stable Task）：`T03 · Medium Change`
- Baseline A：在受控 checkpoint 形成一条后续步骤必需的关键决策，仅保留在 conversation；随后执行一次 `/compact`
- Variant B：形成内容相同的关键决策，同时写入临时实验 Artifact；在相同 checkpoint 执行一次 `/compact`，随后按预先声明的相同步骤显式重载 Artifact
- 单一主要变量（Primary Variable）：关键决策在 `/compact` 后是否可从受控 Artifact 重载
- 固定边界（Fixed Boundary）：本实验只比较 `/compact`，不同时加入 resume、新 Session、不同输出量或 Handoff schema
- 主要观察项（Primary Observations）：decision recall、repeated discovery、sequence drift、recovery action、artifact staleness、Context cost、human intervention
- 结果词汇（Result Vocabulary）：`SUPPORT / REJECT / INCONCLUSIVE`
- 解释边界（Interpretation Boundary）：临时 Artifact 只用于隔离信息位置变量，不构成 Cycle 13 Handoff design proposal

Batch 2 不创建 Run、不填写结果。真正执行时必须为两个实验及 A/B variant 保存独立 Run Metadata，并把 Contract、Behavior 与 Project Artifact 分开登记后再派生 `EVD-*`。

### 退出条件（Exit Criteria）

Cycle 3 只有在以下条件均满足后才能结束：

- 官方 Contract map 绑定 Claude Code version、访问日期与对应 Source ID；
- 能区分 Context、Session transcript、resume、compaction、CLAUDE.md、Auto Memory、Task / Change Artifact 与 Summary；
- `EXP-C03-01` 完成至少一个可复查 T03 trace，且 lifecycle checkpoint 与 Run Metadata 完整；
- `EXP-C03-02` 完成共享 T03 baseline 的 A/B 配对 Run，单一主要变量、`/compact` 边界与 Artifact reload procedure 均可复查；
- Behavior Evidence 能说明观察到什么，同时不推测未公开 Runtime 原因；
- Mental Model V1 记录支持、反例、Unknown 和 Provider / Model confounder；
- Session Handoff 设计问题转交 Cycle 13，不在本 Cycle 扩张。

---

## Cycle 4 · Claude Code Extension & Control Surface

> Claude Code Host · V4.1 映射：Week 4

### 核心研究问题

> **在 Claude Code 的公开 Contract 中，同一个工程要求应由 CLAUDE.md / Rules、Skill、Hook、Subagent、MCP 还是 Plugin 承担，如何验证它被加载、触发、执行并产生预期治理效果？**

### 为什么与 myharness 有关

myharness 的 Claude extension 如果只按目录或产品名分配职责，可能把自然语言 guidance 当成 deterministic enforcement，把 Skill loading 当成流程完成，把 MCP connection 当成工程知识，或把 Plugin packaging 当成可移植语义。Cycle 4 建立 surface responsibility map，并用单一工程约束攻击该模型。

### 研究范围（Scope）

本 Cycle 只研究：

- Claude Code 官方 extension overview、memory / rules、skills、hooks、subagents、MCP 与 plugin Contract；
- load timing、trigger owner、model visibility、determinism、Context cost、scope 与 distribution boundary；
- Rule、Skill 与 deterministic Check 在同一 T01 约束上的方向性差异；
- myharness 现有 Claude artifacts 的只读 Project mapping，执行时再登记 Project Evidence。

本 Cycle 不研究：

- Claude Code 未公开 Runtime source architecture；
- 所有 Hook event、完整 MCP ecosystem、Plugin marketplace 或 enterprise deployment；
- 跨 Host Adapter、Portable Semantic Contract 实现或 Codex / OpenCode surface；
- 借内容生成直接重构 myharness Claude Plugin。

### 主线研究对象与权限边界（Authority Boundary）

| 研究对象（Research Object） | 计划深度 | Cycle 4 用途 | 权限边界（Authority Boundary） |
|---|---|---|---|
| Claude Code official docs：Extend Claude Code、Memory、Hooks、Subagents、Plugins | L2 定向 | 建立 extension / control surface Contract map | 浮动官方文档锚点；执行时绑定 Host version 并重新核验；页面不能证明实际配置已加载或行为有效 |
| myharness Claude extension artifacts | Read-only Project mapping | 映射现有 Rule、Skill、Hook、Check 与 Plugin distribution 的意图和重复 | 文件存在不等于能力有效；只有真实 project artifact / run 才能形成 Project / Behavior Evidence |

Cycle 4 不使用第三方反向工程证明 Claude Code architecture。Skills 与 MCP 的专项页面可在执行时从官方 extension overview 重新定位，不把当前 URL 或页面结构视为永久 Contract。

### 问题驱动的阅读路线（Question-driven Reading Route）

1. 先读官方 `Extend Claude Code`，按 `what loads / when / who triggers / model sees / can block / context cost / distribution` 建矩阵。
2. 用 `How Claude remembers your project` 区分 CLAUDE.md、path-scoped Rules 与 on-demand Skill。
3. Hooks 只定向查看与实验有关的 lifecycle event 和 decision control，不通读无关事件。
4. Subagent 只研究 Context、Tool、instruction 与 result boundary；MCP 只研究 external tool / data connection；Plugin 只研究 packaging、scope 与 distribution。
5. 最后对 myharness 当前 Claude artifacts 做只读映射，所有“不匹配”先写 Hypothesis 或 Open Question，不直接改实现。

### Extension 职责假设（Mental Model V0）

| Surface | 候选职责 | 需要验证的 failure mode |
|---|---|---|
| CLAUDE.md / Rules | always-on 或 path-scoped Instruction / project context | 未加载、冲突、Context 成本、被误当成强制执行 |
| Skill | 按需加载的程序性知识与语义流程 | description 命中但正文未执行，或步骤执行但没有 Evidence |
| Hook | lifecycle trigger 上的观察、注入、验证或阻断 | trigger 配置错误、误报、double block；prompt / agent hook 的结果不必然确定 |
| Subagent | 独立 Context / Tool / responsibility boundary，返回有限结果 | 只换角色 prompt、上下文泄漏、handoff 丢失 |
| MCP | 提供外部 Tool / data connection | 连接成功被误当成工具使用正确或 workflow 正确 |
| Plugin | 安装、命名、版本化与分发多个 Host-specific artifacts | packaging 被误当成 capability semantics 或跨 Host portability |

该表是待 Contract 和 Behavior 攻击的 Mental Model，不构成 Claude Code capability assessment 或 S1–S4。

### 假设（Hypothesis）

> **H-C04-01:** 对同一个 T01「新增或修改的 HTTP client 必须显式设置非默认、可配置 timeout」工程约束，Rule-only 能影响首次选择但不能保证检测；在共享 Rule baseline 上增加 Skill 可能改善实现步骤与自检，在同一 acceptance contract 上增加 deterministic Check 可能改善违规发现的一致性。两者都可能增加 Context、误报、修复轮数或维护成本。

支持信号：B / C 相对共同 A baseline 呈现可解释且职责一致的差异，Skill 的增益主要出现在 procedure / evidence，Check 的增益主要出现在 deterministic detection。

反驳信号：Skill 或 Check 没有产生对应增益，或其误报、Context 与维护成本抵消方向性价值。

不确定信号：三种 variant 没有共享 task baseline，Host、Provider、Model、Rule revision 或 task difficulty 同时变化，导致 surface effect 无法分离。

### 计划实验（Planned Experiment）· `EXP-C04-01`

- 实验类型（Experiment Type）：`COMPARATIVE`
- 稳定任务（Stable Task）：`T01 · Engineering Constraint`
- 历史映射（Legacy Mapping）：`EXP-W04-01`（仅为历史计划）
- 共同 Acceptance Contract：新增或修改的目标 HTTP client 必须显式传入非默认、可配置 timeout；测试或静态 fixture 能对同一条件作出 pass / fail
- 共同基线 A（Shared Baseline）：只用 Rule 表达上述 timeout contract
- 变体 B（Variant B）：相同 Rule + 只教授同一 timeout contract 的 HTTP client Skill
- 变体 C（Variant C）：相同 Rule + 对同一 timeout contract 判定 pass / fail 的 deterministic Check
- 可选变体 D（Optional Variant D）：Rule + Skill + Check；只有 A/B/C 不能解释 interaction effect 时才执行
- 受控变量（Controlled Variables）：repository commit、同一 T01 instance、Host/version、Provider profile、Model、configuration snapshot、Rule/Skill/Check/Adapter revision
- 主要观察项（Primary Observations）：first-pass adherence、omission、Skill discovery / execution、Agent self-correction、deterministic detection、false positive、rework、context cost、human intervention
- 结果词汇（Result Vocabulary）：`SUPPORT / REJECT / INCONCLUSIVE`

每个 variant 使用独立 Run Metadata。A/B/C 的 task statement、acceptance fixture 与 timeout 语义必须完全相同；fallback / degradation 是独立语义问题，不进入本实验。多个近似任务只能作为不同 task instance 登记，不能用“3–5 个相近任务”代替稳定 task identity 或把小样本包装成 benchmark。

### 退出条件（Exit Criteria）

Cycle 4 只有在以下条件均满足后才能结束：

- 完成绑定 Claude Code version 的 surface Contract map，明确 `Supported / Unsupported / Unknown`，但不据此宣称完整支持；
- 每个 surface 都记录 load timing、trigger owner、model visibility、determinism、Context cost、scope、distribution 和 failure route；
- `EXP-C04-01` 的 A/B/C 共享同一 T01 baseline，主要变量可分离，Run Metadata 完整；
- Contract、Behavior 与 myharness Project Evidence 分开登记，并由 `EVD-*` 表达 scoped claim；
- Mental Model V1 明确哪些职责成立、重叠、失败或仍 Unknown；
- 不实现 myharness feature，不提前进入 Cycle 5–6 或 cross-host Adapter。

---

## Batch 2 路线复盘触发条件（Route Review Trigger）

完成 Cycle 4 的真实研究后执行一次 Route Review。它可以调整 Batch 3 的 Codex 项目锚点、阅读深度、实验节奏或借用方法，但不能改变冻结的 Cycle 名称、编号、顺序或 Batch 边界。

内容生成本身不满足 Cycle 3–4 Exit Criteria，也不创建 Route Review 结果。若 Direct Behavior Evidence 推翻 Claude Code Host 工作模型，可在当前 Cycle 内缩小问题；其他旁支进入 Open Questions。

## 迁移记录（Migration Record）

| V4.1 历史计划 | V4.2 研究设计 | 状态（Status） |
|---|---|---|
| Week 3 · `EXP-W03-01` | Cycle 3 · `EXP-C03-01` / `EXP-C03-02` | 拆分为探索性 trace 与必做 `/compact` 对照，尚未执行；旧 ID 只作历史记录 |
| Week 4 · `EXP-W04-01` | Cycle 4 · `EXP-C04-01` | 收敛为单一 timeout acceptance contract 并保留 shared Rule baseline，尚未执行；旧 ID 只作历史记录 |

迁移只更新未来研究设计，不声称 V4.1 实验已发生，也不把旧 ID 重编号成 Evidence。

## V4.1 Week 5–6 Historical Baseline · Pending Batch 3

以下内容继续保持 V4.1 Week-based 形态，供 Batch 3 迁移为 Cycle 5–6。它不是 V4.2 Cycle 5–6 正文，不表示相关实验已经执行。

## Week 5 · Codex Architecture & Customization Model

> Phase 3 · Codex Host Model

### 核心研究问题

> **Codex 如何组织 Agent 能力、项目指导和扩展机制？**

### 主线研究对象

| **研究对象**             | **阅读深度** | **本周只关注**                                                                     |
|--------------------------|--------------|------------------------------------------------------------------------------------|
| Codex 官方 Customization | L2 定向      | 先读稳定 Contract：AGENTS.md、Memories、Skills、MCP、Subagents、Plugins / Hooks 等 |
| openai/codex             | L3 定向源码  | 只跟 Harness 接口相关 crate；建立 Repository Map 后按问题读源码                    |

### 重点查看部分

- 官方资料先读 Customization；先画 Codex Architecture V0，不看源码。

- 仓库根：AGENTS.md、.codex/、codex-cli/、codex-rs/、docs/、sdk/、tools/。

- codex-rs 定位：core、context-fragments、message-history、state、memories、skills、core-skills、plugin、core-plugins、hooks、tools。

- 单 crate 阅读顺序：README → Cargo.toml → lib.rs / entry → 搜索核心概念 → 跟 1–2 层调用 → 停止。

### 阅读时只追这些问题

- Capability 在 Architecture 中扮演什么角色？

- Docs 定义 Contract、Source 定义 Implementation、Behavior 定义什么？

- AGENTS.md、Skill、Plugin、Hook、Memory、State 的边界怎样组织？

- myharness 应依赖 Implementation Detail，还是 Stable Surface？

### 本周不要陷进去

- 从第一行顺序读完整仓库

- 遇到 Rust trait 就全部补课

- 顺着依赖无限展开

- 研究 TUI、网络客户端和无关基础设施

### 学习后的实践：Architecture V0 → Source → Behavior → Architecture V2

> **Experiment ID:** `EXP-W05-01`
> **Experiment Type:** `EXPLORATORY`
> **Evidence Scope:** 个人研究中的方向性证据；小样本用于发现现象、比较机制或形成下一步假设，不包装为统计学结论。

1. 先画 Codex Architecture V0，标所有问号。

2. 建立 Repository Map，针对问号定位对应 crate。

3. AGENTS.md 层级实验：观察 scope 与覆盖。

4. Skill Discovery 实验：description 明确 vs 模糊，观察发现与触发。

5. Plugin 实验：使用当前 Codex Plugin 移植中的一个真实 Capability，比较原认知、官方 Contract、源码 Boundary 与真实加载行为。

### 建议保留的证据

- V0 / V1 / V2 架构图变化

- 源码定位路径与停止点

- 行为实验与源码假设一致 / 不一致之处

- 是否依赖不稳定 Implementation Detail

### 预期成长

| **源码方法** | 掌握 Question-driven Source Reading。                    |
|--------------|----------------------------------------------------------|
| **三层真相** | 开始区分 Contract、Implementation 与 Observed Behavior。 |

### 实践完成后，重新理解

- 开源源码是否一定比行为实验更“真实”？

- 文档、源码和行为各能证明什么？

- myharness 应依赖 Codex Implementation Detail，还是 Stable Surface？

| **弹性规则：** 如果本周实验直接暴露了一个会推翻当前 Mental Model 的问题，可以暂停原计划并追加一个短研究循环；如果只是有趣的旁支问题，记录到 Open Questions，继续主线。 |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Week 6 · Codex Execution、Safety 与 State

> Phase 3 · Codex Host Model

### 核心研究问题

> **什么安全责任属于 Host，什么工程治理责任属于 Harness？**

### 主线研究对象

| **研究对象**              | **阅读深度** | **本周只关注**                                                                                          |
|---------------------------|--------------|---------------------------------------------------------------------------------------------------------|
| Codex 官方安全 / 权限资料 | L2 定向      | Permissions、Rules、Hooks、Sandboxing、Approvals & Security                                             |
| openai/codex codex-rs     | L3 定向源码  | exec、execpolicy、shell-command、shell-escalation、sandboxing、process-hardening、secrets、hooks、state |

### 重点查看部分

- 先建立四层模型：Host Safety Boundary / Harness Engineering Policy / Project Rule / CI & Acceptance Gate。

- 对“读取敏感范围、rm -rf、HTTP 缺 timeout、pytest 失败”等场景先自行分类，再实验。

- 源码只跟 execution / policy / sandbox / state Boundary。

### 阅读时只追这些问题

- Host 权限边界与 Harness 工程策略如何区分？

- Approval、Sandbox、Rule、Hook、CI 是否存在重复拦截？

- Double Block 是否有成本？

- Agent 是否需要理解阻断原因？

### 本周不要陷进去

- 绕过 Sandbox

- 执行危险命令

- 为了验证安全机制进行真实破坏

- 把所有“禁止”都丢给 Host

### 学习后的实践：无破坏性 Safety Responsibility Experiment

> **Experiment ID:** `EXP-W06-01`
> **Experiment Type:** `EXPLORATORY`
> **Evidence Scope:** 个人研究中的方向性证据；小样本用于发现现象、比较机制或形成下一步假设，不包装为统计学结论。

1. 使用无破坏性模拟场景：访问测试文件、向临时目录写入、git status、普通网络请求、项目规则禁止但本身无害的测试命令。

2. 记录谁阻止：Host、Approval、Sandbox、Harness Hook，还是 Rule 只提醒。

3. 检查 Double Block、无意义 Approval、误报和 Agent 对原因的理解。

4. 拿 myharness pre_bash_guard 重新分类。

### 建议保留的证据

- 阻断责任主体

- Double Block / False Positive

- Approval 噪声

- Agent 是否理解理由

- Host 与 Harness 的重叠范围

### 预期成长

| **责任边界** | 形成 Host Safety vs Harness Safety Matrix。            |
|--------------|--------------------------------------------------------|
| **治理意识** | 能区分权限信任边界、工程行为治理、项目约束和结果验证。 |

### 实践完成后，重新理解

- pre_bash_guard 是否重复 Host？

- sudo 与 force push main 是否属于同一类风险？

- Host 管权限边界、Harness 管工程规则，这个假设在哪些场景不成立？

| **弹性规则：** 如果本周实验直接暴露了一个会推翻当前 Mental Model 的问题，可以暂停原计划并追加一个短研究循环；如果只是有趣的旁支问题，记录到 Open Questions，继续主线。 |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|


---

## 路线调整说明

本卷是研究导航，不是冻结的教学脚本。执行到对应研究循环前，应先刷新相关官方文档、默认分支与 Changelog；若项目目录或能力名称发生变化，继续追踪本卷定义的研究问题与 Capability，而不是机械寻找旧路径。
