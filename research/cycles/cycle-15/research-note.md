# Cycle 15 研究笔记（Research Note）· Read-only Architecture Audit

> 状态（Status）：PLANNED · NOT EXECUTED
>
> 内容 Batch：8

[Cycle 正文](../../../docs/05-myharness-Integration-Research.md) · [实验工作区](experiments/README.md) · [证据准备](evidence/README.md) · [来源权限](../../source-authority.md)

## 1. 研究问题

在不修改 myharness 的前提下，哪些架构问题、证据缺口与“不应改变”的边界能够从固定项目制品中被可复查地识别？

## 2. 为什么与 myharness 有关

Cycle 1–14 建立了 Host、Harness abstraction 与治理研究问题；Cycle 15 需要把这些模型用于项目事实，同时防止 Reference Pattern、文件路径或审计者偏好被误写成 Project Evidence。

## 3. 范围与退出条件

- 范围：固定 myharness commit、覆盖 8 个审计维度的 T02 packets、Coverage Matrix、evaluator-only reference 与 16 个只读 Agent Run；V4.1 Week 13 迁移。
- 范围外：修改代码、创建 ADR、提出大型方案、制造 Finding 数量或形成 Support Assessment。
- 退出条件：每个维度和 artifact family 已覆盖，每个 packet 有经过 semantic miss / false-positive 裁决的 Finding / No Finding disposition，最多 8–12 个去重 Finding，且事实、推断、Unknown 与建议分离。

当前退出条件未满足。

## 4. 心智模型 V0

只读审计是 `fixed artifacts → authority gate → bounded observation → evidence-linked finding / no finding → falsifiable candidate`，不是从理想架构反推缺陷清单。

## 5. 证据登记

尚无 `EVD-*` 或 Project Artifact ID。Cycle 15 复用 Cycle 4、6、9–14 的计划来源和研究模型，但不会复制 `SRC-*` 或将其升级为 Evidence Claim。

计划执行时才固定 myharness commit、历史 Change 与 outcome / failure artifacts；详见 [证据准备](evidence/README.md)。

## 6. 参考模式

使用 Host Boundary、Context Lifecycle、Extension Responsibility、Cross-host Portability、Skill Behavior、Change Truth、Workflow Depth、Knowledge & Minimalism 八维框架。Reference Pattern 只帮助提出问题，不能替代项目事实。

## 7. 假设

`H-C15-01 · Evidence-first Bounded Audit`：有界协议能在八个审计维度上识别预注册 review targets，形成可追溯的 Finding 或合格 No Finding，并暴露 Unknown，而不要求先修改代码或凑问题数。

## 8. 实验

- 实验 ID：`EXP-C15-01`
- 类型：`EXPLORATORY`
- Stable Task：`T02 · Semantic Review`
- 历史映射：`EXP-W13-01` → `EXP-C15-01`
- 计划规模：8 个 dimension packets × 2 个 independent Run = 16 个 Agent Run
- Run Metadata：尚未创建
- 结果：尚未运行

## 9. 观察

无。

## 10. 矛盾证据与限制

- 旧 V4.1 路径可能已经迁移；路径不存在不能单独证明 capability 不存在。
- historical Change 存在幸存者偏差与 retention gap。
- 审计者使用的 Model 可能影响发现与解释；必须绑定 Host、Provider、Model 与 Configuration。
- Finding 数量不是审计质量指标；只有 Coverage Matrix 完整、没有未解决 critical miss 时，0 个 Finding 才可能是合法结果。

## 11. 心智模型 V1

等待实验与证据。

## 12. 设计判断

待定。只有引用 scoped `EVD-*` 与底层 Project Artifact / Run / evaluator IDs 的合格 Finding 才进入 Cycle 16 输入候选。

## 13. 开放问题

见 `OQ-011`、`OQ-014` 与 `OQ-015`。

## 14. 路线复盘触发条件

若无法为八个维度构造满足 T02 Contract、authority 可复查的 packets，Coverage Matrix 存在缺口，或审计协议持续混淆 artifact absence 与 capability absence，停止运行并复盘数据门禁。
