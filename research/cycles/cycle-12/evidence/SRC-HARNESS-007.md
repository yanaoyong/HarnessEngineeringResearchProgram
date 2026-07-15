# 来源登记条目（Source Registry Entry）· SRC-HARNESS-007

## 身份（Identity）

- 来源 ID：`SRC-HARNESS-007`
- 来源角色：`OFFICIAL SOURCE`
- 可产生的证据类别：`SOURCE`
- 标题：bmad-code-org/BMAD-METHOD canonical repository
- 权限所有者：bmad-code-org/BMAD-METHOD maintainers
- 来源类型：项目自身公开源码仓库
- 官方状态：`VERIFIED`

## 位置与版本（Location and Revision）

- 规范网址或仓库：https://github.com/bmad-code-org/BMAD-METHOD
- 版本 / 发布：浮动默认分支；执行时固定完整 commit
- 提交：`NOT PINNED`
- 发布日期：不适用
- 访问日期：2026-07-15

## 范围（Scope）

- 宿主：repository integrations；执行时绑定
- 宿主版本 / Provider Profile / 模型：尚未绑定
- Runtime / 组件范围：固定 revision 中与 planning track、workflow、risk / route guidance 相关的 source paths；执行时按 capability 重新定位

## 权限评估（Authority Assessment）

- 权限证据 ID：无；canonical repository identity 已核验
- 本来源可支持的判断：固定完整 commit 并定位 source path 后，对 BMAD 该 revision 的 workflow implementation / artifact boundary 形成 scoped Source claim
- 本来源不可支持的判断：官方文档 Contract、story count 等于 risk、BMAD route 适合 myharness 或 adaptive workflow 已降低风险 / 成本
- 已知限制：当前 `NOT PINNED`；项目版本、术语、path 与 track boundary 会变化；不研究 Party Mode 与全部 Persona
- 过期 / 重新验证触发条件：release、default branch、track、workflow 或 source path 变化

## Host-specific Source Authority

- 是否适用（Applies?）：`NO`
- Policy / Gate：`NONE`
- 状态（Status）：`NOT APPLICABLE`
- 验证依据（Verification Basis）：该来源适用通用 Source Authority 规则，不需要额外 Host-specific gate

## 派生证据

- 证据 ID / 判断位置：无
- 备注：只在固定 commit 后产生 Source Evidence 候选。
