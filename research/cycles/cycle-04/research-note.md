# Cycle 04 研究笔记（Research Note）· Claude Code Extension & Control Surface

> 状态（Status）：PLANNED · NOT EXECUTED
>
> 内容 Batch：2

[Cycle 正文](../../../docs/02-Coding-Agent-Host-Model.md) · [研究工作区](../../README.md) · [来源权限（Source Authority）](../../source-authority.md)

## 1. 研究问题（Research Question）

在 Claude Code 的公开 Contract 中，同一个工程要求应由 CLAUDE.md / Rules、Skill、Hook、Subagent、MCP 还是 Plugin 承担，如何验证它被加载、触发、执行并产生预期治理效果？

## 2. 为什么与 myharness 有关

只有区分 model-mediated guidance、lifecycle trigger、Context isolation、external tool connection 与 packaging，myharness 才能避免职责重叠、错误 enforcement 和 Host-specific 假可移植。

## 3. 研究范围与退出条件（Scope and Exit Criteria）

- 范围（Scope）：Claude Code extension / control surface Contract、load / trigger / visibility / determinism / Context cost / distribution，以及 Rule、Skill、Check 的 T01 对照。
- 范围外（Out of Scope）：未公开 Runtime source、完整 MCP ecosystem、enterprise deployment、跨 Host Adapter 与产品实现。
- 退出条件（Exit Criteria）：绑定 Host version 完成 surface map；执行 `EXP-C04-01` A/B/C；登记 Contract / Behavior / Project `EVD-*`；形成 Mental Model V1；完成 Batch 2 Route Review。

当前 Exit Criteria 未满足。

## 4. 心智模型 V0（Mental Model V0）

- CLAUDE.md / Rules 承担 always-on 或 path-scoped instruction，不等于 deterministic enforcement。
- Skill 承担按需程序性知识；discovery、load、execution 与 outcome 是不同阶段。
- Hook 在 lifecycle trigger 上执行逻辑，但 prompt / agent hook 的判断仍可能 model-mediated。
- Subagent 的候选价值来自独立 Context / Tool / result boundary。
- MCP 提供 external tool / data connection，不自动提供正确 workflow。
- Plugin 是 Host-specific packaging / distribution layer，不等于 Portable Semantic Contract。

这是待验证责任模型，不是 Claude Code capability assessment。

## 5. 证据登记（Evidence Registry）

尚未登记 `EVD-*`。Batch 2 内容生成不建立任何 Host support result。

### 已登记来源制品（Registered Source Artifacts）

- [`SRC-CLAUDE-003`](../cycle-03/evidence/SRC-CLAUDE-003.md)：Memory / CLAUDE.md / Rules 的官方浮动 Contract 锚点。
- [`SRC-CLAUDE-007`](evidence/SRC-CLAUDE-007.md)：Claude Code official docs · Extend Claude Code。
- [`SRC-CLAUDE-008`](evidence/SRC-CLAUDE-008.md)：Claude Code official docs · Hooks reference。
- [`SRC-CLAUDE-009`](evidence/SRC-CLAUDE-009.md)：Claude Code official docs · Create custom subagents。
- [`SRC-CLAUDE-010`](evidence/SRC-CLAUDE-010.md)：Claude Code official docs · Create plugins。

上述官方页面是计划执行时重新核验的浮动锚点。Skills 与 MCP 的专项页面从 `SRC-CLAUDE-007` 在执行时重新定位；当前 URL shape 不视为永久 Contract。

### 契约证据（Contract Evidence）

尚未登记。

### 源码证据（Source Evidence）

尚未登记。Batch 2 不主张 Claude Code 官方 Runtime source architecture。

### 行为证据（Behavior Evidence）

尚未登记。

### 项目证据（Project Evidence）

尚未登记。myharness Claude artifacts 只列为未来只读 mapping 对象。

### 企业事实（Enterprise Fact）

尚未登记。

### 社区主张（Community Claims）

尚未登记。

## 6. 参考模式（Reference Pattern）

按 `intent → load timing → trigger owner → model visibility → action / block → evidence → distribution → failure route` 比较 surface，不按文件名或产品术语推定职责。

## 7. 假设（Hypothesis）

`H-C04-01`：对同一 T01「新增或修改的 HTTP client 必须显式设置非默认、可配置 timeout」约束，Rule-only 能影响首次选择但不能保证检测；在共享 Rule baseline 上增加 Skill 可能改善实现步骤与自检，在同一 acceptance contract 上增加 deterministic Check 可能改善违规发现的一致性，同时各自引入 Context、误报或维护成本。

## 8. 实验（Experiment）

- 实验 ID（Experiment ID）：`EXP-C04-01`
- 实验类型（Experiment Type）：`COMPARATIVE`
- 任务套件 ID（Task Suite ID）：`T01 · Engineering Constraint`
- 历史映射（Legacy Mapping）：`EXP-W04-01`（仅为历史计划）
- 共同 Acceptance Contract：新增或修改的目标 HTTP client 必须显式传入非默认、可配置 timeout；同一测试或静态 fixture 对 A/B/C 作出 pass / fail
- 共同基线（Shared Baseline）：A · 只用 Rule 表达 timeout contract
- 变体（Variants）：B · Rule + 只教授相同 timeout contract 的 Skill；C · Rule + 对相同 timeout contract 判定 pass / fail 的 deterministic Check
- 运行元数据（Run Metadata）：尚未创建
- 结果（Result）：尚未运行

可选 D 只有 A/B/C 不能解释 interaction effect 时才执行。每个 variant 使用独立 Run Metadata。Fallback / degradation 不进入本实验，作为独立语义问题保留。

## 9. 观察（Observation）

无。研究执行尚未开始。

## 10. 矛盾证据与限制（Contradictory Evidence and Limitations）

- 官方 Contract page 不证明本地 configuration 已加载或 behavior 有效。
- myharness artifact 存在不等于 capability 被执行或改善结果。
- Skill、Check、Host、Provider、Model、Rule revision 与 task instance 无法分离时，结果必须为 `INCONCLUSIVE`。
- 小样本只用于方向性比较，不是公开 benchmark。

## 11. 心智模型 V1（Mental Model V1）

等待实验与证据。

## 12. 设计判断（Design Judgment）

待定。不重构 myharness Claude extension，不实现 Adapter，不分配 S1–S4。

## 13. 开放问题（Open Questions）

执行中发现的旁支问题登记到 [Open Questions](../../open-questions.md)。跨 Host 语义映射问题转交 Cycle 9。

## 14. 路线复盘触发条件（Route Review Trigger）

Cycle 4 Exit Criteria 满足后创建 Batch 2 Route Review；若 Direct Behavior Evidence 推翻当前 responsibility map，则提前触发并记录原因。
