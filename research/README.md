# Research Workspace

这里存放执行 Research Program 产生的真实研究制品。

## 原则

- 按真实研究生长，不提前创建 16 个空 Week 目录。
- 一个研究循环只有一个核心 Research Question。
- Open Questions 可以很多，但默认不立即展开。
- Experiment 必须标明 `EXPLORATORY / COMPARATIVE / ABLATION`。
- Evidence 保留到足以复查，不追求建立复杂 observability platform。
- `INCONCLUSIVE` 是合法结果。
- Route Review 可以调整计划，但必须记录为什么改。

## 目录

```text
research/
├── open-questions.md
├── cycles/
├── route-reviews/
├── adr-candidates/
├── templates/
└── design-beliefs.md
```

开始 Week 1 时再创建：

```text
research/cycles/week-01/
├── research-note.md
├── experiments/
└── evidence/
```

建议从 `research/templates/` 复制模板，而不是每次重新设计格式。
