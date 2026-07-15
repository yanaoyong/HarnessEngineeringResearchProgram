# Evidence Classification and Source Authority

> Status: FROZEN IN BATCH 0

[返回 Research Workspace](README.md) · [公共术语](../docs/09-V4.2-Glossary.md) · [Source Registry Template](templates/source-registry.template.md)

## 1. Evidence Classes

| Class | What it can establish | What it cannot establish by itself |
|---|---|---|
| Contract Evidence | 官方承诺的 surface、行为边界、版本或 release information | 未公开内部实现、实际部署行为 |
| Source Evidence | 已验证 revision 中的实现和内部 boundary | 所有版本行为、部署配置、未来 Contract |
| Behavior Evidence | 绑定运行条件下实际观察到的行为 | 未观察路径、内部实现原因、普遍行为 |
| Project Evidence | 问题在目标项目中的存在、影响和维护事实 | Host 官方能力或跨项目普遍结论 |
| Enterprise Fact | 特定组织和部署环境中的可验证事实 | 官方架构、普遍企业现实、法律合规 |
| Community Claim | 值得调查的线索或反例候选 | 官方 Contract、Architecture、Support Level |

Mental Model、Hypothesis、Reference Pattern 和推断必须与 Evidence 分开记录。

## 2. Traceability IDs and Registry Rules

V4.2 使用三层引用关系：

```text
Evidence-bearing Artifact
SRC-* / Run ID / Experiment ID / Project Artifact / Enterprise Fact ID
        ↓
Evidence Claim
EVD-*
        ↓
Support Assessment
SUP-*
```

- Artifact ID 定位可以复查的原始材料或执行记录。
- Evidence ID 定位一个有明确 scope、支持材料和限制的可引用 claim。
- Support Assessment 只能引用 `EVD-*`，不能只引用裸 URL、Source ID、Run ID 或文件路径。
- 一个 Evidence Claim 可以引用多个 Artifact；一个 Artifact 也可以支持或反驳多个 Evidence Claim。
- ID 只提供可追溯性，不提升证据强度。

### Source IDs

每个外部来源分配稳定 Source ID：

```text
SRC-CLAUDE-001
SRC-CODEX-001
SRC-ZCODE-001
SRC-OPENCODE-001
SRC-CROSSHOST-001
```

`SRC-*` 只标识外部或登记来源，不直接充当 Support Assessment 的 Evidence ID。Behavior run 使用 run metadata 中的 Run ID；Project Artifact 和 Enterprise Fact 使用其稳定记录 ID。

同一个 canonical source artifact 跨 Cycle 使用时必须复用最早登记的 Source ID，不得因为研究角色、Cycle 或引用位置变化而重新编号。只有来源是不同的可独立固定 artifact、revision 或官方页面，且 Registry 明确记录 parent / related Source ID 与 scope 差异时，才可分配新 ID。URL 拼写、版本后缀或链接到同仓库具体路径的差异本身不足以创建新 Source ID。

### Evidence IDs

每个将被 Research Note、ADR 或 Support Assessment 引用的证据判断使用 Evidence ID：

```text
EVD-BEHAVIOR-CODEX-001
EVD-PROJECT-MYHARNESS-001
EVD-ENTERPRISE-ZCODE-001
```

每条 `EVD-*` 记录必须包含：

```text
Evidence ID
Evidence Class
Claim / Observation
Supporting Artifact IDs
Bound Host / Provider / Model / Version
Supports / Contradicts
Known Limitations
Inference, if any
Verification Date
```

Source Registry 必须记录 authority owner、source role、版本或 commit、访问日期、适用范围、允许支持的 claim 和限制。

## 3. General Authority Rules

1. 官方文档按 Contract Evidence 登记，不因为可公开访问就归为 Source Evidence。
2. 只有权威归属、仓库身份、revision 和相关 Runtime scope 均可验证时，源码才可登记为 Source Evidence。
3. 行为实验必须绑定 Host、Host version、Provider profile、Model、Configuration 和 verification date。
4. Project Evidence 证明项目相关性，不证明 Host Contract。
5. Enterprise Fact 必须限定组织、部署和时间，不得外推。
6. Community Claim 必须标记为 `COMMUNITY CLAIM`，默认进入 Open Questions。
7. 证据冲突不得静默合并；保留冲突、版本差异和可能解释。

## 4. Host Evidence Boundaries

### Claude Code

- Official product documentation 和 official release information 可以构成 Contract Evidence。
- Direct run、Session、Trace 和 tool observation 可以构成 Behavior Evidence。
- 教学重实现、ACE、社区文章和第三方分析不能证明 Claude Code 官方 Runtime source architecture。
- 未验证的内部实现描述必须保持 Unknown 或 Community Claim。

### Codex

- Official documentation 和 release information 可以构成 Contract Evidence。
- 经验证的 `openai/codex` official source revision 可以构成对应 revision 的 Source Evidence。
- Source、Contract 和 Behavior 必须分别记录；源码存在不保证当前安装版本或配置采用相同行为。
- 源码结论必须绑定 repository、commit 和研究范围。

### OpenCode

- 可以使用 Official Contract、verified Official Source、Direct Behavior 和 Project Evidence。
- 每项行为结论必须分离 Host、Provider、endpoint type 和 Model effects。
- Provider compatibility 不自动证明 Model portability；相同配置文件形状不自动证明行为等价。

## 5. ZCode Source Authority Gate

ZCode 可以通过以下证据研究：

- Official Contract
- official product documentation
- official release information
- Direct Behavior Evidence
- local configuration
- Enterprise Fact

### Gate default

ZCode Runtime Source Authority Gate 默认是 `NOT VERIFIED`。在 Gate 通过前：

- 不得登记 ZCode Runtime Source Evidence。
- 不得形成 ZCode source-code architecture、内部 lifecycle 或实现路径结论。
- Source 字段必须使用 `Unsupported / Unknown` 中的 `Unknown`，而不是猜测路径。
- 社区逆向、非官方仓库、客户端指纹和第三方 patch 只能生成 Open Question。

### Gate pass criteria

只有同时满足以下条件，Gate 才能针对一个明确 scope 标记为 `VERIFIED`：

1. 仓库由 ZCode 官方组织、官方产品文档或官方 release channel 明确识别。
2. 可以验证该仓库对应所研究的 Runtime，而非 SDK、示例、客户端壳或无关组件。
3. 可以固定 repository URL、revision、license/provenance 与验证日期。
4. 目标 claim 可以定位到相关 source path 和 revision。
5. Source Registry 记录验证证据、适用 scope 和已知限制。

Gate 按 scope 生效。某个官方 SDK 通过验证，不代表 ZCode Runtime source authority 自动通过。

### Gate status record

```text
Host: ZCode
Scope: <runtime/component>
Status: NOT VERIFIED / VERIFIED / REVOKED
Authority Evidence IDs: <IDs>
Repository and Revision: <only when verified>
Verified On: <date>
Limitations: <known limits>
```

Batch 0 不识别或预设任何 ZCode 官方 Runtime source repository，因此 Gate 保持协议默认状态，不产生架构结论。

## 6. Claim Construction Rule

每个重要结论应记录：

```text
Evidence ID
Evidence Class
Claim / Observation
Supporting Artifact IDs
Bound Host / Provider / Model / Version
Supports / Contradicts
Known Limitations
Inference, if any
Verification Date
```

如果证据只能支持局部观察，结论必须使用局部措辞。无法区分 Host、Provider 和 Model effects 时，结果为 `INCONCLUSIVE` 或保留为 Hypothesis。Support Assessment 必须通过 `EVD-*` 回溯到 supporting Artifact，不允许跳过 Evidence Claim 层。
