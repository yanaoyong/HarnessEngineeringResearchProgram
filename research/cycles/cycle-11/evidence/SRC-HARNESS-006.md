# 来源登记条目（Source Registry Entry）· SRC-HARNESS-006

## 身份（Identity）

- 来源 ID：`SRC-HARNESS-006`
- 来源角色：`OFFICIAL SOURCE`
- 可产生的证据类别：`SOURCE`
- 标题：Fission-AI/OpenSpec canonical repository
- 权限所有者：Fission-AI/OpenSpec maintainers
- 来源类型：项目自身公开源码与文档
- 官方状态：`VERIFIED`

## 位置与版本（Location and Revision）

- 规范网址或仓库：https://github.com/Fission-AI/OpenSpec
- 版本 / 发布：浮动默认分支；执行时固定完整 commit
- 提交：`NOT PINNED`
- 发布日期：不适用
- 访问日期：2026-07-15

## 范围（Scope）

- 宿主：项目支持的 Agent integrations；执行时核验
- 宿主版本 / Provider Profile / 模型：尚未绑定
- Runtime / 组件范围：artifact-driven change workflow、schemas、instructions / templates 与 change evolution

## 权限评估（Authority Assessment）

- 权限证据 ID：无；canonical repository 已核验
- 本来源可支持的判断：固定 commit 后，对 OpenSpec 自身 artifact / schema / workflow design 形成 scoped Source claim
- 本来源不可支持的判断：myharness Change truth、任一 workflow 更优、无 rigid gate 等于无治理边界
- 已知限制：CLI、schema 与文档会变化；只研究 artifact semantics，不研究安装实现
- 过期 / 重新验证触发条件：schema、CLI、workflow profile、docs 或 default branch 变化

## ZCode 来源权限门禁

- 是否适用：`NO`
- 门禁状态：`NOT APPLICABLE`
- 验证依据：不是 ZCode Runtime Source

## 派生证据

- 证据 ID / 判断位置：无
- 备注：Cycle 12 可复用本 Source ID，但不能因此升级 Evidence Class。
