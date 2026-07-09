# PART V · Harness Engineering Research Themes

> Phase 5 · Week 8–12：按问题研究 Skill、Change、Workflow、Context、Knowledge 与 Minimalism。

[← 上一卷](03-Cross-host-Harness-Abstraction.md) · [返回总览](../README.md) · [下一卷 →](05-myharness-Integration-Research.md)

---

## Week 8 · Skill Behavior & Evaluation

> Phase 5 · Harness Engineering Research

### 核心研究问题

> **什么样的 Skill 真正改变 Agent 行为，而不只是写得很好？**

### 主线研究对象

| **研究对象**      | **阅读深度** | **本周只关注**                                                        |
|-------------------|--------------|-----------------------------------------------------------------------|
| Agent Skills      | L2 定向      | Discovery、Activation、Execution；name / description 在发现阶段的作用 |
| Superpowers       | L3 深拆      | Skill 触发、流程、Evidence、Verification、Skill behavior eval         |
| learn-claude-code | L3 对照      | Skill loading 的教学机制模型                                          |

### 重点查看部分

- Superpowers：README 的 How It Works、Basic Workflow、Philosophy、Contributing。

- 深读 skills/using-superpowers/SKILL.md、skills/writing-skills/SKILL.md、skills/verification-before-completion/SKILL.md、skills/systematic-debugging/SKILL.md；可选 TDD Skill。

- 观察结构而非只看内容：名称、description、trigger、反例、procedure、evidence、completion、failure、next skill。

### 阅读时只追这些问题

- Skill Discovery Quality、Execution Quality、Outcome Quality 是否是三个不同问题？

- Description 决定什么？Trigger 与正文 Procedure 如何配合？

- Evidence 写在 Skill 里，还是由 Hook/Test 验证？

- 一个 Skill 能否证明自己被正确执行？

### 本周不要陷进去

- 一次升级全部 myharness Skills

- 只比较文档长度和写作风格

- 把“Skill 被加载”当成“Skill 有效”

### 学习后的实践：myharness 单 Skill 三版本行为实验

> **Experiment ID:** `EXP-W08-01`  
> **Experiment Type:** `COMPARATIVE`  
> **Evidence Scope:** 个人研究中的方向性证据；小样本用于发现现象、比较机制或形成下一步假设，不包装为统计学结论。

1. 从 code-review 或 expert-reviewer 中只选一个。

2. V1：当前版本。

3. V2：只强化 name / description / 适用场景，测试 Discovery / Trigger。

4. V3：Behavior Contract 实验，增加 Trigger、Preconditions、Required Context、Procedure、Evidence Required、Completion Criteria、Failure Route。

5. 3–5 个相近任务，尽量同模型、同 Host、相似复杂度。

### 建议保留的证据

- 主动调用率、漏调用、误调用

- 步骤遵循

- Evidence Quality

- False Completion

- Context Cost

### 预期成长

| **行为评测** | 能区分 Skill Discovery、Execution、Outcome 三类失败。                |
|--------------|----------------------------------------------------------------------|
| **契约意识** | 形成 Skill Contract V2 Hypothesis，而不是因 Superpowers 好用就照抄。 |

### 实践完成后，重新理解

- myharness Skill 是 SOP，还是 Behavior Contract？

- Evidence 应该写在 Skill 里，还是外部验证？

- Semantic Review Skill 与 Deterministic CI Skill 是否需要同一 Schema？

| **弹性规则：** 如果本周实验直接暴露了一个会推翻当前 Mental Model 的问题，可以暂停原计划并追加一个短研究循环；如果只是有趣的旁支问题，记录到 Open Questions，继续主线。 |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Week 9 · Change Contract & Convergence

> Phase 5 · Harness Engineering Research

### 核心研究问题

> **Change Artifact 怎么避免与真实代码状态漂移？**
>
> **Change 怎么避免“撒谎”？**

### 主线研究对象

| **研究对象**      | **阅读深度** | **本周只关注**                                                                    |
|-------------------|--------------|-----------------------------------------------------------------------------------|
| GitHub Spec Kit   | L2 定向      | constitution → specify → plan → tasks → implement；converge / analyze / checklist |
| OpenSpec          | L1 对照      | Change artifact 演进与非 rigid phase gates                                        |
| myharness Changes | 项目证据     | 历史 Change 状态与 artifact drift                                                 |

### 重点查看部分

- Spec Kit：README 主流程；重点定位 speckit.converge、speckit.analyze、speckit.checklist；定向查看 templates/、workflows/、.specify/memory/。

- 仓库搜索 converge / analyze / checklist，只跟相关 template / workflow；除非问题变成 CLI Integration，不通读 src/specify_cli。

- OpenSpec：README 的 See it in action、Why OpenSpec、Usage Notes；schemas/spec-driven/ 与 openspec/。

### 阅读时只追这些问题

- Spec、Task、Code、Test、CI、Summary 如何建立一致性？

- 哪些判断可以 deterministic，哪些需要语义判断？

- Change 在执行中、关闭后、审计时是否扮演不同角色？

- CodeGraph 对 Convergence 是否真的增加价值？

### 本周不要陷进去

- 直接开发 harness converge

- 默认更多 Artifact 等于更真实

- 把目录存在当成流程完成

### 学习后的实践：历史 Change 的三轮 Convergence Experiment

> **Experiment ID:** `EXP-W09-01`  
> **Experiment Type:** `COMPARATIVE`  
> **Evidence Scope:** 个人研究中的方向性证据；小样本用于发现现象、比较机制或形成下一步假设，不包装为统计学结论。

1. 选择一个曾经状态不一致或怀疑存在 artifact drift 的历史 Change。

2. 建立 Spec Requirement ↔ Task ↔ Git Diff / File / Symbol ↔ Test ↔ CI ↔ Summary Status 的人工表。

3. Round A：人工检查。

4. Round B：让 Claude / Codex 直接检查，不给额外结构。

5. Round C：给明确 Convergence Checklist；可选加入 CodeGraph。

6. 比较发现漂移数、漏报、误报、语义判断、确定性判断和 CodeGraph 增益。

### 建议保留的证据

- 发现的漂移类型与数量

- 漏报 / 误报

- Agent 无结构 vs Checklist

- CodeGraph 增益 / 噪声

- Artifact 与真实结果不一致之处

### 预期成长

| **Change Truth Model** | 能区分 Artifact 存在、完整、一致、与 Code 一致、与结果一致。                        |
|------------------------|-------------------------------------------------------------------------------------|
| **角色重构**           | 重新理解 Changes 在执行中可能是 Active Contract，关闭后可能是 Historical Evidence。 |

### 实践完成后，重新理解

- .harness/changes/ 是日志吗？

- Convergence 是 Skill、Hook、CLI 还是 Acceptance？

- 哪些一致性检查必须 deterministic？

- harness converge 值得进入 Candidate 吗？

| **弹性规则：** 如果本周实验直接暴露了一个会推翻当前 Mental Model 的问题，可以暂停原计划并追加一个短研究循环；如果只是有趣的旁支问题，记录到 Open Questions，继续主线。 |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Week 10 · Adaptive Workflow

> Phase 5 · Harness Engineering Research

### 核心研究问题

> **README 修改、普通 Bug 和架构变更，真的应该走同一套十阶段吗？**

### 主线研究对象

| **研究对象**       | **阅读深度** | **本周只关注**                                                                           |
|--------------------|--------------|------------------------------------------------------------------------------------------|
| BMAD Method        | L2 定向      | Scale-Domain-Adaptive、planning depth、quick flow / project complexity / workflow status |
| OpenSpec           | L1 对照      | small fix vs larger change；无 rigid phase gates                                         |
| myharness 10 Stage | 项目证据     | 真实任务的 ceremony、gate 与风险控制                                                     |

### 重点查看部分

- BMAD：先看当前 README 与官方 Docs 中 `Scale-Domain-Adaptive`、planning depth、quick / dev flow、workflow guidance 等能力说明。

- 源码定位采用 Capability-first：执行 Week 10 时，在当前默认分支搜索 `quick-dev`、`planning depth`、`workflow status`、`workflow help` 等当前术语，再跟 1–2 层实现；不要把 `src/bmm-skills/` 视为永久路径 Contract。

- 不研究 Party Mode 和所有 Persona / Agent Role。

- OpenSpec：small fix、larger change、proposal、no rigid phase gates。

### 阅读时只追这些问题

- Gate 的价值是流程完整，还是风险控制？

- Task Complexity 与 Delivery Risk 是否是一回事？

- Adaptive Workflow 是否等于 Agent 自己随便跳阶段？

- Flow Classification、Mandatory Gate、Escalation 由谁决定？

### 本周不要陷进去

- 看到 BMAD 就直接引入 Light / Standard / Full

- 按 Artifact 数量衡量流程质量

- 把所有任务复杂度判断交给模型

### 学习后的实践：三类真实任务的 Workflow Risk Experiment

> **Experiment ID:** `EXP-W10-01`  
> **Experiment Type:** `COMPARATIVE`  
> **Evidence Scope:** 个人研究中的方向性证据；小样本用于发现现象、比较机制或形成下一步假设，不包装为统计学结论。

1. 选择 README / 文档措辞修改、普通 Hook Bug、Plugin / Architecture Change 三类历史或安全任务。

2. 回顾完整 10 Stage：哪些 Artifact 真有价值，哪些步骤近乎形式，哪一个 Gate 真正发现问题？

3. 提出临时实验模型（例如 Light / Standard / Full），但不写入 myharness。

4. 模拟或在安全任务上实践，记录流程时间、Artifact 数量、Context、Human Checkpoints、漏掉风险、返工、False Completion。

### 建议保留的证据

- 流程时间与 Context 成本

- 真正发现问题的 Gate

- 无效 Artifact / ceremony

- 返工与 escaped risk

- Human Checkpoint 价值

### 预期成长

| **风险模型** | 形成 Workflow Risk Model V1：Requirement Ambiguity、Architecture Risk、Code Risk、Regression Risk、Deployment Risk。 |
|--------------|----------------------------------------------------------------------------------------------------------------------|
| **流程判断** | 开始用“控制什么风险”评价 Gate，而不是用“流程是否完整”。                                                              |

### 实践完成后，重新理解

- Adaptive Workflow 是否等于自由跳阶段？

- 哪些 Gate 绝不能跳？

- 什么条件触发 Escalation？

- Flow Classification 应由规则、Agent 还是人工决定？

| **弹性规则：** 如果本周实验直接暴露了一个会推翻当前 Mental Model 的问题，可以暂停原计划并追加一个短研究循环；如果只是有趣的旁支问题，记录到 Open Questions，继续主线。 |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Week 11 · Context Lifecycle & Session Handoff

> Phase 5 · Harness Engineering Research

### 核心研究问题

> **一个长任务如何跨多个 Session 保持认知连续，同时避免携带所有历史噪声？**

### 主线研究对象

| **研究对象**                | **阅读深度** | **本周只关注**                                                                                        |
|-----------------------------|--------------|-------------------------------------------------------------------------------------------------------|
| HumanLayer ACE              | L2 定向      | Context trajectory、intentional compaction、Research → Plan → Implement、Subagents as context control |
| Ralph                       | L1 对照      | Fresh context + git / progress / PRD artifact persistence                                             |
| Claude / Codex Context      | Host 对照    | Week 3–6 已建立的 Host Mechanism                                                                      |
| myharness summary / changes | 项目证据     | 当前 Session handoff 与持久化制品                                                                     |

### 重点查看部分

- ACE：完整研究 ace-fca.md；重点 Why obsess over context、What Exactly Are We Compacting、Using Sub-Agents、Frequent Intentional Compaction、Research、Plan、Implement。

- Ralph：README 的 Workflow、Critical Concepts；ralph.sh、prompt.md、CLAUDE.md、prd.json.example。

- 本周关注 Harness Strategy，不重复研究 Claude 如何 compact。

### 阅读时只追这些问题

- Raw History、Resume、Compaction、Summary、Handoff Artifact、Persistent Knowledge 有什么差异？

- 保存更多历史是否一定恢复更好？

- Summary 应记录“发生了什么”，还是“下一 Agent 最少需要知道什么”？

- Change Artifact 与 Session Handoff 应否完全相同？

### 本周不要陷进去

- 把 Week 3 重新学一遍

- 用长篇 prose summary 代替实验

- 默认所有决策都应永久进入 Wiki

### 学习后的实践：跨 Session 真实任务的 Handoff Modes Experiment

> **Experiment ID:** `EXP-W11-01`  
> **Experiment Type:** `EXPLORATORY`  
> **Evidence Scope:** 个人研究中的方向性证据；小样本用于发现现象、比较机制或形成下一步假设，不包装为统计学结论。

1. 设计一个不能单 Session 完成的真实独立子问题，例如 Codex Plugin 移植中的一项。

2. 分为 Session A Research、B Plan、C Implementation、D Review。

3. 比较 Mode 1 Resume、Mode 2 普通 prose summary、Mode 3 结构化 Handoff（Goal / Current State / Decisions / Evidence / Files & Symbols / Completed / Next Step / Open Risks / Rejected Approaches）、Mode 4 现有 Changes Artifact。

4. 可在一个连续任务中分段采用不同方式，不要求重复四个完整项目。

> **Interpretation Rule:** 本周证据属于 exploratory qualitative evidence。若在同一连续任务中分段使用不同 Handoff Mode，只能用于发现问题与形成假设，不能直接宣称某个 Mode 性能优于其他 Mode。

### 建议保留的证据

- 重复读取与重新定位

- 错误假设、决策遗失

- 过期信息

- 恢复工作所需 Context / 时间

- trajectory 是否连续

### 预期成长

| **Handoff 模型** | 形成 Session Handoff Mental Model。                         |
|------------------|-------------------------------------------------------------|
| **上下文策略**   | 能区分 Host Context Mechanism 与 Harness Handoff Strategy。 |

### 实践完成后，重新理解

- 保存更多历史真的恢复更好吗？

- summary.md 是历史摘要，还是 next-agent briefing？

- Change 与 Handoff 是否应共用结构？

- 哪些信息只服务 trajectory，不应该进入 Wiki？

| **弹性规则：** 如果本周实验直接暴露了一个会推翻当前 Mental Model 的问题，可以暂停原计划并追加一个短研究循环；如果只是有趣的旁支问题，记录到 Open Questions，继续主线。 |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Week 12 · Knowledge Ratification & Harness Minimalism

> Phase 5 · Harness Engineering Research

### 核心研究问题

> **Agent 发现的一个事实，什么时候值得永久进入 Harness？**

### 主线研究对象

| **研究对象**                    | **阅读深度** | **本周只关注**                                                    |
|---------------------------------|--------------|-------------------------------------------------------------------|
| Agent OS                        | L2 定向      | Discover Standards、Deploy Standards、Shape Spec、Index Standards |
| mini-swe-agent                  | L3 回看      | 用极简 scaffold 反问“为什么不增加更多 Harness”                    |
| SWE-agent ACI                   | L1 理论对照  | Interface Design 与 Scaffold Expansion 的差异                     |
| myharness failure / improvement | 项目证据     | 历史失败与能力沉淀是否有重复价值证据                              |

### 重点查看部分

- Agent OS：先以当前 README / 官方 Docs 的四个 Capability 为导航：Discover Standards、Deploy Standards、Shape Spec、Index Standards。

- 源码定位采用 Capability-first：执行 Week 12 时刷新当前默认分支和 docs，再搜索 discover / deploy / index / shape spec 对应实现；目录只作为当时的导航锚点，不预设 `commands/agent-os/`、`profiles/default/global/` 永久存在。

- 不研究安装脚本。

- 回看 mini-swe-agent 的 Agent、Environment、Model、run 轻量结构。

- 可选 SWE-agent ACI，用于思考有效 Interface Design 与无意义 Scaffold Expansion。

### 阅读时只追这些问题

- Agent 学到一个东西，为什么不能直接写入 Memory / Rule？

- One-off 与 Recurring 如何判断？

- Host Issue、Model Behavior、Project Knowledge、Process Problem、Deterministic Constraint 如何分类？

- 一个 Capability 的收益是否值得 Context、Maintenance、Portability 和 Behavior Complexity 成本？

### 本周不要陷进去

- 每个 Failure 都新增 Rule / Hook

- 把一次严重错误自动当成长期重复价值

- 只做“新增什么”，不允许“Nothing”

### 学习后的实践：10 个历史 Failure / Improvement 的 Ratification Exercise

> **Experiment ID:** `EXP-W12-01`  
> **Experiment Type:** `EXPLORATORY`  
> **Evidence Scope:** 个人研究中的方向性证据；小样本用于发现现象、比较机制或形成下一步假设，不包装为统计学结论。

1. 从 myharness 抽取 10 个 Failure Record、Improvement、真实 Bug、Review 问题或 Agent 误行为。

2. 第一层：One-off / Recurring。

3. 第二层：Host Issue / Model Behavior / Project Knowledge / Process Problem / Deterministic Engineering Constraint。

4. 第三层决定：Rule / Skill / Hook / Wiki / Test / Change Template / Nothing。

5. 对 3 个准备新增能力的案例估算 Recurring Value、Context Cost、Maintenance Cost、Cross-host Portability、Behavior Complexity。

### 建议保留的证据

- 分类依据

- 重复出现证据

- 新增能力预计成本

- Nothing 的理由

- 历史能力是否真的解决过同类问题

### 预期成长

| **Knowledge Ratification** | 形成 Discovery → Evidence → Recurring? → Candidate → Classification → Ratification → Artifact / Discard 模型。 |
|----------------------------|----------------------------------------------------------------------------------------------------------------|
| **最小主义**               | 训练“Nothing”判断，开始接受删除 / 不新增也可能是最佳 Harness 设计。                                            |

### 实践完成后，重新理解

- 三次重复错误和一次严重错误，哪个更值得进入 Harness？

- Rule 越完整，Agent 就越可靠吗？

- No capability without evidence of recurring value 是否成立？

- 哪些例外足以推翻这条假设？

| **弹性规则：** 如果本周实验直接暴露了一个会推翻当前 Mental Model 的问题，可以暂停原计划并追加一个短研究循环；如果只是有趣的旁支问题，记录到 Open Questions，继续主线。 |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|


---

## 路线调整说明

本卷是研究导航，不是冻结的教学脚本。执行到对应研究循环前，应先刷新相关官方文档、默认分支与 Changelog；若项目目录或能力名称发生变化，继续追踪本卷定义的研究问题与 Capability，而不是机械寻找旧路径。
