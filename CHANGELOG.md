# Changelog

## V4.2 Batch 0 · 2026-07-14

V4.2 Batch 0 只冻结公共研究协议。Batch 1 与 Cycle 1–18 正文尚未生成。

### Program Protocol

- 将 Program 从 16 Week 调整为 18 Cycle，并冻结 Cycle 名称、顺序、8 个 Phase 与 Batch 1–8 边界。
- 增加 ZCode 与 OpenCode 研究角色，将原 Week 7 之后内容顺延到 Cycle 9–18。
- 保留 V4.1 内容文件和 `EXP-Wxx-yy` 作为后续内容 Batch 的迁移基线。

### Evidence and Evaluation

- 冻结公共术语以及 Contract、Source、Behavior、Project、Enterprise、Community 六类来源。
- 增加 ZCode Source Authority Gate；未验证官方 Runtime source 时禁止源码架构结论。
- 增加 `T01 · Engineering Constraint`、`T02 · Semantic Review`、`T03 · Medium Change`。
- 新实验使用 `EXP-Cxx-yy`，Run Metadata 分离 Host、Provider、Model、配置、revision、confounder、Evidence 与人工干预。
- 增加 S0–S4 Host Support Levels，且不预设任何 Host 已达到 S1–S4。

### Research Workspace

- 新研究工作区使用 `cycle-xx/`，但不预创建 Cycle 目录。
- 增加 Source Registry、Host Profile、Provider Profile 与 Enterprise Readiness Fact Sheet 模板。

### Non-goals

- 不生成 Cycle 正文，不实现 Batch 1、myharness feature、OpenCode Adapter 或 ZCode Plugin。
- 不创建法律合规结论，不提交或推送。

## V4.1 · 2026-07-09

V4.1 是文档工程与研究基础设施修订，不改变 Week 1–16 的核心研究主题和顺序。

### Documentation Engineering

- 清理 16 个 Week 的 Word / Pandoc HTML 核心问题表格，改为原生 Markdown。
- 每个 Week 的实践增加 `EXP-Wxx-01` Experiment ID。
- 每个 Experiment 标注 `EXPLORATORY / COMPARATIVE / ABLATION`。
- 将跨 Week 的全局步骤编号改为 Week 内局部编号。
- Week 4 比较实验改为共享 Rule baseline，减少多变量混杂。
- Week 11 明确 Handoff Modes 为 exploratory qualitative evidence。

### Research Infrastructure

- 补充 ADR Candidate Template。
- 补充 Open Questions / Research Backlog。
- 补充每 2–4 个研究循环一次的 Route Review。
- 增加轻量 `research/` 工作区与可复制模板。
- 不预创建 16 个空 Week 目录，按真实研究自然生长。

### Research Navigation

- Week 7 将 `Superpowers docs/porting-to-a-new-harness.md` 升级为 L3 主锚点。
- Week 7 从“看多宿主目录表面”升级为研究 port invariants、tool mapping、bootstrap、supportability 与 definition of done。
- BMAD 与 Agent OS 改为 Capability-first 动态源码定位，不把当前目录写成永久 Contract。
- Reference Project Atlas 从 Link Index 升级为 Research Role / Primary Question / Depth / Week / Primary Anchor / Do Not Study 图谱。
- Week 16 移除模糊的“过程评测资料”占位，复用前 15 周积累的过程证据。

### Non-goals

- 不增加新的 Week。
- 不调整 16 周主题顺序。
- 不新增大规模 Eval / Observability 学习专题。
- 不借 V4.1 重构 myharness。
