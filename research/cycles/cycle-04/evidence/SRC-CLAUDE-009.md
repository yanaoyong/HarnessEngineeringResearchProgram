# 来源登记条目（Source Registry Entry）· SRC-CLAUDE-009

## 身份（Identity）

- 来源 ID（Source ID）：`SRC-CLAUDE-009`
- 来源角色（Source Role）：`OFFICIAL CONTRACT`
- 可产生的证据类别（May Produce Evidence Class）：`CONTRACT`
- 标题（Title）：Create custom subagents
- 权限所有者（Authority Owner）：Anthropic / Claude Code
- 来源类型（Source Type）：官方产品文档
- 官方状态（Official Status）：`VERIFIED`

## 位置与版本（Location and Revision）

- 规范网址或仓库（Canonical URL or Repository）：https://code.claude.com/docs/en/sub-agents
- 版本 / 发布（Version / Release）：浮动官方文档锚点；执行时绑定 Claude Code version 并重新核验
- 提交（Commit）：不适用
- 发布日期（Published On）：页面未提供稳定发布日期
- 访问日期（Accessed On）：2026-07-14

## 范围（Scope）

- 宿主（Host）：Claude Code
- 宿主版本（Host Version）：尚未绑定
- Provider Profile：尚未绑定
- 模型（Model）：尚未绑定
- Runtime / 组件范围（Runtime / Component Scope）：custom subagent instruction、Context、Tool、scope、invocation 与 result surface

## 权限评估（Authority Assessment）

- 权限证据 ID（Authority Evidence IDs）：无；官方域名归属已核验
- 本来源可支持的判断（Claim This Source May Support）：执行时所核验版本的 Subagent public Contract
- 本来源不可支持的判断（Claim This Source Cannot Support）：自动委派质量、Context isolation 的 outcome、model behavior、内部 scheduler 或支持等级
- 已知限制（Known Limitations）：surface 与 automatic delegation behavior 受 Host version、Model、Configuration 和 description 影响
- 过期 / 重新验证触发条件（Staleness / Revalidation Trigger）：frontmatter、scope、invocation、tool、memory、Host version 或 model behavior 变化

## Host-specific Source Authority

- 是否适用（Applies?）：`NO`
- Policy / Gate：`NONE`
- 状态（Status）：`NOT APPLICABLE`
- 验证依据（Verification Basis）：该来源适用通用 Source Authority 规则，不需要额外 Host-specific gate

## 派生证据（Derived Evidence）

- 证据 ID（Evidence IDs）：无
- 证据判断位置（Evidence Claim Locations）：无
- 备注（Notes）：Contract 与 Direct Behavior 必须分开登记。
