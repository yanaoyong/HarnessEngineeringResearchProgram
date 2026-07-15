# 来源登记条目（Source Registry Entry）· SRC-HARNESS-010

## 身份（Identity）

- 来源 ID：`SRC-HARNESS-010`
- 来源角色：`OFFICIAL SOURCE`
- 可产生的证据类别：`SOURCE`
- 标题：buildermethods/agent-os canonical repository
- 权限所有者：buildermethods/agent-os maintainers
- 来源类型：项目自身公开源码与文档
- 官方状态：`VERIFIED`

## 位置与版本（Location and Revision）

- 规范网址或仓库：https://github.com/buildermethods/agent-os
- 版本 / 发布：浮动默认分支；执行时固定 release / commit
- 提交：`NOT PINNED`
- 发布日期：不适用
- 访问日期：2026-07-15

## 范围（Scope）

- 宿主：项目声明支持的 coding tools；执行时绑定
- 宿主版本 / Provider Profile / 模型：尚未绑定
- Runtime / 组件范围：Discover Standards、Deploy Standards、Shape Spec 与 Index Standards capabilities

## 权限评估（Authority Assessment）

- 权限证据 ID：无；canonical repository 已核验
- 本来源可支持的判断：固定 revision 后，对 Agent OS 自身 standards workflow 形成 scoped Source claim
- 本来源不可支持的判断：发现的 standards 正确、应永久化、适合 myharness 或能减少未来 failure
- 已知限制：当前公开项目定位与 release 会变化；不研究安装脚本
- 过期 / 重新验证触发条件：release、capability、docs、distribution 或 repository scope 变化

## Host-specific Source Authority

- 是否适用（Applies?）：`NO`
- Policy / Gate：`NONE`
- 状态（Status）：`NOT APPLICABLE`
- 验证依据（Verification Basis）：该来源适用通用 Source Authority 规则，不需要额外 Host-specific gate

## 派生证据

- 证据 ID / 判断位置：无
- 备注：只作 knowledge-to-standard 参考。
