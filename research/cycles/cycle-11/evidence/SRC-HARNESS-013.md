# 来源登记条目（Source Registry Entry）· SRC-HARNESS-013

## 身份（Identity）

- 来源 ID：`SRC-HARNESS-013`
- 来源角色：`OFFICIAL SOURCE`
- 可产生的证据类别：`SOURCE`
- 标题：github/spec-kit canonical repository
- 权限所有者：GitHub / github/spec-kit maintainers
- 来源类型：项目自身公开源码仓库
- 官方状态：`VERIFIED`

## 位置与版本（Location and Revision）

- 规范网址或仓库：https://github.com/github/spec-kit
- 版本 / 发布：浮动默认分支；执行时固定完整 commit
- 提交：`NOT PINNED`
- 发布日期：不适用
- 访问日期：2026-07-15

## 范围（Scope）

- 宿主：repository integrations；具体 Host 执行时绑定
- 宿主版本 / Provider Profile / 模型：尚未绑定
- Runtime / 组件范围：固定 revision 中与 artifact workflow、templates、checklist 和 cross-artifact analysis 相关的 source paths

## 权限评估（Authority Assessment）

- 权限证据 ID：无；canonical repository identity 已核验
- 本来源可支持的判断：固定完整 commit 并定位 source path 后，对 Spec Kit 该 revision 的实现与 artifact boundary 形成 scoped Source claim
- 本来源不可支持的判断：浮动默认分支事实、未来版本、当前安装 Behavior、myharness Change truth 或 Agent review 效果
- 已知限制：当前 `NOT PINNED`；命令、template、path 与 integration 会变化
- 过期 / 重新验证触发条件：default branch、release、source path、template 或 workflow implementation 变化

## ZCode 来源权限门禁

- 是否适用：`NO`
- 门禁状态：`NOT APPLICABLE`
- 验证依据：不是 ZCode Runtime Source

## 派生证据

- 证据 ID / 判断位置：无
- 备注：`SRC-HARNESS-005` 的 Contract claim 与本条目的 Source claim 必须分开。
