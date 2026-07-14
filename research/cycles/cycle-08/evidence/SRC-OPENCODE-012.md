# 来源登记条目（Source Registry Entry）· SRC-OPENCODE-012

## 身份（Identity）

- 来源 ID（Source ID）：`SRC-OPENCODE-012`
- 来源角色（Source Role）：`OFFICIAL CONTRACT`
- 可产生的证据类别（May Produce Evidence Class）：`CONTRACT`
- 标题（Title）：Permissions | OpenCode
- 权限所有者（Authority Owner）：Anomaly / OpenCode
- 来源类型（Source Type）：官方 permission action、rule matching 与 approval 文档
- 官方状态（Official Status）：`VERIFIED`

## 位置与版本（Location and Revision）

- 规范网址或仓库（Canonical URL or Repository）：https://opencode.ai/docs/permissions/
- 版本 / 发布（Version / Release）：浮动官方文档锚点；页面标记最后更新于 2026-07-14，执行时与 OpenCode version / surface / permission profile 重新核验
- 提交（Commit）：不适用
- 发布日期（Published On）：2026-07-14（页面标记）
- 访问日期（Accessed On）：2026-07-15

## 范围（Scope）

- 宿主（Host）：OpenCode
- 宿主版本（Host Version）：尚未绑定
- Provider Profile：尚未绑定
- 模型（Model）：尚未绑定
- Runtime / 组件范围（Runtime / Component Scope）：`allow` / `ask` / `deny` action、global / granular rule、pattern matching、default、external directory、approval outcome 与 per-agent override Contract

## 权限评估（Authority Assessment）

- 权限证据 ID（Authority Evidence IDs）：无；官方文档站点归属与页面导航已核验
- 本来源可支持的判断（Claim This Source May Support）：执行时绑定版本后，对页面明确声明的 permission action、rule evaluation、default、approval scope 与 per-agent override Contract 形成 scoped claim
- 本来源不可支持的判断（Claim This Source Cannot Support）：当前配置值、实际 prompt / decision、内部 evaluation order implementation、sandbox guarantee、跨 surface parity、Provider / Model portability、企业结论或 S1–S4
- 已知限制（Known Limitations）：permission key、default、pattern、auto mode、approval option 与 agent merge semantics 可随版本 / surface 变化；Contract 不证明本地 decision 已发生
- 过期 / 重新验证触发条件（Staleness / Revalidation Trigger）：action vocabulary、rule order、pattern、default、approval persistence、auto mode、external directory 或 per-agent precedence 变化

## ZCode 来源权限门禁（ZCode Source Authority Gate）

- 是否适用（Applies?）：`NO`
- 门禁状态（Gate Status）：`NOT APPLICABLE`
- 验证依据（Verification Basis）：本来源只涉及 OpenCode

## 派生证据（Derived Evidence）

- 证据 ID（Evidence IDs）：无
- 证据判断位置（Evidence Claim Locations）：无
- 备注（Notes）：计划态浮动 Contract anchor；Batch 5 不从 permission documentation 直接形成 Behavior、安全保证或 portability 结论。
