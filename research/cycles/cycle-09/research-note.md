# Cycle 09 研究笔记（Research Note）· Four-host Harness Abstraction

> 状态（Status）：PLANNED · NOT EXECUTED
>
> 内容 Batch：6

[Cycle 正文](../../../docs/03-Cross-host-Harness-Abstraction.md) · [研究工作区](../../README.md) · [来源权限（Source Authority）](../../source-authority.md)

## 1. 研究问题（Research Question）

在 Claude Code、Codex、ZCode 与 OpenCode 的绑定版本和运行条件下，哪些 Harness 语义可以形成 Portable Semantic Contract，哪些必须由 Host Adapter 映射、显式降级或保留为 Host-specific Capability / Unsupported / Unknown？

## 2. 为什么与 myharness 有关

myharness 需要共享可复查的工程语义，而不是共享一组看起来相似的文件。Cycle 9 将 Intent、Trigger、Required Context、Procedure、Evidence、Completion 与 Failure Route 从 Host-specific packaging 中分离，并要求 Adapter 显式记录 tool、permission、lifecycle、distribution、state、observability 与 degradation mapping。

## 3. 研究范围与退出条件（Scope and Exit Criteria）

- 范围（Scope）：四宿主 Contract / Source / Behavior readiness；Instruction / Rule、Skill、Tool、Permission、Hook / lifecycle、Agent / Subagent、Plugin / distribution、Session / State 与 Evidence / Completion semantic slice；Portable Contract 与 Host Adapter；V4.1 Week 7 迁移。
- 范围外（Out of Scope）：Host surface parity 假设、ZCode 未验证 Runtime Source、公开 Model benchmark、企业 / 法律结论、完整 myharness Adapter 实现、Cycle 10–18。
- 退出条件（Exit Criteria）：四宿主 readiness map 完整；每个非 Unknown matrix cell 绑定 scoped `EVD-*`；执行 `EXP-C09-01`；`EXP-C09-02` 至少完成两个目标 Host strata 的独立 A / B Result；明确 Direct / Adapted / Degraded / Host-specific / Unsupported / Unknown；形成 Mental Model V1。

当前 Exit Criteria 未满足。内容生成、Source Registry 条目或计划矩阵都不能满足上述条件。

## 4. 心智模型 V0（Mental Model V0）

```text
Task Intent + Project Constraint
        ↓
Portable Semantic Contract
Intent · Trigger · Context · Procedure · Evidence · Completion · Failure
        ↓
Capability Requirement + Mapping Disposition
        ↓
Host Adapter
Discovery · Bootstrap · Tool · Permission · Lifecycle · Distribution
State · Observability · Degradation
        ↓
Host / Surface + Provider Profile + Model + Configuration
        ↓
Direct Behavior + Project Artifact + scoped EVD
```

这是待验证责任模型，不构成任何 Host 的 capability assessment、portability result 或 Support Level。

## 5. 证据登记（Evidence Registry）

尚未登记 `EVD-*`。Batch 6 只登记计划来源并复用 Cycle 3–8 的 Source artifacts，不创建 Contract / Source / Behavior / Project claim 或 Support Assessment。

### 已登记来源制品（Registered Source Artifacts）

- [`SRC-CROSSHOST-001`](evidence/SRC-CROSSHOST-001.md)：Agent Skills Overview；格式身份与 progressive disclosure 概览。
- [`SRC-CROSSHOST-002`](evidence/SRC-CROSSHOST-002.md)：Agent Skills Specification；`SKILL.md` format 与 resource Contract。
- [`SRC-CROSSHOST-003`](evidence/SRC-CROSSHOST-003.md)：Agent Skills client implementor guide；discovery、activation、permission 与 context-management guidance。
- [`SRC-CROSSHOST-004`](evidence/SRC-CROSSHOST-004.md)：Superpowers porting guide 与 canonical repository 浮动锚点。
- [`SRC-CROSSHOST-005`](evidence/SRC-CROSSHOST-005.md)：Open Harness canonical repository；只作为 V4.1 source-role drift 对照。

四宿主官方来源复用 [Cycle 3–4 Claude Code](../cycle-04/research-note.md)、[Cycle 5–6 Codex](../cycle-06/research-note.md)、[Cycle 7 ZCode](../cycle-07/research-note.md) 与 [Cycle 8 OpenCode](../cycle-08/research-note.md) 已登记的 `SRC-*`。复用 Source ID 不会把计划来源提升为 Evidence Claim。

所有页面和默认分支都是浮动锚点。执行时必须重新核验访问日期、Host release 与 project scope；Superpowers / Open Harness 源码必须固定完整 commit、重新定位 path 并限定 claim scope。

### 契约证据（Contract Evidence）

尚未登记。Agent Skills 官方页面、Host 文档和 Superpowers guide 当前只作为计划来源，不是本 Cycle 已裁决 Contract claim。

### 源码证据（Source Evidence）

尚未登记。`SRC-CROSSHOST-004`、`SRC-CROSSHOST-005` 的 commit 均为 `NOT PINNED`。Codex / OpenCode Source claim 仍分别受 Cycle 5–6 / Cycle 8 的 revision 与 provenance gate 约束；ZCode Runtime Source Gate 保持 `NOT VERIFIED`。

### 行为证据（Behavior Evidence）

尚未登记。没有 Host 已通过 Cycle 9 Cross-host Evidence Readiness Gate。

### 项目证据（Project Evidence）

尚未登记。`EXP-C09-02` 执行前必须登记真实 myharness source artifact、revision、source-host baseline 与已知限制。

### 企业事实（Enterprise Fact）

不在 Cycle 9 当前范围内登记。

### 社区主张（Community Claims）

尚未登记。第三方 port、兼容表、目录对照或 issue 只能形成 Open Question，不能证明四宿主 Contract、Behavior 或 Support Level。

## 6. 参考模式（Reference Pattern）

使用 `Portable Semantic Contract → Capability Requirement → Host Adapter → Bound Host / Provider / Model / Configuration → Direct Behavior / Project Artifact` 证据链。Agent Skills 提供 format / lifecycle question，Superpowers 提供一个项目的 porting pattern；两者都必须接受四个 Host 的官方 Contract 与 Direct Behavior 攻击。

V4.1 OpenHarness 的 shared primitive 角色已经成为浮动历史线索。当前仓库定位变化说明 Reference Project 会漂移，因此 Cycle 9 按研究问题选择锚点，不机械寻找旧 `.oh` 路径。

## 7. 假设（Hypothesis）

`H-C09-01 · Semantic Contract Portability`：对同一个已有 myharness semantic-review capability 和固定 T02 instance，在同一目标 Host、Provider、Model、Configuration 与 permission profile 内，相比只搬运 source-host 文件形状和替换显眼 Tool 名的 naive port，先提取 Intent、Trigger、Required Context、Procedure、Evidence、Completion、Failure Route 与 Limitations，再通过显式 Host Adapter 映射的 variant，应减少 Host leakage、silent degradation 与 false completion，并提高 discovery-to-evidence trace 的可解释性；它也可能增加 Adapter、Context、维护和版本绑定成本。

支持、反驳与不确定信号以 [Cycle 正文](../../../docs/03-Cross-host-Harness-Abstraction.md) 的目标 Host 内配对边界和预注册裁决表为准。一个目标 Host 的 Result 不能替代另一个，也不能外推为四宿主普遍结论。

## 8. 实验（Experiment）

- `EXP-C09-01`：`EXPLORATORY` · `T01 · Engineering Constraint` · Four-host Semantic Capability Trace。
- T01 instance：`T01-C09-LOCAL-HTTP-TIMEOUT`。在同一固定 commit 的隔离 fixture 中，为已有本地 HTTP client 增加显式、非默认、可配置 timeout；本地 acceptance 覆盖字段缺省、合法 / 非法配置与 request construction，不访问网络。
- Host strata：Claude Code、Codex、ZCode、OpenCode 各自使用独立 Run Metadata；只研究一个绑定 surface。Provider / Model 不能相同时不比较 outcome quality。
- 观察项：instruction source、Skill state、actual tool set、tool request / result、permission owner / decision、lifecycle、task / session state、acceptance、artifact、human intervention 与 Unknown。
- `EXP-C09-02`：`COMPARATIVE` · `T02 · Semantic Review` · Naive Artifact Port vs Portable Semantic Contract。
- Project artifact gate：必须存在版本可固定、具备 source-host Behavior baseline 的 myharness code-review 或 research-discovery capability；否则保持 `PLANNED · NOT EXECUTED`。
- Baseline A：只做目标 Host 加载需要的最小包装、路径和显眼 Tool 名调整，不故意破坏 artifact。
- Variant B：Capability intent / procedure 保持相同，先写 Portable Semantic Contract，再用 Host Adapter 映射 discovery / bootstrap、action、permission、lifecycle、distribution、state、evidence 与 degradation。
- Source / target derivation：`source_host` 必须是四宿主之一且具备可复查 Behavior baseline；`target_hosts = four_hosts - {source_host}`。默认 Claude 为 source 时，目标为 Codex、ZCode、OpenCode；Route Review 更换 source 时必须同时重算 targets，不得重合、遗漏或引入第五个 Host。
- Target strata：重算后的每个 target Host 独立 A / B Run group、Result 与 scoped `EVD-*`。
- 重复与顺序：每个可执行目标的 A / B 各至少两个 fresh task Run，顺序交错，并固定 task、Host / surface、Provider、Model、Configuration、permission、capability revision 与 acceptance procedure。
- 裁决：首个 Run 前冻结 Contract / Adapter revision 与主要 checkpoint 表；按 `PASS / FAIL / UNKNOWN` 记录 checkpoint，将 Host leakage、silent degradation 与 false completion 记为 critical failure。两个 replication block 必须持续同向且无新增主要退化才能 `SUPPORT`；持续无增益或持续恶化可 `REJECT`；方向不一致、必需项 Unknown 或 confounder 未分离必须 `INCONCLUSIVE`。
- 运行元数据（Run Metadata）：尚未创建。
- 结果（Result）：尚未运行。
- 历史映射（Legacy Mapping）：`EXP-W07-01` → `EXP-C09-02`；`EXP-C09-01` 是新增 readiness prerequisite。

完整计划见 [实验工作区](experiments/README.md)。

## 9. 观察（Observation）

无。研究执行尚未开始。Batch 6 刷新来源时发现 Open Harness 当前公开定位与 V4.1 旧研究角色不同；这里只更新 reference boundary，不把页面观察登记成 `EVD-*` 或项目演进结论。

## 10. 矛盾证据与限制（Contradictory Evidence and Limitations）

- Agent Skills format compatibility 不证明 Host discovery、activation、permission、compaction 或 outcome parity。
- Superpowers 的 porting invariant 是该项目的 reference pattern，不是四个 Host 的官方 Contract，也不自动适用于 myharness。
- Claude Code 未公开 Runtime Source 不应被其他项目实现替代；Codex / OpenCode 默认分支不产生可复现 Source Evidence；ZCode Source Gate 未通过时保持 Unknown。
- Host 内 surface parity 尚未验证；Cycle 9 的每个 Host stratum 只能绑定一个实际 surface。
- Provider、endpoint、Model、Configuration、tool capability、permission 与 Human intervention 可能污染 cross-host comparison。
- format loaded、discovered、activated、procedure executed、evidence produced、completion satisfied 与 task succeeded 必须分开记录。
- 无法取得授权 Host / profile 时使用 `NOT EXECUTED / UNKNOWN`，不是 `UNSUPPORTED`。

## 11. 心智模型 V1（Mental Model V1）

等待实验与证据。

## 12. 设计判断（Design Judgment）

待定。不实现或合并完整 myharness Adapter，不建立四宿主支持总表，不形成公开 Model benchmark、企业或法律结论。

## 13. 开放问题（Open Questions）

Host surface parity、OpenCode provenance / Provider comparability 与 Cycle 9 target comparability 由 [Open Questions](../../open-questions.md) 跟踪。Skill outcome evaluation 转交 Cycle 10，不在本 Cycle 扩张。

## 14. 路线复盘触发条件（Route Review Trigger）

Cycle 9 Exit Criteria 满足后创建 Batch 6 Route Review；如果 Portable Contract 只能通过隐藏关键 Host 差异成立，或 reference project 不再回答核心问题，则提前触发并记录原因。
