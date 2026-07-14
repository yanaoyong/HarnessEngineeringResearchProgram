# Stable Task Suite · T01–T03

> Status: FROZEN IN BATCH 0

[返回 Research Workspace](README.md) · [Batch 0 Protocol](../docs/08-V4.2-Batch0-Protocol.md) · [Run Metadata Template](templates/run-metadata.template.yaml)

## 1. Purpose

T01–T03 提供跨 Host、Provider、Model 与 Harness variant 的稳定任务语义，用于方向性比较、发现变量和形成 Hypothesis。

它们不是公开 benchmark，不用于模型排行榜，不声称统计显著性，也不允许把小样本外推为普遍性能结论。

## 2. Common Task Instance Contract

每个实例必须记录：

- Task Suite ID 与 instance ID
- repository、baseline commit 与初始工作区状态
- task statement 与 acceptance checks
- in-scope / out-of-scope files or behavior
- engineering constraints
- 允许的 Human intervention
- known ambiguity 与 known confounders
- evidence collection boundary

比较 Run 时，应保持 task instance 和 baseline 相同；无法保持的变量必须记录为 confounder。

## 3. T01 · Engineering Constraint

### Stable intent

在一个小型、可逆的工程修改中满足明确约束，并观察约束由 Instruction、Rule、Skill、Hook 或 Check 承担时的行为差异。

### Required properties

- 修改范围小，预期实现路径清楚。
- 至少有一个显式工程约束。
- 约束是否满足可以通过可复查证据判断。
- 不使用破坏性安全场景。

### Primary observations

- first-pass adherence
- omitted or incorrect action
- Agent self-correction
- deterministic detection or block
- false positive
- rework count、context cost 与 human intervention

### Stable boundary

T01 比较治理机制，不证明某个 Model 普遍更服从约束。

## 4. T02 · Semantic Review

### Stable intent

对一个包含真实语义取舍的有限 Change 或 diff 进行审查，识别 correctness、architecture、risk、evidence 与 scope 问题，并区分语义判断和确定性检查。

### Required properties

- 输入包含足够上下文，但不能直接给出答案。
- 至少包含一个需要语义推理的问题。
- 至少包含一个可由 test、lint、schema 或静态检查验证的问题。
- 参考结论允许保留 disagreement 和 uncertainty。

### Primary observations

- issue discovery、miss 与 false positive
- evidence citation quality
- severity and scope calibration
- semantic reasoning vs deterministic verification
- false completion 与 unsupported certainty

### Stable boundary

T02 不以评论数量衡量质量，也不把单个人工 reviewer 的意见当成绝对 ground truth。

## 5. T03 · Medium Change

### Stable intent

完成一个需要跨多个文件或多个步骤、能够在受控时间内结束的中等 Change，观察 planning、context lifecycle、convergence、handoff 和 acceptance behavior。

### Required properties

- 需要理解现有实现后再修改。
- 包含多个相互依赖步骤或文件。
- 有明确的 acceptance checks 和可逆 baseline。
- 规模足以暴露 context、state 或 convergence 问题，但不演变为项目重构。

### Primary observations

- repeated reads、lost decision 与 sequence drift
- unrelated change、artifact drift 与 missed verification
- test result、rework count 与 false completion
- context recovery、handoff quality 与 human intervention
- final outcome 和 process quality

### Stable boundary

T03 用于比较工作过程和 Harness effect，不用于比较公开吞吐量或端到端商业生产力。

## 6. Comparability Rules

- 先声明比较对象：Host、Provider、Model、Configuration 或 Harness variant。
- 一次比较尽量只改变一个主要变量。
- Run metadata 不完整时，结果最多作为 exploratory evidence。
- Host effect 不得与 Provider-dependent Behavior 或 Model behavior 合并解释。
- 失败、拒绝和 `INCONCLUSIVE` 都是合法结果。
- 任务实例可以随项目演进，但 T01–T03 的 stable intent 不得在内容 Batch 中静默改变。
