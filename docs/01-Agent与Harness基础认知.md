# PART II · Agent 与 Harness 基础认知

> Phase 1 · Week 1–2：建立 Agent Core 与 Harness Primitive 的共同语言。

[← 上一卷](00-研究计划总纲.md) · [返回总览](../README.md) · [下一卷 →](02-Coding-Agent-Host-Model.md)

---

## Week 1 · Coding Agent 最小模型

> Phase 1 · Agent / Harness Foundation

### 核心研究问题

> **一个 Coding Agent 最少需要什么？**
>
> **Agent Core 与 Harness 的边界在哪里？**

### 主线研究对象

| **研究对象**                     | **阅读深度** | **本周只关注**                                        |
|----------------------------------|--------------|-------------------------------------------------------|
| SWE-agent/minimal-agent-tutorial | L3 深拆      | 约 60 行最小终端 Agent；先画数据流，再看实现          |
| SWE-agent/mini-swe-agent         | L3 深拆      | Agent、Environment、Model、Run 的最小拆分与 HITL 扩展 |

### 重点查看部分

- minimal-agent-tutorial：docs/index.md 与完整最小 Agent 实现。

- mini-swe-agent：src/minisweagent/agents/、environments/、models/、run/；优先 agents/default.py、environments/local.py；有余力再看 agents/interactive.py。

### 阅读时只追这些问题

- History 为什么存在？Observation 为什么重新进入 Messages？

- Agent 如何决定停止？异常发生后 Loop 如何继续？

- Environment 和 Tool 是一回事吗？Human-in-the-loop 加在哪里？

- Agent Loop 中真正不可删除的部分是什么？

### 本周不要陷进去

- Benchmark 与 SWE-bench 基础设施

- Deployment 与 Provider 细节

- 大型 Evaluation 系统

### 学习后的实践：最小 Agent：Instruction 与 Interception 对照实验

> **Experiment ID:** `EXP-W01-01`  
> **Experiment Type:** `COMPARATIVE`  
> **Evidence Scope:** 个人研究中的方向性证据；小样本用于发现现象、比较机制或形成下一步假设，不包装为统计学结论。

1. 先运行最小 Agent，理解完整 loop。

2. Experiment A：增加“修改代码前必须先读取目标文件”Instruction，执行 3 个简单任务。

3. Experiment B：把同一要求改成简单的 action interception；只做实验，不实现生产级 Hook。

4. 比较 Instruction 与 Interception 的遵循率、行为变化、阻塞方式、上下文成本和实现复杂度。

### 建议保留的证据

- 任务数量、Loop 次数、Action 数量

- 错误 Action、规则漏执行

- 人工干预、完成声明

### 预期成长

| **机制理解** | 能不用资料解释 Model、Agent Loop、Message History、Action、Environment、Observation、Stop 的关系。 |
|--------------|----------------------------------------------------------------------------------------------------|
| **边界意识** | 第一次明确区分“Agent 能工作”与“Agent 工作得稳定”；后者开始进入 Harness 问题。                      |

### 实践完成后，重新理解

- Tool 到底属于 Agent，还是 Harness？

- Permission 属于 Agent Core 吗？

- Instruction 是 Agent 的一部分，还是 Harness？

- “阻止错误行为”和“告诉 Agent 不要犯错”有什么本质区别？

| **弹性规则：** 如果本周实验直接暴露了一个会推翻当前 Mental Model 的问题，可以暂停原计划并追加一个短研究循环；如果只是有趣的旁支问题，记录到 Open Questions，继续主线。 |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Week 2 · Harness Primitive

> Phase 1 · Agent / Harness Foundation

### 核心研究问题

> **Agent Loop 已经能工作，为什么还需要 Hook、Skill、Task、Permission 和 Subagent？**

### 主线研究对象

| **研究对象**                  | **阅读深度** | **本周只关注**                                                                 |
|-------------------------------|--------------|--------------------------------------------------------------------------------|
| shareAI-lab/learn-claude-code | L3 深拆      | 用教学重实现建立 Harness Primitive 机制模型；不把它当 Claude Code 官方内部源码 |

### 重点查看部分

- 深读：s01_agent_loop、s03_permission、s04_hooks、s06_subagent、s07_skill_loading。

- 快速阅读：s02_tool_use、s05_todo_write、s08_context_compact；s08 只建立概念，Week 3 再深入。

- 每章顺序：README → 写机制猜想 → code.py → 运行 → 修改一个参数或行为。

### 阅读时只追这些问题

- Permission：是告诉 Agent 什么不能做，还是 Host 在 Action 前做决策？

- Hook：为什么不是 Skill？是否需要模型参与？Deterministic Behavior 有什么价值？

- Task / Todo：只是 UI，还是 Externalized State？

- Subagent：核心是角色差异，还是 Context 隔离？

- Skill：是 Prompt 文件，还是 On-demand Procedural Knowledge？

### 本周不要陷进去

- 提前研究复杂 Skill Evaluation

- 提前深入 Context 生命周期

- 横向打开更多 Agent 框架

### 学习后的实践：为最小 Agent 分别增加 Instruction、Externalized Task 与 Subagent Context Boundary

> **Experiment ID:** `EXP-W02-01`  
> **Experiment Type:** `EXPLORATORY`  
> **Evidence Scope:** 个人研究中的方向性证据；小样本用于发现现象、比较机制或形成下一步假设，不包装为统计学结论。

1. 实验 1：延续 Week 1 的 Instruction vs Interception。

2. 实验 2：同一 4–5 步任务，比较直接执行与显式维护 Task 状态；记录漏步骤、重复操作、顺序漂移和完成声明。

3. 实验 3：多文件扫描问题，比较主 Agent 自己读取全部文件与独立研究 Agent 只返回结构化结论。

### 建议保留的证据

- 漏步骤、重复操作、顺序漂移

- 主 Context 中保留的信息量

- Skill / Task / Subagent 是否真正改变行为

### 预期成长

| **词汇模型** | 形成 Harness Primitive Mental Model V1。                                                   |
|--------------|--------------------------------------------------------------------------------------------|
| **职责意识** | 能初步解释 Instruction、Tool、Permission、Hook、Task、Skill、Subagent 各自解决的工程问题。 |

### 实践完成后，重新理解

- Skill 和 Hook 是否解决完全不同的问题？

- Task 是否也是 Context Engineering？

- Subagent 的核心价值到底是“角色”还是“Context Control”？

| **弹性规则：** 如果本周实验直接暴露了一个会推翻当前 Mental Model 的问题，可以暂停原计划并追加一个短研究循环；如果只是有趣的旁支问题，记录到 Open Questions，继续主线。 |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|


---

## 路线调整说明

本卷是研究导航，不是冻结的教学脚本。执行到对应研究循环前，应先刷新相关官方文档、默认分支与 Changelog；若项目目录或能力名称发生变化，继续追踪本卷定义的研究问题与 Capability，而不是机械寻找旧路径。
