# PART VII · V4.2 Research Infrastructure

> Batch 0 冻结的 Research Note、Evidence、Experiment、Run Metadata、Source Registry、Support Level、Open Questions、Route Review 与 ADR 基础设施。

[返回总览](../README.md) · [研究计划总纲](00-研究计划总纲.md) · [Batch 0 Protocol](08-V4.2-Batch0-Protocol.md)

---

## 1. Canonical Protocol Files

- [Common Glossary](09-V4.2-Glossary.md)
- [Stable Task Suite](../research/task-suite.md)
- [Evidence Classification and Source Authority](../research/source-authority.md)
- [Host Support Levels](../research/support-levels.md)
- [Research Workspace](../research/README.md)

本卷说明这些协议如何组合使用；术语和权限冲突时，以对应 canonical protocol file 为准，不在内容 Batch 中静默重定义。

## 2. Research Note

每个真实 Cycle 使用同一认知结构：

```text
Research Question
        ↓
Mental Model V0
        ↓
Contract / Source / Behavior / Project / Enterprise Evidence
        ↓
Community Claims as Open Questions
        ↓
Hypothesis
        ↓
Experiment / Observation
        ↓
Mental Model V1
        ↓
Design Judgment
```

使用 [research-note.template.md](../research/templates/research-note.template.md)。Mental Model、Hypothesis 和 Reference Pattern 不是 Evidence；推断必须明确标记。

## 3. Evidence and Source Registry

V4.2 使用六类来源：

| Class | Primary use |
|---|---|
| Contract Evidence | 公开承诺的 surface 与边界 |
| Source Evidence | 已验证 revision 的实现 |
| Behavior Evidence | 绑定运行条件下的直接观察 |
| Project Evidence | myharness 中问题的存在与影响 |
| Enterprise Fact | 特定企业 profile 的部署事实 |
| Community Claim | 调查线索与 Open Question |

来源使用 [source-registry.template.md](../research/templates/source-registry.template.md) 登记。证据数量不等于证据强度；每条重要 Evidence 还应记录 Direct / Indirect、Repeatable / One-off、Current / Stale、Host-specific / Cross-host、Supports / Contradicts。

ZCode 的 Source Evidence 受独立 Source Authority Gate 约束。未验证官方 Runtime source 时，不允许形成源码架构或内部生命周期结论。

## 4. Experiment and Run Metadata

新 Experiment ID：

```text
EXP-C01-01
EXP-C08-02
EXP-C18-01
```

Experiment 表示研究问题、Hypothesis、设计和结果；Run 表示一次具体执行。使用：

- [experiment-record.template.md](../research/templates/experiment-record.template.md)
- [run-metadata.template.yaml](../research/templates/run-metadata.template.yaml)

Run metadata 必须分离：

- repository commit
- Host 与 Host version
- Provider 与 endpoint type
- Model ID
- configuration snapshot
- Rule、Skill、Check、Adapter revision
- controlled variables
- known confounders
- evidence
- human intervention

V4.1 正文中的 `EXP-Wxx-yy` 保持历史编号，直到对应内容 Batch 迁移。实际历史 Evidence 不重新编号。

### Experiment types

| Type | Purpose |
|---|---|
| EXPLORATORY | 观察现象、发现变量、形成下一步 Hypothesis |
| COMPARATIVE | 在共同 baseline 下比较机制差异 |
| ABLATION | 移除或逐层增加 capability，观察边际贡献 |

## 5. Stable Task Suite

T01–T03 冻结任务语义：

- `T01 · Engineering Constraint`
- `T02 · Semantic Review`
- `T03 · Medium Change`

具体 task instance 在对应内容 Batch 中选择并登记。Task Suite 只用于方向性比较，不用于公开模型 benchmark。

## 6. Host and Provider Profiles

- [host-profile.template.md](../research/templates/host-profile.template.md) 绑定 Host version、Contract surface、source authority、Provider boundary 与 capability assessment。
- [provider-profile.template.md](../research/templates/provider-profile.template.md) 绑定 Provider、endpoint type、Model、路由和 behavior-affecting settings。
- [enterprise-readiness-fact-sheet.template.md](../research/templates/enterprise-readiness-fact-sheet.template.md) 只记录特定部署事实，不创建普遍法律合规结论。

任何 profile 都不得记录 secret、token 或私有凭据值。

## 7. Support Levels

| Level | Meaning |
|---|---|
| S0 | Not Assessed |
| S1 | Contract Mapped |
| S2 | Behavior Verified |
| S3 | Operationally Verified |
| S4 | Enterprise Profile Verified |

S1 不表示 full support，S2 不表示 production ready，S4 不表示 universal legal compliance。Batch 0 不预设任何 Host 达到 S1–S4。

## 8. Open Questions and Route Review

旁支问题统一进入 [open-questions.md](../research/open-questions.md)。Community Claim 默认只能创建 Open Question。

每 2–4 个 Cycle 使用 [route-review.template.md](../research/templates/route-review.template.md) 做 Route Review。允许调整项目、研究深度、执行节奏或提前借用后续方法，但不得改变 Batch 0 冻结的 Cycle 名称、编号、顺序或 Batch 边界。修改冻结协议需要新的 Program version，并必须记录 Why the Route Changed。

## 9. ADR Candidate and Design Beliefs

Cycle 16 的 ADR Candidate 是实验候选，不是已经接受的架构决策。使用 [adr-candidate.template.md](../research/templates/adr-candidate.template.md)。

Implementation 完成不等于 ADR 正确。只有结果回答原 Hypothesis，才可以更新 Decision。Design Beliefs 继续记录在 [design-beliefs.md](../research/design-beliefs.md)，并保留 Evidence、Counterexample、Boundary 与 Confidence。

## 10. Research Workspace

```text
research/
├── README.md
├── task-suite.md
├── source-authority.md
├── support-levels.md
├── open-questions.md
├── cycles/
│   └── README.md
├── route-reviews/
│   └── README.md
├── adr-candidates/
│   └── README.md
├── templates/
│   ├── research-note.template.md
│   ├── experiment-record.template.md
│   ├── run-metadata.template.yaml
│   ├── source-registry.template.md
│   ├── host-profile.template.md
│   ├── provider-profile.template.md
│   ├── enterprise-readiness-fact-sheet.template.md
│   ├── adr-candidate.template.md
│   └── route-review.template.md
└── design-beliefs.md
```

进入对应内容 Batch 时，可以先准备该 Batch 覆盖的 Cycle 工作区：

```text
research/cycles/cycle-01/
├── research-note.md
├── experiments/
└── evidence/
```

工作区准备不表示实验已经执行或证据已经成立。Batch 0 没有创建任何 `cycle-*` 目录；Batch 1 准备 `cycle-01` 与 `cycle-02`，Batch 2 增加 `cycle-03` 与 `cycle-04`，Batch 3 增加 `cycle-05` 与 `cycle-06`，Batch 4 增加 `cycle-07`。Cycle 8–18 目录尚未创建。

## 11. V4.1 Historical Boundary

V4.1 Research Infrastructure 是本卷的迁移来源，不作为并行协议继续演进。V4.1 正文中的 Week、旧实验编号和项目导航保持原状，直到对应内容 Batch 迁移；新产生的研究制品一律使用 V4.2 Cycle-based 协议。
