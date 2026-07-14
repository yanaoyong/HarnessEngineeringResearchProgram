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
- Current Evidence: None registered
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
