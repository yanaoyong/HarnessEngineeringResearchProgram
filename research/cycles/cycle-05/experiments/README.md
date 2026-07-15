# Cycle 05 实验工作区（Experiment Workspace）

> 状态（Status）：PREPARED · NOT EXECUTED

本目录为后续实现预先准备。计划实验：

- `EXP-C05-01` · Contract → Source → Behavior Architecture Trace
- `EXP-C05-02` · Skill Description Discovery Comparison
- `EXP-C05-03` · AGENTS Scope and Override Comparison
- `EXP-C05-04` · Plugin Distribution and Load Boundary Trace

真实执行开始后，使用 [实验记录模板](../../../templates/experiment-record.template.md) 创建独立 Experiment Record，并为每次执行保存独立 Run Metadata。`EXP-C05-01` 使用 `OBSERVATION_ONLY`，只生成三层 architecture question map，Experiment Result 为 `NOT APPLICABLE · OBSERVATION ONLY`；`EXP-C05-02..04` 使用 `HYPOTHESIS_RESULT`。`EXP-C05-02` 必须保持 Skill body、name、scope、location 与 T02 instance 相同，只改变 description；`EXP-C05-03` 必须使用相同 root instruction、target / control fixture 与 acceptance checks，只改变 nested `AGENTS.md`；`EXP-C05-04` 必须固定既有 Plugin revision 与 capability body，只改变 Plugin 是否启用。没有符合边界的既有 Plugin capability 时，`EXP-C05-04` 保持 `NOT EXECUTED`，不得临时实现 Plugin。在此之前不得填写结果、Architecture V1 / V2 或派生 `EVD-*`。
