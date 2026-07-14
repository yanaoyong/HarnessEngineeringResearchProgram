# PART II · V4.2 Agent 与 Harness 基础认知

> Foundation · Batch 1 · Cycle 1–2 正文已生成；研究执行与实验结果尚未开始。

[← 上一卷](00-研究计划总纲.md) · [返回总览](../README.md) · [下一卷 →](02-Coding-Agent-Host-Model.md) · [公共术语](09-V4.2-Glossary.md)

---

## Batch 1 边界（Boundary）

Batch 1 只建立两个 Foundation Cycle：

1. Cycle 1 · Coding Agent 最小模型
2. Cycle 2 · Harness Primitive

本 Batch 将 V4.1 Week 1–2 的研究导航迁移为 V4.2 Cycle 正文，并对齐公共术语、Source Authority、T01–T03、`EXP-Cxx-yy` 与 Run Metadata。它不执行实验，不产生 Support Assessment，不进入 Claude Code、Codex、ZCode、OpenCode 的 Host 专项研究，也不实现 myharness feature 或任何 Adapter。

V4.1 原文仍可在基线提交 `f2b3961cbe125f846818d11a8892fe3c34f2751f` 中复查。旧 `EXP-W01-01`、`EXP-W02-01` 仅作为历史计划 ID（Historical Plan ID）保留，不重编号为已执行 Evidence。

## 基础工作模型（Foundation Working Model）

Batch 1 使用以下待验证分层，不把它写成既定事实：

```text
模型（Model）
  ↓ 提出操作（Action）
智能体循环（Agent Loop）
  ↓ 请求执行
环境 / 工具边界（Environment / Tool Boundary）
  ↓ 返回观察（Observation）
历史 / 状态（History / State）
  ↓ 成为下一轮模型输入
停止 / 继续决策（Stop / Continue Decision）

围绕循环的 Harness 候选机制：
指令（Instruction）· 规则（Rule）· 权限（Permission）· 钩子（Hook）· 任务状态（Task State）· 技能（Skill）· 子智能体边界（Subagent Boundary）
```

这张图是 `Mental Model V0`，不是 Evidence。Cycle 1 先寻找 Agent 能运行的最小闭环；Cycle 2 再研究哪些额外 Primitive 能让行为更受控、可恢复和可复查。

---

## Cycle 1 · Coding Agent 最小模型

> Foundation · V4.1 映射：Week 1

### 核心研究问题

> **一个 Coding Agent 最少需要什么，Agent Core 与 Harness 的可观察边界在哪里？**

### 为什么与 myharness 有关

如果无法说明最小 Agent Loop 已经承担什么，就无法判断 myharness 的 Instruction、Rule、Hook 或其他能力是在补充必要治理，还是重复 Host / Agent 已有责任。Cycle 1 的目标不是做一个高性能 Agent，而是建立足够小、可运行、可攻击的机制模型。

### 研究范围（Scope）

本 Cycle 只研究：

- Model input / output、History、Action、Environment / Tool、Observation、Continue / Stop 的最小闭环；
- 异常如何回到 loop，以及 human intervention 可以插入哪里；
- 同一工程约束由自然语言 Instruction 与确定性 action interception 承担时的差异；
- Agent Core、Host surface 与 Harness candidate 的初步边界。

本 Cycle 不研究：

- SWE-bench 排名、Provider 性能或公开模型 benchmark；
- 大型 Evaluation / Observability 平台；
- Claude Code、Codex、ZCode 或 OpenCode 的内部架构；
- 生产级 Hook、Permission system 或 myharness 实现。

### 主线研究对象与权限边界（Authority Boundary）

| 研究对象（Research Object） | 计划深度 | Cycle 1 用途 | 权限边界（Authority Boundary） |
|---|---|---|---|
| [SWE-agent/minimal-agent-tutorial](https://github.com/SWE-agent/minimal-agent-tutorial) | L3 | 从约 60 行终端 Agent 画出最小数据流 | 项目官方教程与源码只证明该 revision 的教学实现 |
| [SWE-agent/mini-swe-agent](https://github.com/SWE-agent/mini-swe-agent) | L3 targeted | 对照 Agent、Environment、Model、Run 的拆分与 HITL 扩展 | `main` 仅作为计划执行时核验的浮动锚点；执行时必须固定 commit |
| [SWE-agent ACI paper](https://arxiv.org/abs/2405.15793) | L1 theory | 用 interface design 观点解释观察到的行为差异 | 论文不能证明任何商业 Host 的当前实现或支持等级 |

本表只登记计划执行时核验的浮动锚点，不构成已固定 revision 的 Source Evidence。执行时必须重新核验入口与目录，固定 repository、commit、scope、access date 与限制，再派生 Evidence Claim。

### 问题驱动的阅读路线（Question-driven Reading Route）

1. 先读 `minimal-agent-tutorial/docs/index.md`，手画一次 `Model → Action → Environment → Observation → History` 数据流。
2. 再读完整最小实现，逐项标出初始化、loop、action extraction、execution、observation append 与 stop condition。
3. 在 `mini-swe-agent` 当前 revision 中只定位：
   - `src/minisweagent/agents/default.py`
   - `src/minisweagent/environments/local.py`
   - `src/minisweagent/models/`
   - `src/minisweagent/run/`
4. 只有当问题转向 human intervention 时，再看 `agents/interactive.py`。
5. 路径变化时按 capability 重新定位，不把上述目录当永久 Contract。

阅读时只追：

- History 为什么存在，Observation 为什么重新进入下一轮输入？
- Agent 如何决定继续或停止，异常是否被观察并重新进入 loop？
- Environment 与 Tool 是同一抽象，还是两个可分离边界？
- Human intervention 加在 model input、action approval、execution 还是 result interpretation？
- 删除哪一部分会让系统不再是可行动的 Agent？

### 心智模型 V0（Mental Model V0）

- Model 产生候选 Action，但 Model 本身不负责执行。
- Agent Loop 至少负责维护交互状态、把 Observation 送回 Model，并决定继续或停止。
- Environment / Tool Boundary 负责把请求变成外部效果并返回可观察结果。
- Instruction 可能改变行为概率；interception 可以在 Action 执行前做确定性判断。
- “Agent 能运行”与“Agent 在工程约束下稳定运行”是两个不同问题；后者是 Harness 研究入口。

以上均为待 Evidence 攻击的 Mental Model，不是 Cycle 1 结论。

### 假设（Hypothesis）

> **H-C01-01:** 在同一 Host、Provider、Model、task instance 与配置下，把“修改前必须读取目标文件”只作为 Instruction，能够影响行为但不能提供确定性阻断；把同一约束放到 action interception，能够更稳定地发现或阻止违规，但会引入阻塞、误报和实现成本。

支持信号：interception variant 对未读先改的违规有更高且可解释的确定性发现，同时没有不可接受的 false positive 或人工恢复成本。

反驳信号：Instruction baseline 已稳定满足约束，或 interception 无法可靠判断前置读取、产生大量误报，因而没有方向性治理增益。

不确定信号：Host、Provider、Model、task difficulty 或实现差异无法分离，Run Metadata 不完整，或样本只能说明单次偶然行为。

### 计划实验（Planned Experiment）· `EXP-C01-01`

- 实验类型（Experiment Type）：`COMPARATIVE`
- 稳定任务（Stable Task）：`T01 · Engineering Constraint`
- 历史映射（Legacy Mapping）：`EXP-W01-01`（仅为历史计划）
- 基线（Baseline）：相同约束只通过 Instruction 表达
- 变体（Variant）：相同约束通过最小 action interception 检测或阻断
- 受控变量（Controlled Variables）：repository commit、task instance、Host/version、Provider profile、Model、configuration snapshot、Rule/Skill/Check/Adapter revision
- 主要观察项（Primary Observations）：first-pass adherence、错误 Action、Agent self-correction、deterministic detection、false positive、rework、context cost、human intervention
- 结果词汇（Result Vocabulary）：`SUPPORT / REJECT / INCONCLUSIVE`

执行前必须：

1. 固定一个满足 T01 contract 的 task instance 与可逆 repository baseline。
2. 为每个 variant 建立独立 Run Metadata；不得只靠文件名暗示差异。
3. 登记 Source artifact 与 Behavior artifact，再从 artifact 派生 `EVD-*` claim。
4. 不把 3–5 次方向性 Run 包装为公开 benchmark 或普遍模型结论。

Batch 1 不创建 Run、不填写结果，也不预设 Hypothesis 被支持。

### 退出条件（Exit Criteria）

Cycle 1 只有在以下条件均满足后才能结束：

- 能用自己的语言解释最小闭环及每一部分删除后的后果；
- 至少一个固定 revision 的最小 Agent 实现被登记并读到计划深度；
- `EXP-C01-01` 的 baseline、variant、controlled variables、confounders 与 Run Metadata 完整；
- Evidence 能区分 Instruction adherence 与 deterministic interception；
- Mental Model V1 明确记录被支持、被推翻和仍 Unknown 的部分；
- 旁支问题进入 Open Questions，不扩张为 Host 专项研究。

---

## Cycle 2 · Harness Primitive

> Foundation · V4.1 映射：Week 2

### 核心研究问题

> **Agent Loop 已经能工作时，Permission、Hook、Task State、Skill 与 Subagent Boundary 分别解决什么不可互换的工程问题？**

### 为什么与 myharness 有关

myharness 的长期风险不是缺少 Primitive 名称，而是让多个机制承担重叠责任，或把 Host-specific surface 误写成 Portable Semantic Contract。Cycle 2 先建立责任假设，再通过小实验观察 Primitive 是否真的改变行为、状态连续性或 Context boundary。

### 研究范围（Scope）

本 Cycle 只研究：

- Instruction、Permission、Hook、Task State、Skill 与 Subagent Boundary 的职责差异；
- deterministic behavior 与 model-mediated behavior 的边界；
- Externalized State 是否减少漏步骤、重复和顺序漂移；
- Subagent 的 Context isolation 是否能减少主 Context 噪声，同时保留可复查结论。

本 Cycle 不研究：

- Claude Code 官方 Runtime architecture；
- 复杂 Skill Evaluation、完整 Context Lifecycle 或跨 Host portability；
- Plugin packaging、MCP integration、OpenCode Adapter；
- 生产级 Permission / Hook / Task system 或 myharness feature。

### 主线研究对象与权限边界（Authority Boundary）

| 研究对象（Research Object） | 计划深度 | Cycle 2 用途 | 权限边界（Authority Boundary） |
|---|---|---|---|
| [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | L3 teaching model | 逐章运行和修改最小 Harness Primitive | 教学重实现不是 Claude Code 官方源码，不能证明其 Runtime architecture、lifecycle event 或官方 Contract |
| Cycle 1 最小 Agent | 项目 / 行为基线（Project / Behavior Baseline） | 在同一最小 loop 上增加单一 Primitive | 只支持绑定 revision、配置和 Run 的局部观察 |

`learn-claude-code` 的 `s01`–`s08` 仅作为计划执行时核验的浮动章节锚点。Cycle 2 计划只使用下列章节；执行时必须重新核验目录并固定 commit，后续新增章节不自动进入研究范围。

### 问题驱动的阅读路线（Question-driven Reading Route）

深读顺序：

1. `s01_agent_loop`：确认与 Cycle 1 的最小闭环差异。
2. `s03_permission`：观察决策发生在 Action 前还是只在 prompt 中。
3. `s04_hooks`：观察确定性触发、输入输出与失败路径。
4. `s05_todo_write`：观察 Task State 如何外置。
5. `s06_subagent`：观察 Context、Tool 与返回结果边界。
6. `s07_skill_loading`：观察 discovery、loading 与 execution 是否分离。

快速阅读 `s02_tool_use` 与 `s08_context_compact`；`s08` 只建立术语联系，不提前执行 Cycle 3。每章遵循 `README → 机制猜想 → code.py → 运行 → 只修改一个变量`。

阅读时只追：

- Permission 是 Instruction，还是 Host / Harness 在 Action 前的决策点？
- Hook 是否必须由 Model 参与，确定性触发的价值和代价是什么？
- Task / Todo 只是 UI，还是会进入后续决策的 Externalized State？
- Skill 的 discovery、activation 与 execution 分别在哪里发生？
- Subagent 的主要变量是角色 prompt，还是 Context / Tool / result boundary？

### 原语职责假设（Primitive Responsibility Hypotheses）

| 原语（Primitive） | 心智模型 V0（Mental Model V0） | 误用后果（Failure if Misused） |
|---|---|---|
| Instruction | 通过自然语言影响 Model 的选择 | 被误当成确定性 enforcement |
| Permission | 在 Action 执行前做允许、拒绝或升级决策 | 与工程 Rule 混淆，产生无意义 approval |
| Hook | 在生命周期触发点观察、注入、验证或阻断 | 假设跨 Host 事件等价，或把语义 SOP 写成脚本 |
| Task State | 把多步进度外置为可更新状态 | 只做 UI 展示，实际决策不读取它 |
| Skill | 按需提供某类任务的程序性知识 | 被加载但未执行，或退化成长篇 Rule |
| Subagent Boundary | 隔离 Context / Tool / responsibility，并返回有限产物 | 只改变角色名称，没有减少噪声或明确交付 |

该表是待验证责任模型，不是 Host capability mapping，也不构成任何 S1–S4 结果。

### 假设（Hypotheses）

> **H-C02-01:** 对同一个 T03 多步任务，显式维护并在每步决策前读取 Task State，会减少漏步骤、重复操作和顺序漂移，但可能增加状态维护与 Context 成本。

> **H-C02-02:** 对同一个有限 T02 语义审查，使用具有明确 Context、Tool 与 output contract 的 Subagent Boundary，可以减少主 Context 的原始读取量；如果只增加角色 prompt 而不限制边界，则不会产生同等效果。

### 计划实验（Planned Experiments）

#### `EXP-C02-01` · 外置任务状态（Externalized Task State）

- 实验类型（Experiment Type）：`COMPARATIVE`
- 稳定任务（Stable Task）：`T03 · Medium Change`
- 历史映射（Legacy Mapping）：`EXP-W02-01` 中的 Task State 部分（仅为历史计划）
- 基线（Baseline）：Agent 直接执行 4–5 步受控任务
- 变体（Variant）：Agent 显式维护并在决策点读取 Task State
- 主要观察项（Primary Observations）：missed step、duplicate action、sequence drift、false completion、rework、context cost、human intervention

#### `EXP-C02-02` · 子智能体上下文边界（Subagent Context Boundary）

- 实验类型（Experiment Type）：`COMPARATIVE`
- 稳定任务（Stable Task）：`T02 · Semantic Review`
- 历史映射（Legacy Mapping）：`EXP-W02-01` 中的 Subagent 部分（仅为历史计划）
- 基线（Baseline）：主 Agent 读取完成有限 review 所需的全部材料
- 变体（Variant）：独立研究 Agent 在明确 scope 下只返回结构化 finding、artifact reference、limitation 与 unknown
- 主要观察项（Primary Observations）：主 Context 原始读取量、evidence citation quality、遗漏、false positive、重复读取、handoff loss、human intervention

两个实验必须分别执行，不能把 Task State 与 Subagent 同时作为一个 variant 改动。Instruction 与 interception 的延续问题留在 `EXP-C01-01`，不在 Cycle 2 重复制造不可分离变量。

### 退出条件（Exit Criteria）

Cycle 2 只有在以下条件均满足后才能结束：

- 能说明每个 Primitive 的 trigger、是否需要 Model 参与、是否能确定性阻断、Context cost 与 failure route；
- `learn-claude-code` 只作为绑定 revision 的教学 Source 使用，没有被写成 Claude Code 官方 Runtime 证据；
- `EXP-C02-01` 与 `EXP-C02-02` 分别保存完整 Run Metadata 和 `EVD-*` claim；
- 结果能区分 Primitive 被加载、被执行与真正改变 outcome / process；
- Mental Model V1 记录责任重叠、反例和仍 Unknown 的边界；
- 未提前进入 Cycle 3 Context Lifecycle、Cycle 4 Extension Surface 或后续 Adapter 设计。

---

## Batch 1 路线复盘触发条件（Route Review Trigger）

完成 Cycle 2 后执行一次 Route Review。它可以调整 Batch 2 的项目锚点、阅读深度、执行节奏或借用方法，但不能改变冻结的 Cycle 名称、编号、顺序或 Batch 边界。

如果实验直接推翻 Foundation Mental Model，可以在当前 Cycle 内缩小问题并追加最小 Run；如果只是有趣旁支，记录到 Open Questions。不得用“顺便研究一个 Host”扩大 Batch 1。

## 迁移记录（Migration Record）

| V4.1 历史计划 | V4.2 研究设计 | 状态（Status） |
|---|---|---|
| Week 1 · `EXP-W01-01` | Cycle 1 · `EXP-C01-01` | 新设计，尚未执行；旧 ID 作为历史记录保留 |
| Week 2 · `EXP-W02-01` | Cycle 2 · `EXP-C02-01` / `EXP-C02-02` | 为隔离变量而拆分，尚未执行；旧 ID 作为历史记录保留 |

拆分 V4.1 `EXP-W02-01` 历史 ID 只改变未来实验设计，不声称历史实验已经发生，也不把旧 ID 重编号成 Evidence。
