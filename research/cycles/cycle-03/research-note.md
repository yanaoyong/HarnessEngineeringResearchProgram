# Cycle 03 研究笔记（Research Note）· Claude Code Context Lifecycle

> 状态（Status）：PLANNED · NOT EXECUTED
>
> 内容 Batch：2

[Cycle 正文](../../../docs/02-Coding-Agent-Host-Model.md) · [研究工作区](../../README.md) · [来源权限（Source Authority）](../../source-authority.md)

## 1. 研究问题（Research Question）

在绑定 Claude Code 版本与运行条件下，一个工程任务的 Context 如何装载、增长、压缩与恢复，哪些连续性来自 Host lifecycle，哪些必须由外部 Artifact 承担？

## 2. 为什么与 myharness 有关

只有区分 Context、Session persistence、compaction、resume、持久指令与外部 Artifact，myharness 才能避免重复 Host、保存短期噪声，或误判任务在 Session boundary 后能够自然连续。

## 3. 研究范围与退出条件（Scope and Exit Criteria）

- 范围（Scope）：官方 context / session / memory Contract、Context growth、compact / resume observation，以及 Host mechanism 与 Harness Artifact 的边界。
- 范围外（Out of Scope）：未公开 Runtime architecture、Provider benchmark、完整 Handoff schema、长期 Knowledge 与 myharness 实现。
- 退出条件（Exit Criteria）：绑定 Host version 完成 Contract map；完成 `EXP-C03-01` T03 trace 与 `EXP-C03-02` 配对对照；登记 `EVD-*`；形成 Mental Model V1；把 Handoff 设计问题转交 Cycle 13。

当前 Exit Criteria 未满足。

## 4. 心智模型 V0（Mental Model V0）

- Context 不等于 Session 的全部持久化记录。
- Session persistence、Context compaction 与跨 Session memory 是不同机制。
- CLAUDE.md / Rules、Auto Memory、Skill、Task / Change Artifact 与 Summary 的 owner、load timing、scope 和 freshness 不同。
- Tool output 同时可能增加可观察性与 Context 噪声。
- Resume continuity 必须由绑定条件的 Behavior Evidence 验证，不能从功能名称推出。

这是待验证 Mental Model，不是 Claude Code Runtime architecture。

## 5. 证据登记（Evidence Registry）

尚未登记 `EVD-*`。Batch 2 内容生成不产生 Contract claim、Behavior claim 或 Support Assessment。

### 已登记来源制品（Registered Source Artifacts）

- [`SRC-CLAUDE-001`](evidence/SRC-CLAUDE-001.md)：Claude Code official docs · Explore the context window。
- [`SRC-CLAUDE-002`](evidence/SRC-CLAUDE-002.md)：Claude Code official docs · Manage sessions。
- [`SRC-CLAUDE-003`](evidence/SRC-CLAUDE-003.md)：Claude Code official docs · How Claude remembers your project。
- [`SRC-CLAUDE-004`](evidence/SRC-CLAUDE-004.md)：Claude Code official docs · How Claude Code works。
- 复用 Cycle 2 [`SRC-FOUNDATION-004`](../cycle-02/evidence/SRC-FOUNDATION-004.md)：shareAI-lab/learn-claude-code 教学重实现；执行前固定 commit。
- [`SRC-CLAUDE-006`](evidence/SRC-CLAUDE-006.md)：HumanLayer Advanced Context Engineering；只作为 Community Reference。

这些 Source artifact ID 不是 `EVD-*`，不能直接支持 S1–S4。官方页面与默认分支都是执行时重新核验的浮动锚点。

### 契约证据（Contract Evidence）

尚未登记。

### 源码证据（Source Evidence）

尚未登记。Claude Code 官方 Runtime source authority 未建立；教学仓库只可能支持其固定 revision 的教学实现 claim。

### 行为证据（Behavior Evidence）

尚未登记。

### 项目证据（Project Evidence）

尚未登记。

### 企业事实（Enterprise Fact）

尚未登记。

### 社区主张（Community Claims）

尚未派生。ACE 中的方法主张在执行时只能形成 Reference Pattern 或 Open Question。

## 6. 参考模式（Reference Pattern）

按 `load source → enter context → grow / evict / summarize → persist or disappear → reload or recover` 描述信息生命周期，并为每一步标记 Contract、Behavior、Artifact 与 inference。

## 7. 假设（Hypothesis）

`H-C03-01`：在绑定相同运行条件与 T03 instance 时，经过一次受控 `/compact` 后，conversation-only 的关键决策比写入并显式重载自临时实验 Artifact 的同类决策更容易出现 repeated discovery、lost decision 或 sequence drift；Artifact variant 会增加维护、过期和 Context 成本。

## 8. 实验（Experiment）

- `EXP-C03-01`：`EXPLORATORY` · `OBSERVATION_ONLY` · `T03 · Medium Change` · Context Lifecycle Trace；只定位 transition 与 confounder，不单独裁决 Hypothesis。
- `EXP-C03-02`：`COMPARATIVE` · `T03 · Medium Change` · conversation-only 与临时 Artifact 的受控 `/compact` recovery comparison。
- 单一主要变量（Primary Variable）：关键决策在 `/compact` 后是否可从受控 Artifact 重载。
- 固定边界（Fixed Boundary）：`EXP-C03-02` 不同时改变 resume、新 Session、输出量或 Handoff schema。
- 历史映射（Legacy Mapping）：`EXP-W03-01`（拆分为两个新设计，仅为历史计划）
- 运行元数据（Run Metadata）：尚未创建
- Outcome / Result：均尚未运行；`EXP-C03-01` 执行后记录 Observation Outcome，Experiment Result 为 `NOT APPLICABLE · OBSERVATION ONLY`；`EXP-C03-02` 才填写 Hypothesis Result

`EXP-C03-02` 是结束 Cycle 3 前的必做对照，不因首个 trace 是否暴露明显断裂而省略。临时 Artifact 只隔离信息位置变量，不构成 Cycle 13 Handoff design proposal。

## 9. 观察（Observation）

无。研究执行尚未开始。

## 10. 矛盾证据与限制（Contradictory Evidence and Limitations）

- 官方文档可映射 Contract，不能证明未公开内部实现或本地配置的实际行为。
- `learn-claude-code` 不能证明 Claude Code Runtime；ACE 不能证明 Claude Code Contract。
- Host、Provider、Model、configuration 与 task trajectory effect 无法分离时，结果必须为 `INCONCLUSIVE`。
- 未固定 commit 的 repository anchor 不能产生可复现 Source Evidence。

## 11. 心智模型 V1（Mental Model V1）

等待实验与证据。

## 12. 设计判断（Design Judgment）

待定。不实现 myharness Context / Handoff feature，不分配任何 Claude Code 支持等级。

## 13. 开放问题（Open Questions）

执行中发现的旁支问题登记到 [Open Questions](../../open-questions.md)。涉及通用 Session Handoff strategy 的问题转交 Cycle 13。

## 14. 路线复盘触发条件（Route Review Trigger）

完成 Cycle 4 后，或出现能够推翻 Claude Code Host 工作模型的 Direct Behavior Evidence 时触发。
