# 来源登记条目（Source Registry Entry）· SRC-CLAUDE-010

## 身份（Identity）

- 来源 ID（Source ID）：`SRC-CLAUDE-010`
- 来源角色（Source Role）：`OFFICIAL CONTRACT`
- 可产生的证据类别（May Produce Evidence Class）：`CONTRACT`
- 标题（Title）：Create plugins
- 权限所有者（Authority Owner）：Anthropic / Claude Code
- 来源类型（Source Type）：官方产品文档
- 官方状态（Official Status）：`VERIFIED`

## 位置与版本（Location and Revision）

- 规范网址或仓库（Canonical URL or Repository）：https://code.claude.com/docs/en/plugins
- 版本 / 发布（Version / Release）：浮动官方文档锚点；执行时绑定 Claude Code version 并重新核验
- 提交（Commit）：不适用
- 发布日期（Published On）：页面未提供稳定发布日期
- 访问日期（Accessed On）：2026-07-14

## 范围（Scope）

- 宿主（Host）：Claude Code
- 宿主版本（Host Version）：尚未绑定
- Provider Profile：尚未绑定
- 模型（Model）：尚未绑定
- Runtime / 组件范围（Runtime / Component Scope）：Plugin packaging、component layout、scope、loading 与 distribution Contract

## 权限评估（Authority Assessment）

- 权限证据 ID（Authority Evidence IDs）：无；官方域名归属已核验
- 本来源可支持的判断（Claim This Source May Support）：执行时所核验版本的 Plugin public Contract
- 本来源不可支持的判断（Claim This Source Cannot Support）：packaged capability 的语义正确、跨 Host portability、安装后的实际 behavior、企业 readiness 或支持等级
- 已知限制（Known Limitations）：Plugin 是 Host-specific packaging layer；组件、marketplace 与 cache behavior 可能随版本变化
- 过期 / 重新验证触发条件（Staleness / Revalidation Trigger）：manifest、layout、scope、loading、distribution 或 Host version 变化

## Host-specific Source Authority

- 是否适用（Applies?）：`NO`
- Policy / Gate：`NONE`
- 状态（Status）：`NOT APPLICABLE`
- 验证依据（Verification Basis）：该来源适用通用 Source Authority 规则，不需要额外 Host-specific gate

## 派生证据（Derived Evidence）

- 证据 ID（Evidence IDs）：无
- 证据判断位置（Evidence Claim Locations）：无
- 备注（Notes）：不把 packaging existence 当成 capability or portability evidence。
