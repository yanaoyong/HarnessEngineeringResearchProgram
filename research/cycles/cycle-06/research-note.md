# Cycle 06 研究笔记（Research Note）· Codex Execution、Safety & State

> 状态（Status）：PLANNED · NOT EXECUTED
>
> 内容 Batch：3

[Cycle 正文](../../../docs/02-Coding-Agent-Host-Model.md) · [研究工作区](../../README.md) · [来源权限（Source Authority）](../../source-authority.md)

## 1. 研究问题（Research Question）

在 Codex 的执行链中，Sandbox、Approval、Command Rule、Hook 与执行状态各承担什么责任，Host technical boundary 与 Harness engineering governance 应如何分工而不产生无意义的 Double Block？

## 2. 为什么与 myharness 有关

myharness 必须区分 Host 技术边界、人工授权、项目工程策略和结果验收。否则 pre-execution guard 可能重复 Host 的强制控制，制造 approval noise 与重试；或把 Host 不理解的工程语义错误交给 Sandbox。

## 3. 研究范围与退出条件（Scope and Exit Criteria）

- 范围（Scope）：Rules、Hooks、Sandbox、Approvals 与 Config Contract；固定 revision execution / policy / state source boundary；无破坏性 execution trace 与 hard-deny / guard shadowing 对照。
- 范围外（Out of Scope）：Sandbox bypass、危险命令、secret access、真实破坏、完整 OS implementation、企业合规、myharness guard 修改。
- 退出条件（Exit Criteria）：绑定 Host version / surface / platform 完成 Contract map；固定 `openai/codex` commit；完成绑定真实小型工程修改的 `EXP-C06-01` T01 trace 与 `EXP-C06-02` 配对对照；强制执行 fresh-run State checkpoint；区分 decision owner 与 state owner；登记 `EVD-*`；形成 Mental Model V1。

当前 Exit Criteria 未满足。

## 4. 心智模型 V0（Mental Model V0）

- Sandbox 定义技术可达范围，Approval / Trust 决定何时需要人工授权；两者协作但不是同一控制。
- Command Rule 对 Host-recognized command request 作 policy decision；Project Rule 通过 Instruction 表达工程语义。
- Hook / Harness Guard 可以在 lifecycle point 观察、注入、验证或阻断，但可能与 Sandbox / Rule 重复。
- CI / Acceptance Gate 验证结果，不自动替代前置 trust boundary。
- Execution State 必须拆成 request、decision、approval、result、retry、session state、persistent config / trust 与实验 Artifact，不能统称为一个 state。

这是待验证责任模型，不构成安全保证、平台结论或 Codex capability assessment。

## 5. 证据登记（Evidence Registry）

尚未登记 `EVD-*`。Batch 3 内容生成不建立任何安全结论、Behavior claim 或 Support Assessment。

### 已登记来源制品（Registered Source Artifacts）

- [`SRC-CODEX-005`](../cycle-05/evidence/SRC-CODEX-005.md)：`openai/codex` official source repository；执行前固定 commit。
- [`SRC-CODEX-006`](evidence/SRC-CODEX-006.md)：Codex official docs · Rules。
- [`SRC-CODEX-007`](evidence/SRC-CODEX-007.md)：Codex official docs · Sandbox。
- [`SRC-CODEX-008`](evidence/SRC-CODEX-008.md)：Codex official docs · Agent approvals & security。
- [`SRC-CODEX-009`](evidence/SRC-CODEX-009.md)：Codex official docs · Hooks。
- [`SRC-CODEX-010`](evidence/SRC-CODEX-010.md)：Codex official docs · Config basics。

所有官方页面都是执行时绑定 Codex version / surface / platform 并重新核验的浮动锚点。`SRC-CODEX-005` 当前没有固定 commit，不产生 Source Evidence。

### 契约证据（Contract Evidence）

尚未登记。

### 源码证据（Source Evidence）

尚未登记。执行时只跟 execution、policy、sandbox、hook 与 state 的已声明问题，并记录 source path 与 stop point。

### 行为证据（Behavior Evidence）

尚未登记。

### 项目证据（Project Evidence）

尚未登记。myharness pre-execution artifacts 只列为未来只读 mapping 对象。

### 企业事实（Enterprise Fact）

尚未登记。

### 社区主张（Community Claims）

尚未登记。

## 6. 参考模式（Reference Pattern）

按 `request → active configuration → policy match → approval / trust → sandbox / hook → result → retry / stop → acceptance` 记录每次执行，并为每个 decision 标记 owner、reason、state scope 与 Evidence artifact。

## 7. 假设（Hypothesis）

`H-C06-01`：对同一个能够产生隔离、可逆 marker effect 且预先配置为触发 Host hard-deny 的 T01 acceptance command，在相同 Sandbox / Approval / Rule baseline 上再增加覆盖同一 command 与语义范围的 Harness pre-execution deny，不会增加已阻止的 marker effect；两个 hard-deny 也不预设为可同时观察，而应按实际 lifecycle order 分类为 Host-shadowed、Harness-shadowed、sequentially observable 或 unknown。只有 Harness 层提供 Host 层无法表达的项目语义或 Evidence 时，重叠才可能有净价值。

## 8. 实验（Experiment）

- `EXP-C06-01`：`EXPLORATORY` · `OBSERVATION_ONLY` · `T01 · Engineering Constraint` · Non-destructive Execution Boundary Trace。
- `EXP-C06-02`：`COMPARATIVE` · `T01 · Engineering Constraint` · Host hard-deny baseline 与语义重复 Harness guard 的 shadowing comparison。
- 共同 T01 instance：`T01-C06-LOCAL-TIMEOUT-VALIDATION`。在固定 commit 的隔离 fixture repository 中扩展已有本地 config parser，使 `timeout_ms <= 0` 返回既有 validation error，同时保持正值与缺省行为；只修改冻结的 parser source 与对应 test file，不改变公开 schema / error type，不访问网络，acceptance checks 覆盖负数、零、正数与字段缺省。
- 共同 fixture：受挑战的本地 acceptance command 在 control preflight 中会先向隔离实验目录写入内容固定、初始 absent 且可清理的 marker，再运行本地检查；Host hard-deny 必须稳定阻止该 marker，否则 `EXP-C06-01` Observation Outcome 为 `INVALIDATED`，`EXP-C06-02` Result 为 `INCONCLUSIVE`。
- 单一主要变量（Primary Variable）：`EXP-C06-02` 只改变是否增加语义重复的 Harness pre-execution guard。
- 顺序判定（Ordering Classification）：`HOST_SHADOWS_HARNESS / HARNESS_SHADOWS_HOST / SEQUENTIALLY_OBSERVABLE / UNKNOWN`；只看到一次 deny 时不得写成 Double Block。
- State checkpoint：`EXP-C06-01` 在同 Session trace 后必须清理 marker，并以同一 repository commit、task instance 与 configuration snapshot 启动 fresh run，分开观察 conversation / turn state、persistent config / trust 与实验 Artifact。
- Recovery boundary：每个被阻断 variant 只观察一次受挑战 command；随后由预声明 Human intervention 应用相同 recovery profile 完成同一 acceptance checks，不允许 Agent 通过等价命令绕过 policy。
- 历史映射（Legacy Mapping）：`EXP-W06-01`（拆分为两个新设计，仅为历史计划）
- 运行元数据（Run Metadata）：尚未创建
- Outcome / Result：均尚未运行；`EXP-C06-01` 执行后记录 Observation Outcome，Experiment Result 为 `NOT APPLICABLE · OBSERVATION ONLY`；`EXP-C06-02` 才填写 Hypothesis Result

marker 只提供安全、可观察的工作区效果，不代表真实安全影响。不得为了触发安全机制而扩大权限、访问 secret、依赖真实网络副作用或执行危险命令。

## 9. 观察（Observation）

无。研究执行尚未开始。

## 10. 矛盾证据与限制（Contradictory Evidence and Limitations）

- 官方文档可映射公开 control surface，不能证明本地 configuration 或实际 decision order。
- 平台、Codex surface、sandbox profile、approval policy 与 trust state 未绑定时，观察不可比较。
- Hook、Rule 与 Sandbox 的语义范围不相同时，不能把多个阻断都解释为 Double Block。
- fixture 无法在 control preflight 写入 marker、无法稳定触发 Host hard-deny、marker 初始状态不一致，或 decision owner / lifecycle order 无法区分时，结果必须为 `INCONCLUSIVE`。
- Host hard-deny 或 Harness hard-deny 使后续层不可达时，应记录 shadowing，不得推断未执行层也做出了 decision。
- 本 Cycle 不形成普遍安全保证或法律合规结论。

## 11. 心智模型 V1（Mental Model V1）

等待实验与证据。

## 12. 设计判断（Design Judgment）

待定。不修改 myharness guard，不实现 Codex Adapter，不分配任何 Codex 支持等级。

## 13. 开放问题（Open Questions）

执行中发现的旁支问题登记到 [Open Questions](../../open-questions.md)。跨 Host safety mapping 转交 Cycle 9，企业约束分别进入对应 Host 的 Enterprise research。

## 14. 路线复盘触发条件（Route Review Trigger）

Cycle 6 Exit Criteria 满足后创建 Batch 3 Route Review；若无破坏性 Behavior Evidence 推翻当前 responsibility map，则提前触发并记录原因。
