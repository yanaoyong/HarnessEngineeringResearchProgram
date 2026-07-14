# 来源登记条目（Source Registry Entry）· SRC-ZCODE-003

## 身份（Identity）

- 来源 ID（Source ID）：`SRC-ZCODE-003`
- 来源角色（Source Role）：`OFFICIAL CONTRACT`
- 可产生的证据类别（May Produce Evidence Class）：`CONTRACT`
- 标题（Title）：连接模型与套餐
- 权限所有者（Authority Owner）：ZCode / 北京智谱华章科技股份有限公司
- 来源类型（Source Type）：官方 Provider / Model configuration 文档
- 官方状态（Official Status）：`VERIFIED`

## 位置与版本（Location and Revision）

- 规范网址或仓库（Canonical URL or Repository）：https://zcode.z.ai/cn/docs/configuration
- 版本 / 发布（Version / Release）：浮动官方文档锚点；endpoint、套餐与 Model 列表执行时重新核验
- 提交（Commit）：不适用
- 发布日期（Published On）：页面未提供稳定发布日期
- 访问日期（Accessed On）：2026-07-14

## 范围（Scope）

- 宿主（Host）：ZCode
- 宿主版本（Host Version）：尚未绑定
- Provider Profile：BigModel、Z.ai、第三方 / custom provider 的候选配置；执行时只登记实际授权 profile
- 模型（Model）：执行时绑定实际 Model ID
- Runtime / 组件范围（Runtime / Component Scope）：authentication、endpoint type、Base URL category、Provider profile、Model selection 与企业模型通道的公开配置边界

## 权限评估（Authority Assessment）

- 权限证据 ID（Authority Evidence IDs）：无；官方文档站点归属已核验
- 本来源可支持的判断（Claim This Source May Support）：执行时对明确记录的 Provider / endpoint / authentication / Model configuration surface 形成 scoped Contract claim
- 本来源不可支持的判断（Claim This Source Cannot Support）：credential 实际存储、请求真实路由、Provider / Model 等价、输出质量、组织批准、Runtime architecture 或 S1–S4
- 已知限制（Known Limitations）：端点、套餐、模型与活动信息具有时效性；协议兼容不等于 behavior portability
- 过期 / 重新验证触发条件（Staleness / Revalidation Trigger）：Provider、endpoint、authentication、套餐、Model list、自定义通道或 secret management 说明变化

## ZCode 来源权限门禁（ZCode Source Authority Gate）

- 是否适用（Applies?）：`YES`
- 门禁状态（Gate Status）：`NOT VERIFIED`
- 验证依据（Verification Basis）：该页面是 Provider configuration Contract，不是 ZCode Runtime source repository

## 派生证据（Derived Evidence）

- 证据 ID（Evidence IDs）：无
- 证据判断位置（Evidence Claim Locations）：无
- 备注（Notes）：执行记录必须脱敏，不得登记 API Key、token 或可还原 credential。
