# ADR Candidates

这里维护真实 Cycle 16 执行后产生的实验型 ADR Candidate。Batch 8 内容生成阶段没有实际候选；不得仅因计划正文、评分或示例存在就创建 `ADR-*`。

候选首次创建时只能标记 `PROPOSED`，进入 Cycle 17 实验时才可标记 `EXPERIMENT`。Cycle 18 引用有效 `EVD-*` 后，才能更新最终 Decision。

建议状态：

```text
PROPOSED
EXPERIMENT
ACCEPTED
REJECTED
REVISE
MORE EVIDENCE REQUIRED
```

使用 `../templates/adr-candidate.template.md`。
