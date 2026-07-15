# Cycle 17 实验工作区（Experiment Workspace）

> 状态（Status）：PREPARED · NOT EXECUTED

## Candidate experiment family

| Cycle 16 rank | Planned experiment | 状态 |
|---|---|---|
| Rank 1 | `EXP-C17-01` | `PLANNED · NOT EXECUTED` |
| Rank 2 | `EXP-C17-02` | `PLANNED · NOT EXECUTED` |
| Rank 3 | `EXP-C17-03` | `PLANNED · NOT EXECUTED` |

历史映射：`EXP-W15-01` → candidate-specific `EXP-C17-01..03` family。编号按 rank 预留，不表示存在三个合格候选；未入选编号不创建空 Experiment Record。

## Candidate readiness gate

每个 experiment 单独满足：

- 一个 `PROPOSED` ADR Candidate 和一个 `H-C17-0x`；
- 一个固定 `T03 · Medium Change` task instance、共同 task-fixture repository commit 与 deterministic acceptance；candidate build 使用满足 Hypothesis 的最小文件 / 步骤范围；
- myharness 独立 branch / worktree、rollback command 与 artifact retention route；冻结 `H0 · Current myharness` 和从 H0 派生的 `H1 · Candidate variant`；
- A0 / A1 仅改变 H0 / H1 的一个候选机制，所有 Rule / Skill / Check / Adapter / Configuration 与 implementation artifact revision 可追踪；
- 候选专属 primary metric、success / failure / inconclusive threshold 与 critical failure；
- 可绑定 Host、surface、Provider、endpoint / protocol、Model、permission、tool profile 和 Human intervention policy。

不满足 gate 时保持 `NOT EXECUTED`，不得扩大实现范围来挽救候选。

## One-time candidate build

- 在独立 myharness worktree 从 H0 构建 H1，只实现足以触发 Hypothesis 的最小 slice；它可以是一个文件或多个相互依赖步骤，不以文件数量制造 T03 规模。
- 构建过程、diff、build acceptance、dependency state、Human intervention 与 rollback rehearsal 保存为 implementation artifacts，但不计为 paired T03 task Run。
- 只有 H1 通过 preflight、其 revision 与 configuration snapshot 已冻结，才进入 paired protocol。

## Paired comparative protocol

每个候选独立执行：

- `A0 · Current myharness`：绑定冻结 H0；
- `A1 · Minimal candidate variant`：绑定冻结 H1；paired Run 内不再实现 candidate；
- A0 / A1 的 task fixture 在每次 Run 前重置到同一完整 commit，并执行同一 T03 instance；
- A0 / A1 各 3 个 fresh-session Run，组成 3 个 paired blocks；顺序在执行前冻结或随机化；
- Run Metadata 的 `repository.commit` 记录 task-fixture baseline；H0 / H1 通过相关 revisions、Configuration snapshot 与 implementation artifact ID 记录。每个 Run 保存 prompt、task、Host、Provider、Model、trace、diff、test、acceptance、Human intervention 与 known confounders。

Deterministic acceptance、task outcome、process trace、implementation completeness 与 Hypothesis Result 分别记录。候选间 task / metric 不同，禁止汇总成总体胜率。

## Isolation and rollback gate

- 禁止在实验中顺手重构、混入第二个候选或修改 main。
- paired Runs 完成后对 H1 worktree 实际执行 rollback verification，并保留前后状态与命令 artifact。
- 所有实验分支保持未合并，直到 Cycle 18 Decision Update 和 owner 的独立合并授权。
- Rollback 失败是 critical failure；不能以任务成功抵消。

## Result boundary

每个候选使用自己的预注册 threshold 形成 `SUPPORT / REJECT / INCONCLUSIVE`。实现完成不等于 `SUPPORT`；H0 / H1 未冻结、task-fixture baseline 不一致、Run 缺失、Human intervention 不对称或关键 confounder 未分离时必须为 `INCONCLUSIVE`。

本工作区当前没有 implementation、Run、Result、`EVD-*` 或 ADR Decision。
