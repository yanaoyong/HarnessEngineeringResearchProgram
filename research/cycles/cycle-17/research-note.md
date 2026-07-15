# Cycle 17 研究笔记（Research Note）· Minimal Implementation Experiment

> 状态（Status）：PLANNED · NOT EXECUTED
>
> 内容 Batch：8

[Cycle 正文](../../../docs/05-myharness-Integration-Research.md) · [实验工作区](experiments/README.md) · [证据准备](evidence/README.md) · [Run Metadata 模板](../../templates/run-metadata.template.yaml)

## 1. 研究问题

验证一个 ADR Candidate 所需的最小、可逆实现是什么，如何避免把功能完成误当成假设成立？

## 2. 为什么与 myharness 有关

集成研究只有进入真实实现才会暴露接口、上下文、维护与回滚成本；但同时实现多个候选会失去因果解释，并把实验变成重构项目。

## 3. 范围与退出条件

- 范围：Cycle 16 排名第 1–3 的合格候选，分别预留 `EXP-C17-01..03`；每个候选先构建并冻结 H0 / H1 Harness revisions，再使用共同 task-fixture baseline 做独立 T03 A0 / A1 paired experiment；V4.1 Week 15 迁移。
- 范围外：当前生成代码、跨候选重构、自动合并 main、生产发布或最终 ADR Decision。
- 退出条件：每个执行候选有 3 个 paired blocks、可逆 diff、rollback evidence 与候选级 Result。

当前退出条件未满足；Cycle 16 尚未产生候选。

## 4. 心智模型 V0

最小实现是对单一 Hypothesis 的 instrument：one-time build 只改变一个 Harness 机制，paired task Runs 只比较冻结的 H0 / H1，task fixture 始终从共同 baseline 重置，并允许 Reject / Inconclusive。

## 5. 证据登记

尚无 `EVD-*`、Run 或实现 artifact。实际执行只引用 Cycle 16 候选与固定 myharness baseline；当前 [证据准备](evidence/README.md) 只定义准入边界。

## 6. 参考模式

V4.1 的 Evidence Contract、Change convergence check 与单 Skill portability 只说明“最小 slice”的形态，不是预选候选，也不证明任何方案有效。

## 7. 假设

`H-C17-01..03` 等待 Cycle 16 候选后分别定义。每个 Hypothesis 必须绑定独立 success、failure、inconclusive threshold 与 reversal plan。

## 8. 实验

- 实验 ID：`EXP-C17-01`、`EXP-C17-02`、`EXP-C17-03`（候选 family；按 readiness gate 启用）
- 类型：`COMPARATIVE`
- Stable Task：`T03 · Medium Change`
- 历史映射：`EXP-W15-01` → `EXP-C17-01..03`
- Run Metadata：尚未创建
- 结果：尚未运行

## 9. 观察

无。

## 10. 矛盾证据与限制

- 不同候选使用不同 task instance，候选间结果不可直接排序。
- Harness-under-test revision 与 task-fixture commit 是两个身份；若 Run metadata 或 artifact link 无法同时绑定，两者的结果不可归因。
- Model nondeterminism、Human intervention 与依赖变化可能污染 paired comparison。
- 测试通过只证明 acceptance check，不证明架构 Hypothesis。
- 隔离 branch / worktree 降低回滚风险，但不证明长期维护成本。

## 11. 心智模型 V1

等待实验与证据。

## 12. 设计判断

待定。本 Batch 不创建任何 myharness implementation diff。

## 13. 开放问题

见 `OQ-016` 与 `OQ-017`。

## 14. 路线复盘触发条件

若候选无法收敛到单变量、最小且可逆的 H1，或 A0 / A1 无法从同一 task-fixture baseline 运行，不扩大 scope；退回 Cycle 16 修订候选。
