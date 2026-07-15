# PART IV · V4.3 Cross-host Harness Abstraction

> Four-host Abstraction · Batch 6 · Cycle 9 正文已生成；研究执行与实验结果尚未开始。

[← 上一卷](02-Coding-Agent-Host-Model.md) · [返回总览](../README.md) · [下一卷 →](04-Harness-Engineering-Research-Themes.md) · [公共术语](09-V4.2-Glossary.md)

---

## Batch 6 边界（Boundary）

Batch 6 只生成 Cycle 9 · Four-host Harness Abstraction，并将 V4.1 Week 7 迁移为计划态正文。V4.3 的四个主要 Host 是 Claude Code、Codex、Qwen Code 与 OpenCode；Provider 与 Model 不是第五个 Host。

本 Batch 建立 Portable Semantic Contract、Host Adapter、Host-specific Capability 与显式 degradation 的研究方法，设计 `EXP-C09-01`、`EXP-C09-02`，并准备 Cycle 9 工作区。它不运行四个 Host，不实现或合并 myharness Adapter，不产生 `EVD-*`、Support Assessment 或“已经跨四宿主可移植”的结论，也不迁移 Cycle 10–18。

V4.1 Week 7 原文可在基线提交 `f2b3961cbe125f846818d11a8892fe3c34f2751f` 中复查。旧 `EXP-W07-01` 只作为历史计划 ID 保留。

## 四宿主抽象工作模型（Working Model）

```text
Task Intent + Project Constraint
        ↓
Portable Semantic Contract
Intent · Trigger · Required Context · Procedure · Evidence
Completion · Failure Route · Human Intervention · Limitations
        ↓
Capability Requirement + Mapping Disposition
DIRECT · ADAPTED · DEGRADED · HOST_SPECIFIC · UNSUPPORTED · UNKNOWN
        ↓
Host Adapter
Discovery / Bootstrap · Tool Mapping · Permission · Lifecycle
Distribution · State / Artifact · Observability · Degradation
        ↓
Bound Host Surface + Provider Profile + Model + Configuration
        ↓
Direct Behavior + Project Artifact + Scoped Evidence Claim
```

该图是 `Mental Model V0`，不是四宿主 capability matrix 的已验证结果。文件名、目录形状、Tool 名或 Plugin 格式相同，只能形成待验证映射线索；Portable 表示语义能够被显式映射，不表示行为、输出质量或内部实现完全一致。

---

## Cycle 9 · Four-host Harness Abstraction

> Four-host Abstraction · V4.1 映射：Week 7

### 核心研究问题

> **在 Claude Code、Codex、Qwen Code 与 OpenCode 的绑定版本和运行条件下，哪些 Harness 语义可以形成 Portable Semantic Contract，哪些必须由 Host Adapter 映射、显式降级或保留为 Host-specific Capability / Unsupported / Unknown？**

### 为什么与 myharness 有关

myharness 若直接把 `CLAUDE.md`、`AGENTS.md`、Skill、Hook、Plugin 或 Tool 名互相改写，可能得到“文件存在、能力未发生”的假移植；若为了统一而抹平 permission、bootstrap、trigger、lifecycle 或 evidence route，则会把真实 Host 差异隐藏在共享文件后。Cycle 9 用语义契约和分层 Adapter 暴露差异，使共享部分、目标 Host 映射、Provider / Model 条件与无法支持的能力都可复查。

### 研究范围（Scope）

本 Cycle 只研究：

- Claude Code、Codex、Qwen Code、OpenCode 在 Instruction / Rule、Skill、Tool、Permission、Hook / lifecycle、Agent / Subagent、Plugin / distribution、Session / State 与 Evidence / Completion 上的可观察语义映射；
- Portable Semantic Contract 与 Host Adapter 的字段、责任、failure route 和 degradation vocabulary；
- Agent Skills 官方格式与 progressive disclosure Contract；
- Superpowers porting guide 作为项目维护者提出的跨 Harness reference pattern；
- 同一 T01 / T02 instance 中的四宿主 capability trace，以及按目标 Host 分层的 naive artifact port vs semantic-contract port 对照；
- Contract、Source、Behavior、Project 与推断的分离，以及 Provider / Model / Configuration confounder。

本 Cycle 不研究：

- 把相同文件格式、Skill 目录、Tool 名、Plugin installed 或最终任务成功写成 portability；
- 假设四个 Host 的 CLI、IDE、desktop、cloud 或 TUI surface 自动等价；
- 使用浮动 `QwenLM/qwen-code` 默认分支或未建立 provenance 的安装 artifact 形成 Qwen Code Runtime architecture 结论；
- 公开 Model benchmark、企业就绪或法律合规结论；
- 实现完整 myharness Adapter、重写所有 Skill / Plugin、生成 Cycle 10–18 正文。

### 主线研究对象与权限边界（Authority Boundary）

| 研究对象（Research Object） | 计划深度 | Cycle 9 用途 | 权限 / 停止边界 |
|---|---|---|---|
| Agent Skills Overview、Specification、client implementor guide | L2 定向 | 建立 `SKILL.md` 格式、progressive disclosure 与 client integration 的公共 Contract 问题 | 官方格式只说明标准与实现建议；不能证明任一 Host 当前版本已兼容、已加载或行为一致 |
| obra/superpowers `docs/porting-to-a-new-harness.md` | L3 定向 | 提取 shared skill body、tool mapping、bootstrap、capability gate、definition of done 与 degradation reference pattern | 项目维护者对 Superpowers port 的方法，不是四个 Host 的官方 Contract；默认分支浮动，执行时固定 commit，且 guide 明示 live code 可优先于文档 |
| mifunedev/openharness current repository | L1 范围漂移对照 | 检查 V4.1 “shared primitive distribution”锚点是否仍回答 Cycle 9 问题 | 当前 README 主要定位为 Docker sandbox / long-lived agent workspace；不得沿用旧 `.oh` 路径或把项目名当作 portability 证据 |
| Cycle 3–8 已登记 Host 来源 | L2 / L3 scoped | 建立每个 Host 的 Contract / Source / Behavior readiness map | 计划态 `SRC-*` 不等于 `EVD-*`；Claude Code 不推测未公开 Runtime；Codex、Qwen Code、OpenCode Source 都必须固定 revision，Qwen Code / OpenCode 的 Source / Behavior agreement 还需 artifact provenance |
| myharness 既有跨 Host artifact | Read-only Project mapping | 选择真实 source artifact，记录重复、Host leakage 与无法映射语义 | 文件存在或历史移植不自动构成 Project Evidence；没有可复查 artifact 和 source-host behavior 时，`EXP-C09-02` 保持 `NOT EXECUTED` |

Batch 6 新登记 `SRC-CROSSHOST-001..005`，并引用 Cycle 3–8 已登记来源。所有网页和默认分支均为执行时重新核验的浮动锚点；内容生成不派生 `EVD-*`。

### Cross-host Evidence Readiness Gate

一个 Host 进入 Behavior mapping 前，至少必须绑定：

1. Host version、surface、platform 与 installation channel；
2. 当前官方 Contract anchor 与访问日期；
3. Provider profile、endpoint type、Model ID / revision 与脱敏 Configuration snapshot；
4. task instance、repository commit、tool / permission profile、acceptance / review procedure；
5. 该 Host 所需的 Source Authority 边界：Claude Code 不要求不存在的 Runtime Source；Codex Source claim 固定 `openai/codex` commit；Qwen Code Source claim 固定 `QwenLM/qwen-code` commit 并建立 execution-artifact provenance；OpenCode Source / Behavior agreement 同样需要执行 artifact 到 commit 的 provenance；
6. surface parity 未验证时，只研究实际运行 surface，不跨 CLI、IDE、desktop、cloud 或 TUI 外推。

未通过 Gate 的 Host 可以保留 Contract question，但 Behavior、Mapping Disposition 与 portability result 必须保持 `UNKNOWN · NOT ASSESSED`。Host 无法取得授权运行条件时使用 `NOT EXECUTED`，不能自动改写为 `UNSUPPORTED`。

### 问题驱动的研究路线（Question-driven Research Route）

1. 为四个 Host 各选择一个明确 surface，建立版本与 authority map；复用 Cycle 3–8 Source Registry，不重复把 URL 当 Evidence。
2. 选择一个 capability slice，先写与 Host 文件形状无关的 Portable Semantic Contract，再列出需要的 action vocabulary、lifecycle、permission、state 与 evidence point。
3. 对每个 Host 逐项回答 `discover → load / bootstrap → trigger → execute → observe → complete / fail → persist / distribute`，证据不足的格子保持 Unknown。
4. 只在 Cross-host Evidence Readiness Gate 通过后执行 `EXP-C09-01`；每个 Host 使用独立 Run Metadata，不把不同 Provider / Model 的 outcome 差异归因给 Host。
5. 从 myharness 选择一个已有且可复查的 semantic-review capability；若不存在 source-host behavior baseline，不为填满迁移表临时实现 capability。
6. 执行 `EXP-C09-02` 时，在每个目标 Host 内分别比较 naive artifact port 与 Portable Contract + Adapter；同一目标 Host 的 A / B 固定 Provider、Model、task、acceptance、permission 与 Human intervention。
7. 分别登记 format compatibility、discovery、activation、procedure、evidence、completion 与 degradation；目标 Host strata 之间不汇总为模型排名或普遍 portability。
8. Contract、Source、Behavior 或 Project artifact 矛盾时保留冲突；若抽象只能靠隐藏目标 Host 差异成立，应降级、标记 Host-specific 或保留 Unknown。

### Portable Semantic Contract 最小字段

| 字段（Field） | 研究问题 | 不允许的替代 |
|---|---|---|
| Intent | capability 解决什么工程问题？ | 文件名或 Plugin 名 |
| Trigger / Non-trigger | 何时应启动，何时不应启动？由谁判断？ | 仅列关键词 |
| Preconditions | 开始前必须满足什么版本、权限、输入与状态？ | 假设安装即满足 |
| Required Context | 哪些最小事实、文件、Artifact 与限制必须可见？ | 携带全部历史 |
| Procedure | 哪些顺序和决策不可省略？ | Host-specific Tool 名列表 |
| Action Vocabulary | `read`、`review`、`verify`、`delegate` 等语义动作是什么？ | 把某 Host Tool 名当公共语义 |
| Evidence Required | 哪些 observation / artifact 能复查执行？ | “已完成”自然语言声明 |
| Completion Criteria | 何时可以停止并交付？ | 最终输出存在 |
| Failure Route | 缺能力、拒绝、超时、冲突或证据不足时如何处理？ | 静默跳过 |
| Human Intervention | 哪些输入、approval 或 recovery 允许人工介入？ | 不记录人工修正 |
| Limitations / Degradation | 哪些语义无法保持，如何显式降级？ | 伪装为完全等价 |

### Host Adapter 最小字段

| 字段（Field） | 必须记录 |
|---|---|
| Adapter Identity | target Host、version / surface、Adapter revision、适用 Contract revision |
| Discovery / Bootstrap | artifact 如何被发现，必要 instruction 如何在何时进入 Context |
| Action / Tool Mapping | 每个抽象 action 对应的 Host Tool、参数、缺失能力与 fallback |
| Permission / Sandbox Mapping | decision owner、approval vocabulary、scope 与不可映射语义 |
| Lifecycle Mapping | Hook / event / session transition 的实际 Contract 与 Unknown |
| Distribution | Plugin、extension、project artifact 或其他安装 / version route |
| State / Artifact | task state、session state、project artifact 与 handoff 如何区分 |
| Observability | discovery、activation、tool request、decision、evidence、completion 如何留痕 |
| Degradation / Failure | `DEGRADED`、`UNSUPPORTED`、`UNKNOWN` 的触发条件和用户可见结果 |

### Mapping Disposition（局部映射状态）

| 状态 | 含义 | 不能推导 |
|---|---|---|
| `DIRECT` | 绑定版本下，目标 Host 有能表达该局部语义的公开 surface，未发现需要语义改写 | 行为完全一致、无需配置或已达到 S1–S4 |
| `ADAPTED` | 通过显式 Host Adapter 能保留声明的语义和 evidence route | Adapter 对其他版本 / surface 可用 |
| `DEGRADED` | 只能保留子集，丢失项、fallback 与影响已声明 | 仍然“完全 portable” |
| `HOST_SPECIFIC` | capability 依赖目标 Host 独有语义，不进入 Portable Core | capability 没有价值 |
| `UNSUPPORTED` | 在绑定范围内，有足够 Evidence 表明必要语义不能满足 | 永久不支持或其他版本不支持 |
| `UNKNOWN` | Evidence 不足、Gate 未通过或 effect 无法分离 | 不支持 |

这些状态只描述一个 semantic slice 的映射 disposition，不替代 S0–S4 Support Level，也不构成 Host 总评分。

### 四宿主矩阵初始状态（Planned Matrix）

| Semantic Slice | Claude Code | Codex | Qwen Code | OpenCode | 需要的最小 Evidence |
|---|---|---|---|---|---|
| Instruction / Rule | `UNKNOWN · NOT ASSESSED` | `UNKNOWN · NOT ASSESSED` | `UNKNOWN · NOT ASSESSED` | `UNKNOWN · NOT ASSESSED` | version-bound Contract + scoped Behavior |
| Skill discovery / activation | `UNKNOWN · NOT ASSESSED` | `UNKNOWN · NOT ASSESSED` | `UNKNOWN · NOT ASSESSED` | `UNKNOWN · NOT ASSESSED` | discovery catalog / load observation + task Run |
| Action / Tool mapping | `UNKNOWN · NOT ASSESSED` | `UNKNOWN · NOT ASSESSED` | `UNKNOWN · NOT ASSESSED` | `UNKNOWN · NOT ASSESSED` | actual exposed tool set + request / result trace |
| Permission / Approval | `UNKNOWN · NOT ASSESSED` | `UNKNOWN · NOT ASSESSED` | `UNKNOWN · NOT ASSESSED` | `UNKNOWN · NOT ASSESSED` | permission profile + decision owner / result |
| Hook / Lifecycle | `UNKNOWN · NOT ASSESSED` | `UNKNOWN · NOT ASSESSED` | `UNKNOWN · NOT ASSESSED` | `UNKNOWN · NOT ASSESSED` | event Contract + trigger / failure Behavior |
| Agent / Subagent | `UNKNOWN · NOT ASSESSED` | `UNKNOWN · NOT ASSESSED` | `UNKNOWN · NOT ASSESSED` | `UNKNOWN · NOT ASSESSED` | Context / Tool / result boundary trace |
| Plugin / Distribution | `UNKNOWN · NOT ASSESSED` | `UNKNOWN · NOT ASSESSED` | `UNKNOWN · NOT ASSESSED` | `UNKNOWN · NOT ASSESSED` | installed / enabled / discovered / loaded separation |
| Session / State / Artifact | `UNKNOWN · NOT ASSESSED` | `UNKNOWN · NOT ASSESSED` | `UNKNOWN · NOT ASSESSED` | `UNKNOWN · NOT ASSESSED` | lifecycle checkpoints + artifact reload observation |
| Evidence / Completion | `UNKNOWN · NOT ASSESSED` | `UNKNOWN · NOT ASSESSED` | `UNKNOWN · NOT ASSESSED` | `UNKNOWN · NOT ASSESSED` | deterministic check + review artifact + completion trace |

Batch 6 不填写以上单元格。真实执行时每个非 Unknown 单元格必须链接 scoped `EVD-*`、Host / Provider / Model / Configuration 与验证日期。

### 假设（Hypothesis）

`H-C09-01 · Semantic Contract Portability`：对同一个已有 myharness semantic-review capability 和固定 T02 instance，在同一目标 Host、Provider、Model、Configuration 与 permission profile 内，相比只搬运 source-host 文件形状和替换显眼 Tool 名的 naive port，先提取 Intent、Trigger、Required Context、Procedure、Evidence、Completion、Failure Route 与 Limitations，再通过显式 Host Adapter 映射的 variant，应减少 Host leakage、silent degradation 与 false completion，并提高 discovery-to-evidence trace 的可解释性；它也可能增加 Adapter 代码、Context、维护与版本绑定成本。

支持信号：目标 Host 内的配对 Run 显示 Contract + Adapter variant 更完整地保持预声明 semantic checkpoints，无法映射项被显式报告，且差异可追溯到 Adapter 而非 Provider / Model / task drift。

反驳信号：在相同目标 Host 条件下，naive port 同样保持全部 semantic checkpoints，或 Contract + Adapter variant 因 bootstrap、mapping、Context 或维护复杂度产生更多未声明失败且没有方向性增益。

不确定信号：source artifact / behavior baseline 不存在，A / B capability body 或 task 不同，Host surface、Provider、Model、permission、acceptance 或 Human intervention 未固定，或目标 Host 的 readiness gate 未通过。

### 计划实验（Planned Experiments）

#### `EXP-C09-01` · Four-host Semantic Capability Trace

- 实验类型（Experiment Type）：`EXPLORATORY`
- Outcome Mode：`OBSERVATION_ONLY`
- 稳定任务（Stable Task）：`T01 · Engineering Constraint`
- 历史映射（Legacy Mapping）：V4.1 Week 7 无对应独立实验；这是 `EXP-W07-01` 前新增的 readiness prerequisite
- T01 instance：`T01-C09-LOCAL-HTTP-TIMEOUT`。在同一固定 commit 的隔离 fixture repository 中，为已有本地 HTTP client 增加显式、非默认、可配置 timeout，并保持既有 error / response semantics；不访问网络或真实服务
- Acceptance checks：本地 fixture 覆盖 timeout 缺省、合法配置、非法配置与 request construction；保存命令、exit code、diff 与 deterministic check result
- Host strata：Claude Code、Codex、Qwen Code、OpenCode 各自独立执行；每个 stratum 只绑定一个明确 surface，并使用独立 Run Metadata
- Trace：记录 instruction source、Skill state、actual tool set、read / edit / command request、permission owner / decision、Hook / lifecycle observation、task / session state、acceptance、artifact 与 human intervention
- Comparability boundary：尽量固定 repository、task、acceptance、instruction semantic 与 tool / permission intent；Provider / Model 不能相同时只比较 semantic route 是否可观察，不比较 outcome quality 或归因 Host performance
- Observation Outcome boundary：本实验只形成 capability question map 与 scoped observations，不单独裁决 `H-C09-01`；完成记录使用 `COMPLETE / PARTIAL / INVALIDATED`，Experiment Result 为 `NOT APPLICABLE · OBSERVATION ONLY`；未通过 Gate 的 Host 保持 `NOT EXECUTED / UNKNOWN`

#### `EXP-C09-02` · Naive Artifact Port vs Portable Semantic Contract

- 实验类型（Experiment Type）：`COMPARATIVE`
- 稳定任务（Stable Task）：`T02 · Semantic Review`
- 历史映射（Legacy Mapping）：`EXP-W07-01`（仅为历史计划）
- Project artifact gate：从 myharness 选择一个已有、版本可固定、具备 source-host Behavior baseline 的 code-review 或 research-discovery capability；若没有满足条件的 artifact，本实验保持 `PLANNED · NOT EXECUTED`，不得临时实现完整 capability 填补历史映射
- T02 instance：对固定 commit 中含 acceptance reference 的有限 patch 作语义审查；evaluator-only oracle 至少包含一个需推理问题与一个 deterministic defect，答案不得进入 Agent-visible task、Rule、Skill、context 或 output schema
- Baseline A · Naive Port：只做目标 Host 可加载所需的最小包装 / 路径调整和显眼 Tool 名替换，不先写 Portable Semantic Contract；所有修改必须留痕，不能故意破坏 artifact
- Variant B · Contract + Adapter：Capability body 的 Intent / Procedure 保持相同；先写 Portable Semantic Contract，再用目标 Host Adapter 映射 discovery / bootstrap、action、permission、lifecycle、distribution、state、evidence 与 degradation
- 单一主要变量（Primary Variable）：porting method；在同一目标 Host 内固定 task、Host version / surface、Provider profile、Model、configuration、permission、source capability revision 与 acceptance procedure
- Source / target derivation：先从 `Claude Code / Codex / Qwen Code / OpenCode` 四宿主集合中绑定一个拥有可复查 Behavior baseline 的 `source_host`，再定义 `target_hosts = four_hosts - {source_host}`。默认 Claude 为 source 时，目标才是 Codex、Qwen Code、OpenCode；若 Route Review 更改 source，必须同时失效旧 target plan 并重算三个 target，不得让 source Host 与 target Host 重合或遗漏其他主要 Host。source artifact 若不属于四宿主，本实验保持 `NOT EXECUTED` 并进入 Route Review，不得引入第五个 Host
- Target strata：Result Unit 为 `HOST`，Stratum Key 为 `target_host`；在同一个 `EXP-C09-02` Experiment Record 中，对重算后的每个 target Host 单独建立 stratum、A / B Run group、Result、限制与 scoped `EVD-*`，不得把一个目标的结果替代另一个
- 重复与顺序（Replication and Order）：每个可执行目标的 A / B 各至少两个 fresh task Run，顺序交错，从相同 clean baseline 与 Agent-visible input 开始
- 主要观察项（Primary Observations）：format load、discovery、activation、required context、procedure checkpoint、action / permission mapping、evidence citation、deterministic verification、completion、silent degradation、Host leakage、false positive / completion、Context / maintenance cost、human intervention
- 结果词汇（Result Vocabulary）：`SUPPORT / REJECT / INCONCLUSIVE`
- 解释边界（Interpretation Boundary）：每个 Result 只适用于绑定目标 Host 与 capability slice；至少两个目标 strata 完成前，不形成 cross-host Hypothesis Result；缺少访问或 Gate 未通过使用 `NOT EXECUTED / UNKNOWN`，不是 `UNSUPPORTED`

cross-host Experiment Result 的预注册聚合规则为：至少两个 target strata 已完成后，两个或以上 `SUPPORT` 且没有 `REJECT` 才为 `SUPPORT`；两个或以上 `REJECT` 且没有 `SUPPORT` 才为 `REJECT`；其余达到最小完成数的组合为 `INCONCLUSIVE`。不足两个已完成 strata 时不创建 Experiment-level Result，不能用 `INCONCLUSIVE` 代替未执行。

##### `EXP-C09-02` 预注册裁决规则（Pre-registered Decision Rule）

每个 target stratum 在首个 Run 前冻结 Contract revision、Adapter revision 与主要裁决表。一个 replication block 由从同一 clean baseline 和相同 Agent-visible input 开始的一个 A Run 与一个 B Run 组成；第一个 block 的先后顺序预先决定，第二个 block 使用相反顺序。每个 Run 对 discovery、activation、required-context delivery、预声明 procedure checkpoints、evidence citation、deterministic verification、completion 和 degradation reporting 分别记录 `PASS / FAIL / UNKNOWN`；Host leakage、silent degradation 与 false completion 作为 critical failure 单独记录。Context / maintenance cost 与 human intervention 是 secondary trade-off，不得在看到结果后改写主要裁决方向；若要使用 budget，必须在 Run 前固定 threshold。

| Result | 目标 Host 内的预注册条件 |
|---|---|
| `SUPPORT` | 在两个顺序交错的 replication block 中，B 相对 A 至少有一项预声明主要 checkpoint 持续改善或一类 critical failure 持续减少，没有新增主要 checkpoint 退化 / critical failure，且差异可追溯到 porting method 而非 confounder |
| `REJECT` | A 与 B 在所有预声明主要项上保持相同且 B 没有预注册的方向性增益，或 B 在两个 replication block 中持续新增主要 checkpoint 退化 / critical failure 而无主要改善；差异仍必须排除已知 confounder |
| `INCONCLUSIVE` | replication 方向不一致、主要指标有未预声明的互换、任一必需项为 `UNKNOWN`、样本 / trace 不完整，或 Provider、Model、task、permission、Human intervention 等 confounder 不能分离 |

`SUPPORT` 只支持该 target Host / capability slice 下的方向性 `H-C09-01` Result，不等于 portability 已普遍证明、Mapping Disposition 已自动确定或 Host 已达到 S1–S4。

两个实验必须使用独立 Experiment Record，并为每次执行保存独立 Run Metadata。内容生成阶段不创建 Experiment Record、Run record、Adapter implementation、Result 或 `EVD-*`。

### 退出条件（Exit Criteria）

Cycle 9 只有在以下条件均满足后才能结束：

- 四宿主 authority / readiness map 分别绑定 Host version、surface、platform、Provider profile、Model、Configuration、Source IDs 与限制；
- capability matrix 的每个非 Unknown 单元格都引用 scoped `EVD-*`，Unknown 与 Unsupported 没有混用；
- Qwen Code Source claim 绑定 `QwenLM/qwen-code` 固定 commit 并满足 artifact provenance；Codex / OpenCode Source claim 同样绑定固定 commit，OpenCode Source / Behavior agreement 满足 artifact provenance；
- `EXP-C09-01` 对所有可用 Host 完成独立 trace；不可用 Host 明确记录 `NOT EXECUTED / UNKNOWN` 原因，不伪造对照；
- `EXP-C09-02` 至少完成两个目标 Host strata 的 A / B 配对 Run、独立 Result 与 Evidence；其余目标若未执行，必须保留 limitation，不能形成“四宿主普遍可移植”结论；
- Evidence 能分别回答 format loaded、discovered、activated、procedure executed、evidence produced、completion satisfied 与 degradation reported；
- Portable Semantic Contract、Host Adapter、Provider Profile、Provider-dependent Behavior 与 Host-specific Capability 分层清楚；
- Mental Model V1 记录 Direct / Adapted / Degraded / Host-specific / Unsupported / Unknown 及反例；
- 不实现或合并完整 myharness Adapter，不形成 Host 总评分、公开 Model benchmark、企业或法律结论。

---

## Batch 6 路线复盘触发条件（Route Review Trigger）

完成 Cycle 9 的真实研究后执行一次 Route Review。它可以调整 Batch 7 的 Skill / Change / Workflow / Context / Knowledge source anchor、实验节奏或借用方法，但不能改变冻结的 Cycle 名称、编号、顺序或 Batch 边界。

内容生成本身不满足 Cycle 9 Exit Criteria，也不创建 Route Review 结果。若真实 Host mapping 显示 Portable Semantic Contract 只能通过隐藏关键差异成立，或 V4.1 主锚点已不再回答原问题，应提前记录 contradiction 并调整 reference pool；不能为了保留旧路线而制造 portability 结论。

## Batch 6 迁移记录（Migration Record）

| V4.1 历史计划 | V4.2 研究设计 | 状态（Status） |
|---|---|---|
| Week 7 · `EXP-W07-01` | Cycle 9 · `EXP-C09-01` / `EXP-C09-02` | 增加四宿主 readiness trace，并把 naive port vs semantic contract 设计扩展为按目标 Host 独立分层；尚未执行，旧 ID 只作历史记录 |

V4.1 OpenHarness 的 `.oh/docs/oh-directory-layout.md` 与 shared primitive pack 描述只保留为历史迁移线索。Batch 6 刷新时，当前项目 README 主要定位已转向 Docker sandbox / long-lived workspace，因此不沿用旧路径或旧角色形成 Cycle 9 结论。
