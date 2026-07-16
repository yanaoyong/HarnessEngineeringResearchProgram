# PART III · V4.3 Coding Agent Host Model

> Claude Code / Codex / Qwen Code / OpenCode Host · Batch 2–5 · Cycle 3–8 正文已生成；研究执行与实验结果尚未开始。

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
- Outcome Mode：`OBSERVATION_ONLY`；Experiment Result 为 `NOT APPLICABLE · OBSERVATION ONLY`
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

## Batch 3 边界（Boundary）

Batch 3 只生成 Codex Host 的两个 Cycle：

1. Cycle 5 · Codex Architecture & Customization
2. Cycle 6 · Codex Execution、Safety & State

本 Batch 将 V4.1 Week 5–6 迁移为计划态 V4.2 正文，并对齐官方 Contract、verified Official Source、Direct Behavior、T01–T03、`EXP-Cxx-yy` 与 Run Metadata。它不执行 Codex，不产生 `EVD-*`、Support Assessment 或已验证 architecture 结论，不实现 myharness feature，也不迁移 Cycle 7–18。

V4.1 Week 5–6 原文可在基线提交 `f2b3961cbe125f846818d11a8892fe3c34f2751f` 中复查。旧 `EXP-W05-01` 与 `EXP-W06-01` 只作为历史计划 ID 保留。

## Codex Host 工作模型（Working Model）

```text
公开 Contract Surface
  AGENTS.md · Memories · Skills · MCP · Subagents · Plugins · Hooks · Config
        ↓
绑定 revision 的 Official Source Boundary
        ↓
绑定 Host / Provider / Model / Configuration 的 Observed Behavior

执行治理候选层：
Sandbox Boundary → Approval / Trust Decision → Command Rule / Hook → Project Rule → CI / Acceptance
```

该图是 `Mental Model V0`，不是 Codex 已验证 architecture。官方文档、源码和行为分别回答公开承诺、特定 revision 实现与特定运行条件下实际发生了什么；任何一个来源都不能代替另外两个。`openai/codex` 在固定 commit 前只是官方浮动仓库锚点，不能产生可复现 Source Evidence。

---

## Cycle 5 · Codex Architecture & Customization

> Codex Host · V4.1 映射：Week 5

### 核心研究问题

> **Codex 如何通过公开 customization surface 与特定 revision 的实现组织项目指导、可复用能力和扩展边界，myharness 应依赖哪些 Stable Surface 而不是 Implementation Detail？**

### 为什么与 myharness 有关

Codex 是 advanced open-source implementation reference，但“源码可见”不等于“内部结构就是稳定 Contract”。如果 myharness 直接依赖某个 crate、目录或当前加载顺序，Host 升级就可能破坏 Adapter；如果只看官方功能名称，又可能把 AGENTS.md、Skill、MCP、Subagent、Hook 与 Plugin 当成可互换机制。Cycle 5 用 Contract → Source → Behavior 三层方法建立可攻击的 architecture map。

### 研究范围（Scope）

本 Cycle 只研究：

- Codex 官方 Customization、AGENTS.md、Skills、MCP、Subagents、Plugins、Hooks 与 Config 的公开 Contract；
- 每个 surface 的 owner、discovery / load timing、scope、trigger、Context boundary、distribution 与 failure route；
- `openai/codex` 固定 revision 中与上述 capability boundary 直接相关的实现入口；
- 同一 Skill body 在清晰与模糊 description 下的 discovery / activation 差异；
- Contract、Source 与 Behavior 一致、不一致和 Unknown 的明确记录。

本 Cycle 不研究：

- 从第一行顺序阅读完整仓库，或追踪 TUI、网络客户端与无关基础设施；
- 把当前 crate、module 或目录名写成长期 Contract；
- 完整 Skill outcome evaluation、跨 Host portability 或 myharness Plugin 实现；
- 未绑定 commit 的 Source Evidence、未绑定运行条件的 Behavior Evidence 或 Support Assessment。

### 主线研究对象与权限边界（Authority Boundary）

| 研究对象（Research Object） | 计划深度 | Cycle 5 用途 | 权限边界（Authority Boundary） |
|---|---|---|---|
| Codex official docs：Customization、AGENTS.md、Build skills、Build plugins | L2 定向 | 建立公开 customization surface、scope、progressive disclosure 与 packaging Contract map | 浮动官方页面；执行时绑定 Codex version、重新核验页面与访问日期；不能证明本地加载或内部实现 |
| Codex official docs：MCP、Subagents、Hooks、Config | L2 定向 | 补齐 external tool、delegation、lifecycle 与 configuration boundary | 从官方导航按 capability 重新定位；页面存在不等于配置已启用或行为有效 |
| [openai/codex](https://github.com/openai/codex) | L3 targeted source | 对 Contract / Behavior 暴露的问号做 question-driven source reading | 官方仓库身份已知，但默认分支是浮动锚点；执行时必须固定 commit、重新定位 source path 并限定 claim scope |

Batch 3 只登记计划来源，不产生 Contract 或 Source Evidence claim。不得把源码中存在的 capability 自动解释为当前安装版本已启用、公开承诺或行为已验证。

### 问题驱动的阅读路线（Question-driven Reading Route）

1. 先读官方 Customization overview，画出只含公开 surface 的 Architecture V0，并标记所有 Unknown。
2. 定向阅读 AGENTS.md、Skills、Plugins、MCP、Subagents、Hooks 与 Config；为每项填写 `discover → load → trigger → execute → persist / distribute → fail`。
3. 固定 `openai/codex` commit，先建立当时的 Repository Map；按 capability 搜索，不沿用 V4.1 写下的 crate / module 名。
4. 单个源码问题只跟到能回答 boundary 的 1–2 层调用，并记录 search term、path、stop point 与仍未回答的问题。
5. 最后执行 Behavior observation；若 Contract、Source 与 Behavior 不一致，分别登记，不用源码“纠正文档”或用行为猜内部原因。

阅读时只追：

- AGENTS.md、Skill、MCP、Subagent、Hook 与 Plugin 分别在何时被发现、加载或触发？
- Plugin 是 capability 语义、依赖集合，还是 Host-specific distribution unit？
- Skill metadata 与 full instructions 是否处于不同 Context 阶段？
- 哪些 implementation boundary 对 myharness 只是解释材料，哪些公开 surface 才可作为 Adapter dependency？
- 同名 capability 在 CLI、IDE、desktop 或 cloud surface 是否需要分别验证？

### Customization 职责假设（Mental Model V0）

| Surface | 候选职责 | 需要验证的边界 / failure mode |
|---|---|---|
| AGENTS.md | 按 global → project → nested scope 组合的持久项目指导 | discovery root、override precedence、size limit、session start timing |
| Memory | Host 管理的可延续上下文候选 | owner、freshness、load timing 与 project artifact 的差异 |
| Skill | 通过 metadata discovery、按需加载 full instructions 的可复用 workflow | description 命中、正文是否加载、procedure 是否执行 |
| MCP | 把外部 Tool / system 接入 Host | 连接可用不等于工具选择、调用或 workflow 正确 |
| Subagent | 独立 responsibility、Context 与 Tool boundary | 只换角色名称、上下文泄漏或 handoff loss |
| Hook | 在 lifecycle event 上运行受信任或受管理逻辑 | event、trust、并发、阻断语义和 failure route |
| Plugin | 安装、版本化和分发 Skill、Hook、MCP-backed app 等 Host-specific artifacts | packaging 被误当成 capability semantics 或 Portable Contract |

该表是待验证责任模型。具体 discovery、加载、并发或 trust 语义必须绑定官方页面版本、源码 commit 与 Behavior Run，不能从 Mental Model V0 直接形成结论。

### 假设（Hypothesis）

> **H-C05-01:** 在绑定相同 Codex、Provider、Model、Configuration 与 T02 task instance，且 Skill body、scope 和文件位置相同的条件下，边界清晰、前置关键触发词的 description 比刻意模糊的 description 更容易被正确发现并激活；description 只影响 discovery / activation，不能单独保证 procedure adherence 或 review outcome。

> **H-C05-02:** 在相同 T01 fixture、root `AGENTS.md` 与运行条件下，增加一个只适用于目标子目录的 nested `AGENTS.md`，会只改变该 scope 内的 Instruction 组合与行为，而不会改变 control scope；如果目标文件、工作目录或 instruction chain 无法绑定，观察不能归因于层级覆盖。

> **H-C05-03:** 对同一 T02 instance 和同一现有 Codex Plugin capability，启用 Plugin distribution 会改变该 capability 的可发现性或加载路径；Plugin 显示为 installed、capability listed 或 artifact present，均不能单独证明 capability 已激活、执行或改善结果。

支持信号：清晰 description variant 的正确发现 / 激活更稳定，且差异能与 full `SKILL.md` 是否加载及后续执行阶段分开记录。

反驳信号：两种 description 在相同条件下没有方向性差异，或模糊 variant 同样稳定且不存在额外误触发。

不确定信号：技能列表预算、显式调用、安装位置、同名 Skill、Host surface、Model 或 task wording 同时变化，无法把差异归因于 description。

`H-C05-02` 的支持信号是 nested scope 内出现与 instruction chain 一致、control scope 不出现的方向性差异；反驳信号是绑定条件下两个 scope 无差异；若两组 task、文件或配置不一致则为 `INCONCLUSIVE`。`H-C05-03` 的支持信号是启用 Plugin 后出现可复查的 distribution → discovery → load transition；反驳信号是启用与禁用状态没有对应差异；如果 capability 本身、Plugin revision 或显式调用同时变化则为 `INCONCLUSIVE`。

### 计划实验（Planned Experiments）

#### `EXP-C05-01` · Contract → Source → Behavior Architecture Trace

- 实验类型（Experiment Type）：`EXPLORATORY`
- Outcome Mode：`OBSERVATION_ONLY`；Experiment Result 为 `NOT APPLICABLE · OBSERVATION ONLY`
- 稳定任务（Stable Task）：`T03 · Medium Change`
- 历史映射（Legacy Mapping）：`EXP-W05-01` 的 Architecture V0 → Source → Behavior 部分（仅为历史计划）
- 观察设计（Observation Design）：先画 Contract-only V0；固定官方页面访问日期和 `openai/codex` commit；在一个 T03 task 中只追实际涉及的 AGENTS、Skill、Plugin / Hook 或 Tool surface；记录 discovery、load、trigger、action、state transition、artifact、failure 与 stop point
- 主要观察项（Primary Observations）：Contract / Source / Behavior agreement、unexpected boundary、source path stability、unloaded artifact、Host-surface difference、Provider / Model confounder
- 解释边界（Interpretation Boundary）：本实验只生成 architecture question map 和候选 claim，不因一次 trace 宣称完整 Runtime architecture

#### `EXP-C05-02` · Skill Description Discovery Comparison

- 实验类型（Experiment Type）：`COMPARATIVE`
- 稳定任务（Stable Task）：`T02 · Semantic Review`
- 历史映射（Legacy Mapping）：`EXP-W05-01` 的 Skill Discovery 部分（仅为历史计划）
- Baseline A：同一 Skill body 使用边界清晰、前置关键触发词的 description
- Variant B：同一 Skill body 使用语义宽泛、缺少边界与关键触发词的 description
- 单一主要变量（Primary Variable）：Skill description；Skill body、name、scope、location、task statement 与运行条件保持相同
- 主要观察项（Primary Observations）：listed / omitted、implicit discovery、correct activation、false activation、full body loaded、procedure adherence、review evidence、Context cost
- 固定边界（Fixed Boundary）：不得显式点名 Skill；本实验主要裁决 discovery / activation，不承担 Cycle 10 的完整 Skill outcome evaluation
- 结果词汇（Result Vocabulary）：`SUPPORT / REJECT / INCONCLUSIVE`

#### `EXP-C05-03` · AGENTS Scope and Override Comparison

- 实验类型（Experiment Type）：`COMPARATIVE`
- 稳定任务（Stable Task）：`T01 · Engineering Constraint`
- 历史映射（Legacy Mapping）：`EXP-W05-01` 的 `AGENTS.md` 层级实验部分（仅为历史计划）
- 共同任务（Shared Task）：在隔离 fixture repository 中，对 target scope 与 control scope 各做一个同构、小型、可逆修改；root `AGENTS.md`、task statement、acceptance checks 与初始文件保持相同
- Baseline A：只有 root `AGENTS.md`
- Variant B：在 target scope 增加 nested `AGENTS.md`，其可观察约束只适用于该目录；control scope 不变
- 单一主要变量（Primary Variable）：是否存在 nested `AGENTS.md`；必须记录工作目录、目标文件、instruction chain 与实际适用 scope
- 主要观察项（Primary Observations）：instruction discovery、scope selection、override / merge behavior、target adherence、control leakage、acceptance result、false attribution、human intervention
- 结果词汇（Result Vocabulary）：`SUPPORT / REJECT / INCONCLUSIVE`

#### `EXP-C05-04` · Plugin Distribution and Load Boundary Trace

- 实验类型（Experiment Type）：`COMPARATIVE`
- 稳定任务（Stable Task）：`T02 · Semantic Review`
- 历史映射（Legacy Mapping）：`EXP-W05-01` 的 Plugin 实验部分（仅为历史计划）
- Fixture 边界：执行时从已存在的 myharness Codex Plugin 移植中选择一个不需修改的真实 capability，固定 Plugin revision、capability body 与 T02 instance；若没有满足条件的现有 capability，本实验保持 `NOT EXECUTED`，不得临时实现 Plugin 来填补迁移记录
- Baseline A：Plugin 未启用，且不存在其他提供同一 capability 的重复安装
- Variant B：启用同一固定 Plugin revision；不显式点名 Plugin 或 capability
- 单一主要变量（Primary Variable）：Plugin distribution 是否启用；Host、Provider、Model、Configuration、task statement 与 capability content 保持相同
- 主要观察项（Primary Observations）：installed / enabled state、artifact discovery、capability listed、body loaded、activation、procedure execution、review evidence、failure route、Context cost
- 解释边界（Interpretation Boundary）：本实验只研究 Plugin packaging / load boundary；不修改 myharness Plugin，不把 installed / listed 写成 capability effective，也不提前裁决 Cycle 9 portability
- 结果词汇（Result Vocabulary）：`SUPPORT / REJECT / INCONCLUSIVE`

四个实验分别保存 Run Metadata。`EXP-C05-01` 不能替代三个受控对照；内容生成不创建 Run、不填写结果，也不产生 Architecture V1 / V2 结论。

### 退出条件（Exit Criteria）

Cycle 5 只有在以下条件均满足后才能结束：

- 官方 Contract map 绑定 Codex version、surface、访问日期与 Source ID；
- `openai/codex` Source Evidence 固定完整 commit，并记录 authority、scope、path、search term 与 stop point；
- Architecture V0 / V1 明确区分 Contract、Source、Behavior 与 inference；
- `EXP-C05-01` 至少完成一个可复查 T03 trace，`EXP-C05-02` 完成共享 T02 baseline 的配对 Run；
- `EXP-C05-03` 完成 root-only / nested `AGENTS.md` 配对 Run，且 target 与 control scope 均有可复查 acceptance evidence；
- `EXP-C05-04` 完成 Plugin disabled / enabled 配对 Run；若没有符合 fixture 边界的既有 capability，必须明确保持 `NOT EXECUTED`，Cycle 5 不得把 Week 5 Plugin 迁移项标记为已验证；
- 结果区分 discovery、activation、execution 与 outcome，没有把 Skill loaded 写成 Skill effective；
- Mental Model V1 标明 Stable Surface、Implementation Detail、Host-surface difference 与 Unknown；
- 不实现 myharness Codex Adapter，不提前进入 Cycle 9 cross-host abstraction 或 Cycle 10 Skill evaluation。

---

## Cycle 6 · Codex Execution、Safety & State

> Codex Host · V4.1 映射：Week 6

### 核心研究问题

> **在 Codex 的执行链中，Sandbox、Approval、Command Rule、Hook 与执行状态各承担什么责任，Host technical boundary 与 Harness engineering governance 应如何分工而不产生无意义的 Double Block？**

### 为什么与 myharness 有关

如果 myharness 的 pre-execution guard 重复 Host 已经强制的技术边界，可能增加 approval noise、重复阻断和不可解释的 retry；如果把项目工程语义全部交给 Sandbox，又会让 Host 无法理解 timeout、branch policy 或验证要求。Cycle 6 建立责任矩阵，并要求每次阻断都能追溯请求、决策者、理由、状态变化与最终结果。

### 研究范围（Scope）

本 Cycle 只研究：

- Codex 官方 Rules、Hooks、Sandbox、Agent approvals & security 与 Config Contract；
- Host Safety Boundary、Approval / Trust Decision、Harness Engineering Policy、Project Rule 与 CI / Acceptance Gate 的职责差异；
- 无破坏性命令的 request → policy → approval → sandbox / hook → result → retry / stop 状态轨迹；
- 固定 `openai/codex` revision 中与 execution、policy、sandbox、hook 和 state boundary 直接相关的实现；
- myharness `pre_bash_guard` 的未来只读 Project mapping，不在本 Batch 修改实现。

本 Cycle 不研究：

- 绕过 Sandbox、真实破坏、敏感数据访问、危险命令或真实凭据；
- 完整 OS sandbox implementation、企业合规或所有平台差异；
- 把 project engineering policy 伪装成 Host trust boundary，或反过来；
- 未固定 commit 的 Source Evidence、未执行的 Behavior claim、Support Assessment 或产品实现。

### 主线研究对象与权限边界（Authority Boundary）

| 研究对象（Research Object） | 计划深度 | Cycle 6 用途 | 权限边界（Authority Boundary） |
|---|---|---|---|
| Codex official docs：Rules、Hooks、Sandbox、Agent approvals & security、Config basics | L2 定向 | 映射 command policy、lifecycle interception、technical boundary、approval 与 configuration Contract | 浮动官方页面；执行时绑定 Host version / surface / platform；不能证明本地配置或行为 |
| [openai/codex](https://github.com/openai/codex) | L3 targeted source | 只回答 execution / policy / sandbox / hook / state boundary 的已声明问题 | 默认分支不是可复现 Source Evidence；执行时固定 commit 并按 capability 重新定位路径 |
| myharness pre-execution artifacts | Read-only Project mapping | 判断现有 guard 的 intent 是否与 Host boundary 重叠 | 文件存在不等于 guard 已触发、有效或需要保留；必须由 Project / Behavior Evidence 支持 |

官方 Contract 可以说明公开控制面，Source 可以解释绑定 revision，Behavior 才能说明特定配置下谁实际阻断。三者冲突时保留冲突和限制。

### 问题驱动的阅读路线（Question-driven Reading Route）

1. 先用官方 Sandbox 与 approvals 文档区分 technical boundary 和 human trust / escalation decision。
2. 再读 Rules 与 Hooks，记录匹配对象、触发点、decision vocabulary、trust、并发、错误与可见理由。
3. 用 Config basics 固定 active config layer、permission / sandbox profile、network setting 与 experiment snapshot。
4. 固定 `openai/codex` commit，只针对尚未回答的 execution / policy / state 问题搜索并跟 1–2 层调用。
5. 最后对无破坏性 fixture 做 Behavior trace；每次记录 request、matched policy、approval、hook、sandbox outcome、Agent interpretation、retry 与持久化 / 重载观察。

阅读和观察时只追：

- Sandbox 决定“技术上能否做”，Approval 决定“何时必须问人”，两者在哪些 surface 不同？
- Command Rule、Hook、AGENTS / Project Rule 与 CI 各自能观察、提示、阻断或验证什么？
- 一个请求被多层同时阻断时，谁先决策、理由是否可见、Agent 是否重复尝试？
- 哪些 state 属于当前 turn / session，哪些来自持久 config / trust，哪些只是实验 Artifact？
- Host、Harness、Project 与 CI 责任重叠时，删除哪一层仍能保留必要控制？

### 执行责任假设（Mental Model V0）

| Layer | 候选职责 | 失败 / 重叠风险 |
|---|---|---|
| Host Sandbox | 以平台机制限制文件、网络和进程可达范围 | 被误当成理解项目工程语义；平台差异未记录 |
| Approval / Trust | 在越过边界或使用有副作用能力前请求授权，并记录授权范围 | approval fatigue、范围过宽、理由不清 |
| Command Rule | 对命令前缀等 Host-recognized request 做 allow / prompt / forbid 类决策 | experimental semantics 变化、匹配误判、被误当成通用项目 Rule |
| Hook / Harness Guard | 在 lifecycle point 注入项目特定观察、验证或阻断 | 与 Rule / Sandbox double block、并发、trust 和维护成本 |
| Project Rule | 向 Model 表达工程约束和理由 | 依赖遵循，不能代替确定性 enforcement |
| CI / Acceptance Gate | 在结果边界验证代码、测试与 policy outcome | 只能事后发现、反馈过晚或与前置 guard 重复 |
| Execution State | 关联 request、decision、approval、result、retry 与 configuration snapshot | 将 UI / transcript / config / trust / artifact 混成一个“state” |

该表是待验证责任模型，不构成安全保证、平台结论或 Codex capability assessment。

### 假设（Hypothesis）

> **H-C06-01:** 对同一个能够产生隔离、可逆 marker effect 且预先配置为触发 Host hard-deny 的 T01 acceptance command，在相同 Sandbox / Approval / Rule baseline 上再增加覆盖同一 command 与语义范围的 Harness pre-execution deny，不会增加已阻止的 marker effect；两个 hard-deny 也不应预设为可同时观察，而会按实际 lifecycle order 表现为 Host-shadowed、Harness-shadowed 或 sequentially observable。只有 Harness 层提供 Host 层无法表达的项目语义或可复查 Evidence 时，重叠才可能有净价值。

支持信号：A / B 都阻止同一 marker effect，B 中新增 guard 被一层遮蔽，或在可观察的顺序中增加 decision、重试、人工干预或理由混淆，但没有增加被阻止的效果。

反驳信号：Harness 层在不增加不可接受噪声的情况下，稳定提供 Host baseline 缺失的项目语义、Evidence 或更早且更准确的治理。

不确定信号：fixture 没有稳定触发 Host hard-deny、marker 初始状态或清理不一致、两层判定语义不相同、配置或平台改变，或无法确定 lifecycle order 与最终 decision owner。

### 计划实验（Planned Experiments）

#### `EXP-C06-01` · Non-destructive Execution Boundary Trace

- 实验类型（Experiment Type）：`EXPLORATORY`
- Outcome Mode：`OBSERVATION_ONLY`；Experiment Result 为 `NOT APPLICABLE · OBSERVATION ONLY`
- 稳定任务（Stable Task）：`T01 · Engineering Constraint`
- 历史映射（Legacy Mapping）：`EXP-W06-01` 的责任分类与无破坏性观察部分（仅为历史计划）
- 共同 T01 instance：`T01-C06-LOCAL-TIMEOUT-VALIDATION`。在固定 commit 的隔离 fixture repository 中，扩展已有本地 config parser，使 `timeout_ms <= 0` 返回既有 validation error，同时保持正值与未提供该字段时的既有行为
- 工程约束（Engineering Constraints）：只修改实验记录中冻结的 parser source 与对应 test file；不改变公开 schema 或 error type；不访问网络；acceptance checks 必须覆盖负数、零、正数与字段缺省四种情况
- Acceptance effect：受挑战的本地 acceptance command 在运行测试前，只向隔离工作区的实验目录写入一个内容固定的 marker；marker 初始为 absent、可复查且可清理，不访问外网、secret 或工作区外路径
- Fixture 边界：除受挑战的 acceptance command 外，只使用读取测试文件、工作区内可逆写入、`git status`、本地 no-op / dry-run command 等无破坏性动作；不运行危险命令，不把 marker 解释为真实安全影响
- 观察设计（Observation Design）：为每个动作记录 request、active config、matched Rule、approval、Hook、Sandbox result、marker before / after、Agent-visible reason、retry / fallback、acceptance result、artifact 与 human intervention
- 强制 State checkpoint：完成同 Session trace 后，清理 marker 并从同一 repository commit、task instance 与 configuration snapshot 启动 fresh run；分别记录 conversation / turn state、persistent config / trust、实验 Artifact 的 reload / reset，不作性能比较
- T01 完成边界：被阻断的 challenge observation 完成后，只能使用预先声明并记录为 Human intervention 的 recovery profile 运行同一 acceptance checks；不得由 Agent 自行寻找等价命令绕过 policy
- 主要观察项（Primary Observations）：decision owner、block / allow reason、approval scope、state transition、duplicate decision、false positive、recovery path、fresh-run difference
- 解释边界（Interpretation Boundary）：本 trace 发现责任重叠与候选 confounder，不单独裁决 `H-C06-01`

#### `EXP-C06-02` · Host Deny vs Guard Shadowing Comparison

- 实验类型（Experiment Type）：`COMPARATIVE`
- 稳定任务（Stable Task）：`T01 · Engineering Constraint`
- 历史映射（Legacy Mapping）：`EXP-W06-01` 的 Double Block 部分（仅为历史计划）
- 共同 T01 instance：复用 `EXP-C06-01` 的 `T01-C06-LOCAL-TIMEOUT-VALIDATION`、repository baseline、task statement、工程约束、acceptance checks 与隔离 marker effect
- 共同 fixture：受挑战的 acceptance command 经预检查能稳定命中 Host `forbid` / hard-deny，并且在无 deny 的 control preflight 中会写入 marker；如果任一条件不成立，实验结果为 `INCONCLUSIVE`
- Baseline A：固定 Sandbox / Approval / Command Rule，只由 Host hard-deny 处理受挑战的 acceptance command
- Variant B：与 A 相同，再增加对同一 command、同一语义范围作 hard-deny 的 Harness pre-execution guard
- 单一主要变量（Primary Variable）：是否增加语义重复的 Harness guard
- 顺序判定（Ordering Classification）：根据绑定 Host version / surface 的 Contract、固定 source revision 与 Direct Behavior trace，将 B 记录为 `HOST_SHADOWS_HARNESS`、`HARNESS_SHADOWS_HOST`、`SEQUENTIALLY_OBSERVABLE` 或 `UNKNOWN`；不得把只观察到一次 deny 写成 Double Block
- 效果判定（Effect Measurement）：每个 Run 前 marker 必须 absent；记录 command control preflight、A / B 的 marker before / after 与 cleanup。只有 control 会写入而 A / B 均未写入时，才能说两层针对同一个可观察效果
- 恢复边界（Recovery Boundary）：每个 variant 只观察一次受挑战 command；随后由预先声明的 Human intervention 应用相同 recovery profile，执行同一 acceptance checks 完成 T01。Agent 不得通过改写命令逃避 policy
- 主要观察项（Primary Observations）：marker effect、ordering classification、decision count、approval count、retry、reason attribution、shadowed layer、false positive、recovery cost、task completion、Context cost、human intervention
- 结果词汇（Result Vocabulary）：`SUPPORT / REJECT / INCONCLUSIVE`

两个实验都必须保存独立 Run Metadata，绑定 platform、Codex version、Provider profile、Model、configuration snapshot、Rule / Hook / Check / Adapter revision。A / B 必须从相同 repository baseline 与 absent marker 状态开始；不得为了触发安全机制而扩大权限或制造真实风险。

### 退出条件（Exit Criteria）

Cycle 6 只有在以下条件均满足后才能结束：

- Contract map 绑定 Codex version、surface、platform、访问日期与 Source ID；
- Source reading 固定 `openai/codex` 完整 commit，并记录 question、path、stop point 和 limitation；
- `EXP-C06-01` 完成满足冻结 T01 contract 的无破坏性 execution / state trace，包括同 Session 与强制 fresh-run checkpoint；
- `EXP-C06-02` 完成共享 T01 instance、相同 marker 初始状态与相同 recovery profile 的 A/B 配对 Run，并给出 ordering classification；
- Evidence 能区分 Sandbox、Approval、Command Rule、Hook / Harness、Project Rule 与 CI / Acceptance 的 decision owner；
- 能解释当前 turn / session state、persistent config / trust 与实验 Artifact 的区别，Unknown 明确保留；
- Mental Model V1 记录 Double Block、false positive、approval noise、reason visibility 和平台限制；
- 不修改 myharness guard，不执行危险操作，不形成法律合规或普遍安全结论。

---

## Batch 3 路线复盘触发条件（Route Review Trigger）

完成 Cycle 6 的真实研究后执行一次 Route Review。它可以调整 Batch 4 的 Qwen Code Contract / Enterprise 项目锚点、证据深度、实验节奏或借用方法，但不能改变冻结的 Cycle 名称、编号、顺序或 Batch 边界。

内容生成本身不满足 Cycle 5–6 Exit Criteria，也不创建 Route Review 结果。若 Contract、Source 与 Direct Behavior 的冲突推翻 Codex Host 工作模型，可在当前 Cycle 内缩小问题；跨 Host 映射、完整 Skill evaluation 和其他旁支进入后续 Cycle 或 Open Questions。

## Batch 3 迁移记录（Migration Record）

| V4.1 历史计划 | V4.2 研究设计 | 状态（Status） |
|---|---|---|
| Week 5 · `EXP-W05-01` | Cycle 5 · `EXP-C05-01`–`EXP-C05-04` | 拆分为三层 architecture trace、Skill description、AGENTS hierarchy 与 Plugin load 四项设计，尚未执行；旧 ID 只作历史记录 |
| Week 6 · `EXP-W06-01` | Cycle 6 · `EXP-C06-01` / `EXP-C06-02` | 拆分为绑定真实 T01 修改的 execution / state trace 与 Host deny / guard shadowing 对照，尚未执行；旧 ID 只作历史记录 |

迁移只更新未来研究设计，不声称 V4.1 实验已发生，也不把旧 ID 重编号成 Evidence。执行前必须刷新官方文档、固定 `openai/codex` commit，并按 capability 重新定位 source path。

---

## Batch 4 边界（Boundary）

Batch 4 已生成 Cycle 7 · Qwen Code Host Architecture & Enterprise Reality；该 V4.3 owner decision 取代 V4.2 的 ZCode 研究对象，但保留 Cycle / Batch / Experiment 编号。

Cycle 7 是 V4.2 新增、在 V4.3 替换主要 Host 的研究单元，没有 V4.1 Week 或 `EXP-Wxx-yy` 历史迁移对象。本 Batch 只建立计划态 Contract / pinned Official Source / Behavior / local configuration / Enterprise Fact 研究边界、官方来源登记与 `EXP-C07-yy` 实验设计。它不运行 Qwen Code，不产生 `EVD-*`、Enterprise Fact、Support Assessment 或法律合规结论，不实现 Qwen Code Adapter，也不迁移 Cycle 8–18。

## Qwen Code Host 工作模型（Working Model）

```text
Official Contract + Bound Qwen Code Version / Surface
        ↓
Pinned QwenLM/qwen-code Revision + Capability Map
        ↓
Host Runtime
QWEN.md / Memory · Session · Tool · Approval · Sandbox
Hook · Skill · Subagent · Extension
        ↓
Provider Adapter + Endpoint / Protocol + Authentication + Routing
        ↓
Model ID / Revision + Capability + Options
        ↓
Direct Behavior + Project Artifact + Enterprise Fact + Run Metadata
```

该图是 `Mental Model V0`，不是 Qwen Code 已验证 architecture、Behavior 或企业就绪结论。官方文档说明公开 Contract；固定 `QwenLM/qwen-code` revision 只能说明该 revision 的实现；Direct Behavior 才能说明绑定 Host、surface、Provider、Model 与 Configuration 条件下实际发生了什么。Enterprise Fact 必须绑定组织环境、部署方式、证据与日期。

---

## Cycle 7 · Qwen Code Host Architecture & Enterprise Reality

> Qwen Code Host · V4.3 Host-set replacement · 无 V4.1 Week 映射

### 核心研究问题

> **在绑定 Qwen Code 版本、surface 与官方源码 revision 后，哪些 Harness 语义由 Host 保持，哪些依赖 Provider、endpoint / protocol、Model 或 Configuration；哪些部署事实足以支持 enterprise reality，哪些仍必须保持 Unsupported / Unknown？**

### 为什么与 myharness 有关

Qwen Code 的研究角色是 domestic open-source coding-agent、Qwen ecosystem 与 enterprise deployment reality reference。myharness 不能把“使用 Qwen 系列模型”“兼容某种 API”“官方源码存在”“某个企业环境允许部署”混成一个 Host 支持结论。Cycle 7 通过 Contract → pinned Source → Provider / Model Profile → Behavior → Project / Enterprise Fact 的证据链，识别哪些语义可进入 Portable Semantic Contract，哪些只能留在 Qwen Code Host Adapter、Provider Profile 或特定 deployment fact sheet。

### 研究范围（Scope）

本 Cycle 只研究：

- Qwen Code 官方 overview、configuration、model providers、memory / `QWEN.md`、tools、approval、sandbox、hooks、skills、subagents、extensions 与 session Contract；
- `QwenLM/qwen-code` 固定 revision 中与本次 capability slice 直接相关的 bounded implementation path；
- Qwen / Alibaba Cloud、OpenAI-compatible、Anthropic-compatible、Gemini-compatible 或其他已授权通道中的 Provider、endpoint / protocol、authentication、Model ID 与 Configuration 分离；
- 绑定 Host version / platform / deployment profile 的无破坏性 Direct Behavior；
- 安装分发、身份访问、数据处理、日志审计、代理 / 证书、升级回退、远程执行、支持路径与采购等 deployment-specific Enterprise Fact；
- 实际执行 artifact 到 official release / tag / commit 的 provenance，以及 Contract / Source / Behavior 的一致、冲突与 Unknown。

本 Cycle 不研究：

- 把浮动默认分支、官方 architecture overview 或当前 package path 写成所有版本的稳定 Contract；
- 没有真实组织记录支撑的私有化、数据驻留、SLA、审计、采购或合规结论；
- 把 Qwen 系列 Model、其他 Model 或 Provider 的输出效果自动归因给 Qwen Code Host；
- 以兼容 OpenAI / Anthropic 协议推导 Provider 或 Model behavior 等价；
- Qwen Code Adapter 实现、跨 Host abstraction、公开模型 benchmark 或危险权限测试。

### 官方来源路线与权限边界（Authority Boundary）

| 来源组 | 计划深度 | Cycle 7 用途 | 权限 / 停止边界 |
|---|---|---|---|
| Qwen Code Overview、Settings、Model Providers、Memory | L2 定向 | 建立 installation、configuration precedence、`QWEN.md` / memory、Provider / protocol / Model Contract map | 浮动官方页面；不能证明本地配置已生效、Provider / Model behavior 等价或企业批准 |
| Qwen Code Approval、Sandbox、Hooks、Skills、Subagents、Extensions | L2 定向 | 建立 tool decision、isolation、lifecycle、discovery / activation、delegation 与 distribution boundary | surface 存在不等于配置已启用、机制已触发、任务有效或跨版本一致 |
| [`QwenLM/qwen-code`](https://github.com/QwenLM/qwen-code) + official releases | L3 targeted source | 对绑定 capability question 做 revision-bound source reading，并建立 release / artifact provenance | 官方仓库身份已核验；默认分支与 latest release 浮动，执行时固定完整 commit；Source 不替代 Behavior |
| local configuration 与 Direct Behavior | L3 受控观察 | 验证特定版本、平台、Provider profile 与权限模式下的 observable behavior | 必须脱敏、可逆并保存 Run Metadata；单次行为不得外推到其他 profile |
| organization-specific records | L2 fact verification | 填写 Enterprise Readiness Fact Sheet | 没有 `ENT-*` 与 Enterprise Evidence 时保持 Unknown；不得形成普遍法律结论 |

Batch 4 只登记 `SRC-QWENCODE-001..013` 计划来源，不从来源条目直接派生 `EVD-*`。所有官方页面、release 列表与默认分支都是执行时重新核验的浮动锚点；源码必须固定完整 commit 后才能派生 revision-bound Source Evidence。

### Qwen Code Official Source Verification

```text
Host: Qwen Code
Scope: CLI Runtime and explicitly bound surfaces
Repository Identity: VERIFIED
Repository: https://github.com/QwenLM/qwen-code
Pinned Revision: NOT PINNED
Execution Artifact Provenance: NOT VERIFIED
Authority Basis: official QwenLM organization, official docs link, releases and repository license
Limitations: 当前只确认仓库身份；没有固定 commit、source path、安装 artifact mapping 或 EVD claim
```

在 revision / provenance gate 未通过时：

- 不创建 revision-bound Qwen Code Runtime `SOURCE` Evidence；
- 不用默认分支解释当前安装版本的内部 module、call path、context lifecycle 或 permission order；
- 固定源码但无法映射安装 artifact 时，Source observation 与 Behavior observation 分开，agreement 保持 `UNKNOWN`；
- Contract、Behavior、local configuration 与 Enterprise Fact 研究可以继续，但不能互相替代。

### 问题驱动的研究路线（Question-driven Research Route）

1. 从官方 overview、repository 与 release channel 核验产品 / artifact identity，冻结本次研究的 Host version、surface、platform、installation channel 与访问日期。
2. 建立 Contract matrix：为 `QWEN.md` / memory、Session、Tool、Approval、Sandbox、Hook、Skill、Subagent、Extension 与 Provider / Model configuration 分别记录 owner、scope、trigger、persistence、observable state 与 Unknown。
3. 建立 Provider Profile 与 deployment profile；分别记录 authentication、endpoint type、base URL category、Model ID、credential owner、network boundary 与 secret redaction，禁止把 Provider / Model 写进 Host 固有能力。
4. 固定 `QwenLM/qwen-code` 完整 commit，只追本次实验实际触及的 capability path，并通过 official release / package / build metadata 建立执行 artifact provenance；无法映射时保留 `UNKNOWN`。
5. 执行 `EXP-C07-01`，用安全、确定、可逆的 T01 实例追踪 Contract → Source → Configuration → Behavior；不读取 secret，不访问工作区外路径。
6. 在能固定相同 Host / surface / repository / task / configuration 且核验同一 Model identity 时执行 `EXP-C07-02`；只有完成两个 Provider profile 的配对 Run 后，才可因 endpoint、routing、quota 或 policy 无法分离而输出 `INCONCLUSIVE`。无法通过 comparability gate 时保持 `NOT EXECUTED`，不填写 Result。
7. 只在取得真实组织 / 环境记录后创建 `ENT-QWENCODE-*`，逐项验证安装、访问、credential、network、telemetry / logging、升级、支持和采购事实；缺失项保持 Unknown。
8. 将 Contract / Source / Behavior / Project / Enterprise contradictions 分开登记；默认分支、release 或文档变化触发重新验证，不静默改写结论。

### Host / Provider / Enterprise 分层表

| 层（Layer） | 需要绑定的最小字段 | 可以回答 | 不能自动回答 |
|---|---|---|---|
| Host Contract | product identity、Host version、platform、surface、Source ID、access date | 官方公开了什么 capability / configuration surface | 本地是否启用、内部如何实现、企业是否允许 |
| Official Source | repository、完整 commit、path、question、stop point、artifact provenance | 特定 revision 如何实现限定 capability | 安装版本是否采用、未来 Contract、其他 surface / branch behavior |
| Provider Profile | provider、endpoint type、authentication、Model ID、quota / policy context | 模型请求通过什么通道、哪些变量属于 Provider / Model | Host control surface 是否等价、输出质量是否可移植 |
| Local Configuration | redacted snapshot、workspace、permission mode、remote / local execution location | 特定环境配置了什么 | 配置是否生效、其他机器是否相同 |
| Direct Behavior | Experiment / Run、request、decision、result、artifact、human intervention | 特定条件下实际观察到什么 | 内部源码原因、其他版本 / profile behavior |
| Enterprise Fact | organization alias、deployment、evidence、owner、verified date、limitations | 特定部署事实 | 通用 enterprise readiness 或法律合规 |

### Enterprise Reality 检查面

| 检查面 | 必需事实 | 没有事实时的记录 |
|---|---|---|
| Installation / Distribution | 安装来源、版本锁定、受支持平台、离线 / 远程资源要求 | `Unknown` |
| Identity and Access | 登录方式、credential owner、权限模式、项目 / 会话授权范围 | `Unknown` |
| Provider and Network | Provider、endpoint type、代理 / 证书、egress、secret storage / rotation | `Unknown` |
| Data Handling | 输入内容类别、传输对象、保留 / 删除、组织 policy 与合同依据 | `Unknown`；不得用营销文案补齐 |
| Logging / Audit | 可导出日志、事件范围、脱敏、保存位置、访问控制、留存期 | `Unknown` |
| Upgrade / Rollback | release channel、强制 / 自动更新、兼容性、rollback procedure | `Unknown` |
| Remote Execution | 本地 / SSH / container 的 execution location、runtime distribution 与 boundary | `Unknown` |
| Incident / Support | support channel、ticket / evidence route、响应承诺、责任 owner | `Unknown` |
| Procurement / Compliance | 合同、SLA、许可、法务与区域审查 | `Unknown`；必须由具体组织验证 |

该表是未来事实采集 schema，不是 Qwen Code enterprise capability 清单。官方文档中的可见入口只形成待验证问题；只有 deployment-specific record 才能进入 `ENT-*`。

### 假设（Hypothesis）

`H-C07-01`：如果将 Qwen Code 的 Host-owned control surface 与 Provider / Model / endpoint profile 分开记录，那么在相同 Host version、platform、repository baseline、Stable Task、project instruction、permission mode 与 acceptance checks 下，仅切换已授权的模型通道时，Workspace、Host-side tool exposure / filtering policy 与 decision owner、configured permission / approval route、Review 与 artifact route 的可观察责任边界应保持一致；实际 exposed tool set、Provider / Model 的 tool-calling capability、实际 tool request、输出内容和完成路径可以不同。若 Host-owned control points 随模型通道变化，或已完成配对 Run 但仍无法控制 Model / policy confounder，则该边界模型被反驳或结果为 `INCONCLUSIVE`。无论结果如何，没有 deployment-specific Enterprise Fact 都不能把 Contract / Behavior 提升为 enterprise readiness 或 S1–S4。

支持信号：两个 profile 中 Host-side tool exposure / filtering policy 与 decision owner、permission / approval owner、execution location、Review 与 artifact route 一致，而 actual exposed tool set、实际 tool request、tool-call success 或输出差异可以被限定在 Configuration、Provider / Model response、protocol capability 或已记录的 policy / quota。

反驳信号：只改变模型通道就稳定改变 Host-side tool exposure / filtering policy 或其 decision owner、configured permission / approval route、execution location、Review 或 persistence semantics，且重复 Run 排除 configuration drift。Actual exposed tool set 变化、Provider / Model 不支持 tool calling、没有发出 tool request 或 tool call 失败，都不能单独作为反驳信号。

不确定信号：Host version、Model ID、endpoint policy、quota、authentication、workspace state 或 project instruction 无法固定，页面 Contract 与安装版本不匹配，或 observation artifact 不足以判断 owner。

### 计划实验（Planned Experiments）

#### `EXP-C07-01` · Contract → Source → Configuration → Behavior Trace

- 实验类型（Experiment Type）：`EXPLORATORY`
- Outcome Mode：`OBSERVATION_ONLY`；Experiment Result 为 `NOT APPLICABLE · OBSERVATION ONLY`
- 稳定任务（Stable Task）：`T01 · Engineering Constraint`
- 历史映射（Legacy Mapping）：无；Cycle 7 是 V4.2 新增 Cycle
- T01 instance：`T01-C07-LOCAL-RETRY-LIMIT-VALIDATION`。在固定 commit 的隔离 fixture repository 中，为已有本地 configuration parser 补充 `retry_limit` 上界验证；只修改冻结的 parser source 与对应 test file，不改变公开 schema / error type，不访问网络
- Deterministic acceptance checks：覆盖负数、零、允许上界、超过上界与字段缺省；全部使用本地测试并保存命令、exit code 与 diff
- Trace：记录 Host version / surface、platform、installation channel、official source commit、artifact provenance、`QWEN.md` / memory、approval / sandbox、Hook / Skill / Subagent / Extension state、Provider profile、Model ID、redacted configuration snapshot、Host-side tool exposure / filtering policy 与 decision owner、actual exposed tool set、实际 tool request / success、result、Review、artifact 与 human intervention
- Security boundary：不读取或复制 API Key / token，不调用真实业务服务，不测试权限绕过，不访问工作区外路径；配置快照只保留字段名、端点类别和脱敏值
- 主要观察项（Primary Observations）：Contract / Source / Behavior agreement、source path stability、local config observability、Host / Provider / Model owner、tool / approval / sandbox route、extension activation、state persistence、artifact provenance 与 Unknown
- 解释边界（Interpretation Boundary）：单个 profile trace 只能发现责任边界与下一步问题，不单独裁决跨 profile invariant 或 enterprise readiness

#### `EXP-C07-02` · Provider Profile Boundary Comparison

- 实验类型（Experiment Type）：`COMPARATIVE`
- 稳定任务（Stable Task）：`T02 · Semantic Review`
- 历史映射（Legacy Mapping）：无；Cycle 7 是 V4.2 新增 Cycle
- 共同 T02 instance：对同一固定 commit 中一个含明确 acceptance reference 的有限 patch 做语义审查。Evaluator-only oracle 记录一个需要推理的缺陷“重试状态在成功后未清零”，以及一个可由 schema check 确定检出的缺陷“新增配置字段未同步到 schema”；oracle 及缺陷名称不得进入 Agent-visible task statement、Rule、context files、acceptance reference 或 output schema。两个 profile 的 Agent-visible 输入、permission mode 与 Review procedure 完全相同
- Baseline A / Variant B：使用两个已授权 Provider profile；必须核验相同 Model identity / revision 与 capability preflight，只改变 Provider / endpoint route。除模型通道外，Host version / surface、platform、workspace baseline、configuration semantics 与 permission procedure 保持一致
- 单一主要变量（Primary Variable）：Provider profile / endpoint route；如果 Model identity、tool protocol、context / output limit、quota 或 policy 不能保持一致，comparability gate 不通过，本实验保持 `NOT EXECUTED`
- 重复与顺序（Replication and Order）：每个 profile 至少两个 fresh task Run，顺序交错；每次从相同 repository commit、clean workspace 与相同 task statement 开始
- 主要观察项（Primary Observations）：Host-side tool exposure / filtering policy 与 decision owner、actual exposed tool set、configured permission / confirmation route、Provider / Model tool-calling capability、实际 tool request / success、execution location、Review / artifact route、issue detection、reasoning / output difference、retry、human intervention、quota / provider error
- 结果词汇（Result Vocabulary）：`SUPPORT / REJECT / INCONCLUSIVE`
- 解释边界（Interpretation Boundary）：只判断绑定版本与两个 profile 下的责任边界；不做公开 Model benchmark，不声称协议兼容等于 Model portability，不形成企业或合规结论

两个实验都必须保存独立 Run Metadata，绑定 repository commit、Qwen Code version / surface、platform、installation channel、`QwenLM/qwen-code` source commit、execution artifact provenance、Provider / endpoint type、Model ID、redacted configuration、Rule / Skill / Check / Adapter revision、controlled variables、known confounders、evidence 与 human intervention。内容生成阶段不创建 Experiment Record、Run record 或结果。

### 退出条件（Exit Criteria）

Cycle 7 只有在以下条件均满足后才能结束：

- 官方 product identity、Host version、platform、installation / release channel 与访问日期已绑定；
- Contract matrix 覆盖 `QWEN.md` / memory、Session、Tool、Approval、Sandbox、Hook、Skill、Subagent、Extension 与 Provider / Model configuration，并为每项标明 owner 与 Unknown；
- `QwenLM/qwen-code` Source Evidence 固定完整 commit，记录 scope / path / question / stop point，并以可复查材料建立 execution artifact provenance；无法映射时 Cycle 退出条件未满足；
- `EXP-C07-01` 完成无破坏性的 T01 Contract → Source → Configuration → Behavior trace，并保存脱敏 Run Metadata；
- `EXP-C07-02` 完成相同 T02 instance 的配对 fresh-task Run；只有 Run 已真实执行且 Evidence 仍无法分离 Provider / Model / endpoint confounder 时，结果才可为 `INCONCLUSIVE`。无法合规取得两个 Provider profile 时，实验保持 `PLANNED · NOT EXECUTED`、不填写 Result，且 Cycle 退出条件未满足；
- Host effect、Provider effect、Model effect、Configuration effect 与 deployment effect 分开记录；
- 至少为一个真实部署 profile 创建 `ENT-QWENCODE-*`，逐项填入 verified / unknown / unsupported；如果没有可用企业记录，Cycle 保持未完成；
- 所有 Evidence claim 绑定 Evidence ID、scope、limitation 与 verification date；Support Assessment 仍按 capability scope 单独评定；
- Mental Model V1 与 Design Judgment 明确哪些语义可移植、哪些属于 Host Adapter / Provider Profile、哪些仍是 Unknown；
- 不实现 Qwen Code Adapter，不形成普遍 enterprise readiness、安全保证或法律合规结论。

---

## Batch 4 路线复盘触发条件（Route Review Trigger）

完成 Cycle 7 的真实研究后执行一次 Route Review。它可以调整 Batch 5 的 OpenCode source anchor、Provider / Model 分离方法、实验节奏或借用方法，但不能改变冻结的 Cycle 名称、编号、顺序或 Batch 边界。

内容生成本身不满足 Cycle 7 Exit Criteria，也不创建 Route Review 结果。若 Direct Behavior 推翻 Qwen Code Host / Provider 分层，官方 repository identity / license 被撤销，或 release artifact 无法映射到 source revision，应提前触发 Route Review 并保留 Unknown。

## Batch 4 迁移记录（Migration Record）

| V4.1 历史计划 | V4.3 研究设计 | 状态（Status） |
|---|---|---|
| 无 | Cycle 7 · `EXP-C07-01` / `EXP-C07-02` | V4.2 新增编号、V4.3 替换为 Qwen Code；计划态 Contract / Source / Behavior trace 与 Provider profile 对照，尚未执行 |

Cycle 7 没有旧 Week 正文或 `EXP-Wxx-yy` 可重编号。本记录只说明新增研究边界，不声称实验、Enterprise Fact、Support Assessment 或迁移 Evidence 已产生。

---

## Batch 5 边界（Boundary）

Batch 5 只生成 Cycle 8 · OpenCode Host Architecture & Model Portability。

Cycle 8 是 V4.2 新增研究单元，没有 V4.1 Week 或 `EXP-Wxx-yy` 历史迁移对象。本 Batch 只建立计划态 Contract / Source / Behavior 研究边界、官方来源登记与 `EXP-C08-yy` 实验设计。它不运行 OpenCode，不产生 `EVD-*`、Support Assessment、已固定 Source Evidence 或 Model portability conclusion，不实现 OpenCode Adapter / Plugin，也不迁移 Cycle 9–18。

## OpenCode Host 工作模型（Working Model）

```text
Official Contract + Bound OpenCode Version / Surface
        ↓
Pinned Official Source Revision + Capability Map
        ↓
Host Runtime：Config · Session · Agent · Tool · Permission · Extension
        ↓
Provider Adapter + Endpoint / Protocol + Authentication + Routing
        ↓
Model ID / Revision + Capability + Model Options
        ↓
Direct Behavior + Project Artifact + Run Metadata
```

该图是 `Mental Model V0`，不是已经验证的 OpenCode architecture 或 Model portability 结论。官方文档说明公开 Contract；固定 revision 的官方源码只能说明该 revision 的实现；Direct Behavior 才能说明绑定 Host、Provider、endpoint、Model 与 Configuration 条件下实际发生了什么。配置文件形状相同、模型可被选中、协议标称兼容或单次工具调用成功，都不能单独证明语义或行为可移植。

---

## Cycle 8 · OpenCode Host Architecture & Model Portability

> OpenCode Host · V4.2 新增 Cycle · 无 V4.1 Week 映射

### 核心研究问题

> **在绑定 OpenCode 版本与官方源码 revision 后，哪些 Agent、Context、Tool、Permission 与 extension 语义由 Host 保持，哪些行为依赖 Provider adapter、endpoint / protocol、Model 与 Configuration，从而使“Model portability”成立、失败或保持 Unknown？**

### 为什么与 myharness 有关

OpenCode 的研究角色是 open-source、multi-provider、vendor-neutral Host reference。myharness 若把“同一个 `provider/model` 字符串可配置”“相同 Tool 名出现在 UI”“相同任务最终完成”当成 portability，就会掩盖 provider transform、tool schema、permission、reasoning、context limit 与 output behavior 的差异。Cycle 8 通过 Contract → pinned Source → Direct Behavior 三层证据，把可依赖的 Host semantic boundary 与 Provider / Model variation 分开，为 Cycle 9 的 Four-host abstraction 提供受限而可复查的输入。

### 研究范围（Scope）

本 Cycle 只研究：

- OpenCode 官方 Intro、Config、Providers、Models、Rules、Agents、Tools / Permissions、Skills、Plugins 与 MCP Contract；
- `anomalyco/opencode` 固定 revision 中与 config resolution、session / agent loop、tool registry / permission、provider / model selection 和 extension loading 直接相关的实现入口；
- CLI / TUI 中绑定版本的无破坏性 Direct Behavior；其他 surface 必须单独验证；
- Host-owned config / instruction / tool / permission / artifact route 与 Provider adapter、endpoint / protocol、Model capability / option 的分层；
- 同一 T02 task 上用独立 Experiment Record 分别隔离 Provider contrast 与 Model contrast；
- Contract、Source、Behavior 与 Project artifact 的一致、不一致和 Unknown。

本 Cycle 不研究：

- 按仓库目录从头通读，或把当前 package、module、function 与默认分支写成稳定 Contract；
- 把 provider 列表、协议兼容、模型推荐、配置可解析或模型可选自动提升为 Model portability；
- 同时改变 Provider 与 Model 后把差异归因给任一单独变量；
- 公开模型 benchmark、统计排名、企业部署结论或未绑定版本的安全保证；
- OpenCode Adapter / Plugin 实现、Cycle 9 Four-host abstraction 或 myharness feature 修改。

### 官方来源路线与权限边界（Authority Boundary）

| 来源组 | 计划深度 | Cycle 8 用途 | 权限 / 停止边界 |
|---|---|---|---|
| OpenCode Intro、Config、Rules、Agents、Tools、Permissions | L2 定向 | 建立 Host surface、config precedence、instruction、agent、tool 与 permission Contract map | 浮动官方页面；执行时绑定 OpenCode version / surface / platform；不能证明本地配置已生效或内部实现 |
| OpenCode Providers、Models | L2 定向 | 建立 Provider、endpoint、authentication、Model ID、option 与 capability 问题清单 | provider / model 可配置不等于行为可移植；页面列表与推荐会变化 |
| OpenCode Skills、Plugins、MCP | L2 定向 | 建立 discovery、load、tool extension 与 distribution boundary | artifact present / plugin loaded / MCP connected 不等于 workflow effective |
| [`anomalyco/opencode`](https://github.com/anomalyco/opencode) | L3 targeted source | 对 Contract / Behavior 暴露的架构问题做 question-driven source reading | 官方仓库已核验，但默认开发分支是浮动锚点；执行时必须固定完整 commit 并重新定位 path |
| local Direct Behavior 与 project fixture | L3 受控观察 | 追踪 Host / Provider / Model boundary 与 portability failure | 必须脱敏、可逆并保存 Run Metadata；单次或不可比 Run 不得外推 |

Batch 5 只登记 `SRC-OPENCODE-001..012` 计划来源，不从来源条目直接派生 `EVD-*`。官方页面与源码默认分支都是浮动锚点；源码只有在执行时固定完整 commit、记录 authority、scope、path、search term 与 stop point 后，才能派生 scoped Source Evidence。

### 问题驱动的研究路线（Question-driven Research Route）

1. 绑定 OpenCode version、surface、platform、installation channel 与官方页面访问日期，建立 Contract-only Architecture V0。
2. 为 Config、Rule / Instruction、Agent、Tool、Permission、Skill、Plugin、MCP、Session、Provider 与 Model 分别记录 owner、discover / load / select / execute timing、scope、observable artifact、failure route 与 Unknown。
3. 固定 `anomalyco/opencode` 完整 commit，并通过官方 release / tag provenance、package / binary build metadata 或其他可复查官方映射证明该 commit 对应实际执行的 OpenCode artifact。若只能固定源码而无法建立安装映射，Source 与 Behavior 保持独立，Source / Behavior agreement 为 `UNKNOWN`，且不满足 Cycle 8 的相关退出条件。
4. 创建脱敏 Host Profile、Provider Profile 与 configuration snapshot；分别记录 endpoint type、authentication category、routing、Model ID / revision、tool-calling capability、context / output limit 与 model options。
5. 执行 `EXP-C08-01`，把 T03 中实际使用的 config、instruction、tool、permission、provider / model selection、session state 与 artifact route 连接到 Contract / Source / Behavior。
6. 分别执行 `EXP-C08-02` 与 `EXP-C08-03`：Provider experiment 只改变 Provider profile，Model experiment 只改变 Model ID / revision。任一实验无法取得满足 comparability gate 的 profile 时，该实验保持 `NOT EXECUTED`，不借另一实验的结果替代。
7. Contract、Source 与 Behavior 不一致时分别登记；Provider transform、endpoint policy、Model capability、quota 或 routing 无法分离时保留 Unknown，不以源码猜测未观察行为。

### Architecture 与 Portability 分层表

| 层（Layer） | 必须绑定 | 可以回答 | 不能自动回答 |
|---|---|---|---|
| Host Contract | OpenCode version、surface、platform、Source ID、access date | 官方公开了什么 config / agent / tool / permission / extension surface | 当前环境是否启用、内部如何实现、跨 surface 是否一致 |
| Official Source | repository、完整 commit、path、question、stop point | 特定 revision 如何实现限定 boundary | 安装版本是否采用、未来 Contract、所有运行分支 |
| Provider Profile | Provider、endpoint type、authentication、routing、protocol / adapter、quota | 请求通过什么通道，哪些变化属于 Provider / endpoint | Model behavior、Host semantic invariance |
| Model Profile | Model ID / revision、capability、context / output limit、options | 本 Run 使用什么 Model 条件 | 跨 Provider identity、普遍质量或 portability |
| Direct Behavior | Run、Host / Provider / Model / Configuration、request、decision、result、artifact | 特定条件下实际观察到什么 | 未执行组合、内部原因、普遍可移植性 |

### 可移植性判断门禁（Portability Comparability Gate）

Provider contrast 必须尽量固定：OpenCode version / surface / platform、repository baseline、task statement、instruction、tool / permission profile、Model ID / revision、model options、context / output limit 与 acceptance / review procedure，只改变 Provider profile / endpoint route。若同一 Model identity 或等价 capability 无法核验，该 contrast 不得启动。

Model contrast 必须固定：OpenCode version / surface / platform、Provider profile、endpoint type、authentication category、repository baseline、task statement、instruction、tool / permission profile 与 review procedure，只改变 Model ID / revision；两个 Model 都必须满足实验所需 tool calling、context 与 output preflight。

`Provider A + Model A` 与 `Provider B + Model B` 的两格比较同时改变两个主要变量，只能产生探索性问题，不能支持或反驳 Provider portability、Model portability 或 Host invariant。配置解析成功、模型出现在 selector、请求被 Provider 接受、工具 schema 被发送、工具调用成功和最终任务完成必须分别记录，不能合并成一个 portability outcome。

### 假设（Hypothesis）

`H-C08-01 · Provider Portability`：在绑定相同 OpenCode version / surface、repository baseline、instruction、tool / permission profile、Model ID / revision、model options 与 T02 instance 的条件下，只切换通过 comparability gate 的 Provider profile / endpoint route，应保持 Host-owned config resolution、instruction source、permission decision owner、Review / artifact route 与 task contract；provider transform、protocol acceptance、tool request / arguments、retry 与 completion path 可以不同。

`H-C08-02 · Model Portability`：在绑定相同 OpenCode version / surface、Provider profile / endpoint / routing、repository baseline、instruction、tool / permission profile 与 T02 instance 的条件下，只切换通过 capability preflight 的 Model ID / revision，应保持相同 Host-owned route 与 task contract；tool use、reasoning、issue detection、evidence quality、false positive、retry 与 completion path 可以不同。

支持信号：对应 Experiment 的单变量 contrast 中，Host-owned instruction、permission、Review 与 artifact route 可复查地保持一致，差异能够限定为 Provider adapter / endpoint 或 Model capability / option，并且两边都完成预先声明的 observation contract。

反驳信号：只改变该 Experiment 声明的一个 profile 变量后，Host-owned config / instruction / permission / artifact semantics 稳定变化，或某个满足 preflight 的 profile 无法表达同一必要 task semantic，且重复 Run 排除 configuration drift。

不确定信号：Model revision、Provider routing、tool protocol、context / output limit、quota、feature flag、workspace state 或 evaluator procedure 未固定，或 trace 不能判断 decision owner。comparability gate 未通过时，对应 Experiment 保持 `NOT EXECUTED`；只有配对 Run 已完成但关键 confounder 仍无法分离时才使用 `INCONCLUSIVE`。

### 计划实验（Planned Experiments）

#### `EXP-C08-01` · Contract → Source → Behavior Architecture Trace

- 实验类型（Experiment Type）：`EXPLORATORY`
- Outcome Mode：`OBSERVATION_ONLY`；Experiment Result 为 `NOT APPLICABLE · OBSERVATION ONLY`
- 稳定任务（Stable Task）：`T03 · Medium Change`
- 历史映射（Legacy Mapping）：无；Cycle 8 是 V4.2 新增 Cycle
- T03 instance：`T03-C08-LOCAL-RETRY-BUDGET`。在固定 commit 的隔离 fixture repository 中，为已有本地 job runner 增加可配置 retry budget，修改 config type / parser、validation、runtime use、tests 与用户文档；不访问网络或真实服务
- Acceptance checks：覆盖字段缺省、合法边界、非法边界、runtime 停止条件与文档示例；保存本地命令、exit code、diff 与 artifact convergence check
- Trace：记录 OpenCode version / surface / platform、官方页面版本、固定 source commit、configuration precedence、instruction source、agent、tool registry、permission decision、Skill / Plugin / MCP state、Provider profile、Model、session / task state、request / result、Review、artifact 与 human intervention
- Provenance gate：在解释 Source / Behavior agreement 前，必须用官方 release / tag provenance、package / binary build metadata 或其他可复查官方材料，把实际执行的 OpenCode artifact 映射到固定 source commit；只有 commit pinned 但映射缺失时，分别保留 Source observation 与 Behavior observation，agreement 为 `UNKNOWN`
- Source boundary：只追本 Run 真实触及的 capability；记录 search term、source path、1–2 层调用、stop point 与 Unknown，不生成完整 Runtime architecture 图
- 主要观察项（Primary Observations）：Contract / Source / Behavior agreement、config owner、tool / permission owner、provider / model boundary、state transition、unloaded extension、source path stability、artifact drift 与 confounder
- 解释边界（Interpretation Boundary）：单次 trace 只建立 scoped architecture question map，不裁决跨 Provider / Model portability

#### `EXP-C08-02` · Provider Portability Comparison

- 实验类型（Experiment Type）：`COMPARATIVE`
- 稳定任务（Stable Task）：`T02 · Semantic Review`
- 历史映射（Legacy Mapping）：无；Cycle 8 是 V4.2 新增 Cycle
- T02 instance：对固定 commit 中一个含 acceptance reference 的有限 patch 作语义审查。Evaluator-only oracle 记录一个需要推理的缺陷“重试预算在成功后仍被后续任务复用”，以及一个可由 schema / test 检出的缺陷“新增配置字段未加入边界验证”；oracle 与缺陷名称不得进入 Agent-visible task statement、Rule、context、acceptance reference 或 output schema
- 强制 Evidence procedure：Agent-visible task 要求先用 read tool 检查预先登记的 implementation、schema 与 test 文件，再运行 fixture 内固定的本地 `./scripts/check-review-fixture`；该 exact command 在共同 permission profile 中设置为 `ask`，每个 Run 由 Human intervention 以相同 `approve once` procedure 处理。命令不访问网络、secret 或工作区外路径
- Baseline A / Variant B：相同 Model ID / revision、model options 与 capability preflight，使用两个已授权 Provider profile；只改变 Provider / endpoint route
- 单一主要变量（Primary Variable）：Provider profile / endpoint route；Host、Model、task、instruction、tool / permission profile 与 evidence procedure 保持相同
- 重复与顺序（Replication and Order）：A / B 各至少两个 fresh task Run，顺序交错；每次从相同 repository commit、clean workspace 与 Agent-visible input 开始
- 主要观察项（Primary Observations）：config resolution、instruction source、Host-side tool / permission route、actual tool set、provider transform / protocol error、tool request / arguments / success、issue detection、evidence quality、false positive、retry、Review / artifact route、human intervention
- 结果词汇（Result Vocabulary）：`SUPPORT / REJECT / INCONCLUSIVE`
- 解释边界（Interpretation Boundary）：Provider comparability gate 未通过时，本 Experiment 保持 `PLANNED · NOT EXECUTED`，不填写 Result；只有 A / B 配对 Run 完成但已登记 Provider confounder 仍无法分离时才填写 `INCONCLUSIVE`

#### `EXP-C08-03` · Model Portability Comparison

- 实验类型（Experiment Type）：`COMPARATIVE`
- 稳定任务（Stable Task）：`T02 · Semantic Review`
- 历史映射（Legacy Mapping）：无；Cycle 8 是 V4.2 新增 Cycle
- T02 instance 与 Evidence procedure：完全复用 `EXP-C08-02` 的 fixed patch、Agent-visible input、evaluator-only oracle、read file set、`./scripts/check-review-fixture` 与相同 `ask` → `approve once` permission procedure
- Baseline A / Variant B：相同 Provider profile、endpoint type、authentication category 与 routing，使用两个通过 tool calling、context / output 与 task compatibility preflight 的 Model ID / revision；只改变 Model
- 单一主要变量（Primary Variable）：Model ID / revision；Host、Provider、task、instruction、tool / permission profile 与 evidence procedure 保持相同
- 重复与顺序（Replication and Order）：A / B 各至少两个 fresh task Run，顺序交错；每次从相同 repository commit、clean workspace 与 Agent-visible input 开始
- 主要观察项（Primary Observations）：config resolution、instruction source、Host-side tool / permission route、actual tool set、tool request / arguments / success、reasoning、issue detection、evidence quality、false positive、retry、Review / artifact route、human intervention
- 结果词汇（Result Vocabulary）：`SUPPORT / REJECT / INCONCLUSIVE`
- 解释边界（Interpretation Boundary）：Model comparability gate 未通过时，本 Experiment 保持 `PLANNED · NOT EXECUTED`，不填写 Result；只有 A / B 配对 Run 完成但已登记 Model confounder 仍无法分离时才填写 `INCONCLUSIVE`

三个实验都必须使用独立 Experiment Record，并为每次执行保存独立 Run Metadata，绑定 repository commit、OpenCode version / surface / platform、`anomalyco/opencode` source commit、Provider / endpoint type、Model ID / revision、脱敏 Configuration、Rule / Skill / Check / Adapter revision、controlled variables、known confounders、evidence 与 human intervention。`EXP-C08-02` 与 `EXP-C08-03` 分别填写 Result 和派生 scoped `EVD-*`；一个 Experiment 的结果不能替代另一个。内容生成阶段不创建 Experiment Record、Run record 或结果。

### 退出条件（Exit Criteria）

Cycle 8 只有在以下条件均满足后才能结束：

- 官方 Contract map 绑定 OpenCode version、surface、platform、access date 与 `SRC-OPENCODE-*`；
- 实际执行的 OpenCode artifact 已通过可复查官方 provenance 映射到 `anomalyco/opencode` 完整 commit，并记录 authority、release / artifact identity、mapping basis、scope、path、search term、stop point 与 limitation；
- Architecture V0 / V1 明确区分 Contract、Source、Behavior、Project artifact 与 inference；
- `EXP-C08-01` 完成可复查 T03 trace，Contract / Source / Behavior checkpoint 与 Run Metadata 完整；
- `EXP-C08-02` 完成通过 Provider comparability gate 的 A / B 配对 Run，并形成独立 Result；
- `EXP-C08-03` 完成通过 Model comparability gate 的 A / B 配对 Run，并形成独立 Result；任一实验未通过 gate 时保持 `NOT EXECUTED`，Cycle 8 退出条件未满足；
- 结果能区分 config / model selection、tool schema exposure、provider acceptance、tool request / success、review artifact 与 task outcome；
- Host effect、Provider adapter / endpoint effect、Model effect 与 Configuration effect 分开记录；
- 所有 `EVD-*` 绑定 claim scope、supporting artifact、limitation 与 verification date；Support Assessment 仍按 capability scope 单独评定；
- Mental Model V1 与 Design Judgment 明确 Stable Host Semantic、Provider / Model-dependent Behavior、unsupported combination 与 Unknown；
- 不实现 OpenCode Adapter / Plugin，不形成公开 Model benchmark、普遍 portability 或 enterprise conclusion。

---

## Batch 5 路线复盘触发条件（Route Review Trigger）

完成 Cycle 8 的真实研究后执行一次 Route Review。它可以调整 Batch 6 的 Four-host abstraction source anchor、capability matrix、degradation vocabulary、实验节奏或借用方法，但不能改变冻结的 Cycle 名称、编号、顺序或 Batch 边界。

内容生成本身不满足 Cycle 8 Exit Criteria，也不创建 Route Review 结果。若固定 Source revision 与官方 Contract 明显冲突，或 Direct Behavior 推翻 Host / Provider / Model 分层，应提前触发 Route Review；浮动默认分支变化只触发重新定位，不自动改变结论。

## Batch 5 迁移记录（Migration Record）

| V4.1 历史计划 | V4.2 研究设计 | 状态（Status） |
|---|---|---|
| 无 | Cycle 8 · `EXP-C08-01` / `EXP-C08-02` / `EXP-C08-03` | V4.2 新增 OpenCode Cycle；计划态 architecture trace、Provider portability 与 Model portability 独立对照，尚未执行 |

Cycle 8 没有旧 Week 正文或 `EXP-Wxx-yy` 可重编号。本记录只说明新增研究边界，不声称实验、Source Evidence、Model portability、Support Assessment 或迁移 Evidence 已产生。
