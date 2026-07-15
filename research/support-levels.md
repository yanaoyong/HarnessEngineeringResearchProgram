# Host Support Levels · S0–S4

> Status: FROZEN IN BATCH 0
>
> Batch 0 does not assign S1–S4 to any Host.

[返回 Research Workspace](README.md) · [Source Authority](source-authority.md) · [Host Profile Template](templates/host-profile.template.md)

## 1. Purpose

Support Level 描述一个明确 capability scope 在绑定运行条件下的证据成熟度。它不是 Host 的永久总评分，不是产品排名，也不等同于 capability availability。

每个结果必须绑定：

- capability scope
- Host 与 Host version
- Provider profile
- Model ID
- configuration snapshot
- Evidence IDs (`EVD-*`)
- known limitations
- verification date

缺少上述绑定时，不得发布 S1–S4 结果。Support Assessment 必须引用 `EVD-*` claim；Source ID、Run ID、Experiment ID、URL 或文件路径只能作为 supporting Artifact，不能替代 Evidence ID。

## 2. Levels

### S0 · Not Assessed

尚未按本协议评估，或现有证据不足以进入 S1。S0 不表示支持，也不表示不支持。

### S1 · Contract Mapped

已用 Contract Evidence 映射目标 capability 的公开 surface、边界和版本，并明确 `Supported / Unsupported / Unknown`。

S1 不表示完整支持，不证明实际行为，也不表示所有 Provider 或 Model 条件可用。

### S2 · Behavior Verified

在绑定 Host、Provider profile、Model 和 Configuration 下，以 Direct Behavior Evidence 验证关键行为，并记录偏差、失败与限制。

S2 不表示 production ready，不证明企业部署、长期稳定性或所有配置组合。

### S3 · Operationally Verified

在项目相关的重复工作流中验证 capability 的安装或配置、执行、失败处理、升级或回退、证据保留与维护边界。必须包含可复查 Project Evidence。

S3 仍然限定于记录的项目、版本和运行条件，不表示普遍企业适用。

### S4 · Enterprise Profile Verified

在一个明确企业 profile 中验证相关部署、访问控制、运维、安全、审计、支持或治理事实，并记录 Enterprise Fact 与未验证项。

S4 不表示 universal legal compliance，不适用于未记录的组织、地区、合同、Provider、Model 或部署方式。

## 3. Progression Rules

- S1–S4 是证据门槛；更高等级必须保留较低等级需要的绑定和证据。
- Level 按 capability scope 评定，不能因一个能力达到某等级而给整个 Host 同级结论。
- Host、Provider、Model、version 或关键 Configuration 改变后，结果必须重新验证或标记 stale。
- Contract 与 Behavior 冲突时保留冲突，不自动提升等级。
- `Unsupported` 可以是 S1 或更高等级中的受证据支持结果；`Unknown` 不能被包装为支持。
- 没有可复查 Evidence ID 的结果保持 S0。

## 4. Required Result Record

```text
Assessment ID: SUP-<HOST>-<NNN>
Capability Scope:
Support Level: S0 / S1 / S2 / S3 / S4
Availability: SUPPORTED / UNSUPPORTED / UNKNOWN
Host and Version:
Provider Profile:
Model ID:
Configuration Snapshot:
Evidence IDs (EVD-* only):
Known Limitations:
Contradictory Evidence:
Verified On:
Verified By:
Freshness / Revalidation Trigger:
```

## 5. Batch 0 Initialization Rule

Host profile 和 enterprise fact sheet 模板中的 Support Level 字段保持空白或 `S0 · Not Assessed`。当前计划不预设 Claude Code、Codex、Qwen Code 或 OpenCode 的 S1–S4 achievement table。
