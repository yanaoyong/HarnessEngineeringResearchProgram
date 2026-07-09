# PART III · Coding Agent Host Model

> Phase 2–3 · Week 3–6：先理解 Host 如何工作，再讨论 Harness 应该如何利用它。

[← 上一卷](01-Agent与Harness基础认知.md) · [返回总览](../README.md) · [下一卷 →](03-Cross-host-Harness-Abstraction.md)

---

## Week 3 · Claude Code Context Lifecycle

> Phase 2 · Claude Code Host Model

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>核心研究问题<br />
一个任务在 Claude Code 中，是怎么“活过”整个 Session 的？</strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### 主线研究对象

| **研究对象**         | **阅读深度** | **本周只关注**                                                         |
|----------------------|--------------|------------------------------------------------------------------------|
| Claude Code 官方资料 | L2 定向      | Context window、sessions、project memory；以官方 Contract 为准         |
| learn-claude-code    | L3 深拆      | s08/s09/s10/s12 的教学机制模型                                         |
| HumanLayer ACE       | L2 定向      | 在观察真实 Context 问题后，用理论解释 compaction 与 context trajectory |

### 重点查看部分

- Claude 官方：Explore the context window、Manage sessions、How Claude remembers your project。

- learn-claude-code 深读：s08_context_compact、s09_memory、s10_system_prompt、s12_task_system；快速读 s11_error_recovery。

- ACE：先实验，再读 Why obsess over context、What Exactly Are We Compacting、Intentional Compaction、Using Sub-Agents、Frequent Intentional Compaction。

### 阅读时只追这些问题

- Context 不只包括对话，还包括哪些内容？

- 什么时候发生 Context Growth？哪些 tool outputs 是高噪声？

- Compaction 后保留什么、丢失什么、下一步 trajectory 是否连续？

- CLAUDE.md、Auto Memory、Task State、Change Artifact、Summary 到底是不是同一种“Memory”？

### 本周不要陷进去

- 先背 ACE 理论再套现象

- 把所有持久化信息统称 Memory

- 立刻修改 L1/L2/L3 架构

### 学习后的实践：myharness 中等任务的 Context Trace Experiment

13. 选一个中等规模且可逆的真实研究任务，例如调查 Codex Plugin 的一个迁移差异。

14. 在 T0 Session 开始、T1 初步定位、T2 大量代码读取后、T3 大量日志后、T4 Compact 前、T5 Compact 后、T6 Resume 后记录状态。

15. 记录 Claude 现在知道什么、哪些文件重复读取、哪些日志污染 Context、Compact / Resume 后什么需要重新发现。

16. 观察问题后再读 ACE，用理论解释，再回到实验验证。

### 建议保留的证据

- 重复读取与重复定位

- 大量工具输出 / 测试日志

- Compact 前后保留与丢失的信息

- Resume 后 trajectory 连续性

### 预期成长

| **Context 模型** | 形成 Claude Context Lifecycle V2。                                                                                |
|------------------|-------------------------------------------------------------------------------------------------------------------|
| **概念分辨**     | 能区分 Conversation History、Session State、CLAUDE.md、Auto Memory、Skill、Task State、Change Artifact、Summary。 |

### 实践完成后，重新理解

- L1 是“重要信息”，还是“每次都值得支付 Context 成本的信息”？

- summary.md 是 Memory，还是 Handoff Artifact？

- Changes 是 Session Persistence 吗？

- 哪些东西应该进入下一 Session？

| **弹性规则：** 如果本周实验直接暴露了一个会推翻当前 Mental Model 的问题，可以暂停原计划并追加一个短研究循环；如果只是有趣的旁支问题，记录到 Open Questions，继续主线。 |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Week 4 · Claude Code Extension & Control Surface

> Phase 2 · Claude Code Host Model

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>核心研究问题<br />
同一个工程要求，应该放 CLAUDE.md、Rules、Skill、Hook、Subagent、MCP，还是 Plugin？</strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### 主线研究对象

| **研究对象**               | **阅读深度** | **本周只关注**                                                        |
|----------------------------|--------------|-----------------------------------------------------------------------|
| Claude Code 官方资料       | L2 定向      | CLAUDE.md / Memory、Skills、Hooks、Subagents、MCP、Plugins 的职责边界 |
| myharness Claude Extension | 项目证据     | 映射现有 Rules、Skills、Hooks、Plugin 分发                            |

### 重点查看部分

- 官方：How Claude remembers your project、Extend Claude with skills、Hooks reference、Create custom subagents、MCP、Plugins。

- Hooks 只定向研究：UserPromptSubmit、PreToolUse、PostToolUse、Stop、SessionEnd。

- 映射现有：user_prompt_state_inject、pre_bash_guard、post_lint_check、static_security_scan、stop_progress_check。

### 阅读时只追这些问题

- 什么时候加载？模型是否看到？谁决定触发？

- 能否确定性阻断？是否增加 Context？是否跨项目分发？

- Rule 是解释正确性，Skill 是教流程，Hook 是执行确定性逻辑——这个模型是否被实验支持？

- Plugin 分发的到底是 Capability，还是 Harness Artifact？

### 本周不要陷进去

- 通读所有 Hook 事件

- 把 Plugin 当运行时抽象的唯一答案

- 因为已有实现就默认当前职责分配正确

### 学习后的实践：“HTTP 调用必须 timeout 并考虑降级”的三种治理方式对照

17. A：Instruction / Rule Only。

18. B：Skill Only，提供 HTTP Client Implementation 流程和检查。

19. C：Rule 解释原因 + Deterministic Check 发现明显违规。

20. 使用 3–5 个近似任务：新增 HTTP client、修改已有 request、增加 fallback；记录首次遵循、遗漏、Agent 自发现、Hook 发现、误报、修复轮数和 Context Cost。

### 建议保留的证据

- 首次遵循率与遗漏

- Agent 自发现 vs Hook 发现

- False Positive

- 修复轮数、Context Cost、维护复杂度

### 预期成长

| **职责矩阵** | 形成 Claude Extension Responsibility Matrix V1。                                           |
|--------------|--------------------------------------------------------------------------------------------|
| **工程判断** | 开始能解释为什么某些要求应 instruction、某些应 Skill、某些必须 deterministic enforcement。 |

### 实践完成后，重新理解

- 是否有 Hook 在承担 Skill 的责任？

- 是否有 Rule 实际上是多步骤 SOP？

- 是否有 Skill 只是长篇 Rules？

- Plugin 分发的到底是什么？

| **弹性规则：** 如果本周实验直接暴露了一个会推翻当前 Mental Model 的问题，可以暂停原计划并追加一个短研究循环；如果只是有趣的旁支问题，记录到 Open Questions，继续主线。 |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Week 5 · Codex Architecture & Customization Model

> Phase 3 · Codex Host Model

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>核心研究问题<br />
Codex 如何组织 Agent 能力、项目指导和扩展机制？</strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

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

21. 先画 Codex Architecture V0，标所有问号。

22. 建立 Repository Map，针对问号定位对应 crate。

23. AGENTS.md 层级实验：观察 scope 与覆盖。

24. Skill Discovery 实验：description 明确 vs 模糊，观察发现与触发。

25. Plugin 实验：使用当前 Codex Plugin 移植中的一个真实 Capability，比较原认知、官方 Contract、源码 Boundary 与真实加载行为。

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

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>核心研究问题<br />
什么安全责任属于 Host，什么工程治理责任属于 Harness？</strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

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

26. 使用无破坏性模拟场景：访问测试文件、向临时目录写入、git status、普通网络请求、项目规则禁止但本身无害的测试命令。

27. 记录谁阻止：Host、Approval、Sandbox、Harness Hook，还是 Rule 只提醒。

28. 检查 Double Block、无意义 Approval、误报和 Agent 对原因的理解。

29. 拿 myharness pre_bash_guard 重新分类。

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
