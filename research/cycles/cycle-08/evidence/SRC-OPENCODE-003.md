# 来源登记条目（Source Registry Entry）· SRC-OPENCODE-003

## 身份（Identity）

- 来源 ID（Source ID）：`SRC-OPENCODE-003`
- 来源角色（Source Role）：`OFFICIAL CONTRACT`
- 可产生的证据类别（May Produce Evidence Class）：`CONTRACT`
- 标题（Title）：Providers | OpenCode
- 权限所有者（Authority Owner）：Anomaly / OpenCode
- 来源类型（Source Type）：官方 Provider configuration 文档
- 官方状态（Official Status）：`VERIFIED`

## 位置与版本（Location and Revision）

- 规范网址或仓库（Canonical URL or Repository）：https://opencode.ai/docs/providers/
- 版本 / 发布（Version / Release）：浮动官方文档锚点；Provider 列表与配置示例执行时重新核验
- 提交（Commit）：不适用
- 发布日期（Published On）：页面未提供稳定发布日期
- 访问日期（Accessed On）：2026-07-14

## 范围（Scope）

- 宿主（Host）：OpenCode
- 宿主版本（Host Version）：尚未绑定
- Provider Profile：尚未绑定
- 模型（Model）：尚未绑定
- Runtime / 组件范围（Runtime / Component Scope）：Provider credential category、endpoint / base URL、adapter package、routing 与 custom provider configuration surface

## 权限评估（Authority Assessment）

- 权限证据 ID（Authority Evidence IDs）：无；官方文档站点归属已核验
- 本来源可支持的判断（Claim This Source May Support）：执行时对页面明确声明的 Provider setup、endpoint category 与 configuration Contract 形成 scoped claim
- 本来源不可支持的判断（Claim This Source Cannot Support）：credential 值、当前授权、Provider SLA / policy、协议等价、Model behavior、tool-call compatibility 或 portability
- 已知限制（Known Limitations）：Provider、authentication、adapter、endpoint 与 routing 选项会变化；列表存在不表示 profile 可用或可比较
- 过期 / 重新验证触发条件（Staleness / Revalidation Trigger）：Provider list、auth flow、adapter package、protocol、endpoint option、routing 或 troubleshooting guidance 变化

## Host-specific Source Authority

- 是否适用（Applies?）：`NO`
- Policy / Gate：`NONE`
- 状态（Status）：`NOT APPLICABLE`
- 验证依据（Verification Basis）：该来源适用通用 Source Authority 规则，不需要额外 Host-specific gate

## 派生证据（Derived Evidence）

- 证据 ID（Evidence IDs）：无
- 证据判断位置（Evidence Claim Locations）：无
- 备注（Notes）：Provider profile 在执行时另行登记，不记录 token、secret header 或私有 endpoint 值。
