# V4.2 研究工作区（Research Workspace）

> Batch 0 已冻结公共协议；Batch 1–8 的 C01–C18 正文与计划态 Research Note 已生成，研究执行尚未开始。

这里存放 Research Program 内容准备与执行产生的真实研究制品。计划态制品必须明确标记 `NOT EXECUTED`；工作区按内容 Batch 生长，不一次性预创建 18 个空目录。

## 协议（Protocol）

- [Stable Task Suite · T01–T03](task-suite.md)
- [Evidence Classification and Source Authority](source-authority.md)
- [Host Support Levels · S0–S4](support-levels.md)
- [V4.2 Common Glossary](../docs/09-V4.2-Glossary.md)
- [Research Infrastructure](../docs/06-Research-Infrastructure.md)

## 原则（Principles）

- 一个 Cycle 只有一个核心 Research Question。
- 新 Experiment 使用 `EXP-Cxx-yy`，每次执行保存独立 run metadata。
- Host、Provider、Model 与 Configuration 分开记录。
- Evidence 保留到足以复查，不追求复杂 observability platform。
- Community Claim 只进入 Open Questions，不能证明官方 Contract 或 Architecture。
- `INCONCLUSIVE` 是合法结果。
- Route Review 可以调整路线，但必须记录为什么改。
- 当前不预设任何 Host 已达到 S1–S4。

## 目录（Directory）

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

Batch 1–8 已创建十八个非空的计划态 Cycle workspace：

```text
research/cycles/cycle-01/
├── research-note.md
├── experiments/
│   └── README.md
└── evidence/
    └── SRC-FOUNDATION-001..003.md

research/cycles/cycle-02/
├── research-note.md
├── experiments/
│   └── README.md
└── evidence/
    └── SRC-FOUNDATION-004.md

research/cycles/cycle-03/
├── research-note.md
├── experiments/
│   └── README.md
└── evidence/
    └── SRC-CLAUDE-001..004.md + SRC-CLAUDE-006.md；复用 Cycle 2 SRC-FOUNDATION-004

research/cycles/cycle-04/
├── research-note.md
├── experiments/
│   └── README.md
└── evidence/
    └── SRC-CLAUDE-007..010.md

research/cycles/cycle-05/
├── research-note.md
├── experiments/
│   └── README.md
└── evidence/
    └── SRC-CODEX-001..005.md

research/cycles/cycle-06/
├── research-note.md
├── experiments/
│   └── README.md
└── evidence/
    └── SRC-CODEX-006..010.md

research/cycles/cycle-07/
├── research-note.md
├── experiments/
│   └── README.md
└── evidence/
    └── SRC-ZCODE-001..009.md

research/cycles/cycle-08/
├── research-note.md
├── experiments/
│   └── README.md
└── evidence/
    └── SRC-OPENCODE-001..012.md

research/cycles/cycle-09/
├── research-note.md
├── experiments/
│   └── README.md
└── evidence/
    └── SRC-CROSSHOST-001..005.md

research/cycles/cycle-10/
├── research-note.md
├── experiments/
│   └── README.md
└── evidence/
    └── SRC-HARNESS-001..002.md；复用 Cycle 2 / 9 来源

research/cycles/cycle-11/
├── research-note.md
├── experiments/
│   └── README.md
└── evidence/
    └── SRC-HARNESS-005..006.md + SRC-HARNESS-013.md

research/cycles/cycle-12/
├── research-note.md
├── experiments/
│   └── README.md
└── evidence/
    └── SRC-HARNESS-007.md + SRC-HARNESS-014.md

research/cycles/cycle-13/
├── research-note.md
├── experiments/
│   └── README.md
└── evidence/
    └── SRC-HARNESS-009.md；复用 Cycle 3 SRC-CLAUDE-006

research/cycles/cycle-14/
├── research-note.md
├── experiments/
│   └── README.md
└── evidence/
    └── SRC-HARNESS-010.md；复用 Cycle 1 SRC-FOUNDATION-002..003

research/cycles/cycle-15..18/
├── research-note.md
├── experiments/
│   └── README.md
└── evidence/
    └── README.md
```

`experiments/` 已为后续实现准备，但只包含计划状态说明；Cycle 1–14 的 `evidence/` 包含已登记、尚未派生 `EVD-*` 的 Source Registry entries，Cycle 15–18 的 `evidence/README.md` 只说明未来 Project / Run evidence 门禁。实验尚未执行，因此没有 Experiment Record、Run record、Finding、ADR Candidate、implementation artifact、Decision Update 或 Design Belief。执行真实研究时再按模板增加制品，不要为每个 Cycle 重新发明协议。

## V4.1 历史内容（Historical Content）

V4.1 正文中的 `Week`、`week-xx/` 示例和 `EXP-Wxx-yy` 是历史迁移来源。Week 1–16 已全部迁移；旧实验 ID 只作为 historical plan mapping 保留。Cycle 7–8 是 V4.2 新增内容，没有旧 Week / 实验 ID。旧 Evidence ID 不重新编号；新制品不得继续使用 Week 命名。
