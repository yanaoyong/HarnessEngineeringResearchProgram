# 来源登记条目（Source Registry Entry）· SRC-OPENCODE-007

## 身份（Identity）

- 来源 ID（Source ID）：`SRC-OPENCODE-007`
- 来源角色（Source Role）：`OFFICIAL CONTRACT`
- 可产生的证据类别（May Produce Evidence Class）：`CONTRACT`
- 标题（Title）：Tools | OpenCode
- 权限所有者（Authority Owner）：Anomaly / OpenCode
- 来源类型（Source Type）：官方 tool surface 文档
- 官方状态（Official Status）：`VERIFIED`

## 位置与版本（Location and Revision）

- 规范网址或仓库（Canonical URL or Repository）：https://opencode.ai/docs/tools/
- 版本 / 发布（Version / Release）：浮动官方文档锚点；执行时与 OpenCode version / agent / permission profile 重新核验
- 提交（Commit）：不适用
- 发布日期（Published On）：页面未提供稳定发布日期
- 访问日期（Accessed On）：2026-07-14

## 范围（Scope）

- 宿主（Host）：OpenCode
- 宿主版本（Host Version）：尚未绑定
- Provider Profile：尚未绑定
- 模型（Model）：尚未绑定
- Runtime / 组件范围（Runtime / Component Scope）：built-in / custom / MCP tool exposure、tool configuration 与 selected tool Contract

## 权限评估（Authority Assessment）

- 权限证据 ID（Authority Evidence IDs）：无；官方文档站点归属已核验
- 本来源可支持的判断（Claim This Source May Support）：执行时绑定版本后，对页面明确声明的 tool surface、tool configuration 与 permission linkage 形成 scoped Contract claim
- 本来源不可支持的判断（Claim This Source Cannot Support）：实际 exposed tool set、Provider / Model tool-calling capability、tool schema acceptance、request / success、sandbox guarantee 或 portability
- 已知限制（Known Limitations）：built-in tool、custom tool、MCP exposure 与 availability 可随版本、agent、Provider 或 feature flag 变化；permission resolution 的完整 Contract 由独立 Permissions 来源登记
- 过期 / 重新验证触发条件（Staleness / Revalidation Trigger）：tool list、configuration、custom tool、MCP naming、Provider-specific availability 或 execution semantics 变化

## ZCode 来源权限门禁（ZCode Source Authority Gate）

- 是否适用（Applies?）：`NO`
- 门禁状态（Gate Status）：`NOT APPLICABLE`
- 验证依据（Verification Basis）：本来源只涉及 OpenCode

## 派生证据（Derived Evidence）

- 证据 ID（Evidence IDs）：无
- 证据判断位置（Evidence Claim Locations）：无
- 备注（Notes）：tool listed、schema exposed、request issued、execution succeeded 与 task outcome 必须分别观察。
