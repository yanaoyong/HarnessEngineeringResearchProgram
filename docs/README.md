# 文档导航（Documentation Map）

> 当前有效计划：V4.3
>
> 协议组成：V4.2 Batch 0 common protocol + V4.3 Qwen Code Host-set Amendment
>
> 内容状态：Batch 1–8 / Cycle 1–18 已生成；研究执行尚未开始

[返回仓库首页](../README.md) · [贡献指南](../CONTRIBUTING.md) · [研究工作区](../research/README.md) · [Cycle 索引](../research/cycles/README.md)

## 从哪里开始（Start Here）

| 目标 | 推荐入口 |
|---|---|
| 理解计划、阶段与当前状态 | [研究计划总纲](00-研究计划总纲.md) |
| 理解当前有效协议 | [V4.2 Batch 0 Protocol](08-V4.2-Batch0-Protocol.md) + [V4.3 Amendment](10-V4.3-Qwen-Code-Host-Amendment.md) |
| 查询冻结术语 | [V4.2 Common Glossary](09-V4.2-Glossary.md) |
| 查看 18 个 Cycle 正文 | 下方 Batch / Cycle 导航 |
| 查看计划实验和 Source Registry | [研究工作区](../research/README.md) |
| 了解 Evidence 与 Source 权限 | [Source Authority](../research/source-authority.md) |
| 提交内容修正或研究提案 | [贡献指南](../CONTRIBUTING.md) |

## Batch / Cycle 内容导航

| Batch | Cycle | 当前正文 | Workspace |
|---:|---:|---|---|
| 1 | C01–C02 | [Agent 与 Harness 基础认知](01-Agent与Harness基础认知.md) | [Cycle 01](../research/cycles/cycle-01/research-note.md) · [Cycle 02](../research/cycles/cycle-02/research-note.md) |
| 2 | C03–C04 | [Claude Code Host](02-Coding-Agent-Host-Model.md) | [Cycle 03](../research/cycles/cycle-03/research-note.md) · [Cycle 04](../research/cycles/cycle-04/research-note.md) |
| 3 | C05–C06 | [Codex Host](02-Coding-Agent-Host-Model.md) | [Cycle 05](../research/cycles/cycle-05/research-note.md) · [Cycle 06](../research/cycles/cycle-06/research-note.md) |
| 4 | C07 | [Qwen Code Host](02-Coding-Agent-Host-Model.md) | [Cycle 07](../research/cycles/cycle-07/research-note.md) |
| 5 | C08 | [OpenCode Host](02-Coding-Agent-Host-Model.md) | [Cycle 08](../research/cycles/cycle-08/research-note.md) |
| 6 | C09 | [Four-host Harness Abstraction](03-Cross-host-Harness-Abstraction.md) | [Cycle 09](../research/cycles/cycle-09/research-note.md) |
| 7 | C10–C14 | [Harness Engineering Research Themes](04-Harness-Engineering-Research-Themes.md) | [Cycle 10–14](../research/cycles/README.md) |
| 8 | C15–C18 | [myharness Integration Research](05-myharness-Integration-Research.md) | [Cycle 15–18](../research/cycles/README.md) |

## 协议与基础设施

- [Research Infrastructure](06-Research-Infrastructure.md)：Research Note、Experiment、Run、Evidence、Support 与自动完整性门禁。
- [Reference Project Atlas](07-Reference-Project-Atlas.md)：当前 active overlay 与 V4.1 historical mapping。
- [Stable Task Suite](../research/task-suite.md)：T01–T03 的稳定任务语义。
- [Support Levels](../research/support-levels.md)：S0–S4 与证据绑定要求。
- [Open Questions](../research/open-questions.md)：尚未解决、不得越权升级为结论的问题。

## 当前效力与历史边界

- `docs/08-V4.2-Batch0-Protocol.md` 是冻结的 V4.2 历史基线，其中 ZCode 表述不代表 V4.3 当前 Host 集合。
- `docs/10-V4.3-Qwen-Code-Host-Amendment.md` 对 Host 集合、Cycle 7 和相关 Source Authority 具有当前效力。
- `docs/01` 至 `docs/05` 是已迁移的 Cycle 正文；其中 V4.1 Week / `EXP-Wxx-yy` 只作为 historical mapping。
- 所有 Cycle 仍为 `PLANNED · NOT EXECUTED`；目录和实验设计存在不表示实验已运行。

## 公共仓库入口

- 内容错误、断链、状态或 Source Registry 问题：使用 GitHub 的 Content correction Issue Form。
- 真实研究执行建议：使用 Research execution proposal Issue Form；Issue 不等于授权执行或产生结果。
- 安全问题：遵循 [Security Policy](../SECURITY.md)，不要创建公开 Issue。
- 治理与决策权限：参见 [Governance](../GOVERNANCE.md) 与 [Code of Conduct](../CODE_OF_CONDUCT.md)。

仓库当前没有声明项目级 `LICENSE`。公开可见不等于授予复制、修改或再分发许可；许可证选择由 repository owner 单独决定。
