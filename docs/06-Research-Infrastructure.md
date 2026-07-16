# PART VII · Research Infrastructure（V4.2 Base · V4.3 Effective）

> Batch 0 冻结的 Research Note、Evidence、Experiment、Run Metadata、Source Registry、Support Level、Open Questions、Route Review 与 ADR 基础设施。

[返回总览](../README.md) · [研究计划总纲](00-研究计划总纲.md) · [Batch 0 Protocol](08-V4.2-Batch0-Protocol.md)

---

## 1. Canonical Protocol Files

- [Common Glossary](09-V4.2-Glossary.md)
- [V4.3 Qwen Code Host-set Amendment](10-V4.3-Qwen-Code-Host-Amendment.md)
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

Qwen Code 的官方源码仓库身份已核验，但 Source Evidence 仍必须固定完整 commit，并在连接 Direct Behavior 时建立安装 artifact → release / commit 的可复查 provenance。默认分支或官方 architecture overview 不能替代 revision-bound Source Evidence。

## 4. Experiment and Run Metadata

新 Experiment ID：

```text
EXP-C01-01
EXP-C08-02
EXP-C18-01
```

Experiment 表示 Research Question，以及 Hypothesis / Result 或 Observation Contract / Outcome，并记录设计、运行与限制；Run 表示一次具体执行。`SUPPORT / REJECT / INCONCLUSIVE` 只属于 Experiment 或预注册 stratum Result；Run 只记录 execution / acceptance outcome，不能独立裁决 Hypothesis。使用：

- [experiment-record.template.md](../research/templates/experiment-record.template.md)
- [run-metadata.template.yaml](../research/templates/run-metadata.template.yaml)

Run metadata 必须分离：

- Program version、base protocol schema、Research Program commit 与 applied amendment；
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
- Harness-under-test cell、Harness revision 与 implementation artifact IDs（与 task-fixture commit 分开）

`v4.3-r1` 是当前首个 V4.3 Run Metadata schema：它保留 `v4.2-batch0-r2` 字段并新增 protocol binding。当前没有真实 Run 需要迁移；未来 Run 必须分别绑定 Research Program commit 与 task-fixture `repository.commit`，不得用其中一个替代另一个。

Experiment Record 还必须声明 Result cardinality。若 Host、task instance 或其他 strata 的 Result 不可互相替代，记录 Result unit、stratum key 与预注册 aggregation rule；没有合理聚合规则时只保留 stratum Result，不创建统一 Experiment Result。

V4.1 正文中的 `EXP-Wxx-yy` 已随对应内容 Batch 完成迁移，只保留为 historical mapping ID。实际历史 Evidence 不重新编号，新研究制品不得复用旧 Week ID。

### Experiment types

| Type | Purpose |
|---|---|
| EXPLORATORY | 观察现象、发现变量、形成下一步 Hypothesis |
| COMPARATIVE | 在共同 baseline 下比较机制差异 |
| ABLATION | 移除或逐层增加 capability，观察边际贡献 |

Experiment Type 与 Outcome Mode 分开。`EXPLORATORY` 可以使用 `OBSERVATION_ONLY`，也可以在已有预注册 Hypothesis 与裁决规则时使用 `HYPOTHESIS_RESULT`；`COMPARATIVE` / `ABLATION` 通常使用 `HYPOTHESIS_RESULT`。Observation-only record 不把“未裁决 Hypothesis”写成 `INCONCLUSIVE`。

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

正式 Support Assessment 统一存放在 [research/support-assessments/](../research/support-assessments/README.md)。当 `research_execution = NOT_STARTED` 时，该目录只能包含 README；模板、Source Registry、计划实验或 Host Profile 不能替代正式评估。

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

工作区准备不表示实验已经执行或证据已经成立。Batch 0 没有创建任何 `cycle-*` 目录；Batch 1 准备 `cycle-01` 与 `cycle-02`，Batch 2 增加 `cycle-03` 与 `cycle-04`，Batch 3 增加 `cycle-05` 与 `cycle-06`，Batch 4 增加 `cycle-07`，Batch 5 增加 `cycle-08`，Batch 6 增加 `cycle-09`，Batch 7 增加 `cycle-10` 至 `cycle-14`，Batch 8 增加 `cycle-15` 至 `cycle-18`。其中 evidence preparation README 只说明未来证据门禁，不是 `SRC-*` 或 `EVD-*`。

## 11. V4.1 Historical Boundary

V4.1 Research Infrastructure 是本卷的历史迁移来源，不作为并行协议继续演进。Week 1–16 已全部迁移；旧 Week、实验编号和项目导航只在 migration record / historical Atlas 中保留。新产生的研究制品一律使用 V4.3 当前有效的 Cycle-based 协议，即 V4.2 Batch 0 base protocol 加已登记的 V4.3 amendment。

## 12. Content Integrity Automation

`validation/content-baseline.json` 以机器可读方式登记当前 Program version、协议 amendment、四个主要 Host、Batch 状态、Cycle 名称与映射、计划 Experiment ID 和 Source Registry ID。`scripts/validate_content.py` 使用 Python 标准库校验：

- `MANIFEST.txt` 的路径集合与字节数；
- Markdown 内部相对链接；
- Cycle 1–18 的目录、Research Note、Experiment preparation 与 evidence workspace；
- Cycle 名称、Batch、`PLANNED · NOT EXECUTED`、Experiment ID 与 Source ID 基线；
- Source Registry 文件名、标题、身份字段、必需章节与未固定来源的 pin / revalidation boundary；
- V4.3 protocol binding 与 amendment ID；
- `research_execution = NOT_STARTED` 时不存在 Run、Result、`EVD-*`、`ENT-*`、Finding、ADR Candidate 或 Route Review 制品。

GitHub Actions 在 Pull Request 与 `main` push 上运行同一命令。校验通过只表示 repository state 与已声明基线一致，不升级 Source Authority、不证明研究执行，也不产生 Evidence Claim 或 Support Assessment。

```bash
python3 scripts/validate_content.py
python3 scripts/test_content_validation.py
python3 scripts/validate_content.py --write-manifest  # 仅在有意变更受管文件后
```

回归测试在临时 Git 副本中验证两条语义门禁：Research Note 不能遗漏其显式登记的 Experiment ID；研究未开始时不能创建 Support Assessment。临时副本不会修改工作树。

更新 Manifest 是机械操作；更新 `content-baseline.json` 是协议或内容状态操作，必须有可追溯的 owner decision、内容 Batch 修订或真实研究执行制品。不得通过删除校验项、扩大忽略范围或把意外文件加入基线来掩盖漂移。
