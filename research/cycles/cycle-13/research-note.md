# Cycle 13 研究笔记（Research Note）· Context Lifecycle & Session Handoff

> 状态（Status）：PLANNED · NOT EXECUTED
>
> 内容 Batch：7

[Cycle 正文](../../../docs/04-Harness-Engineering-Research-Themes.md) · [实验工作区](experiments/README.md) · [来源权限](../../source-authority.md)

## 1. 研究问题

多 Session 任务如何保留目标、决定、证据和未完成状态，而不把全部 trajectory noise 带入下一 Session？

## 2. 为什么与 myharness 有关

长任务会跨 Research、Plan、Implement、Review。若 resume、summary、Change artifact 与永久知识职责混合，下一 Session 可能继承过期信息或丢失关键决定。

## 3. 范围与退出条件

- 范围：一个连续 T03 task 的五 phase / 四 transition exploratory trace；Resume、prose summary、structured handoff 与 Changes artifact 四种 mode；V4.1 Week 11 迁移。
- 范围外：宣称最佳 handoff mode、跨 Host session parity、实现自动 memory。
- 退出条件：固定 boundary、schema、mode assignment 与 rubric；保存绑定 Run Metadata；只形成 exploratory V1。

当前退出条件未满足。

## 4. 心智模型 V0

Handoff 是从 live context 中 ratify durable task state，再由下一 Session 验证 freshness；不是复制聊天历史。

## 5. 证据登记

尚无 `EVD-*`。计划来源：

- 复用 Cycle 3 [`SRC-CLAUDE-006`](../cycle-03/evidence/SRC-CLAUDE-006.md)：HumanLayer Advanced Context Engineering。
- [`SRC-HARNESS-009`](evidence/SRC-HARNESS-009.md)：snarktank/ralph。
- 复用 Cycle 3–6 Host sources；复用 `SRC-*` 不形成新的 Contract / Behavior claim。

## 6. 参考模式

ACE 提供 intentional compaction 方法问题，Ralph 提供 fresh-context + persistent artifact 对照。两者都不是通用最佳实践证明。

## 7. 假设

`H-C13-01 · Structured Handoff Observability`：结构化字段能暴露交接遗漏，但单一任务的轮换设计不能比较 mode 优劣。

## 8. 实验

- 实验 ID：`EXP-C13-01`
- 类型：`EXPLORATORY`
- Outcome Mode：`OBSERVATION_ONLY`
- Stable Task：`T03 · Medium Change`
- 历史映射：`EXP-W11-01` → `EXP-C13-01`
- Run Metadata：尚未创建
- Observation Outcome：尚未运行；执行后使用 `COMPLETE / PARTIAL / INVALIDATED`
- Experiment Result：`NOT APPLICABLE · OBSERVATION ONLY`

## 9. 观察

无。

## 10. 矛盾证据与限制

- phase 的自然差异与 handoff mode 完全混杂；本实验不能比较 mode superiority。
- Resume 使用同一 Host session identity；其他三种 mode 使用 fresh session。若 Host 不能区分 session identity 与 execution episode，则对应 mode 保持 `UNKNOWN / NOT EXECUTED`。
- Host resume、compaction 与 artifact loading 可能有不同 surface behavior。
- 恢复更快可能来自遗漏检查，而不代表交接更好。
- summary 内的事实需要 freshness / authority 验证。

## 11. 心智模型 V1

等待实验与证据。

## 12. 设计判断

待定。不实现自动 handoff 或永久 memory。

## 13. 开放问题

见 `OQ-013`。

## 14. 路线复盘触发条件

若任何 transition 无法独立观察 hydration 与遗漏，或 Host 自动 compaction 无法与手工 artifact 分离，先复盘设计。
