# PART IV · Cross-host Harness Abstraction

> Phase 4 · Week 7：通过真实迁移建立 Portable Core、Host Adapter 与 Host-specific Capability 三分法。

[← 上一卷](02-Coding-Agent-Host-Model.md) · [返回总览](../README.md) · [下一卷 →](04-Harness-Engineering-Research-Themes.md)

---

## Week 7 · Cross-host Harness Abstraction

> Phase 4 · Cross-host Harness Abstraction

### 核心研究问题

> **Claude Code 和 Codex 中，哪些能力本质相同，哪些只是名字相似？**

### 主线研究对象

| **研究对象**                         | **阅读深度** | **本周只关注**                                                                 |
|--------------------------------------|--------------|--------------------------------------------------------------------------------|
| Superpowers Porting Guide            | L3 定向深拆  | 跨 Harness invariants、tool mapping、bootstrap、supportability、definition of done |
| Agent Skills                         | L2 定向      | SKILL.md Contract 与 Discovery → Activation → Execution progressive disclosure |
| OpenHarness                          | L1 对照      | 共享 primitive pack 与 provider surface                                        |
| myharness Claude → Codex Plugin 移植 | 项目证据     | 真实迁移差异作为实验数据                                                       |

### 重点查看部分

- Superpowers：优先深读 `docs/porting-to-a-new-harness.md` 的 Part 1–3，重点追踪 harness-agnostic skills、per-harness tool mapping、per-harness bootstrap、automatic session-start injection 与 definition of done。

- Superpowers 的 `.claude-plugin`、`.codex-plugin`、`.cursor-plugin`、`.opencode`、`.pi/extensions` 只作为 live reference implementation，用于验证 guide 中的 invariants；不要把目录形状本身当成抽象。

- Agent Skills：SKILL.md、name、description、instructions、scripts、references、assets。

- OpenHarness：README 与 `.oh/docs/oh-directory-layout.md`；观察 primitive pack、`.oh/skills` / `.oh/agents` / `.oh/hooks` / `.oh/skills.lock` 与 provider surfaces。

### 阅读时只追这些问题

- 一个 Harness port 成立所需的 invariants 是什么？

- Portable 的应该是文件、action vocabulary，还是行为语义？

- Skill discovery 与 bootstrap delivery 是否是两个独立问题？

- 名字类似是否意味着语义等价？Trigger Semantics 不同，会不会让“同一个 Skill”产生不同 Harness 行为？

- Portable Core、Tool Mapping / Host Adapter、Host-specific Capability 应如何划分？

### 本周不要陷进去

- 直接写“CLAUDE.md = AGENTS.md”

- 把共享 SKILL.md 等同于跨宿主一致行为

- 顺便重构整个 Plugin Distribution

### 学习后的实践：Naive Port vs Portable Contract

> **Experiment ID:** `EXP-W07-01`  
> **Experiment Type:** `COMPARATIVE`  
> **Evidence Scope:** 个人研究中的方向性证据；小样本用于发现现象、比较机制或形成下一步假设，不包装为统计学结论。

1. 从 myharness 选择 code-review Skill 或 research-discovery。

2. Approach A：Claude Artifact 改格式直接搬到 Codex，记录修改量、重复和无法对应概念。

3. Approach B：先抽象 Intent、Trigger、Required Context、Procedure、Evidence、Completion，再分别写 Claude Adapter 与 Codex Adapter。

4. 比较两种迁移方式；将当前 Codex Plugin 移植作为真实数据。

### 建议保留的证据

- 迁移修改量与重复

- 无法映射能力

- Host-specific 语义差异

- 两种 approach 的维护成本

- 行为一致性

### 预期成长

| **跨宿主抽象** | 形成 Portable Core / Host Adapter / Host-specific Capability 三分法。 |
|----------------|-----------------------------------------------------------------------|
| **迁移视角**   | 从“把 Claude Plugin 搬到 Codex”升级为“通过移植发现抽象边界”。         |

### 实践完成后，重新理解

- Portable 的应该是文件，还是语义？

- 共用 SKILL.md 是否足够？

- myharness 的核心究竟是什么？

- 哪些 Contract 应该独立于 Host？

| **弹性规则：** 如果本周实验直接暴露了一个会推翻当前 Mental Model 的问题，可以暂停原计划并追加一个短研究循环；如果只是有趣的旁支问题，记录到 Open Questions，继续主线。 |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|


---

## 路线调整说明

本卷是研究导航，不是冻结的教学脚本。执行到对应研究循环前，应先刷新相关官方文档、默认分支与 Changelog；若项目目录或能力名称发生变化，继续追踪本卷定义的研究问题与 Capability，而不是机械寻找旧路径。
