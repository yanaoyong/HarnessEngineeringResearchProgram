# 来源登记条目（Source Registry Entry）· SRC-CODEX-010

## 身份（Identity）

- 来源 ID（Source ID）：`SRC-CODEX-010`
- 来源角色（Source Role）：`OFFICIAL CONTRACT`
- 可产生的证据类别（May Produce Evidence Class）：`CONTRACT`
- 标题（Title）：Config basics
- 权限所有者（Authority Owner）：OpenAI / Codex
- 来源类型（Source Type）：官方 configuration 文档
- 官方状态（Official Status）：`VERIFIED`

## 位置与版本（Location and Revision）

- 规范网址或仓库（Canonical URL or Repository）：https://learn.chatgpt.com/docs/config-file/config-basic
- 版本 / 发布（Version / Release）：浮动官方文档锚点；执行时绑定 Codex version / surface 并重新核验
- 提交（Commit）：不适用
- 发布日期（Published On）：页面未提供稳定发布日期
- 访问日期（Accessed On）：2026-07-14

## 范围（Scope）

- 宿主（Host）：Codex
- 宿主版本（Host Version）：尚未绑定
- Provider Profile：尚未绑定
- 模型（Model）：尚未绑定
- Runtime / 组件范围（Runtime / Component Scope）：configuration layer、project trust 与 behavior-affecting setting snapshot 的公开入口

## 权限评估（Authority Assessment）

- 权限证据 ID（Authority Evidence IDs）：无；官方文档站点归属已核验
- 本来源可支持的判断（Claim This Source May Support）：执行时绑定版本的 config location / layer 与 snapshot field Contract
- 本来源不可支持的判断（Claim This Source Cannot Support）：当前 active configuration 的值、credential、actual Behavior、内部 state implementation 或支持等级
- 已知限制（Known Limitations）：config keys、layering、trust 与 supported surface 可变化；本来源不得记录 token、secret 或私有 endpoint 值
- 过期 / 重新验证触发条件（Staleness / Revalidation Trigger）：页面、Host version、config path、layering、trust 或 relevant key 变化

## Host-specific Source Authority

- 是否适用（Applies?）：`NO`
- Policy / Gate：`NONE`
- 状态（Status）：`NOT APPLICABLE`
- 验证依据（Verification Basis）：该来源适用通用 Source Authority 规则，不需要额外 Host-specific gate

## 派生证据（Derived Evidence）

- 证据 ID（Evidence IDs）：无
- 证据判断位置（Evidence Claim Locations）：无
- 备注（Notes）：计划态浮动 Contract anchor；只登记非秘密 configuration snapshot 元数据。
