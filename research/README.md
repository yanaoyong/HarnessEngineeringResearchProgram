# V4.2 Research Workspace

> Batch 0 已冻结公共协议；Batch 1 和 Cycle 1–18 正文尚未生成。

这里存放执行 Research Program 后产生的真实研究制品。工作区按真实 Cycle 自然生长，不预创建 18 个空目录。

## Protocol

- [Stable Task Suite · T01–T03](task-suite.md)
- [Evidence Classification and Source Authority](source-authority.md)
- [Host Support Levels · S0–S4](support-levels.md)
- [V4.2 Common Glossary](../docs/09-V4.2-Glossary.md)
- [Research Infrastructure](../docs/06-Research-Infrastructure.md)

## Principles

- 一个 Cycle 只有一个核心 Research Question。
- 新 Experiment 使用 `EXP-Cxx-yy`，每次执行保存独立 run metadata。
- Host、Provider、Model 与 Configuration 分开记录。
- Evidence 保留到足以复查，不追求复杂 observability platform。
- Community Claim 只进入 Open Questions，不能证明官方 Contract 或 Architecture。
- `INCONCLUSIVE` 是合法结果。
- Route Review 可以调整路线，但必须记录为什么改。
- Batch 0 不预设任何 Host 已达到 S1–S4。

## Directory

```text
research/
├── task-suite.md
├── source-authority.md
├── support-levels.md
├── open-questions.md
├── cycles/
├── route-reviews/
├── adr-candidates/
├── templates/
└── design-beliefs.md
```

开始真实 Cycle 1 时才可以创建：

```text
research/cycles/cycle-01/
├── research-note.md
├── experiments/
└── evidence/
```

建议复制 `research/templates/` 中的模板，不要为每个 Cycle 重新发明协议。

## V4.1 Historical Content

V4.1 正文中的 `Week`、`week-xx/` 示例和 `EXP-Wxx-yy` 是待迁移历史内容。旧 Evidence ID 不重新编号；新制品不得继续使用 Week 命名。
