# Harness Engineering Research Program

> 面向 `myharness` 的 Harness Engineering 研究—实践—认知升级计划。

## Current Status

- Program：V4.2
- Structure：18 Cycle-based research cycles
- Batch 0：已冻结公共协议
- Batch 1：尚未生成
- V4.1 baseline：提交 `f2b3961cbe125f846818d11a8892fe3c34f2751f`

Batch 0 只建立所有后续 Cycle 共用的术语、证据权限、任务套件、实验元数据、支持等级、工作区命名与迁移边界。当前没有生成 Cycle 1–18 正文。

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

| Phase / Batch | Cycles | Theme |
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

## V4.2 Protocol Navigation

1. [研究计划总纲](docs/00-研究计划总纲.md)
2. [V4.2 Batch 0 Common Protocol](docs/08-V4.2-Batch0-Protocol.md)
3. [V4.2 Common Glossary](docs/09-V4.2-Glossary.md)
4. [Stable Task Suite · T01–T03](research/task-suite.md)
5. [Evidence Classification and Source Authority](research/source-authority.md)
6. [Host Support Levels · S0–S4](research/support-levels.md)
7. [Research Infrastructure](docs/06-Research-Infrastructure.md)
8. [Research Workspace](research/README.md)

## V4.1 Content Baseline

以下正文保留为后续内容 Batch 的迁移基线，当前仍是 V4.1 Week-based 内容：

- [Agent 与 Harness 基础认知](docs/01-Agent与Harness基础认知.md)
- [Coding Agent Host Model](docs/02-Coding-Agent-Host-Model.md)
- [Cross-host Harness Abstraction](docs/03-Cross-host-Harness-Abstraction.md)
- [Harness Engineering Research Themes](docs/04-Harness-Engineering-Research-Themes.md)
- [myharness Integration Research](docs/05-myharness-Integration-Research.md)
- [Reference Project Atlas](docs/07-Reference-Project-Atlas.md)

其中的 `Week` 与 `EXP-Wxx-yy` 在对应内容 Batch 迁移前保持历史形态，不代表 Cycle 正文已经生成。

## Four-host Research Roles

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
- Research Workspace 按真实 Cycle 生长，不预创建 18 个空目录。
- Batch 0 不预设任何 Host 已达到 S1–S4。

详见 [Changelog](CHANGELOG.md)。
