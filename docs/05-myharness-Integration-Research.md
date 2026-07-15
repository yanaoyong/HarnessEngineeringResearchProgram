# PART VI · myharness Integration Research

> V4.2 Batch 8 正文由 V4.3 Host-set Amendment 继承，并将 Cycle 18 第三个 Host stratum 更新为 Qwen Code。状态：`PLANNED · NOT EXECUTED`。

[← 上一卷](04-Harness-Engineering-Research-Themes.md) · [返回总览](../README.md)

---

## Batch 8 研究边界

Batch 8 把 V4.1 Week 13–16 迁移为四个 Cycle，形成从只读审计、候选选择、最小实现实验到验收与设计信念更新的研究闭环。生成正文和工作区不表示审计已经进行、ADR Candidate 已产生、实现已经开始、实验已经运行或设计决策已经接受。

共同边界：

- Cycle 15 的审计对象是执行时固定 commit 的 myharness artifact packet；当前仓库只定义方法，不补写不存在的项目事实。
- Cycle 16 只在 Cycle 15 的合格 Finding 上形成至多三个 `PROPOSED` 候选；候选不是 ADR 决策，评分也不是证据。
- Cycle 17 的任何代码修改只允许在未来独立 branch / worktree 中作为可逆实验；本 Batch 不实现、不提交、不合并 myharness 功能。
- Cycle 18 只对通过前置门禁的 variant 做绑定条件下的小样本验收与消融；不得形成 Host、Provider 或 Model 排名。
- 新实验使用 `EXP-Cxx-yy` 与稳定任务套件 T01–T03；V4.1 `EXP-Wxx-yy` 只保留历史映射。
- Source Registry ID、Project Artifact ID、Run 与 `EVD-*` 分开；复用 Cycle 1–14 的 `SRC-*` 不会把来源升级为 Evidence Claim。
- Host、surface、Provider、endpoint / protocol、Model 与 Configuration 分别绑定。不同 Host stratum 的结果不合并为架构效果。
- `SUPPORT` 只回答预注册 Hypothesis；实现完成、测试通过或任务成功都不自动表示 ADR 正确。
- 本 Batch 不创建 Run、`EVD-*`、`ENT-*`、Support Assessment、实际 ADR Candidate、Design Belief 或 Route Review 结果。

## Cycle 15 · Read-only Architecture Audit

> 历史来源：V4.1 Week 13 · `EXP-W13-01`

### 核心研究问题

> 在不修改 myharness 的前提下，哪些架构问题、证据缺口与“不应改变”的边界能够从固定项目制品中被可复查地识别？

### Audit Model V0

```text
fixed repository commit
        ↓
artifact inventory + authority gate
        ↓
finite T02 audit packets
        ↓
Observation → Project Evidence → Contrary Evidence / Unknown
        ↓
bounded Finding | No Finding
        ↓
falsifiable Hypothesis candidate
```

审计不是实现建议清单。Observed Problem、当前解释、Project Evidence、Reference Pattern、Contrary Evidence、Hypothesis 与 Open Question 必须分开；`No Finding` 和“保持现状”都是合法输出。

### 审计范围

执行时先固定 myharness commit，再按 capability 重新定位下列对象，而不是假设 V4.1 路径仍存在：

- Agent、Rule、Skill、Change template、历史 Change 与 Hook；
- Claude Plugin Distribution、Codex Migration、CodeGraph、Research Discovery 与 A/B Test artifact；
- task-outcome、agent-effectiveness-report 与 failure-record 等结果或失败记录；
- Cycle 4、6、9–14 已定义的 Host boundary、guard、portability、Skill、Change、workflow、handoff 与 ratification question。

若旧路径不存在，只记录 relocation / retention gap，不推断功能缺失。审计维度冻结为：Host Boundary、Context Lifecycle、Extension Responsibility、Cross-host Portability、Skill Behavior、Change Truth、Workflow Depth、Knowledge & Minimalism。

### 假设与实验

`H-C15-01 · Evidence-first Bounded Audit`：对覆盖八个审计维度的 myharness packets，证据优先、只读且有界的审计协议能够识别预注册 semantic review targets、形成可追溯的 Finding 或 `No Finding`，同时暴露 Unknown，而不要求先修改代码或制造问题数量。

`EXP-C15-01` 使用 `T02 · Semantic Review`：

- 数据准备者在 Agent Run 前固定 repository commit、选择 2–3 个历史 Change，并构造 8 个 dimension packets；每个 packet 对应一个冻结审计维度，包含有限 Change / diff、相关当前 artifact slice、至少一个语义 review target 和一个 deterministic check。
- Coverage Matrix 必须把上文列出的每个 artifact family 映射到至少一个 packet，并记录 `INSPECTED / NOT PRESENT / NOT APPLICABLE / UNKNOWN`；未覆盖的维度或 artifact family 阻塞实验。
- 每个 packet 做 2 个 independent fresh-session Agent Run，共 16 个 Run；输入、Host / surface、Provider、Model、Configuration 与 audit contract 相同。
- 两名人工 evaluator 在 Agent Run 前独立建立 evaluator-only reference，记录 semantic review targets、critical issue、允许 disagreement 与 deterministic result；它用于衡量 miss / false positive，不向 Agent 泄漏答案。
- Findings 在 Run 后去重，最多保留 8–12 个高质量条目；没有达到 Finding gate 的观察进入 `No Finding`、Unknown 或 Open Question，而不是凑数。

每个 Finding 使用：Observed Problem、Current Mental Model、Project Evidence、Reference Pattern、Contrary Evidence、Candidate Hypothesis、Open Question、Scope / Unknown。只有固定 artifact 和 revision 后才可能形成 Project Evidence；Reference Pattern 本身不证明 myharness 存在问题。

### 退出条件

- 固定 repository commit、artifact inventory、Coverage Matrix、8 个 T02 packets、evaluator-only reference、audit contract、rubric 与 Run conditions。
- 16 个 Agent Run 都有完整 metadata；缺失 artifact、authority、维度覆盖或可比绑定条件时保持 `INCONCLUSIVE`。
- 每个 packet 有 Finding 或 `No Finding` disposition；`No Finding` 只有在没有未解决的 evaluator critical issue 时才算 audit-complete，事实、推断、Unknown 与建议不得混写。
- 总 Finding 不超过 12 个；允许 0 个，不把问题数量作为成功指标。
- 真实执行后为固定 Project Artifact、Run 与 scoped claim 分配 ID / `EVD-*`；没有修改 myharness、创建 ADR 或把审计 observation 写成 S1–S4。

完整计划见 [Cycle 15 实验工作区](../research/cycles/cycle-15/experiments/README.md)。

## Cycle 16 · Hypothesis & ADR Candidate

> 历史来源：V4.1 Week 14 · `EXP-W14-01`

### 核心研究问题

> 哪些经证据约束的架构假设值得进入可逆实验，哪些应进入 Backlog、Open Question 或保持现状？

### Candidate Model V0

```text
qualified Cycle 15 Finding
        ↓
falsifiable Hypothesis
        ↓
eligibility gate + eight-dimension score profile
        ↓
up to three PROPOSED ADR Candidates
        ↓
experiment / success / failure / reversal contract
```

评分维度保留 V4.1 的八项：myharness relevance、Evidence Strength、Expected Value、Context Cost、Maintenance Cost、Cross-host Portability、Implementation Cost、Reversibility。成本项与收益项方向必须明确；权重和准入阈值在看到排序前冻结。总分只帮助暴露取舍，不替代证据或 owner decision。

### 候选资格与状态

只有满足以下条件的 Finding 才能进入候选池：

- 引用 Cycle 15 scoped `EVD-*` 与底层 Project Artifact / Run / evaluator IDs，或明确记录的 evidence gap；
- Hypothesis 可证伪，能写出 success、failure 与 `INCONCLUSIVE` 条件；
- 最小实验可在隔离环境中执行且有 reversal plan；
- 未把 Host、Provider、Model 或 Configuration effect 混成单一架构因果；
- 不要求先做大规模、不可逆或跨候选的重构。

候选状态只能是 `PROPOSED`；未来开始 Cycle 17 实验时才可改为 `EXPERIMENT`。`ACCEPTED / REJECTED / REVISE / MORE EVIDENCE REQUIRED` 属于 Cycle 18 真实证据后的 Decision Update。

### 假设与实验

`H-C16-01 · Traceable Candidate Selection`：对同一个冻结 Cycle 15 finding packet，显式资格门禁、八维评分与 reversal contract 能让两个独立候选组合都保持 Finding → Hypothesis → Experiment → Reversal 的可追溯性，并把排序分歧显式暴露，而不是把功能偏好包装成决策。

`EXP-C16-01` 使用 `T03 · Medium Change`。每个 independent Run 在隔离的研究 workspace 中生成一个 portfolio index 与至多 3 个 ADR Candidate 文件：

- 两个 Run 使用相同 finding packet、rubric、模板、Host / surface、Provider、Model 与 Configuration；彼此不可见输出。
- 每个候选必须通过 schema / link checker，并绑定来源 Finding、Hypothesis、最小实验、success / failure signal、boundary 与 reversal plan。
- 人工 evaluator 在 Run 后记录候选重合、排序分歧、authority gap 与进入 Backlog 的原因；不以强制共识掩盖分歧。
- 若合格候选少于 3 个，只输出实际合格数量；0 个候选是合法结果。

本 Batch 只规划这个实验，不实际创建 `research/adr-candidates/ADR-*`。

### 退出条件

- Cycle 15 已真实结束且 finding packet、authority、rubric、权重 / 阈值与 evaluator procedure 固定。
- 两个 T03 Run 完成 schema 与 deterministic check，并分别保存完整 metadata。
- 至多三个候选保持 `PROPOSED`，其余明确进入 Backlog / Open Question / No Change。
- 排序分歧、成本方向、证据强度和不可分离 confounder 可见。
- 没有候选被标为已接受，没有实现 myharness，也没有创建 Support Assessment。

完整计划见 [Cycle 16 实验工作区](../research/cycles/cycle-16/experiments/README.md)。

## Cycle 17 · Minimal Implementation Experiment

> 历史来源：V4.1 Week 15 · `EXP-W15-01`

### 核心研究问题

> 验证一个 ADR Candidate 所需的最小、可逆实现是什么，如何避免把功能完成误当成假设成立？

### Experiment Isolation Model V0

```text
Candidate → isolated one-time build → freeze H0 / H1 Harness revisions
                                      ↓
same task-fixture commit + same T03 instance
              ├── A0 · H0 Current myharness
              └── A1 · H1 Frozen candidate variant
                                      ↓
              paired task Runs + deterministic acceptance
                                      ↓
             candidate-scoped Result + verified rollback
```

Top candidate 不能共享一个多变量实现。Cycle 16 排名第 1–3 的候选分别预留 `EXP-C17-01`、`EXP-C17-02`、`EXP-C17-03`；只有实际入选并通过 readiness gate 的候选才创建 Experiment Record。未入选的编号保持 `NOT EXECUTED`，不生成空结果。

### Readiness Gate

每个候选在执行前必须具备：

- `PROPOSED` ADR Candidate、单一可证伪 Hypothesis 与候选专属 success / failure / inconclusive threshold；
- 一个固定 `T03 · Medium Change` task instance、task-fixture repository baseline 与 deterministic acceptance checks；candidate build 采用满足 Hypothesis 的最小文件 / 步骤范围，不以文件数量凑规模；
- 分别冻结 Harness-under-test 的 `H0` current revision 与 `H1` candidate revision，以及共同的 task-fixture commit；A0 / A1 只改变一个候选机制，Rule、Skill、Check、Adapter、Configuration 与 implementation artifact revision 可分别追踪；
- 独立 branch / worktree、rollback command、artifact retention route 与禁止自动合并的门禁；
- Host、surface、Provider、endpoint / protocol、Model、permission、tool profile 与 human-intervention policy 可绑定。

不满足任一条件时保持 `PLANNED · NOT EXECUTED`。

### 假设与实验

每个 `EXP-C17-0x` 使用候选自己的 `H-C17-0x`，类型为 `COMPARATIVE`，Stable Task 为 T03：

- 先在独立 myharness worktree 中一次性构建 H1，只实现足以触发 Hypothesis 的最小 slice；构建 / preflight 不是 paired T03 task Run，禁止顺手重构、共享未登记变更或扩大功能面。
- H1 通过 build acceptance 与 rollback rehearsal 后冻结；A0 绑定 H0、A1 绑定 H1。每个 paired Run 都把 task fixture 重置到同一完整 commit，执行同一个 task instance；A0 / A1 各做 3 个 fresh-session Run，顺序在执行前冻结或随机化。
- Run Metadata 的 `repository.commit` 绑定 task fixture；独立 `harness_under_test` block 绑定 A0 / A1 cell、H0 / H1 Harness revision、Harness repository / distribution revision、implementation artifact IDs 与 task-fixture relationship。Rule / Skill / Check / Adapter revision 和 Configuration snapshot 继续分项记录，不能替代完整 Harness identity。保存 prompt、task、Host、Provider、Model、trace、diff、test、Human intervention 与 rollback evidence。
- 每个候选独立形成 Result，不能将三个候选的不同任务、实现或指标汇总为一个胜率。

V4.1 示例只保留为候选形态，不是预选结论：单一 Skill 的 Evidence Contract、单一 Change 的 convergence check、单一 Skill 的 Claude → Codex portability slice。实际候选必须来自 Cycle 16，不能因示例存在而跳过证据门禁。

### 退出条件

- 每个已执行候选完成 3 个 A0 / A1 paired blocks，且通过候选专属 acceptance 与 confounder review。
- H1 实现 diff 有界、可逆且没有合并到 main；paired Runs 后 rollback 被实际验证并留下 artifact。
- Result 只回答该候选 Hypothesis；实现完成、测试通过与任务成功分别记录。
- 失败与 `INCONCLUSIVE` 不被隐藏；未执行候选保持 `NOT EXECUTED`。
- 不更新最终 ADR Decision、不写 Design Belief、不声称生产就绪或 S1–S4。

完整计划见 [Cycle 17 实验工作区](../research/cycles/cycle-17/experiments/README.md)。

## Cycle 18 · Acceptance、Ablation & Design Beliefs

> 历史来源：V4.1 Week 16 · `EXP-W16-01`

### 核心研究问题

> 哪些实验性 Harness capability 在绑定条件下带来可接受的边际价值，哪些应拒绝、修订或要求更多证据？

### Acceptance Model V0

```text
eligible Cycle 17 variants
        ↓
pre-registered smallest informative matrix
        ↓
same T03 task × same Host stratum × repeated Runs
        ↓
Outcome / Process / Governance / Context / Cost
        ↓
ADR Decision Update + bounded Design Belief | No Change
```

### 计划对照矩阵

- `B0 · Native Host`：绑定 Host 的原生能力，不加载 myharness experimental mechanism。
- `A0 · Current myharness`：固定当前 myharness baseline。
- `A1 · One candidate-specific variant`：A0 加一个通过 Cycle 17 readiness / evidence gate 的最小 variant；每个 Experiment Record 只绑定一个 candidate 和一个 Host / surface stratum。

不是每个候选或 Host 都必须进入矩阵。单个 candidate 内只有在存在明确 component Hypothesis 且保持可解释性时，才增加 Rules-only / Rules+Skills / Rules+Skills+Changes 等内部消融 cell；跨 candidate stack 必须另建 Experiment Record。每个 Host stratum 内固定 Provider、endpoint / protocol、Model 与 Configuration。

Cycle 18 可复用 Cycle 1 `SRC-FOUNDATION-003` 的 SWE-agent ACI paper 作为 interface / experiment theory 背景，但该论文不是 myharness Project Evidence、Host Contract 或本项目 Result，不参与候选胜负裁决。

### 假设与实验

`H-C18-<candidate>-<host> · Evidence-gated Marginal Value`：对一个 candidate、一个绑定 Host / surface stratum 和三个位于该 stratum 的固定 T03 task instances，最小信息量消融矩阵可以暴露 Current myharness 与候选 variant 在 Outcome、Process、Governance、Context 和 Cost 上的边际取舍，并支持该 candidate / Host scope 的 Decision Update；它不能证明跨 Host、Provider、Model 或项目的普遍优越性。

Cycle 18 预留 `EXP-C18-01..12` candidate × Host family：Rank 1 使用 `01..04`、Rank 2 使用 `05..08`、Rank 3 使用 `09..12`，每组依次绑定 Claude Code、Codex、Qwen Code、OpenCode。只有 candidate 与 Host stratum 通过 readiness / authority / parity gate 时才创建对应 Experiment Record；每个记录只有一个 Hypothesis 与 Result。

每个 `EXP-C18-xx` 类型为 `ABLATION`，Stable Task 为 `T03 · Medium Change`：

- 在看到结果前冻结 3 个 task instances、eligible cells、primary / secondary metrics、critical failure、Human intervention policy 与 candidate / Host-specific Decision threshold。
- Applicability Matrix 必须包含至少 2 个 activation-positive tasks 与 1 个 non-trigger control；每个 task 预注册 candidate applicability、expected Discovery / Activation / Execution signal 和 verifier。无法观测 activation 时该 candidate / Host record 保持 `NOT EXECUTED`。
- 每个 cell 对每个 task 做 3 个 fresh-session Run；总 Run 数为 `eligible cells × 3 tasks × 3 repetitions`，每个 Run 独立记录 metadata。
- 每个 Run 的 `repository.commit` 绑定 task fixture；`harness_under_test` 独立绑定 B0 / A0 / A1、native-host / H0 / H1 revision 与 implementation artifact IDs。
- Outcome：Task Success、First-pass Acceptance、Tests；Process：Rework、False Completion、Blind Retry、Missed Verification、Unrelated Change；Governance：Rule Violation、Human Intervention、Gate Trigger；Context：Consumption、Repeated Reads、Recovery；Cost：Harness complexity、Maintenance、Cross-host duplication。
- activation-positive task 中 A1 未激活时，记录 activation / implementation failure，不能解释为“无边际价值”；non-trigger control 中意外激活作为 false activation。安全、正确性或证据完整性 critical failure 不能被平均成本优势抵消。

每个 Experiment Result 只解释一个 candidate / Host stratum。Candidate ADR 在执行前声明 required target Host set；只有该集合的 scoped Results 与 `EVD-*` 完整后，才更新为 `ACCEPTED / REJECTED / REVISE / MORE EVIDENCE REQUIRED`，否则保持 `MORE EVIDENCE REQUIRED` 或 scoped decision。只有引用有效 Evidence、写明 Counterexample、Boundary 与 Confidence 的判断才可加入 `research/design-beliefs.md`；`No Change` 是合法结论。

### 退出条件

- Cycle 17 的 eligible variant、baseline 与 rollback artifact 完整，每个 candidate / Host Experiment Record、Applicability Matrix 和所有 cells 在运行前冻结。
- 每个执行 record 的 Run 完整；缺失 cell、activation signal、不可比 task 或未分离 confounder 时该 candidate / Host Result 保持 `INCONCLUSIVE`。
- Outcome、Process、Governance、Context 与 Cost 分开报告，critical failure 规则没有被后验修改。
- ADR Decision Update、Design Belief 与 No Change 都可追溯到 `EVD-*`，并保留反例与适用边界。
- 不把小样本写成统计显著性、公开 benchmark、四宿主普遍结论、生产就绪或法律合规判断。

完整计划见 [Cycle 18 实验工作区](../research/cycles/cycle-18/experiments/README.md)。

## V4.1 历史迁移映射

| V4.1 | V4.2 | 新实验 | 状态 |
|---|---|---|---|
| Week 13 · myharness Read-only Architecture Audit | Cycle 15 | `EXP-W13-01` → `EXP-C15-01` | `PLANNED · NOT EXECUTED` |
| Week 14 · Hypothesis & ADR Candidate | Cycle 16 | `EXP-W14-01` → `EXP-C16-01` | `PLANNED · NOT EXECUTED` |
| Week 15 · Minimal Implementation Experiment | Cycle 17 | `EXP-W15-01` → `EXP-C17-01..03` candidate family | `PLANNED · NOT EXECUTED` |
| Week 16 · Acceptance、Ablation & Design Beliefs | Cycle 18 | `EXP-W16-01` → `EXP-C18-01..12` candidate × Host family | `PLANNED · NOT EXECUTED` |

历史 ID 只表示研究意图的迁移关系，不表示旧实验已执行，也不能与新 ID 同时创建重复结果。

## Batch 8 完成边界

Batch 8 完成仅表示 Cycle 15–18 的正文、计划实验与工作区已准备，V4.2 的 18 个 Cycle 都有计划态正文。它不表示 V4.2 研究已执行或项目已经完成。

只有在真实完成 Cycle 15–18 Exit Criteria 后，才能创建 Finding、ADR Candidate、实验实现、Run、Evidence Claim、Decision Update、Design Belief 与最终 Route Review。Batch 内容生成阶段不会修改 myharness、不会接受架构决策，也不会产生任何 S1–S4 Support Level。
