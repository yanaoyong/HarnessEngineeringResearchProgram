# 来源登记条目（Source Registry Entry）· SRC-CODEX-006

## 身份（Identity）

- 来源 ID（Source ID）：`SRC-CODEX-006`
- 来源角色（Source Role）：`OFFICIAL CONTRACT`
- 可产生的证据类别（May Produce Evidence Class）：`CONTRACT`
- 标题（Title）：Rules
- 权限所有者（Authority Owner）：OpenAI / Codex
- 来源类型（Source Type）：官方 command policy 文档
- 官方状态（Official Status）：`VERIFIED`

## 位置与版本（Location and Revision）

- 规范网址或仓库（Canonical URL or Repository）：https://learn.chatgpt.com/docs/agent-configuration/rules
- 版本 / 发布（Version / Release）：浮动官方文档锚点；页面标记 capability 为 experimental，执行时重新核验
- 提交（Commit）：不适用
- 发布日期（Published On）：页面未提供稳定发布日期
- 访问日期（Accessed On）：2026-07-14

## 范围（Scope）

- 宿主（Host）：Codex
- 宿主版本（Host Version）：尚未绑定
- Provider Profile：尚未绑定
- 模型（Model）：尚未绑定
- Runtime / 组件范围（Runtime / Component Scope）：command prefix rule、decision、active config layer、trust 与 escalation policy 的公开 Contract

## 权限评估（Authority Assessment）

- 权限证据 ID（Authority Evidence IDs）：无；官方文档站点归属已核验
- 本来源可支持的判断（Claim This Source May Support）：执行时绑定版本的 Command Rule configuration 与公开 decision Contract
- 本来源不可支持的判断（Claim This Source Cannot Support）：特定 command 实际匹配、decision order、Hook / Sandbox behavior、项目工程语义或 S1–S4
- 已知限制（Known Limitations）：capability 为 experimental；语法、decision vocabulary、matching 与 config layer 可变化
- 过期 / 重新验证触发条件（Staleness / Revalidation Trigger）：页面、experimental status、rule syntax、matching、decision 或 active config layer 变化

## Host-specific Source Authority

- 是否适用（Applies?）：`NO`
- Policy / Gate：`NONE`
- 状态（Status）：`NOT APPLICABLE`
- 验证依据（Verification Basis）：该来源适用通用 Source Authority 规则，不需要额外 Host-specific gate

## 派生证据（Derived Evidence）

- 证据 ID（Evidence IDs）：无
- 证据判断位置（Evidence Claim Locations）：无
- 备注（Notes）：计划态浮动 Contract anchor；Command Rule 与 glossary 中的通用 Project Rule 不得混用。
