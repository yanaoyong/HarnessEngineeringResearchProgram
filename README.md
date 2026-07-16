# Harness Engineering Research Program

[![Content integrity](https://github.com/yanaoyong/HarnessEngineeringResearchProgram/actions/workflows/content-integrity.yml/badge.svg)](https://github.com/yanaoyong/HarnessEngineeringResearchProgram/actions/workflows/content-integrity.yml)

> 面向 `myharness` 的 Harness Engineering 研究—实践—认知升级计划。

## 快速导航（Quick Navigation）

| 你要做什么 | 入口 |
|---|---|
| 阅读计划与 Cycle 正文 | [文档导航](docs/README.md) |
| 查看计划实验与 Source Registry | [研究工作区](research/README.md) |
| 查询 Cycle 1–18 状态 | [Cycle 索引](research/cycles/README.md) |
| 提交贡献 | [贡献指南](CONTRIBUTING.md) |
| 了解维护与决策权限 | [仓库治理](GOVERNANCE.md) |
| 私下报告安全问题 | [Security Policy](SECURITY.md) |

## 当前状态（Current Status）

- 计划（Program）：V4.3
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
- 当前活动内容 Batch：无；Batch 1–8 内容生成已完成
- V4.3 Amendment：ZCode 已由 Qwen Code 取代；Cycle / Batch / Experiment 编号保持不变
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

## V4.3 · 18 个研究循环

| 阶段（Phase）/ Batch | Cycle | 主题（Theme） |
|---|---:|---|
| Foundation / Batch 1 | C01–C02 | Coding Agent 最小模型、Harness Primitive |
| Claude Code Host / Batch 2 | C03–C04 | Context Lifecycle、Extension & Control Surface |
| Codex Host / Batch 3 | C05–C06 | Architecture & Customization、Execution、Safety & State |
| Qwen Code Host / Batch 4 | C07 | Host Architecture & Enterprise Reality |
| OpenCode Host / Batch 5 | C08 | Host Architecture & Model Portability |
| Four-host Abstraction / Batch 6 | C09 | Four-host Harness Abstraction |
| Harness Engineering / Batch 7 | C10–C14 | Skill、Change、Workflow、Context、Knowledge |
| Integration Research / Batch 8 | C15–C18 | Audit、Hypothesis、Experiment、Acceptance |

18 个 Cycle 的编号、顺序与迁移映射源自 [V4.2 Batch 0 Protocol](docs/08-V4.2-Batch0-Protocol.md)；当前 Host 集合与 Cycle 7 名称以 [V4.3 Qwen Code Host-set Amendment](docs/10-V4.3-Qwen-Code-Host-Amendment.md) 为准。

## V4.3 协议导航（Protocol Navigation）

1. [Documentation Map](docs/README.md)
2. [研究计划总纲](docs/00-研究计划总纲.md)
3. [V4.2 Batch 0 Common Protocol](docs/08-V4.2-Batch0-Protocol.md)
4. [V4.2 Common Glossary](docs/09-V4.2-Glossary.md)
5. [V4.3 Qwen Code Host-set Amendment](docs/10-V4.3-Qwen-Code-Host-Amendment.md)
6. [Stable Task Suite · T01–T03](research/task-suite.md)
7. [Evidence Classification and Source Authority](research/source-authority.md)
8. [Host Support Levels · S0–S4](research/support-levels.md)
9. [Research Infrastructure](docs/06-Research-Infrastructure.md)
10. [Research Workspace](research/README.md)

## V4.3 当前内容（Current Content）

| Batch | Cycle | 内容入口 | Workspace |
|---:|---:|---|---|
| 1 | C01–C02 | [Agent 与 Harness 基础认知](docs/01-Agent与Harness基础认知.md) | [Cycle 01–02](research/cycles/README.md) |
| 2 | C03–C04 | [Claude Code Host](docs/02-Coding-Agent-Host-Model.md) | [Cycle 03–04](research/cycles/README.md) |
| 3 | C05–C06 | [Codex Host](docs/02-Coding-Agent-Host-Model.md) | [Cycle 05–06](research/cycles/README.md) |
| 4 | C07 | [Qwen Code Host](docs/02-Coding-Agent-Host-Model.md) | [Cycle 07](research/cycles/cycle-07/research-note.md) |
| 5 | C08 | [OpenCode Host](docs/02-Coding-Agent-Host-Model.md) | [Cycle 08](research/cycles/cycle-08/research-note.md) |
| 6 | C09 | [Four-host Harness Abstraction](docs/03-Cross-host-Harness-Abstraction.md) | [Cycle 09](research/cycles/cycle-09/research-note.md) |
| 7 | C10–C14 | [Harness Engineering Research Themes](docs/04-Harness-Engineering-Research-Themes.md) | [Cycle 10–14](research/cycles/README.md) |
| 8 | C15–C18 | [myharness Integration Research](docs/05-myharness-Integration-Research.md) | [Cycle 15–18](research/cycles/README.md) |

完整的逐 Cycle 导航、计划状态与 Research Note 入口见 [Cycle 索引](research/cycles/README.md)。

## V4.1 迁移基线（Migration Baseline）

V4.1 Week 1–16 已全部迁移到 V4.2 Cycle 计划态正文。旧 `Week` / `EXP-Wxx-yy` 只在 migration record 与 historical Atlas 中保留，不表示历史实验已执行，也不与 `EXP-Cxx-yy` 重复创建结果。

[Reference Project Atlas](docs/07-Reference-Project-Atlas.md) 保留完整 historical rows，并提供 Batch 1–8 active overlay。Cycle 7–8 是 V4.2 新增内容，没有 V4.1 Week / 实验 ID。

## 四宿主研究角色（Four-host Research Roles）

- Claude Code：mature Harness best-practice reference
- Codex：advanced open-source implementation reference
- Qwen Code：domestic open-source coding-agent、Qwen ecosystem 与 enterprise deployment reality reference
- OpenCode：open-source、multi-provider、vendor-neutral Host reference

Qwen Code 的官方源码判断必须固定 `QwenLM/qwen-code` commit，并将实际执行 artifact 映射到对应 release / revision；OpenCode 研究同样必须固定来源，并分离 Host、Provider 与 Model effects。

## 内容完整性校验（Content Integrity Validation）

仓库使用 [机器可读内容基线](validation/content-baseline.json) 和 [零依赖校验器](scripts/validate_content.py) 防止 Cycle、Experiment、Source Registry、计划状态、内部链接、协议绑定与 Manifest 静默漂移。Pull Request 和 `main` push 会由 GitHub Actions 自动运行：

```bash
python3 scripts/validate_content.py
```

有意增加、删除或修改受管文件后，使用下列命令重建 `MANIFEST.txt`，再审查 Manifest 与基线 diff：

```bash
python3 scripts/validate_content.py --write-manifest
```

基线只声明“当前仓库应当是什么”，不证明来源正确、实验已经执行或研究结论成立。Cycle / Batch / Experiment / Source 集合或 `research_execution` 状态变化必须对应明确的 Program 决策或真实研究制品，不能只为让 CI 通过而修改基线。

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
