# 来源登记条目（Source Registry Entry）· SRC-OPENCODE-009

## 身份（Identity）

- 来源 ID（Source ID）：`SRC-OPENCODE-009`
- 来源角色（Source Role）：`OFFICIAL CONTRACT`
- 可产生的证据类别（May Produce Evidence Class）：`CONTRACT`
- 标题（Title）：Plugins | OpenCode
- 权限所有者（Authority Owner）：Anomaly / OpenCode
- 来源类型（Source Type）：官方 Plugin load、event 与 extension 文档
- 官方状态（Official Status）：`VERIFIED`

## 位置与版本（Location and Revision）

- 规范网址或仓库（Canonical URL or Repository）：https://opencode.ai/docs/plugins/
- 版本 / 发布（Version / Release）：浮动官方文档锚点；执行时与 OpenCode version / runtime 重新核验
- 提交（Commit）：不适用
- 发布日期（Published On）：页面未提供稳定发布日期
- 访问日期（Accessed On）：2026-07-14

## 范围（Scope）

- 宿主（Host）：OpenCode
- 宿主版本（Host Version）：尚未绑定
- Provider Profile：尚未绑定
- 模型（Model）：尚未绑定
- Runtime / 组件范围（Runtime / Component Scope）：project / global / package Plugin source、startup load、event hook、custom tool 与 dependency surface

## 权限评估（Authority Assessment）

- 权限证据 ID（Authority Evidence IDs）：无；官方文档站点归属已核验
- 本来源可支持的判断（Claim This Source May Support）：执行时对页面明确声明的 Plugin location、package configuration、load order、event / tool extension Contract 形成 scoped claim
- 本来源不可支持的判断（Claim This Source Cannot Support）：Plugin 实际安装 / 加载、event order、trusted behavior、capability effectiveness、跨 Provider / Model portability 或安全保证
- 已知限制（Known Limitations）：Plugin API、event、load order、package installation 与 runtime dependency behavior 可随版本变化
- 过期 / 重新验证触发条件（Staleness / Revalidation Trigger）：Plugin path、config key、installation、load order、event、tool API 或 dependency behavior 变化

## ZCode 来源权限门禁（ZCode Source Authority Gate）

- 是否适用（Applies?）：`NO`
- 门禁状态（Gate Status）：`NOT APPLICABLE`
- 验证依据（Verification Basis）：本来源只涉及 OpenCode

## 派生证据（Derived Evidence）

- 证据 ID（Evidence IDs）：无
- 证据判断位置（Evidence Claim Locations）：无
- 备注（Notes）：Batch 5 不实现或安装 OpenCode Plugin，且不把 loaded 写成 effective。
