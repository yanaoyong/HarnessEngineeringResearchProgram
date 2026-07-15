# Open Questions / Research Backlog

> 发现问题不等于马上研究。Community Claim 默认只能在这里创建调查项。

## Status

- `BACKLOG`
- `ACTIVE`
- `ANSWERED`
- `DROPPED`
- `MERGED`

## Questions

### OQ-001 · 是否存在可通过 Source Authority Gate 的 ZCode 官方 Runtime source repository？

- Discovered In: Batch 0
- Why It Matters: 决定 Cycle 7 是否允许形成 ZCode Runtime Source Evidence 与 source architecture conclusion
- Current Evidence: `SRC-ZCODE-001..009` 已登记官方产品、Contract、release 与 support 浮动锚点；这些入口均未指认满足五项 Gate criteria 的 ZCode Runtime source repository，尚无 `EVD-*`
- Authority Boundary: 非官方仓库、社区逆向、客户端指纹和第三方 patch 不能回答本问题
- Blocks Current Research?: NO；Contract、Behavior、local configuration 与 Enterprise Fact 研究仍可进行
- Priority: HIGH
- Candidate Cycle: Cycle 7
- Status: BACKLOG

### OQ-002 · 仓库外是否已经存在需要迁移登记的 `EXP-Wxx-yy` 历史 Evidence？

- Discovered In: Batch 0
- Why It Matters: 已执行的历史实验必须保留原 ID，不能在内容迁移时误重编号
- Current Evidence: 当前仓库没有实际 experiment record，只有 V4.1 正文中的计划 ID
- Blocks Current Research?: NO
- Priority: MEDIUM
- Candidate Cycle: Corresponding content Batch
- Status: BACKLOG

### OQ-003 · 学术论文在六类 Evidence taxonomy 中应如何登记？

- Discovered In: Batch 1 / Cycle 1 source registration
- Why It Matters: SWE-agent ACI paper 可提供 interface theory 与实验背景，但它既不是 Host Contract / Runtime Source，也不是 myharness Project Evidence；强行归类可能赋予错误 authority
- Current Evidence: `SRC-FOUNDATION-003` 暂以 `OTHER` source role 登记，并保守限制为 Reference Pattern / Community Claim authority，不派生 `EVD-*`
- Authority Boundary: 在 taxonomy 决策前，论文不能证明商业 Host 当前实现、Program Behavior、Support Level 或公开模型排名
- Blocks Current Research?: NO；可作为问题形成和 Reference Pattern，Cycle 1 机制结论仍需固定 revision Source 与 Direct Behavior Evidence
- Priority: MEDIUM
- Candidate Cycle: Cycle 1 Route Review / next protocol revision if taxonomy changes
- Status: BACKLOG

### OQ-004 · HTTP fallback / degradation 语义应由哪类任务和治理机制验证？

- Discovered In: Batch 2 / Cycle 4 experiment review
- Why It Matters: “显式 timeout”可由 deterministic fixture 判断，而“考虑 fallback / degradation”依赖调用语境、失败模型与产品语义；合并实验会让 Skill 与 Check 实际治理不同约束
- Current Evidence: None registered；`EXP-C04-01` 已收敛为 timeout-only T01 contract
- Authority Boundary: 不能因 Rule、Skill 或 Check 文件存在就断言 fallback 语义已被正确处理；需要独立 task statement、acceptance reference 与 Behavior Evidence
- Blocks Current Research?: NO；Cycle 4 可先完成 timeout responsibility comparison
- Priority: MEDIUM
- Candidate Cycle: Cycle 4 follow-up / Cycle 10 Skill Behavior & Evaluation
- Status: BACKLOG

### OQ-005 · Codex CLI、IDE、desktop 与 cloud 是否共享同一 customization / execution 语义？

- Discovered In: Batch 3 / Cycle 5–6 official Contract registration
- Why It Matters: 当前官方导航覆盖多个 Codex surface；如果直接合并，可能把 AGENTS.md、Skill、Plugin、Hook、Sandbox 或 Approval 在一个 surface 的 Contract / Behavior 外推到另一个 surface
- Current Evidence: 只有计划态官方文档锚点 `SRC-CODEX-001..004`、`SRC-CODEX-006..010`；尚未绑定 Host version、surface、platform 或 Behavior Run
- Authority Boundary: 官方 overview 只能支持其明确声明的公开范围；未执行 Direct Behavior、未固定 Source revision 时，不能宣称 surface parity 或共同 Runtime implementation
- Blocks Current Research?: NO；Cycle 5–6 可以先按实际实验 surface 建立 scoped map，其余 surface 保持 Unknown
- Priority: HIGH
- Candidate Cycle: Cycle 5 / Cycle 6 / Cycle 9 cross-host abstraction
- Status: BACKLOG

### OQ-006 · 安装的 OpenCode release 应如何与官方源码 commit 建立可复查映射？

- Discovered In: Batch 5 / Cycle 8 official Source registration
- Why It Matters: Cycle 8 需要同时绑定 Host version 与 `anomalyco/opencode` revision；若 release、binary、package 与 commit 无法对应，Source 只能解释候选实现，不能解释安装 Behavior
- Current Evidence: `SRC-OPENCODE-001` 与 `SRC-OPENCODE-011` 只登记官方安装入口和浮动源码仓库；commit 为 `NOT PINNED`，尚无 `EVD-*`
- Authority Boundary: tag 名、默认分支 HEAD、package version 或目录相似不能单独证明安装 artifact 对应某个 commit；需要官方 release / provenance 与本地版本记录
- Blocks Current Research?: YES；不阻塞独立 Contract map 或 Behavior trace，但阻塞 Source / Behavior agreement claim 与 Cycle 8 Exit Criteria
- Priority: HIGH
- Candidate Cycle: Cycle 8
- Status: BACKLOG

### OQ-007 · 哪些 OpenCode Provider / Model 组合能通过单变量 portability comparability gate？

- Discovered In: Batch 5 / Cycle 8 experiment design
- Why It Matters: Provider contrast 需要尽量固定同一 Model ID / revision，Model contrast 需要固定同一 Provider profile；如果只能取得 Provider 与 Model 同时变化的组合，就不能裁决任一 portability hypothesis
- Current Evidence: `SRC-OPENCODE-003..004` 只证明官方存在 Provider / Model configuration surface；没有已授权 Provider Profile、Model revision mapping、capability preflight 或 Run
- Authority Boundary: 模型显示名相同、协议标称兼容、配置解析成功或模型可选择都不能证明 revision、tool protocol、routing、quota 与 capability 可比
- Blocks Current Research?: YES；不满足 gate 的 `EXP-C08-02` 或 `EXP-C08-03` 保持 `PLANNED · NOT EXECUTED`，另一实验可以独立执行，但不能替代前者或满足 Cycle 8 Exit Criteria
- Priority: HIGH
- Candidate Cycle: Cycle 8 / Cycle 9
- Status: BACKLOG

### OQ-008 · OpenCode CLI / TUI、desktop 与 IDE extension 是否共享同一 Host semantic？

- Discovered In: Batch 5 / Cycle 8 official Contract registration
- Why It Matters: OpenCode Intro 同时列出 terminal、desktop 与 IDE surface；如果直接合并，可能把 config、instruction、agent、tool、permission、session 或 extension 在一个 surface 的 Contract / Behavior 外推到其他 surface
- Current Evidence: 只有计划态 `SRC-OPENCODE-001..012`；尚未绑定各 surface 的 OpenCode version、platform、installation artifact、source revision 或 Behavior Run
- Authority Boundary: 官方 Intro 只能证明公开列出的 surface；共享产品名、repository 或配置格式不能证明 surface parity、共同 Runtime path 或相同行为
- Blocks Current Research?: NO；Cycle 8 先限定实际实验 surface，其余 surface 保持 `Unknown`
- Priority: HIGH
- Candidate Cycle: Cycle 8 / Cycle 9 cross-host abstraction
- Status: BACKLOG

### OQ-009 · 哪些四宿主 surface / Provider / Model 组合能通过 Cycle 9 target comparability gate？

- Discovered In: Batch 6 / Cycle 9 experiment design
- Why It Matters: `EXP-C09-01` 需要把 Host semantic route 与 Provider / Model outcome 分开，`EXP-C09-02` 又要求在同一目标 Host 内固定 surface、Provider、Model、permission 与 source capability revision；若只能取得不同 surface 或不同 Model 的 Run，porting method effect 无法裁决
- Current Evidence: 只有 Cycle 3–8 与 `SRC-CROSSHOST-001..005` 的计划态来源；没有绑定四宿主版本的 Host Profile、Provider Profile、共同 task Run、source-host Project / Behavior baseline 或 `EVD-*`
- Authority Boundary: 产品名、CLI 可安装、Agent Skills 格式、相同 Tool 名、相同模型显示名、Provider 协议兼容或最终任务成功都不能证明 target strata 可比
- Blocks Current Research?: YES；不阻塞 Contract question map，但不满足 Gate 的 Host stratum 保持 `PLANNED · NOT EXECUTED / UNKNOWN`，不能进入 Cycle 9 portability Result
- Priority: HIGH
- Candidate Cycle: Cycle 9
- Status: BACKLOG

### OQ-010 · 如何在不同 Host 中可靠区分 Skill Discovery 与 Activation？

- Discovered In: Batch 7 / Cycle 10 experiment design
- Why It Matters: `EXP-C10-01` 与 `EXP-C10-02` 需要把 description effect 与正文 procedure effect 分开；若 Host 只暴露最终调用或结果，就无法知道 Skill 是未发现、未激活还是已加载但未遵循
- Current Evidence: 只有 `SRC-HARNESS-001..004` 的计划态来源；没有绑定 Host / surface 的 discovery trace 或 `EVD-*`
- Authority Boundary: Skill 文件存在、最终输出提到 Skill、用户显式命名 Skill 或任务成功都不能单独证明自动 Discovery / Activation
- Blocks Current Research?: YES；不阻塞 query / oracle 设计，但阻塞不可观察 Host stratum 的 Discovery Result
- Priority: HIGH
- Candidate Cycle: Cycle 10
- Status: BACKLOG

### OQ-011 · 历史 Change 的 evaluator-only truth map 需要什么最低 Project Evidence？

- Discovered In: Batch 7 / Cycle 11 experiment design
- Why It Matters: 如果 Spec、CI、外部 issue 或关闭时状态缺失，人工 oracle 可能把 retention gap 误判为 drift，进而污染 checklist recall / false-positive 裁决
- Current Evidence: 尚未选择历史 Change；`SRC-HARNESS-005..006` 与 `SRC-HARNESS-013` 只提供 reference workflow，不证明 myharness artifact truth
- Authority Boundary: 当前分支状态、目录存在、Agent summary 或单一评审者记忆不能补写历史事实
- Blocks Current Research?: YES；最低 packet gate 未满足时 `EXP-C11-01` 保持 `NOT EXECUTED`
- Priority: HIGH
- Candidate Cycle: Cycle 11
- Status: BACKLOG

### OQ-012 · Adaptive Workflow 的 risk classifier 如何在不看结果的情况下校准？

- Discovered In: Batch 7 / Cycle 12 experiment design
- Why It Matters: 若 risk label 在 escaped failure 或 rework 出现后才确定，route 选择存在 outcome leakage，完整 workflow 与 risk-routed workflow 不可比较
- Current Evidence: `SRC-HARNESS-006..007` 与 `SRC-HARNESS-014` 只登记 OpenSpec / BMAD 浮动来源；尚无 myharness task set、risk rubric、inter-rater result 或 `EVD-*`
- Authority Boundary: artifact 数量、story count、Agent 自报复杂度或 historical severity 不能单独定义 delivery risk
- Blocks Current Research?: YES；不阻塞 rubric 草拟，但阻塞 `EXP-C12-01` 与 `EXP-C12-02` Run
- Priority: HIGH
- Candidate Cycle: Cycle 12
- Status: BACKLOG

### OQ-013 · Session Handoff mode 如何在不混入 phase 与 trajectory 差异时比较？

- Discovered In: Batch 7 / Cycle 13 experiment design
- Why It Matters: 单个任务的 Research、Plan、Implement、Review transition 天然不同；轮换 Resume、自由摘要与结构化 artifact 只能探索遗漏位置，不能裁决 mode 优劣
- Current Evidence: `SRC-HARNESS-008..009` 与 Cycle 3–6 Host sources 只有计划态锚点；没有 matched tasks、balanced order 或 Behavior Run
- Authority Boundary: 恢复速度、Context token 数、任务完成或作者案例不能单独证明 handoff completeness / correctness
- Blocks Current Research?: NO；`EXP-C13-01` 可保持 exploratory，但 comparative claim 被阻塞
- Priority: MEDIUM
- Candidate Cycle: Cycle 13 follow-up
- Status: BACKLOG

### OQ-014 · 什么 recurrence / authority threshold 足以把观察固化为永久 Harness？

- Discovered In: Batch 7 / Cycle 14 experiment design
- Why It Matters: 阈值过低会制造 Rule / Skill / Hook 债务，过高会重复失败；严重性、复发概率、可确定验证性与维护成本需要独立处理
- Current Evidence: `SRC-HARNESS-010..012` 只提供项目 / 论文参考；尚未选择十个 myharness packets，没有 reviewer agreement 或 future recurrence Evidence
- Authority Boundary: 单次事故、Agent 总结、社区 pattern、论文结论或高 severity 不能自动批准 ratification
- Blocks Current Research?: NO；可先做 exploratory classification，但不能直接修改 Harness 或声称 future reliability 改善
- Priority: HIGH
- Candidate Cycle: Cycle 14 / Cycle 15 audit / Cycle 16 hypothesis
- Status: BACKLOG

### OQ-015 · 哪些 historical Change packets 足以支持只读架构 Finding？

- Discovered In: Batch 8 / Cycle 15 experiment design
- Why It Matters: 缺失 Spec、issue、CI、outcome 或固定 revision 时，审计者可能把 retention gap、路径迁移或个人偏好误写成架构问题
- Current Evidence: Batch 8 已规划 Coverage Matrix 与 8 个 dimension packets，但尚未固定 myharness commit 或选择 artifacts；Cycle 11 / 14 只有计划态 dataset gate，没有 Project Evidence 或 `EVD-*`
- Authority Boundary: 当前目录、旧 V4.1 路径、Agent 推断、单一 summary 或 Reference Pattern 都不能补写历史项目事实
- Blocks Current Research?: YES；不阻塞 audit rubric 草拟，但阻塞 `EXP-C15-01` Run
- Priority: HIGH
- Candidate Cycle: Cycle 15
- Status: BACKLOG

### OQ-016 · 八维评分在 reviewer 与权重变化下是否足够稳定？

- Discovered In: Batch 8 / Cycle 16 experiment design
- Why It Matters: relevance、value、portability 与成本可能采用不同方向和尺度；若轻微权重变化就改变 Top3，单一总分会制造伪精确决策
- Current Evidence: 没有 Cycle 15 Finding、评分 rubric、sensitivity analysis 或 independent portfolio Run
- Authority Boundary: Agent agreement、总分高低或 owner preference 不能提升 Evidence Strength；Reversibility 与 evidence gate 不得被加权平均覆盖
- Blocks Current Research?: YES；Cycle 16 可准备模板，但没有真实 finding packet 时 `EXP-C16-01` 保持 `NOT EXECUTED`
- Priority: HIGH
- Candidate Cycle: Cycle 16
- Status: BACKLOG

### OQ-017 · 候选最小实现如何证明只改变了一个机制？

- Discovered In: Batch 8 / Cycle 17 experiment design
- Why It Matters: shared refactor、依赖升级、configuration drift、Agent 自由修改或不对称 Human intervention 都会让 A0 / A1 comparison 失去解释力
- Current Evidence: Batch 8 已把 one-time H1 build、H0 / H1 revisions 与共同 task-fixture baseline 分开，但没有实际 ADR Candidate、implementation diff、paired Run 或 rollback artifact
- Authority Boundary: 小 diff、测试通过、branch 隔离或实现者声明都不能单独证明 single-variable isolation
- Blocks Current Research?: YES；任一 candidate readiness gate 未满足时，对应 `EXP-C17-0x` 保持 `NOT EXECUTED`
- Priority: HIGH
- Candidate Cycle: Cycle 17
- Status: BACKLOG

### OQ-018 · Native Host、Current myharness 与 experimental variant 如何通过 matrix parity gate？

- Discovered In: Batch 8 / Cycle 18 experiment design
- Why It Matters: B0 / A0 / A1 的可用 surface、Tool、permission、Context 与 task path 可能天然不同；若无法固定同一任务和 Host stratum，所谓边际贡献会混入 capability availability
- Current Evidence: Batch 8 已规划 candidate × Host 独立 records 与 Applicability Matrix，但没有 eligible Cycle 17 variant、固定 T03 tasks、Host / Provider profiles、activation trace、matrix cell 或 Run
- Authority Boundary: 任务成功、相同 Model 显示名、相近 prompt、工具名称相同、文件已加载或单次成本下降都不能证明 matrix parity / actual activation
- Blocks Current Research?: YES；不满足 parity 的 Host stratum 保持 `NOT EXECUTED / INCONCLUSIVE`
- Priority: HIGH
- Candidate Cycle: Cycle 18
- Status: BACKLOG

## Template

<!--
### OQ-XXX · <Question>

- Discovered In: Cycle / Experiment / Evidence ID
- Why It Matters:
- Current Evidence:
- Authority Boundary:
- Blocks Current Research?: YES / NO
- Priority: HIGH / MEDIUM / LOW
- Candidate Cycle:
- Status: BACKLOG
-->
