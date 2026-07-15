# Harness Engineering Research Program

> 面向 `myharness` 的 Harness Engineering 研究—实践—认知升级计划。

## 当前状态（Current Status）

- 计划（Program）：V4.2
- 结构（Structure）：18 个基于 Cycle 的研究循环
- Batch 0：已冻结公共协议
- Batch 1：C01–C02 正文已生成；研究执行尚未开始
- Batch 2：C03–C04 正文已生成；研究执行尚未开始
- Batch 3：C05–C06 正文已生成；研究执行尚未开始
- Batch 4：C07 正文已生成；研究执行尚未开始
- Batch 5：C08 正文已生成；研究执行尚未开始
- Batch 6：C09 正文已生成；研究执行尚未开始
- Batch 7：C10–C14 正文已生成；研究执行尚未开始
- Batch 8：C15–C18 正文已生成；研究执行尚未开始
- V4.1 基线（Baseline）：提交 `f2b3961cbe125f846818d11a8892fe3c34f2751f`

Batch 0 建立所有后续 Cycle 共用的协议。Batch 1–8 已生成全部 18 个 Cycle 的计划态正文与 Research Note；实验、Evidence Claim、Enterprise Fact、架构审计 Finding、ADR Candidate、实现、Design Belief、结论与 Support Assessment 均尚未产生。内容生成完成不等于研究执行完成。

## 核心研究循环

```text
Research Question
        ↓
Build Mental Model
        ↓
Hypothesis
        ↓
Small Experiment
        ↓
Observe Evidence
        ↓
Update Mental Model
        ↓
Design Judgment
        ↓
Next Question
```

**核心原则：认知必须接受实践攻击，实践必须反过来修正认知。**

## V4.2 · 18 个研究循环

| 阶段（Phase）/ Batch | Cycle | 主题（Theme） |
|---|---:|---|
| Foundation / Batch 1 | C01–C02 | Coding Agent 最小模型、Harness Primitive |
| Claude Code Host / Batch 2 | C03–C04 | Context Lifecycle、Extension & Control Surface |
| Codex Host / Batch 3 | C05–C06 | Architecture & Customization、Execution、Safety & State |
| ZCode Host / Batch 4 | C07 | Host Contract & Enterprise Reality |
| OpenCode Host / Batch 5 | C08 | Host Architecture & Model Portability |
| Four-host Abstraction / Batch 6 | C09 | Four-host Harness Abstraction |
| Harness Engineering / Batch 7 | C10–C14 | Skill、Change、Workflow、Context、Knowledge |
| Integration Research / Batch 8 | C15–C18 | Audit、Hypothesis、Experiment、Acceptance |

18 个 Cycle 的冻结名称、顺序与迁移映射见 [V4.2 Batch 0 Protocol](docs/08-V4.2-Batch0-Protocol.md)。

## V4.2 协议导航（Protocol Navigation）

1. [研究计划总纲](docs/00-研究计划总纲.md)
2. [V4.2 Batch 0 Common Protocol](docs/08-V4.2-Batch0-Protocol.md)
3. [V4.2 Common Glossary](docs/09-V4.2-Glossary.md)
4. [Stable Task Suite · T01–T03](research/task-suite.md)
5. [Evidence Classification and Source Authority](research/source-authority.md)
6. [Host Support Levels · S0–S4](research/support-levels.md)
7. [Research Infrastructure](docs/06-Research-Infrastructure.md)
8. [Research Workspace](research/README.md)

## V4.2 已生成内容（Generated Content）

- [Batch 1 · Cycle 1–2 · Agent 与 Harness 基础认知](docs/01-Agent与Harness基础认知.md)
- [Batch 2 · Cycle 3–4 · Claude Code Host](docs/02-Coding-Agent-Host-Model.md)
- [Batch 3 · Cycle 5–6 · Codex Host](docs/02-Coding-Agent-Host-Model.md)
- [Batch 4 · Cycle 7 · ZCode Host](docs/02-Coding-Agent-Host-Model.md)
- [Batch 5 · Cycle 8 · OpenCode Host](docs/02-Coding-Agent-Host-Model.md)
- [Batch 6 · Cycle 9 · Four-host Harness Abstraction](docs/03-Cross-host-Harness-Abstraction.md)
- [Batch 7 · Cycle 10–14 · Harness Engineering Research Themes](docs/04-Harness-Engineering-Research-Themes.md)
- [Batch 8 · Cycle 15–18 · myharness Integration Research](docs/05-myharness-Integration-Research.md)
- [Cycle 1 Research Note](research/cycles/cycle-01/research-note.md)（planned / not executed）
- [Cycle 2 Research Note](research/cycles/cycle-02/research-note.md)（planned / not executed）
- [Cycle 3 Research Note](research/cycles/cycle-03/research-note.md)（planned / not executed）
- [Cycle 4 Research Note](research/cycles/cycle-04/research-note.md)（planned / not executed）
- [Cycle 5 Research Note](research/cycles/cycle-05/research-note.md)（planned / not executed）
- [Cycle 6 Research Note](research/cycles/cycle-06/research-note.md)（planned / not executed）
- [Cycle 7 Research Note](research/cycles/cycle-07/research-note.md)（planned / not executed）
- [Cycle 8 Research Note](research/cycles/cycle-08/research-note.md)（planned / not executed）
- [Cycle 9 Research Note](research/cycles/cycle-09/research-note.md)（planned / not executed）
- [Cycle 10 Research Note](research/cycles/cycle-10/research-note.md)（planned / not executed）
- [Cycle 11 Research Note](research/cycles/cycle-11/research-note.md)（planned / not executed）
- [Cycle 12 Research Note](research/cycles/cycle-12/research-note.md)（planned / not executed）
- [Cycle 13 Research Note](research/cycles/cycle-13/research-note.md)（planned / not executed）
- [Cycle 14 Research Note](research/cycles/cycle-14/research-note.md)（planned / not executed）
- [Cycle 15 Research Note](research/cycles/cycle-15/research-note.md)（planned / not executed）
- [Cycle 16 Research Note](research/cycles/cycle-16/research-note.md)（planned / not executed）
- [Cycle 17 Research Note](research/cycles/cycle-17/research-note.md)（planned / not executed）
- [Cycle 18 Research Note](research/cycles/cycle-18/research-note.md)（planned / not executed）

## V4.1 迁移基线（Migration Baseline）

V4.1 Week 1–16 已全部迁移到 V4.2 Cycle 计划态正文。旧 `Week` / `EXP-Wxx-yy` 只在 migration record 与 historical Atlas 中保留，不表示历史实验已执行，也不与 `EXP-Cxx-yy` 重复创建结果。

[Reference Project Atlas](docs/07-Reference-Project-Atlas.md) 保留完整 historical rows，并提供 Batch 1–8 active overlay。Cycle 7–8 是 V4.2 新增内容，没有 V4.1 Week / 实验 ID。

## 四宿主研究角色（Four-host Research Roles）

- Claude Code：mature Harness best-practice reference
- Codex：advanced open-source implementation reference
- ZCode：domestic model ecosystem and enterprise reality reference
- OpenCode：open-source、multi-provider、vendor-neutral Host reference

ZCode 的 Runtime source architecture 必须通过 Source Authority Gate 才能形成结论。OpenCode 研究必须分离 Host、Provider 与 Model effects。

## 使用原则

- “Cycle”是研究单元，不是硬性日历门禁。
- 每个 Cycle 只追一个核心问题；旁支问题进入 Open Questions。
- 使用 Contract、Source、Behavior、Project、Enterprise 与 Community 六类来源时遵守各自权限。
- 小实验优先于大重构，且必须保留可复查 run metadata。
- T01–T03 只用于方向性比较，不用于公开模型 benchmark。
- `INCONCLUSIVE` 是合法结果。
- Research Workspace 按内容 Batch 生长；Batch 8 已准备 `cycle-01` 至 `cycle-18` 的非空计划态目录。
- Batch 1–8 只创建计划态 Research Note、实验说明、Source Registry entry 或 evidence preparation note；不创建 Experiment Run、`EVD-*` 或 `ENT-*`。
- 当前不预设任何 Host 已达到 S1–S4。

详见 [Changelog](CHANGELOG.md)。
