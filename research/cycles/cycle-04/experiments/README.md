# Cycle 04 实验工作区（Experiment Workspace）

> 状态（Status）：PREPARED · NOT EXECUTED

本目录为后续实现预先准备。计划实验：

- `EXP-C04-01` · HTTP timeout Rule / Skill / deterministic Check responsibility comparison

真实执行开始后，使用 [实验记录模板](../../../templates/experiment-record.template.md) 创建 Experiment Record，并为 A/B/C 各保存独立 Run Metadata。所有 variant 必须共享同一 T01 task statement、timeout acceptance contract 与 pass / fail fixture；fallback / degradation 不进入本实验。在此之前不得填写结果或派生 `EVD-*`。
