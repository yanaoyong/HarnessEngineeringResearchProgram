# 来源登记条目（Source Registry Entry）· SRC-FOUNDATION-004

## 身份（Identity）

- 来源 ID（Source ID）：`SRC-FOUNDATION-004`
- 来源角色（Source Role）：`OFFICIAL SOURCE`
- 可产生的证据类别（May Produce Evidence Class）：`SOURCE`
- 标题（Title）：shareAI-lab/learn-claude-code
- 权限所有者（Authority Owner）：shareAI-lab GitHub 组织
- 来源类型（Source Type）：教学重实现的官方源码
- 官方状态（Official Status）：`VERIFIED`

## 位置与版本（Location and Revision）

- 规范网址或仓库（Canonical URL or Repository）：https://github.com/shareAI-lab/learn-claude-code
- 版本 / 发布（Version / Release）：浮动 `main` 计划锚点；执行时重新核验
- 提交（Commit）：`NOT PINNED`——派生源码证据前必须固定
- 发布日期（Published On）：尚未评估
- 访问日期（Accessed On）：2026-07-14

## 范围（Scope）

- 宿主（Host）：不适用；教学重实现
- 宿主版本（Host Version）：不适用
- Provider Profile：不适用
- 模型（Model）：不适用
- Runtime / 组件范围（Runtime / Component Scope）：`s01_agent_loop`、`s03_permission`、`s04_hooks`、`s05_todo_write`、`s06_subagent`、`s07_skill_loading`；快速参考 `s02_tool_use` 与 `s08_context_compact`

## 权限评估（Authority Assessment）

- 权限证据 ID（Authority Evidence IDs）：无；这里只登记仓库身份，命名目录在执行时重新核验
- 本来源可支持的判断（Claim This Source May Support）：固定教学仓库 revision 实现的机制
- 本来源不可支持的判断（Claim This Source Cannot Support）：Claude Code 官方 Contract、Runtime architecture、内部生命周期事件、源码路径或 Host 支持等级
- 已知限制（Known Limitations）：默认分支可变；该仓库明确呈现教学 Harness，而不是 Anthropic Runtime 源码
- 过期 / 重新验证触发条件（Staleness / Revalidation Trigger）：默认分支、目录结构、所有权、教学范围或目标 Cycle 问题发生变化

## ZCode 来源权限门禁（ZCode Source Authority Gate）

- 是否适用（Applies?）：`NO`
- 门禁状态（Gate Status）：`NOT APPLICABLE`
- 验证依据（Verification Basis）：该来源与 ZCode Runtime 无关

## 派生证据（Derived Evidence）

- 证据 ID（Evidence IDs）：无
- 证据判断位置（Evidence Claim Locations）：无
- 备注（Notes）：为 Cycle 2 计划阅读登记；不授权形成 Claude Code 架构结论。
