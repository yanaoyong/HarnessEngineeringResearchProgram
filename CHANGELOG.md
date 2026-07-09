# Changelog

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
