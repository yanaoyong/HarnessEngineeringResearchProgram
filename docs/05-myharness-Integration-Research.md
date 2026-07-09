# PART VI · myharness Integration Research

> Phase 6 · Week 13–16：Audit → Hypothesis / ADR → Minimal Experiment → Acceptance / Design Beliefs。

[← 上一卷](04-Harness-Engineering-Research-Themes.md) · [返回总览](../README.md) · [下一卷 →](06-Research-Infrastructure.md)

---

## Week 13 · myharness Read-only Architecture Audit

> Phase 6 · myharness Integration Research

### 核心研究问题

> **经过前 12 个研究循环，我现在看到的 myharness 与 12 周前有什么不同？**

### 主线研究对象

| **研究对象** | **阅读深度** | **本周只关注**                                                                     |
|--------------|--------------|------------------------------------------------------------------------------------|
| myharness    | 项目主审计   | 不引入新主项目；以过去 12 周 Mental Model、Evidence 和 Open Questions 作为审计框架 |

### 重点查看部分

- 重点查看：.harness/agents/application-owner.md、.harness/rules/、.harness/skills/、.harness/changes/\_TEMPLATE/、2–3 个历史 Change、.claude/hooks/。

- 再看 Claude Plugin Distribution、Codex Migration、CodeGraph、Research Discovery、A/B Test、task-outcome、agent-effectiveness-report、failure-record。

- 八个审计维度：Host Boundary、Context Lifecycle、Extension Responsibility、Cross-host Portability、Skill Behavior、Change Truth、Workflow Depth、Knowledge & Minimalism。

### 阅读时只追这些问题

- 是否重新实现 Host 已解决的能力？

- L1/L2/L3 是否符合 Context Cost？Rule / Skill / Hook 职责是否混乱？

- Portable Core 与 Adapter 是否明确？Skill 是否真正改变行为？

- Artifact 是否与代码和状态一致？十阶段是否匹配不同风险？

- 哪些能力有重复价值证据？

### 本周不要陷进去

- 改代码

- 发现差异就立即提出大改

- 输出 50 条优化建议

- 为了证明前 12 周有价值而强行找问题

### 学习后的实践：Observation 与 Solution 分离的 Read-only Audit

> **Experiment ID:** `EXP-W13-01`  
> **Experiment Type:** `EXPLORATORY`  
> **Evidence Scope:** 个人研究中的方向性证据；小样本用于发现现象、比较机制或形成下一步假设，不包装为统计学结论。

1. 每个 Finding 使用：Observed Problem / Current Mental Model / Project Evidence / Reference Pattern / Contrary Evidence / Candidate Hypothesis / Open Question。

2. 最多 8–12 个高质量 Finding。

3. 允许结论为“不改”：当前设计与参考模式不同，但项目 Evidence 支持现有设计。

### 建议保留的证据

- 真实 failure / change / A/B 证据

- 与参考 Pattern 的差异

- Contrary Evidence

- Candidate Hypothesis 的可证伪性

### 预期成长

| **审计能力** | 看到优秀设计后不再立即说“myharness 也要有”。           |
|--------------|--------------------------------------------------------|
| **问题匹配** | 训练“参考项目解决的问题”与“myharness 实际问题”的对照。 |

### 实践完成后，重新理解

- 我的旧设计判断哪些被证据支持？

- 哪些只是经验直觉？

- 哪些“缺口”其实不是问题？

- 哪 8–12 个 Finding 真值得进入下一周？

| **弹性规则：** 如果本周实验直接暴露了一个会推翻当前 Mental Model 的问题，可以暂停原计划并追加一个短研究循环；如果只是有趣的旁支问题，记录到 Open Questions，继续主线。 |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Week 14 · Hypothesis & ADR Candidate

> Phase 6 · myharness Integration Research

### 核心研究问题

> **哪些架构变化真正值得进入实验？**

### 主线研究对象

| **研究对象**     | **阅读深度** | **本周只关注**                               |
|------------------|--------------|----------------------------------------------|
| Week 13 Findings | 项目主线     | 不广泛阅读新项目；仅在关键争议时回看对应资料 |

### 重点查看部分

- 先把 Feature 改写为 Hypothesis。例如“增加 Skill Contract v2”改为“在 semantic review Skill 增加 observable evidence requirement，可以降低 false completion”。

- 评分维度：myharness Relevance、Evidence Strength、Expected Value、Context Cost、Maintenance Cost、Cross-host Portability、Implementation Cost、Reversibility。

- 只选 Top 3；其他进入 Research Backlog。

- ADR Candidate 状态为 PROPOSED / EXPERIMENT；内容：Context、Observed Problem、Current Evidence、Hypothesis、Experiment Design、Success Signal、Failure Signal、Boundary、Reversal Plan。

### 阅读时只追这些问题

- 这个判断是否可证伪？

- 成功 / 失败信号是否可观察？

- 是否能用更小实验验证？

- 这个 Hypothesis 是在解决 myharness 问题，还是在复制参考项目？

### 本周不要陷进去

- 把 Feature 名称当 Hypothesis

- 一次选 5–8 个实现目标

- 把 ADR 直接标 ACCEPTED

- 选择不可逆大重构作为第一次实验

### 学习后的实践：Finding → Hypothesis → Top 3 → ADR Candidate

> **Experiment ID:** `EXP-W14-01`  
> **Experiment Type:** `EXPLORATORY`  
> **Evidence Scope:** 个人研究中的方向性证据；小样本用于发现现象、比较机制或形成下一步假设，不包装为统计学结论。

1. 将 Week 13 的 8–12 个 Finding 全部改写为可验证 Hypothesis。

2. 按八个维度评分。

3. 只选择 Top 3。

4. 为 Top 3 写实验型 ADR Candidate。

### 建议保留的证据

- Hypothesis 与 Project Evidence 的对应

- Success / Failure Signal

- Reversal Plan

- Top 3 选择与 Backlog 淘汰理由

### 预期成长

| **可证伪思维** | 把 Architecture Decision 当成一个可被现实攻击的设计赌注。          |
|----------------|--------------------------------------------------------------------|
| **优先级判断** | 学会用证据、成本、可逆性和项目相关性选择实验，而不是用“有趣程度”。 |

### 实践完成后，重新理解

- ADR 是决策记录，还是实验假设记录？

- Implementation 完成为什么不等于 ADR 正确？

- 哪些设计应先小范围试验，哪些必须直接建立确定性 Gate？

| **弹性规则：** 如果本周实验直接暴露了一个会推翻当前 Mental Model 的问题，可以暂停原计划并追加一个短研究循环；如果只是有趣的旁支问题，记录到 Open Questions，继续主线。 |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Week 15 · Minimal Implementation Experiments

> Phase 6 · myharness Integration Research

### 核心研究问题

> **验证一个架构假设所需的最小实现是什么？**

### 主线研究对象

| **研究对象**        | **阅读深度** | **本周只关注**                       |
|---------------------|--------------|--------------------------------------|
| Top 3 ADR Candidate | 项目实验     | 只实现能够验证 Hypothesis 的最小版本 |

### 重点查看部分

- 必须保留 Baseline：Current myharness vs Experimental Variant。

- 小范围：例如 Skill Contract 只改 code-review，不升级全部 Skills。

- 可逆：branch、worktree、experimental profile、isolated adapter。

- 不顺手重构；“既然都……”是本周头号敌人。

### 阅读时只追这些问题

- 当前实现验证的是 Hypothesis，还是只是证明代码能运行？

- 是否同时改了太多变量？

- 结果变化来自 Harness，还是模型随机性？

- 最小实现还可以更小吗？

### 本周不要陷进去

- 实现 Top 3 Feature 的完整版

- 顺手统一目录 / Schema / Owner

- 把实验代码直接合并 main

- 隐藏 INCONCLUSIVE 结果

### 学习后的实践：Top 3 Hypothesis 的最小实现与证据保留

> **Experiment ID:** `EXP-W15-01`  
> **Experiment Type:** `COMPARATIVE`  
> **Evidence Scope:** 个人研究中的方向性证据；小样本用于发现现象、比较机制或形成下一步假设，不包装为统计学结论。

1. 示例 A：Evidence Contract 降低 Reviewer False Completion → 只修改 expert-reviewer Skill。

2. 示例 B：Change Convergence 减少 Artifact Drift → 只对一个 Change 建立半自动 checker。

3. 示例 C：Shared Portable Skill Contract 降低 Claude → Codex Migration Duplication → 只迁移一个 Skill。

4. 保存 Prompt / Task、Config、Host、Model、Artifact、Trace / Session Evidence、Git Diff、Test Result、Human Intervention。

### 建议保留的证据

- Baseline 与 Variant

- Git Diff 与配置

- Trace / Session Evidence

- Test Result

- Human Intervention

- INCONCLUSIVE 的理由

### 预期成长

| **Experiment Engineering** | 明确 Feature Design ≠ Experiment Design。                                |
|----------------------------|--------------------------------------------------------------------------|
| **最小验证**               | 学会用 2 小时的小实现攻击核心 Hypothesis，而不是先花两周做完整 Feature。 |

### 实践完成后，重新理解

- 实验真的验证了 Hypothesis 吗？

- 同时改了几个变量？

- 是否需要更多样本？

- 结果不明确时，下一步应缩小问题还是增加任务？

| **弹性规则：** 如果本周实验直接暴露了一个会推翻当前 Mental Model 的问题，可以暂停原计划并追加一个短研究循环；如果只是有趣的旁支问题，记录到 Open Questions，继续主线。 |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Week 16 · Acceptance、Ablation 与 Design Beliefs

> Phase 6 · myharness Integration Research

### 核心研究问题

> **16 个研究循环以后，我到底改变了哪些设计认知？**

### 主线研究对象

| **研究对象**                    | **阅读深度** | **本周只关注**                                               |
|---------------------------------|--------------|--------------------------------------------------------------|
| myharness experimental variants | 项目验收     | Native Host / Current Harness / Experimental Capability 对照 |
| SWE-agent ACI                   | L1 理论对照  | Agent Interface Design 会影响行为与任务表现                  |
| 前 15 周 Experiment / Evidence | 内部研究证据 | 复用已积累的 process evidence，不临时引入模糊的“过程评测资料” |

### 重点查看部分

- 根据 Top 3 Hypothesis 选择 B0 Native Claude / Codex、A0 Current myharness、A1/A2/A3 Experimental Capability。

- 需要时做 Rules Only、Rules + Skills、Rules + Skills + Changes、+ Experimental Capability 的 Ablation；不为漂亮表格强制所有组合。

- 观察 Outcome、Process、Governance、Context、Cost 五类指标。

- 小样本 3–5 个任务用于发现趋势和形成下一步 Hypothesis，不包装成统计学结论。

### 阅读时只追这些问题

- 结果是否回答了原 Hypothesis？

- 最终成功掩盖了哪些过程问题？

- 收益是否值得 Context / Maintenance / Cross-host Duplication 成本？

- 哪些 Design Beliefs 应接受、拒绝、修订或继续收集证据？

### 本周不要陷进去

- 把 3–5 个任务包装成统计显著结论

- 只看 Task Success

- 为了证明 16 周有成果而保留无效 Capability

- 把 Design Beliefs 写成永久 Rules

### 学习后的实践：Acceptance / Ablation / Mental Model Update

> **Experiment ID:** `EXP-W16-01`  
> **Experiment Type:** `ABLATION`  
> **Evidence Scope:** 个人研究中的方向性证据；小样本用于发现现象、比较机制或形成下一步假设，不包装为统计学结论。

1. Outcome：Task Success、First-pass Rate、Tests。

2. Process：Rework Count、False Completion、Blind Retry、Missed Verification、Unrelated Change。

3. Governance：Rule Violation、Human Intervention、Gate Trigger。

4. Context：Context Consumption、Repeated Reads、Recovery Time。

5. Cost：Harness Complexity、Maintenance Cost、Cross-host Duplication。

6. ADR 状态更新为 ACCEPTED / REJECTED / REVISE / MORE EVIDENCE REQUIRED。

### 建议保留的证据

- Hypothesis 对应指标

- Baseline / Variant 差异

- 过程质量与最终结果

- 能力成本

- Counterexample 与 Boundary

### 预期成长

| **设计信念** | 形成 myharness Design Beliefs v1。                                                                   |
|--------------|------------------------------------------------------------------------------------------------------|
| **证据习惯** | 从“我读过很多项目”升级为“我能观察 Agent、建立机制模型、提出可证伪假设、做小实验并根据证据修正设计”。 |

### 实践完成后，重新理解

- 哪些旧认知被推翻？

- 哪些 Belief 证据不足？

- 哪些 Capability 应删除或保持不变？

- 下一轮研究问题是什么？

| **弹性规则：** 如果本周实验直接暴露了一个会推翻当前 Mental Model 的问题，可以暂停原计划并追加一个短研究循环；如果只是有趣的旁支问题，记录到 Open Questions，继续主线。 |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|


---

## 路线调整说明

本卷是研究导航，不是冻结的教学脚本。执行到对应研究循环前，应先刷新相关官方文档、默认分支与 Changelog；若项目目录或能力名称发生变化，继续追踪本卷定义的研究问题与 Capability，而不是机械寻找旧路径。
