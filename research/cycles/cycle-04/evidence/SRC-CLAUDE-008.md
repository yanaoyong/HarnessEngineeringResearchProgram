# 来源登记条目（Source Registry Entry）· SRC-CLAUDE-008

## 身份（Identity）

- 来源 ID（Source ID）：`SRC-CLAUDE-008`
- 来源角色（Source Role）：`OFFICIAL CONTRACT`
- 可产生的证据类别（May Produce Evidence Class）：`CONTRACT`
- 标题（Title）：Hooks reference
- 权限所有者（Authority Owner）：Anthropic / Claude Code
- 来源类型（Source Type）：官方技术参考
- 官方状态（Official Status）：`VERIFIED`

## 位置与版本（Location and Revision）

- 规范网址或仓库（Canonical URL or Repository）：https://code.claude.com/docs/en/hooks
- 版本 / 发布（Version / Release）：浮动官方文档锚点；执行时绑定 Claude Code version 并重新核验
- 提交（Commit）：不适用
- 发布日期（Published On）：页面未提供稳定发布日期
- 访问日期（Accessed On）：2026-07-14

## 范围（Scope）

- 宿主（Host）：Claude Code
- 宿主版本（Host Version）：尚未绑定
- Provider Profile：尚未绑定
- 模型（Model）：尚未绑定
- Runtime / 组件范围（Runtime / Component Scope）：与 `EXP-C04-01` 相关的 lifecycle events、input / output 与 decision control Contract

## 权限评估（Authority Assessment）

- 权限证据 ID（Authority Evidence IDs）：无；官方域名归属已核验
- 本来源可支持的判断（Claim This Source May Support）：绑定版本下官方公开的 Hook event 与 control surface
- 本来源不可支持的判断（Claim This Source Cannot Support）：特定 Hook 配置正确、执行成功、所有 Hook 都确定性、治理效果或 S1–S4
- 已知限制（Known Limitations）：Hook 类型可能包含 command、HTTP、prompt 或 agent；trigger 确定不等于所有 handler outcome 确定
- 过期 / 重新验证触发条件（Staleness / Revalidation Trigger）：event、schema、decision control、Host version 或实验 scope 变化

## Host-specific Source Authority

- 是否适用（Applies?）：`NO`
- Policy / Gate：`NONE`
- 状态（Status）：`NOT APPLICABLE`
- 验证依据（Verification Basis）：该来源适用通用 Source Authority 规则，不需要额外 Host-specific gate

## 派生证据（Derived Evidence）

- 证据 ID（Evidence IDs）：无
- 证据判断位置（Evidence Claim Locations）：无
- 备注（Notes）：只登记计划态 Contract anchor；不创建 Behavior claim。
