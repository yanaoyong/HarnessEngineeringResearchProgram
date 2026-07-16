# Cycle 16 实验工作区（Experiment Workspace）

> 状态（Status）：PREPARED · NOT EXECUTED

## `EXP-C16-01` · Traceable Hypothesis and ADR Candidate Portfolio

- 类型：`EXPLORATORY`
- Outcome Mode：`HYPOTHESIS_RESULT`
- Stable Task：`T03 · Medium Change`
- 历史映射：`EXP-W14-01`

## Prerequisite and eligibility gate

Cycle 15 未真实完成前不得创建 Experiment Record。输入 packet 必须固定所有合格 Finding、Project Evidence / evidence gap、Contrary Evidence、Unknown 与 audit scope。

每个候选先通过资格门禁：可证伪、最小实验可逆、因果变量可分离、不要求大规模重构，并可写出 success、failure、inconclusive 与 reversal contract。不合格项进入 Backlog / Open Question / No Change。

## Eight-dimension scoring

执行前冻结 1–5 评分说明、权重与阈值：

- benefit direction：myharness relevance、Evidence Strength、Expected Value、Cross-host Portability、Reversibility；
- cost direction：Context Cost、Maintenance Cost、Implementation Cost。

若汇总总分，必须先把成本方向规范化并公开公式。Evidence gate 与 Reversibility gate 优先于总分；评分不能升级来源 authority。

## T03 task and independent Runs

每个 Run 从相同 finding packet 开始，在独立研究 workspace 中修改 3–4 个 Markdown 文件：一个 portfolio index 与至多三个基于模板的 ADR Candidate 文件。Deterministic checks 验证 schema、状态、link、ID uniqueness 与候选数量；人工 evaluator 评价 Hypothesis 可证伪性、evidence trace 与 reversal quality。

- 执行 2 个 independent fresh-session Run；Host / surface、Provider、Model、Configuration、模板和 rubric 相同，Run 彼此不可见。
- 候选状态只能是 `PROPOSED`，Result / Decision Update 保持未填写；少于三个或 0 个均合法。
- Run 后 evaluator 建立 reconciliation artifact，记录重合、排序分歧、authority gap 与 Backlog 理由；不强迫两个 Run 选出同一 Top3。

## Result boundary

- `SUPPORT`：两个 Run 都通过 deterministic checks，所有候选都能追溯到合格 Finding，并完整定义 Hypothesis、实验、success / failure / inconclusive、boundary 与 reversal；排序分歧被显式记录。
- `REJECT`：至少一个完整 Run 的多数候选无法追溯或证伪，或评分越过 evidence / reversibility gate 把候选包装为已接受决策。
- `INCONCLUSIVE`：输入 Finding 不完整、Run 缺失、evaluator disagreement 未记录或其他 confounder 未分离。

Batch 8 内容生成阶段不执行本实验，也不创建 `research/adr-candidates/ADR-*`。
