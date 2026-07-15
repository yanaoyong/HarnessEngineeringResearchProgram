# Cycle 07 研究笔记（Research Note）· Qwen Code Host Architecture & Enterprise Reality

> 状态（Status）：PLANNED · NOT EXECUTED
>
> 内容 Batch：4 · V4.3 Host-set replacement

[Cycle 正文](../../../docs/02-Coding-Agent-Host-Model.md) · [V4.3 Amendment](../../../docs/10-V4.3-Qwen-Code-Host-Amendment.md) · [来源权限（Source Authority）](../../source-authority.md)

## 1. 研究问题（Research Question）

在绑定 Qwen Code 版本、surface 与官方源码 revision 后，哪些 Harness 语义由 Host 保持，哪些依赖 Provider、endpoint / protocol、Model 或 Configuration；哪些部署事实足以支持 enterprise reality，哪些仍必须保持 Unsupported / Unknown？

## 2. 为什么与 myharness 有关

myharness 需要把 Qwen Code Host surface、official source、Provider / endpoint、Model、Configuration 与组织部署事实分开。否则 Qwen-first integration、多协议支持、模型输出和企业 policy 会被错误合并成“Host 支持”，Adapter 也可能依赖浮动源码或未经验证的 surface parity。

## 3. 研究范围与退出条件（Scope and Exit Criteria）

- 范围（Scope）：official Contract；`QWEN.md` / memory、Session、Tool、Approval、Sandbox、Hook、Skill、Subagent、Extension；`QwenLM/qwen-code` bounded source reading；Provider / Model configuration；无破坏性 Direct Behavior；deployment-specific Enterprise Fact。
- 范围外（Out of Scope）：公开 Model benchmark、协议兼容即 portability、浮动默认分支即部署实现、危险权限测试、Qwen Code Adapter 实现、通用 enterprise / legal conclusion。
- 退出条件（Exit Criteria）：绑定 Host / surface / release；固定 official source commit 与 execution-artifact provenance；完成 Contract matrix；真实执行 `EXP-C07-01` / `EXP-C07-02`；分离 Host / Provider / endpoint / Model / Configuration / deployment effect；至少验证一个 `ENT-QWENCODE-*` profile；登记 scoped `EVD-*`；形成 Mental Model V1。

当前 Exit Criteria 未满足。

## 4. 心智模型 V0（Mental Model V0）

```text
Official Contract + Bound Qwen Code Version / Surface
        ↓
Pinned QwenLM/qwen-code Revision + Capability Map
        ↓
Host Runtime Surface
QWEN.md / Memory · Session · Tool · Approval · Sandbox
Hook · Skill · Subagent · Extension
        ↓
Provider / Endpoint / Protocol + Model + Configuration
        ↓
Direct Behavior + Project Artifact + Enterprise Fact
```

这是待验证责任模型，不构成 Qwen Code architecture、Behavior、enterprise readiness、安全或合规结论。

## 5. 证据登记（Evidence Registry）

尚未登记 `EVD-*`。V4.3 Host 替换只登记计划来源，不创建 Contract / Source / Behavior claim、Enterprise Fact 或 Support Assessment。

### 已登记来源制品（Registered Source Artifacts）

- [`SRC-QWENCODE-001`](evidence/SRC-QWENCODE-001.md)：Qwen Code Overview 与 installation / product surface。
- [`SRC-QWENCODE-002`](evidence/SRC-QWENCODE-002.md)：Settings 与 configuration precedence。
- [`SRC-QWENCODE-003`](evidence/SRC-QWENCODE-003.md)：Model Providers 与 protocol / routing / Model boundary。
- [`SRC-QWENCODE-004`](evidence/SRC-QWENCODE-004.md)：Memory、`QWEN.md` 与跨 Session knowledge surface。
- [`SRC-QWENCODE-005`](evidence/SRC-QWENCODE-005.md)：Approval Mode 与 tool decision surface。
- [`SRC-QWENCODE-006`](evidence/SRC-QWENCODE-006.md)：Sandbox Contract。
- [`SRC-QWENCODE-007`](evidence/SRC-QWENCODE-007.md)：Hooks lifecycle Contract。
- [`SRC-QWENCODE-008`](evidence/SRC-QWENCODE-008.md)：Agent Skills discovery / activation Contract。
- [`SRC-QWENCODE-009`](evidence/SRC-QWENCODE-009.md)：Subagents boundary Contract。
- [`SRC-QWENCODE-010`](evidence/SRC-QWENCODE-010.md)：Extensions packaging / distribution Contract。
- [`SRC-QWENCODE-011`](evidence/SRC-QWENCODE-011.md)：Official architecture overview。
- [`SRC-QWENCODE-012`](evidence/SRC-QWENCODE-012.md)：`QwenLM/qwen-code` official repository 与 releases。
- [`SRC-QWENCODE-013`](evidence/SRC-QWENCODE-013.md)：Qwen Code official releases / artifact provenance anchor。

所有官方页面、release 列表与默认分支都是浮动 anchor；执行时必须重新核验访问日期、Host version、完整 source commit 与 artifact provenance。

### 契约证据（Contract Evidence）

尚未登记。

### 源码证据（Source Evidence）

尚未登记。当前 verification status：

```text
Host: Qwen Code
Scope: CLI Runtime and explicitly bound surfaces
Repository Identity: VERIFIED
Repository: https://github.com/QwenLM/qwen-code
Pinned Revision: NOT PINNED
Execution Artifact Provenance: NOT VERIFIED
Authority Basis: official QwenLM organization, official docs link, releases and repository license
```

官方仓库身份已核验，不等于默认分支已成为 revision-bound Source Evidence。

### 行为证据（Behavior Evidence）

尚未登记。

### 项目证据（Project Evidence）

尚未登记。实验 fixture 和 myharness artifacts 只在执行时按 scope 登记。

### 企业事实（Enterprise Fact）

尚未登记。没有组织 / 环境记录时，不创建 `ENT-*`。

### 社区主张（Community Claims）

尚未登记。非官方 fork、体验排名或未绑定版本的产品比较只能创建 Open Question。

## 6. 参考模式（Reference Pattern）

使用 `Contract → pinned Official Source → Provider / Model Profile → Direct Behavior → Project / Enterprise Fact` 证据链。Qwen Code 与 OpenCode 都能研究多 Provider，但前者聚焦 Qwen / 国内模型生态与组织部署事实，后者聚焦 vendor-neutral portability；角色差异不是能力高低结论。

## 7. 假设（Hypothesis）

`H-C07-01`：在相同 Qwen Code version / surface、platform、repository baseline、task、instruction、permission 与 acceptance 条件下，只切换通过 comparability gate 的 Provider profile / endpoint route 时，Host-owned configuration resolution、instruction / memory source、tool exposure policy 与 decision owner、approval / sandbox、Review 与 artifact route 应保持一致；Provider transform、protocol acceptance、actual tool request、reasoning、retry 与 completion path 可以不同。

支持信号是 Host-owned route 在配对 Run 中保持一致，差异可限定到 Provider / endpoint / Model；反驳信号是只改变 Provider profile 后 Host-owned semantic 稳定变化；无法核验相同 Model identity、protocol、limit 或 routing 时不启动实验，而不是事后填写 `INCONCLUSIVE`。

## 8. 实验（Experiment）

- `EXP-C07-01`：`EXPLORATORY` · `OBSERVATION_ONLY` · `T01 · Engineering Constraint` · Contract → Source → Configuration → Behavior Trace。
- T01 instance：`T01-C07-LOCAL-RETRY-LIMIT-VALIDATION`。在固定 commit 的隔离 fixture 中补充 `retry_limit` 上界验证；本地 acceptance 覆盖负数、零、允许上界、超过上界与字段缺省，不访问网络。
- Trace：绑定 Qwen Code version / surface、installation artifact、official source commit / provenance、`QWEN.md` / memory、approval / sandbox、Hook / Skill / Subagent / Extension state、Provider、Model、脱敏 Configuration、tool request / result、Review、artifact 与 Human intervention。
- `EXP-C07-02`：`COMPARATIVE` · `T02 · Semantic Review` · Provider Profile Boundary Comparison。
- T02 instance：固定 patch、Agent-visible input、evaluator-only oracle 与 review procedure；oracle 含一个语义缺陷和一个 deterministic defect，不向 Agent 泄漏答案。
- Variants：两个已授权 Provider profile，必须核验相同 Model identity / revision 与 capability preflight，只改变 Provider / endpoint route；每个 profile 至少两个 fresh-task Run，顺序交错。
- Gate：Model identity、tool protocol、context / output limit、quota 或 routing 不能保持可比时，`EXP-C07-02` 保持 `PLANNED · NOT EXECUTED`；只有配对 Run 已完成而残余 confounder 仍不可分时才可填写 `INCONCLUSIVE`。
- 运行元数据（Run Metadata）：尚未创建。
- Outcome / Result：均尚未运行；`EXP-C07-01` 使用 Observation Outcome，`EXP-C07-02` 才填写 Hypothesis Result。
- 历史映射（Legacy Mapping）：无；Cycle 7 在 V4.3 替换 Host，但没有旧 Run / Result / `EVD-*` 需要迁移。

完整计划见 [实验工作区](experiments/README.md)。

## 9. 观察（Observation）

无。官方仓库身份与文档入口的核验只用于制定来源边界，不登记为本计划的 `EVD-*` 或 Behavior result。

## 10. 矛盾证据与限制（Contradictory Evidence and Limitations）

- 官方页面是 Contract anchor，不证明当前安装配置已启用或 Behavior 已验证。
- 官方 architecture overview 与默认分支不替代 pinned Source Evidence。
- Source commit 无 execution-artifact provenance 时，不解释安装 Behavior。
- Qwen Code Host、Qwen Model、Alibaba Cloud Provider、compatible endpoint 与 local Configuration 必须分开。
- Skills / Hooks / Extensions 文件存在或被列出，不等于被激活、执行或改善 outcome。
- 官方开源、Sandbox 或 telemetry settings 不等于组织批准、SLA、审计完备、数据驻留或法律合规。

## 11. 心智模型 V1（Mental Model V1）

等待实验与证据。

## 12. 设计判断（Design Judgment）

待定。不实现 Qwen Code Adapter，不分配任何 Qwen Code 支持等级，不形成 enterprise readiness、产品排名或合规结论。

## 13. 开放问题（Open Questions）

Qwen Code artifact-to-source provenance 与 Provider comparability 由 [Open Questions](../../open-questions.md) 跟踪。跨 Host portability 转交 Cycle 9。

## 14. 路线复盘触发条件（Route Review Trigger）

Cycle 7 Exit Criteria 满足后创建 Route Review；若 official repository identity / license 变化、artifact provenance 无法建立，或 Direct Behavior 推翻 Host / Provider 分层，则提前触发并记录原因。
