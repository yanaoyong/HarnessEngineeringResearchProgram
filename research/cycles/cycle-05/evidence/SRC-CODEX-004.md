# 来源登记条目（Source Registry Entry）· SRC-CODEX-004

## 身份（Identity）

- 来源 ID（Source ID）：`SRC-CODEX-004`
- 来源角色（Source Role）：`OFFICIAL CONTRACT`
- 可产生的证据类别（May Produce Evidence Class）：`CONTRACT`
- 标题（Title）：Build plugins
- 权限所有者（Authority Owner）：OpenAI / Codex
- 来源类型（Source Type）：官方 Plugin authoring / distribution 文档
- 官方状态（Official Status）：`VERIFIED`

## 位置与版本（Location and Revision）

- 规范网址或仓库（Canonical URL or Repository）：https://learn.chatgpt.com/docs/build-plugins
- 版本 / 发布（Version / Release）：浮动官方文档锚点；执行时绑定 Codex version / surface 并重新核验
- 提交（Commit）：不适用
- 发布日期（Published On）：页面未提供稳定发布日期
- 访问日期（Accessed On）：2026-07-14

## 范围（Scope）

- 宿主（Host）：Codex
- 宿主版本（Host Version）：尚未绑定
- Provider Profile：尚未绑定
- 模型（Model）：尚未绑定
- Runtime / 组件范围（Runtime / Component Scope）：Plugin manifest、packaging、bundled Skills / Hooks / MCP-backed app 与 distribution boundary 的公开 Contract

## 权限评估（Authority Assessment）

- 权限证据 ID（Authority Evidence IDs）：无；官方文档站点归属已核验
- 本来源可支持的判断（Claim This Source May Support）：执行时绑定版本的 Plugin packaging 与 distribution Contract
- 本来源不可支持的判断（Claim This Source Cannot Support）：已安装 Plugin 的 capability outcome、跨 Host portability、内部 loader implementation 或支持等级
- 已知限制（Known Limitations）：Plugin surface、manifest、marketplace 与 supported clients 可能变化；packaging 不等于 Portable Semantic Contract
- 过期 / 重新验证触发条件（Staleness / Revalidation Trigger）：页面、manifest、path rule、bundled artifact 或 distribution surface 变化

## ZCode 来源权限门禁（ZCode Source Authority Gate）

- 是否适用（Applies?）：`NO`
- 门禁状态（Gate Status）：`NOT APPLICABLE`
- 验证依据（Verification Basis）：该来源与 ZCode Runtime 无关

## 派生证据（Derived Evidence）

- 证据 ID（Evidence IDs）：无
- 证据判断位置（Evidence Claim Locations）：无
- 备注（Notes）：计划态浮动 Contract anchor；不得把 Plugin 安装或目录存在当成 capability 有效。
