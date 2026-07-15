# Cycle 14 实验工作区（Experiment Workspace）

> 状态（Status）：PREPARED · NOT EXECUTED

## `EXP-C14-01` · Historical Knowledge Ratification Review

- 类型：`EXPLORATORY`
- Stable Task：`T02 · Semantic Review`
- 历史映射：`EXP-W12-01`

## Dataset and T02 Gate

在看到分类结果前，按冻结时间窗选择十个 myharness historical failure / improvement packets。每个 packet 必须是一个独立 T02 task instance，并满足全部条件：

- 包含一个有限 Change / diff、固定 repository commit 与初始状态；
- 提供足够但不泄漏参考答案的 task / project context；
- 至少包含一个需要语义判断的 correctness、architecture、risk、evidence 或 scope 问题；
- 至少包含一个可由 test、lint、schema 或静态检查验证的问题；
- 包含发生时间、相关 artifact、验证结果，以及已知 Host / Provider / Model / Configuration 与 authority；
- 参考结论允许 disagreement 和 uncertainty。

不能满足 T02 Contract 的历史记录只进入 dataset-preparation exclusion log，不得以 `UNKNOWN` 补齐后进入十个正式 task instances。

## Experimental subjects and evaluator reference

- 每个 packet 在同一个绑定 Host / surface、Provider、Model、Configuration 与 ratification rubric 下执行 2 个 independent Agent reviewer Run，共 20 个 Agent Run；每个 Run 使用 fresh session、同一 task input 与独立 Run Metadata。
- 两名人工 evaluator 在 Agent Run 前独立建立 evaluator-only reference，记录语义 disagreement、deterministic result 与允许的多个 ratification answer；人工 evaluator 不计 Agent Run。
- Agent 不可见 evaluator reference，也不得访问其他 packet 的输出。

## Classification and output contract

每个 Agent reviewer 必须独立判断：

- One-off / Recurring / Unknown；
- Host Issue / Model Behavior / Project Knowledge / Process Problem / Deterministic Constraint / Mixed；
- authority、scope、blast radius、determinism、expected recurrence value；
- Context、maintenance、portability 与 behavior-complexity cost；
- target：Rule / Skill / Hook / Test / Wiki / Change Template / Nothing。

每个目标必须附证据引用、owner、revalidation trigger、removal condition 与替代方案。人工 evaluator 按预注册 rubric 评分，不以多数感觉覆盖 authority gap。

## Observations and result

记录 reference issue discovery、deterministic verification、citation validity、reviewer agreement、unsupported ratification、deterministic-to-semantic mismatch、重复 / 冲突候选、Nothing 理由与未知项。

一个 packet 只有在两个 Agent Run 都发现全部预注册 critical issues、引用有效且完成 authority / scope / target / owner / revalidation / removal 字段时才算 ratification-complete：

- `SUPPORT`：至少 8/10 packets ratification-complete，且没有 unsupported permanent ratification critical failure。
- `REJECT`：至多 4/10 packets ratification-complete，或至少 3 个 packets 出现 unsupported permanent ratification critical failure。
- `INCONCLUSIVE`：其余结果、evaluator reference 未决、Run 缺失或 confounder 未分离。

后续时间窗中的复发只能作 exploratory cross-check，不证明所选治理位置能防止未来失败。任何实现建议都进入 Cycle 15 audit / Cycle 16 Hypothesis candidate；本 Cycle 不修改 Harness，不创建 `EVD-*`、ADR 或 Support Level。
