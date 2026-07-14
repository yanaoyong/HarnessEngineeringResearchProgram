# Cycle 01 研究笔记（Research Note）· Coding Agent 最小模型

> 状态（Status）：PLANNED · NOT EXECUTED
>
> 内容 Batch：1

[Cycle 正文](../../../docs/01-Agent与Harness基础认知.md) · [研究工作区](../../README.md) · [来源权限（Source Authority）](../../source-authority.md)

## 1. 研究问题（Research Question）

一个 Coding Agent 最少需要什么，Agent Core 与 Harness 的可观察边界在哪里？

## 2. 为什么与 myharness 有关

只有先说明最小 Agent Loop 已承担的责任，才能判断 myharness 的治理机制是在补足稳定性，还是重复 Agent / Host 能力。

## 3. 研究范围与退出条件（Scope and Exit Criteria）

- 范围（Scope）：Model、History、Action、Environment / Tool、Observation、Continue / Stop，以及 Instruction 与 action interception 的最小对照。
- 范围外（Out of Scope）：Host 专项架构、Provider benchmark、生产级 Hook、myharness feature。
- 退出条件（Exit Criteria）：以固定 revision 建立机制图；完成 `EXP-C01-01` 的受控 Run；形成可追溯 `EVD-*`；更新 Mental Model V1；记录 Unknown。

当前 Exit Criteria 未满足。

## 4. 心智模型 V0（Mental Model V0）

- Model 产生候选 Action，但不执行外部效果。
- Agent Loop 维护 History，把 Observation 放回下一轮输入，并做继续或停止决策。
- Environment / Tool Boundary 执行 Action 并返回 Observation。
- Instruction 影响选择；interception 在执行边界做确定性判断。
- 从“能运行”到“受工程约束地稳定运行”的差距，是 Harness 的候选范围。

这是待验证 Mental Model，不是 Evidence。

## 5. 证据登记（Evidence Registry）

尚未登记 `EVD-*`。Batch 1 内容生成不产生实验结果。

### 已登记来源制品（Registered Source Artifacts）

- [`SRC-FOUNDATION-001`](evidence/SRC-FOUNDATION-001.md): SWE-agent/minimal-agent-tutorial；执行前固定 commit。
- [`SRC-FOUNDATION-002`](evidence/SRC-FOUNDATION-002.md): SWE-agent/mini-swe-agent；`main` 是计划执行时核验的浮动锚点，执行前固定 commit。
- [`SRC-FOUNDATION-003`](evidence/SRC-FOUNDATION-003.md): SWE-agent ACI paper；只用于 Reference Pattern / investigation question。

这些 Source artifact ID 不是 Evidence claim，也不能直接支持 Support Assessment。前三个 Registry entry 均未派生 `EVD-*`。

### 契约证据（Contract Evidence）

尚未登记。

### 源码证据（Source Evidence）

尚未登记。

### 行为证据（Behavior Evidence）

尚未登记。

### 项目证据（Project Evidence）

尚未登记。

### 企业事实（Enterprise Fact）

尚未登记。

### 社区主张（Community Claims）

尚未登记。

## 6. 参考模式（Reference Pattern）

最小参考闭环：`Model → Action → Environment / Tool → Observation → History → next decision`。该 pattern 仅用于组织问题；必须通过绑定 revision 的 Source 与 Behavior Evidence 验证。

## 7. 假设（Hypothesis）

`H-C01-01`: 在绑定相同运行条件下，Instruction 能影响“修改前读取目标文件”的遵循，但不能提供确定性阻断；最小 action interception 可能提高违规发现的一致性，同时引入 false positive、阻塞与实现成本。

## 8. 实验（Experiment）

- 实验 ID（Experiment ID）：`EXP-C01-01`
- 实验类型（Experiment Type）：`COMPARATIVE`
- 任务套件 ID（Task Suite ID）：`T01 · Engineering Constraint`
- 历史映射（Legacy Mapping）：`EXP-W01-01`（仅为历史计划）
- 运行元数据（Run Metadata）：尚未创建
- 结果（Result）：尚未运行

## 9. 观察（Observation）

无。研究执行尚未开始。

## 10. 矛盾证据与限制（Contradictory Evidence and Limitations）

- 当前只有研究设计，没有可支持或反驳 Hypothesis 的 Behavior Evidence。
- 浮动默认分支不能提供可复现 Source Evidence；执行时必须固定 commit。
- 无法分离 Host、Provider、Model 与配置 effect 时，结果必须为 `INCONCLUSIVE`。

## 11. 心智模型 V1（Mental Model V1）

等待实验与证据。

## 12. 设计判断（Design Judgment）

待定。不对 myharness 做实现建议，不分配任何 Host 支持等级（Support Level）。

## 13. 开放问题（Open Questions）

执行中发现的旁支问题登记到 [Open Questions](../../open-questions.md)，不得在本 Note 中无边界扩张。

## 14. 路线复盘触发条件（Route Review Trigger）

完成 Cycle 2 后，或出现能够推翻 Foundation Working Model 的直接 Evidence 时触发。
