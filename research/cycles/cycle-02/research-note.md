# Cycle 02 研究笔记（Research Note）· Harness Primitive

> 状态（Status）：PLANNED · NOT EXECUTED
>
> 内容 Batch：1

[Cycle 正文](../../../docs/01-Agent与Harness基础认知.md) · [研究工作区](../../README.md) · [来源权限（Source Authority）](../../source-authority.md)

## 1. 研究问题（Research Question）

Agent Loop 已经能工作时，Permission、Hook、Task State、Skill 与 Subagent Boundary 分别解决什么不可互换的工程问题？

## 2. 为什么与 myharness 有关

Primitive 职责不清会造成重复治理、错误 enforcement、额外 Context 成本和 Host-specific 假可移植。Cycle 2 先以教学实现建立可攻击模型，不直接设计产品能力。

## 3. 研究范围与退出条件（Scope and Exit Criteria）

- 范围（Scope）：Primitive trigger、model participation、determinism、state、context boundary、evidence 与 failure route。
- 范围外（Out of Scope）：Claude Code 官方 Runtime、复杂 Skill Evaluation、完整 Context Lifecycle、Adapter 与产品实现。
- 退出条件（Exit Criteria）：完成 Primitive responsibility map；分别执行 `EXP-C02-01` 和 `EXP-C02-02`；登记 `EVD-*`；形成 Mental Model V1；完成 Batch 1 Route Review。

当前 Exit Criteria 未满足。

## 4. 心智模型 V0（Mental Model V0）

- Instruction 通过自然语言影响 Model，不保证 enforcement。
- Permission 在 Action 前决定允许、拒绝或升级。
- Hook 在明确 trigger 上观察、注入、验证或阻断。
- Task State 外置多步进度，只有被后续决策读取时才超出 UI 价值。
- Skill 按需提供程序性知识；discovery、activation 与 execution 是不同阶段。
- Subagent 的候选价值来自 Context / Tool / output boundary，而不只是角色名称。

这是待验证责任模型，不是 Host capability mapping。

## 5. 证据登记（Evidence Registry）

尚未登记 `EVD-*`。Batch 1 内容生成不产生实验结果。

### 已登记来源制品（Registered Source Artifacts）

- [`SRC-FOUNDATION-004`](evidence/SRC-FOUNDATION-004.md): shareAI-lab/learn-claude-code；只作为教学重实现，执行前固定 commit。

该 Source artifact ID 不是 Claude Code 官方 Contract / Runtime Evidence，也不能直接支持 Support Assessment。Registry entry 尚未派生 `EVD-*`。

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

按 `trigger → model participation → action / state effect → evidence → failure route` 比较 Primitive；不按文件名或产品术语推定等价。

## 7. 假设（Hypothesis）

- `H-C02-01`: 显式维护并读取 Task State 会减少 T03 的漏步骤、重复与顺序漂移，但增加状态和 Context 成本。
- `H-C02-02`: 具有明确 Context、Tool 与 output contract 的 Subagent Boundary 会减少 T02 主 Context 的原始读取量；只改变角色 prompt 不会产生同等效果。

## 8. 实验（Experiment）

- `EXP-C02-01`: `COMPARATIVE` · `T03 · Medium Change` · Externalized Task State
- `EXP-C02-02`: `COMPARATIVE` · `T02 · Semantic Review` · Subagent Context Boundary
- 历史映射（Legacy Mapping）：`EXP-W02-01`（历史计划已拆分，尚未执行）
- 运行元数据（Run Metadata）：尚未创建
- 结果（Result）：尚未运行

两个实验必须单独改变主要变量。

## 9. 观察（Observation）

无。研究执行尚未开始。

## 10. 矛盾证据与限制（Contradictory Evidence and Limitations）

- `learn-claude-code` 是教学重实现，不能证明 Claude Code 官方 Runtime architecture 或 lifecycle event。
- 当前没有 Behavior Evidence 证明任何 Primitive 改变了 process 或 outcome。
- Task、Subagent、Host、Provider、Model 或配置 effect 无法分离时，结果必须为 `INCONCLUSIVE`。

## 11. 心智模型 V1（Mental Model V1）

等待实验与证据。

## 12. 设计判断（Design Judgment）

待定。不实现 myharness feature、OpenCode Adapter 或任何 Host Plugin，不分配 S1–S4。

## 13. 开放问题（Open Questions）

执行中发现的旁支问题登记到 [Open Questions](../../open-questions.md)。Host 专项问题转交其冻结 Cycle，不在 Batch 1 展开。

## 14. 路线复盘触发条件（Route Review Trigger）

Cycle 2 Exit Criteria 满足后创建 Batch 1 Route Review；若 Foundation Working Model 被直接 Evidence 推翻，则提前触发并记录原因。
