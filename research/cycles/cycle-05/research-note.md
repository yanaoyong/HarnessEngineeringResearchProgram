# Cycle 05 研究笔记（Research Note）· Codex Architecture & Customization

> 状态（Status）：PLANNED · NOT EXECUTED
>
> 内容 Batch：3

[Cycle 正文](../../../docs/02-Coding-Agent-Host-Model.md) · [研究工作区](../../README.md) · [来源权限（Source Authority）](../../source-authority.md)

## 1. 研究问题（Research Question）

Codex 如何通过公开 customization surface 与特定 revision 的实现组织项目指导、可复用能力和扩展边界，myharness 应依赖哪些 Stable Surface 而不是 Implementation Detail？

## 2. 为什么与 myharness 有关

Codex 的源码可见性为架构研究提供了额外视角，但源码路径不是自动稳定的 Contract。只有分别记录官方文档、固定 revision 源码和绑定条件的 Behavior，myharness 才能避免把 AGENTS.md、Skill、MCP、Subagent、Hook 与 Plugin 混为一谈，或让 Adapter 依赖短寿命 implementation detail。

## 3. 研究范围与退出条件（Scope and Exit Criteria）

- 范围（Scope）：Codex customization Contract、question-driven official source reading、surface discovery / load / trigger / distribution，以及 Skill description discovery 对照。
- 范围外（Out of Scope）：完整仓库漫游、TUI / network client、跨 Host portability、完整 Skill outcome eval、myharness Plugin / Adapter 实现。
- 退出条件（Exit Criteria）：绑定 Codex version 完成 Contract map；固定 `openai/codex` commit；完成 `EXP-C05-01` T03 trace、`EXP-C05-02` Skill description 对照、`EXP-C05-03` AGENTS hierarchy 对照与 `EXP-C05-04` Plugin load 对照；登记 `EVD-*`；形成区分 Stable Surface / Implementation Detail / Unknown 的 Mental Model V1。

当前 Exit Criteria 未满足。

## 4. 心智模型 V0（Mental Model V0）

- AGENTS.md 是有 scope 与 precedence 的持久项目指导候选，不等于确定性 enforcement。
- Skill 具有 metadata discovery 与 full instructions loading 两个阶段；被列出或加载不等于 procedure 或 outcome 有效。
- MCP 提供 external tool / system connection，Subagent 提供 responsibility / Context / Tool boundary。
- Hook 提供 lifecycle extension；Plugin 提供 Host-specific packaging / distribution，可以包含 Skill、Hook 或 MCP-backed app 等 artifact。
- Official Contract、verified Source revision 与 Direct Behavior 是三种不同真相层，不能相互替代。

这是待验证 Mental Model，不是 Codex Runtime architecture 或 capability assessment。

## 5. 证据登记（Evidence Registry）

尚未登记 `EVD-*`。Batch 3 内容生成不产生 Contract claim、Source claim、Behavior claim 或 Support Assessment。

### 已登记来源制品（Registered Source Artifacts）

- [`SRC-CODEX-001`](evidence/SRC-CODEX-001.md)：Codex official docs · Customization overview。
- [`SRC-CODEX-002`](evidence/SRC-CODEX-002.md)：Codex official docs · Custom instructions with AGENTS.md。
- [`SRC-CODEX-003`](evidence/SRC-CODEX-003.md)：Codex official docs · Build skills。
- [`SRC-CODEX-004`](evidence/SRC-CODEX-004.md)：Codex official docs · Build plugins。
- [`SRC-CODEX-005`](evidence/SRC-CODEX-005.md)：`openai/codex` official source repository；执行前固定 commit。
- [`SRC-CODEX-009`](../cycle-06/evidence/SRC-CODEX-009.md)：Codex official docs · Hooks；Cycle 5 只使用其公开 customization boundary。
- [`SRC-CODEX-010`](../cycle-06/evidence/SRC-CODEX-010.md)：Codex official docs · Config basics。

官方页面与默认分支均是执行时重新核验的浮动锚点。`SRC-CODEX-005` 的官方仓库身份与“已固定可复现 revision”是两件不同的事；当前 commit 为 `NOT PINNED`，不能派生 Source Evidence。

### 契约证据（Contract Evidence）

尚未登记。

### 源码证据（Source Evidence）

尚未登记。执行时必须固定 `openai/codex` 完整 commit、source path、scope 与 stop point。

### 行为证据（Behavior Evidence）

尚未登记。

### 项目证据（Project Evidence）

尚未登记。

### 企业事实（Enterprise Fact）

尚未登记。

### 社区主张（Community Claims）

尚未登记。

## 6. 参考模式（Reference Pattern）

按 `public contract → fixed source boundary → bound behavior → agreement / conflict / unknown → adapter dependency judgment` 研究每项 capability；source path 只作为特定 revision 的解释材料，不自动进入 Portable Semantic Contract。

## 7. 假设（Hypothesis）

`H-C05-01`：在相同 Codex、Provider、Model、Configuration、T02 instance、Skill body、name、scope 与 location 下，边界清晰、前置关键触发词的 description 比刻意模糊的 description 更容易被正确发现并激活；description 不单独保证 procedure adherence 或 review outcome。

`H-C05-02`：在相同 T01 fixture、root `AGENTS.md` 与运行条件下，增加只适用于目标子目录的 nested `AGENTS.md`，只应改变 target scope 的 Instruction 组合与行为，不应影响 control scope。

`H-C05-03`：对同一 T02 instance 和同一现有 Codex Plugin capability，启用 Plugin distribution 应改变可发现性或加载路径；installed、listed 或 artifact present 不能单独证明 activation、execution 或 outcome。

## 8. 实验（Experiment）

- `EXP-C05-01`：`EXPLORATORY` · `T03 · Medium Change` · Contract → Source → Behavior Architecture Trace。
- `EXP-C05-02`：`COMPARATIVE` · `T02 · Semantic Review` · Skill body 相同、只改变 description 的 discovery / activation comparison。
- `EXP-C05-03`：`COMPARATIVE` · `T01 · Engineering Constraint` · root-only 与 nested `AGENTS.md` 的 target / control scope comparison。
- `EXP-C05-04`：`COMPARATIVE` · `T02 · Semantic Review` · 同一现有 Plugin revision 的 disabled / enabled distribution and load comparison。
- 单一主要变量（Primary Variable）：`EXP-C05-02` 只改变 Skill description，不显式点名 Skill。
- 单一主要变量（Primary Variable）：`EXP-C05-03` 只改变 nested `AGENTS.md` 是否存在；task、root instruction、target / control fixture 与 acceptance checks 相同。
- 单一主要变量（Primary Variable）：`EXP-C05-04` 只改变固定 Plugin revision 是否启用；不得同时修改 capability body 或显式点名 Plugin。
- 固定边界（Fixed Boundary）：`EXP-C05-02` 主要裁决 discovery / activation，不承担 Cycle 10 的完整 Skill behavior evaluation。
- 固定边界（Fixed Boundary）：`EXP-C05-04` 只能使用无需修改的既有 myharness Codex Plugin capability；若不存在，保持 `NOT EXECUTED`，不得为完成迁移而实现 Plugin。
- 历史映射（Legacy Mapping）：`EXP-W05-01`（拆分为四个新设计，仅为历史计划）
- 运行元数据（Run Metadata）：尚未创建
- 结果（Result）：尚未运行

`EXP-C05-01` 只产生 architecture question map 与候选 claim，不能替代 `EXP-C05-02`–`EXP-C05-04` 的受控对照，也不能由一次 trace 宣称完整 Codex architecture。

## 9. 观察（Observation）

无。研究执行尚未开始。

## 10. 矛盾证据与限制（Contradictory Evidence and Limitations）

- 当前官方页面是浮动锚点，执行时必须绑定 Codex version、surface 与访问日期。
- 默认分支不是固定 Source Evidence；源码存在不证明当前安装版本采用、启用或公开承诺该实现。
- CLI、IDE、desktop 与 cloud surface 可能不同，未分离时保持 Unknown。
- Host、Provider、Model、task wording、skill budget 或 explicit invocation effect 无法分离时，结果必须为 `INCONCLUSIVE`。
- AGENTS target / control scope、工作目录或 instruction chain 未绑定时，不得形成 hierarchy / override Behavior claim。
- Plugin capability、revision、安装位置或显式调用同时变化时，不得把差异归因于 distribution；没有符合边界的既有 capability 时保持 `NOT EXECUTED`。

## 11. 心智模型 V1（Mental Model V1）

等待实验与证据。

## 12. 设计判断（Design Judgment）

待定。不实现 myharness Codex Plugin / Adapter，不分配任何 Codex 支持等级。

## 13. 开放问题（Open Questions）

执行中发现的旁支问题登记到 [Open Questions](../../open-questions.md)。跨 Host mapping 转交 Cycle 9，完整 Skill outcome evaluation 转交 Cycle 10。

## 14. 路线复盘触发条件（Route Review Trigger）

完成 Cycle 6 后，或 Contract / Source / Behavior 冲突足以推翻 Codex Host 工作模型时触发。
