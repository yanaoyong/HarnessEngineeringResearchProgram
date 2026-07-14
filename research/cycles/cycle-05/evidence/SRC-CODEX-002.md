# 来源登记条目（Source Registry Entry）· SRC-CODEX-002

## 身份（Identity）

- 来源 ID（Source ID）：`SRC-CODEX-002`
- 来源角色（Source Role）：`OFFICIAL CONTRACT`
- 可产生的证据类别（May Produce Evidence Class）：`CONTRACT`
- 标题（Title）：Custom instructions with AGENTS.md
- 权限所有者（Authority Owner）：OpenAI / Codex
- 来源类型（Source Type）：官方 agent configuration 文档
- 官方状态（Official Status）：`VERIFIED`

## 位置与版本（Location and Revision）

- 规范网址或仓库（Canonical URL or Repository）：https://learn.chatgpt.com/docs/agent-configuration/agents-md
- 版本 / 发布（Version / Release）：浮动官方文档锚点；执行时绑定 Codex version / surface 并重新核验
- 提交（Commit）：不适用
- 发布日期（Published On）：页面未提供稳定发布日期
- 访问日期（Accessed On）：2026-07-14

## 范围（Scope）

- 宿主（Host）：Codex
- 宿主版本（Host Version）：尚未绑定
- Provider Profile：尚未绑定
- 模型（Model）：尚未绑定
- Runtime / 组件范围（Runtime / Component Scope）：AGENTS.md discovery、global / project / nested scope、override precedence 与配置入口的公开 Contract

## 权限评估（Authority Assessment）

- 权限证据 ID（Authority Evidence IDs）：无；官方文档站点归属已核验
- 本来源可支持的判断（Claim This Source May Support）：执行时绑定版本的 AGENTS.md instruction discovery Contract
- 本来源不可支持的判断（Claim This Source Cannot Support）：特定 Session 确实加载某文件、Instruction adherence、内部 source path、Provider / Model 行为或支持等级
- 已知限制（Known Limitations）：discovery order、filename、size limit 与 surface behavior 可能变化；当前没有 Behavior Run
- 过期 / 重新验证触发条件（Staleness / Revalidation Trigger）：页面、Codex version、project root、fallback filename、scope 或 precedence 变化

## ZCode 来源权限门禁（ZCode Source Authority Gate）

- 是否适用（Applies?）：`NO`
- 门禁状态（Gate Status）：`NOT APPLICABLE`
- 验证依据（Verification Basis）：该来源与 ZCode Runtime 无关

## 派生证据（Derived Evidence）

- 证据 ID（Evidence IDs）：无
- 证据判断位置（Evidence Claim Locations）：无
- 备注（Notes）：计划态浮动 Contract anchor；文档存在不等于当前任务已经读取对应 instruction chain。
