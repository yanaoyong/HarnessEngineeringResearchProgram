# Cycle 15 实验工作区（Experiment Workspace）

> 状态（Status）：PREPARED · NOT EXECUTED

## `EXP-C15-01` · Evidence-first Read-only Architecture Audit

- 类型：`EXPLORATORY`
- Outcome Mode：`HYPOTHESIS_RESULT`
- Stable Task：`T02 · Semantic Review`
- 历史映射：`EXP-W13-01`

## Artifact inventory and packet gate

数据准备者在任何 Agent Run 前固定 myharness 完整 commit，并按 capability 重新定位 V4.1 列出的 Agent、Rule、Skill、Change、Hook、distribution、migration、graph、research、A/B、outcome 与 failure artifacts。路径不存在只记录 relocation / retention gap。

从 2–3 个历史 Change 与相关当前 artifacts 构造 8 个独立 dimension packets，分别绑定 Host Boundary、Context Lifecycle、Extension Responsibility、Cross-host Portability、Skill Behavior、Change Truth、Workflow Depth、Knowledge & Minimalism。每个 packet 必须：

- 包含有限 Change / diff、固定初态 / 终态、相关 artifact 和 authority；
- 至少包含一个需要语义判断的 architecture、risk、scope、evidence 或 correctness question；
- 至少包含一个可由 test、lint、schema、静态检查或已固定 CI result 验证的 deterministic check；
- 不泄漏 evaluator 的语义判断或预期 Finding 数量；
- 明确已知 Host / surface、Provider、endpoint / protocol、Model 与 Configuration，未知项保持 Unknown。

Coverage Matrix 必须把 Agent / Rule / Skill / Change template / historical Change / Hook、distribution / migration / graph / research / A/B artifacts、outcome / effectiveness / failure records 与 Cycle 4、6、9–14 question 映射到至少一个 packet，并记录 `INSPECTED / NOT PRESENT / NOT APPLICABLE / UNKNOWN`、artifact citation 与理由。未覆盖的维度或 artifact family 阻塞实验。

不满足 T02 Contract 的候选进入 exclusion log；对应维度必须重新构造合格 packet，不得用自由仓库阅读或空白 disposition 替代正式 task instance。

## Runs and evaluator boundary

- 每个 packet 执行 2 个 independent fresh-session Agent Run，共 16 个 Run。
- 所有 Run 使用相同 audit contract、可见输入和绑定条件；每个 Run 保存独立 metadata。
- 两名人工 evaluator 在 Agent Run 前独立建立 evaluator-only reference，记录 semantic review targets、critical issues、允许 disagreement 与 deterministic results；Run 后再裁决 citation validity、fact / inference boundary、miss、false positive 与 schema completeness，不向 Agent 提供答案。
- repository inventory、packet selection 和 Run 后去重不计为 Agent Run，必须作为 Human intervention / preparation artifact 记录。

## Finding contract

每条候选 Finding 必须包含：Observed Problem、Current Mental Model、Project Evidence、Reference Pattern、Contrary Evidence、Candidate Hypothesis、Open Question、Scope / Unknown。无充分 Project Evidence 时只能标为 Unknown / Open Question。

每个 packet 必须得到以下之一：

- `Finding`：全部必填字段可追溯，且没有把 Reference Pattern 当成 Project Evidence；
- `No Finding`：说明检查范围、已执行 deterministic check 与仍未知事项，且没有未解决的 evaluator critical issue；
- `INCONCLUSIVE`：artifact、authority、Run 或 confounder 不完整。

Run 后由 evaluator 去重，最多保留 8–12 个 Finding；0 个 Finding 合法，禁止为达到数量阈值制造问题。

## Result boundary

- `audit-complete packet`：两个 Run 都完成 deterministic check；所有 evaluator critical issues 被发现或作为有理由的 disagreement 裁决；没有 critical false positive；引用和必填字段有效。
- `SUPPORT`：Coverage Matrix 完整、8 个 packets / 16 个 Run 均完成，至少 6/8 packets 为 audit-complete，且没有 unsupported architecture critical claim。
- `REJECT`：至多 3/8 packets 为 audit-complete，或至少 2 个完整 packets 把路径缺失、Reference Pattern / Agent preference 写成项目事实，或无法区分 Finding 与建议。
- `INCONCLUSIVE`：其余结果、packet / Run 缺失、维度覆盖或 authority 不足、evaluator reference 未决、绑定条件不可比。

Batch 8 内容生成阶段不创建 `EVD-*`。真实执行完成后，固定 Project Artifacts、每次 Run 与 evaluator artifact 必须分配 ID；每个复用 Finding / No Finding claim 必须派生 scoped `EVD-*`。实验不修改 myharness，不创建实际 ADR、Design Belief 或 Support Level。
