# Harness Engineering Research Program

> 面向 `myharness` 的 Harness Engineering 研究—实践—认知升级计划。

本仓库不是一份固定课程表，也不是“16 周读完若干开源项目”的打卡清单。

它是一套研究导航：从 Coding Agent 最小模型出发，理解 Claude Code 与 Codex 这类 Host 的工作方式，建立跨宿主抽象，再围绕 Skill、Change、Workflow、Context、Knowledge 等 Harness Engineering 问题开展小实验，最终回到 `myharness` 做审计、提出假设、验证设计判断，并沉淀当前阶段的 Design Beliefs。

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

## 16 个研究循环

| Part | 主题 | 研究周期 |
|---|---|---|
| I | 研究计划总纲 | 全程 |
| II | Agent 与 Harness 基础认知 | Week 1–2 |
| III | Coding Agent Host Model | Week 3–6 |
| IV | Cross-host Harness Abstraction | Week 7 |
| V | Harness Engineering Research Themes | Week 8–12 |
| VI | myharness Integration Research | Week 13–16 |
| VII | Research Infrastructure | 全程 |
| VIII | Reference Project Atlas | 按问题使用 |

## 文档导航

1. [PART I · 研究计划总纲](docs/00-研究计划总纲.md)
2. [PART II · Agent 与 Harness 基础认知](docs/01-Agent与Harness基础认知.md)
3. [PART III · Coding Agent Host Model](docs/02-Coding-Agent-Host-Model.md)
4. [PART IV · Cross-host Harness Abstraction](docs/03-Cross-host-Harness-Abstraction.md)
5. [PART V · Harness Engineering Research Themes](docs/04-Harness-Engineering-Research-Themes.md)
6. [PART VI · myharness Integration Research](docs/05-myharness-Integration-Research.md)
7. [PART VII · Research Infrastructure](docs/06-Research-Infrastructure.md)
8. [PART VIII · Reference Project Atlas](docs/07-Reference-Project-Atlas.md)

## 使用原则

- “Week” 是研究单元，不是硬性日历门禁。
- 每个研究循环只追一个核心问题；旁支问题进入 Open Questions。
- 开源项目按问题阅读，不按仓库顺序通读。
- 进入 Claude Code、Codex 或大型项目阶段前，先刷新官方资料与默认分支。
- 小实验优先于大重构；实验要尽量保留 baseline、可逆、可复查。
- 允许结果是 `REJECTED`、`REVISE` 或 `INCONCLUSIVE`。
- 计划会随着认知变化而调整；调整路线时记录“为什么改”。

## 当前版本

- Program：V4
- 文档形态：8-Part 分卷导航版
- 基准日期：2026-07-09
- 状态：Draft / 可随研究结果迭代
