# Cycle 07 研究笔记（Research Note）· ZCode Host Contract & Enterprise Reality

> 状态（Status）：PLANNED · NOT EXECUTED
>
> 内容 Batch：4

[Cycle 正文](../../../docs/02-Coding-Agent-Host-Model.md) · [研究工作区](../../README.md) · [来源权限（Source Authority）](../../source-authority.md)

## 1. 研究问题（Research Question）

在不借助未验证 Runtime source 的前提下，ZCode 的公开 Contract、绑定版本的 Direct Behavior、local configuration 与部署事实能够分别证明哪些 Host capability 和 enterprise reality，哪些判断必须保持 Unsupported / Unknown？

## 2. 为什么与 myharness 有关

myharness 需要把 ZCode Host surface、Provider / endpoint、Model、Configuration 与组织部署事实分开。否则产品入口、模型效果和企业 policy 会被错误合并成“Host 支持”，Adapter 也可能依赖未经验证的内部实现。

## 3. 研究范围与退出条件（Scope and Exit Criteria）

- 范围（Scope）：官方 product identity 与 Contract；Workspace、Agent、Instruction、Tool、Permission、Review 与 Remote Execution；Provider / Model configuration；绑定版本的无破坏性 Behavior；deployment-specific Enterprise Fact；ZCode Runtime Source Authority Gate。
- 范围外（Out of Scope）：社区逆向、客户端指纹、第三方 patch、未验证 Runtime source、危险权限测试、公开 Model benchmark、ZCode Plugin / Adapter、通用法律合规结论。
- 退出条件（Exit Criteria）：绑定 Host version / platform / release channel；完成 Contract matrix；明确 Gate status；真实执行 `EXP-C07-01` 与 `EXP-C07-02`；只有已完成的配对 Run 无法分离 confounder 时才记录 `INCONCLUSIVE`；分离 Host / Provider / Model / Configuration / deployment effect；至少验证一个真实 `ENT-ZCODE-*` deployment profile；登记 `EVD-*`；形成 Mental Model V1。

当前 Exit Criteria 未满足。

## 4. 心智模型 V0（Mental Model V0）

```text
Official Product Identity + Host Version
        ↓
Host Contract Surface
        ↓
Provider Profile + Model + Endpoint + Authentication
        ↓
Local Configuration + Direct Behavior
        ↓
Deployment-specific Enterprise Fact

Runtime Source ── Gate NOT VERIFIED ──→ Unknown
```

这是待验证责任模型，不构成 ZCode architecture、Behavior、enterprise readiness、安全或合规结论。

## 5. 证据登记（Evidence Registry）

尚未登记 `EVD-*`。Batch 4 内容生成只登记计划来源，不创建 Contract claim、Source claim、Behavior claim、Enterprise Fact 或 Support Assessment。

### 已登记来源制品（Registered Source Artifacts）

- [`SRC-ZCODE-001`](evidence/SRC-ZCODE-001.md)：ZCode 用户协议；产品 / 服务提供者身份与责任边界。
- [`SRC-ZCODE-002`](evidence/SRC-ZCODE-002.md)：ZCode Agent 官方文档；Host-owned Agent / workspace surface。
- [`SRC-ZCODE-003`](evidence/SRC-ZCODE-003.md)：连接模型与套餐；Provider / endpoint / Model / authentication 配置边界。
- [`SRC-ZCODE-004`](evidence/SRC-ZCODE-004.md)：安全操作确认；permission mode 与 confirmation Contract。
- [`SRC-ZCODE-005`](evidence/SRC-ZCODE-005.md)：远程开发；本地 / SSH / container execution location Contract。
- [`SRC-ZCODE-006`](evidence/SRC-ZCODE-006.md)：ZCode 隐私政策；未来 data-handling fact verification 的官方 Contract anchor。
- [`SRC-ZCODE-007`](evidence/SRC-ZCODE-007.md)：版本发布与更新；Host version / release channel anchor。
- [`SRC-ZCODE-008`](evidence/SRC-ZCODE-008.md)：用户反馈与支持；日志导出与 incident / support route anchor。
- [`SRC-ZCODE-009`](evidence/SRC-ZCODE-009.md)：ZCode Agent 交互文档；`AGENTS.md` 项目指令、context attachment 与执行模式 Contract。

所有条目都是浮动官方锚点，执行时必须重新核验访问日期、条款 / 页面版本与对应 Host release。

### 契约证据（Contract Evidence）

尚未登记。

### 源码证据（Source Evidence）

尚未登记，也不得登记。Gate status：

```text
Host: ZCode
Scope: ZCode Agent / desktop and remote Runtime internal architecture
Status: NOT VERIFIED
Authority Evidence IDs: None
Repository and Revision: Unknown
Verified On: Not applicable
Limitations: 官方产品与 Contract 页面未指认满足门禁条件的 Runtime source repository
```

### 行为证据（Behavior Evidence）

尚未登记。

### 项目证据（Project Evidence）

尚未登记。实验 fixture 和 myharness artifacts 只在执行时按 scope 登记。

### 企业事实（Enterprise Fact）

尚未登记。没有组织 / 环境记录时，不创建 `ENT-*`。

### 社区主张（Community Claims）

尚未登记。任何 Runtime repository、逆向或客户端 fingerprint 候选只能更新 [OQ-001](../../open-questions.md)。

## 6. 参考模式（Reference Pattern）

使用 `Product identity → Contract → Provider Profile → Local Configuration → Direct Behavior → Enterprise Fact` 证据链。每一层记录 authority owner、scope、version / revision、可支持判断、不可支持判断与 Unknown，不允许下一层替上一层作答。

## 7. 假设（Hypothesis）

`H-C07-01`：在相同 ZCode version、platform、repository baseline、Stable Task、project instruction、permission mode 与 acceptance checks 下，仅切换已授权的 Provider profile 时，Workspace、Host-side tool exposure / filtering policy 与 decision owner、configured permission / approval route、Review 与 artifact route 的 Host-owned 责任边界应保持一致；actual exposed tool set、Provider / Model 的 tool-calling capability、实际 tool request、输出内容和完成路径可以不同。若 Host-owned control points 稳定随模型通道变化，边界模型被反驳；只有配对 Run 已执行但 Model、endpoint policy、quota 或 configuration drift 仍无法分离时，结果才为 `INCONCLUSIVE`。没有 deployment-specific Enterprise Fact 时，任何结果都不能提升为 enterprise readiness 或 S1–S4。

## 8. 实验（Experiment）

- `EXP-C07-01`：`EXPLORATORY` · `T01 · Engineering Constraint` · Contract → Configuration → Behavior Trace。
- T01 instance：`T01-C07-LOCAL-RETRY-LIMIT-VALIDATION`。在固定 commit 的隔离 fixture repository 中，为已有本地 configuration parser 补充 `retry_limit` 上界验证；只修改冻结的 parser source 与 test file，不改变公开 schema / error type，不访问网络。
- T01 acceptance：覆盖负数、零、允许上界、超过上界与字段缺省；保存本地命令、exit code 与 diff。
- T01 trace：绑定 product / Host version、platform、installation channel、workspace、project instruction、permission mode、Provider profile、Model ID、脱敏 configuration、Host-side tool exposure / filtering policy 与 decision owner、actual exposed tool set、Provider / Model tool-calling capability、实际 tool request / success、confirmation、execution location、Review、artifact 与 human intervention。
- `EXP-C07-02`：`COMPARATIVE` · `T02 · Semantic Review` · Provider Profile Boundary Comparison。
- T02 instance：对固定 commit 中含 acceptance reference 的有限 patch 作审查。Evaluator-only oracle 记录需要推理的“重试状态在成功后未清零”与可由 schema check 确定检出的“新增配置字段未同步到 schema”两个预植入缺陷；oracle 及缺陷名称不得进入 Agent-visible task statement、Rule、context、acceptance reference 或 output schema。两个 profile 的 Agent-visible 输入、permission mode 与 Review procedure 相同。
- T02 variants：两个已授权 Provider profile；优先固定相同 Model ID。每个 profile 至少两个 fresh task Run，顺序交错并从相同 clean baseline 开始。
- 单一主要变量（Primary Variable）：Provider profile。Model ID、endpoint policy、quota 或 tool policy 不一致时登记 confounder，不得声称 Host invariant；只有配对 Run 已完成时才可据此填写 `INCONCLUSIVE`。
- 安全边界（Safety Boundary）：不记录 API Key / token，不测试 bypass，不访问真实业务服务或工作区外路径。
- 运行元数据（Run Metadata）：尚未创建。
- 结果（Result）：尚未运行。
- 历史映射（Legacy Mapping）：无；Cycle 7 是 V4.2 新增 Cycle。

## 9. 观察（Observation）

无。研究执行尚未开始。

## 10. 矛盾证据与限制（Contradictory Evidence and Limitations）

- 官方页面是 Contract anchor，不证明安装版本、配置已启用或 Behavior 已验证。
- 官方条款和文档是浮动页面，执行时必须重新核验；Changelog 与安装版本不匹配时不得拼接结论。
- local configuration 只能证明特定环境配置，不能证明实际生效或其他环境一致。
- Provider、endpoint、authentication、Model、quota 和 policy 任一变化都可能污染 Host effect。
- Contract / Behavior 不一致时分别登记，不使用未验证 source 猜测内部原因。
- 官方产品入口不等于组织批准、审计完备、SLA、私有化、数据驻留或法律合规。
- 如果两个 Provider profile 无法合规取得，`EXP-C07-02` 保持 `PLANNED · NOT EXECUTED`，不得填写 Result，Cycle 退出条件保持未满足。只有配对 Run 已完成但共同 baseline 或 observation artifact 仍不足以分离 effect 时，结果才可为 `INCONCLUSIVE`。

## 11. 心智模型 V1（Mental Model V1）

等待实验与证据。

## 12. 设计判断（Design Judgment）

待定。不实现 ZCode Plugin / Adapter，不分配任何 ZCode 支持等级，不形成 enterprise readiness 或合规结论。

## 13. 开放问题（Open Questions）

Runtime source authority 继续由 [OQ-001](../../open-questions.md) 跟踪。Host / Provider / Model 分层若在真实 Behavior 中失效，新增独立 Open Question；跨 Host portability 转交 Cycle 9。

## 14. 路线复盘触发条件（Route Review Trigger）

Cycle 7 Exit Criteria 满足后创建 Batch 4 Route Review；若新官方材料改变 Source Authority Gate，或 Direct Behavior 推翻 Host / Provider 分层，则提前触发并记录原因。
