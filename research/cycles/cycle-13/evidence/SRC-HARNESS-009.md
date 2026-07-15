# 来源登记条目（Source Registry Entry）· SRC-HARNESS-009

## 身份（Identity）

- 来源 ID：`SRC-HARNESS-009`
- 来源角色：`OFFICIAL SOURCE`
- 可产生的证据类别：`SOURCE`
- 标题：snarktank/ralph canonical repository
- 权限所有者：snarktank/ralph maintainers
- 来源类型：项目自身公开源码与 workflow artifacts
- 官方状态：`VERIFIED`

## 位置与版本（Location and Revision）

- 规范网址或仓库：https://github.com/snarktank/ralph
- 版本 / 发布：浮动 `main`；执行时固定完整 commit
- 提交：`NOT PINNED`
- 发布日期：不适用
- 访问日期：2026-07-15

## 范围（Scope）

- 宿主：项目当前支持的 tool modes；执行时逐项核验
- 宿主版本 / Provider Profile / 模型：尚未绑定
- Runtime / 组件范围：README、prompt / CLAUDE instructions、PRD、progress log 与 fresh-iteration workflow

## 权限评估（Authority Assessment）

- 权限证据 ID：无；canonical repository 已核验
- 本来源可支持的判断：固定 commit 后，对 Ralph 自身 persistent artifact / iteration design 形成 scoped Source claim
- 本来源不可支持的判断：fresh context 优于 resume；Host auto-handoff parity；myharness session continuity
- 已知限制：prompt、supported tool 与 artifact format 会变化；项目会提交代码，不等于本研究授权提交
- 过期 / 重新验证触发条件：workflow、prompt、artifact、integration 或 default branch 变化

## ZCode 来源权限门禁

- 是否适用：`NO`
- 门禁状态：`NOT APPLICABLE`
- 验证依据：不是 ZCode Runtime Source

## 派生证据

- 证据 ID / 判断位置：无
- 备注：只作 fresh-context handoff contrast。
