# 来源登记条目（Source Registry Entry）· SRC-HARNESS-005

## 身份（Identity）

- 来源 ID：`SRC-HARNESS-005`
- 来源角色：`OFFICIAL CONTRACT`
- 可产生的证据类别：`CONTRACT`
- 标题：GitHub Spec Kit Documentation
- 权限所有者：GitHub / github/spec-kit maintainers
- 来源类型：项目官方文档
- 官方状态：`VERIFIED`

## 位置与版本（Location and Revision）

- 规范网址或仓库：https://github.github.com/spec-kit/index.html
- 版本 / 发布：浮动官方文档锚点；执行时重新核验页面与访问日期
- 提交：不适用
- 发布日期：页面随项目更新
- 访问日期：2026-07-15

## 范围（Scope）

- 宿主：文档公开列出的 Agent integrations；具体 Host 执行时绑定
- 宿主版本 / Provider Profile / 模型：尚未绑定
- Runtime / 组件范围：Spec → Plan → Tasks → Implement、quality checklist 与 cross-artifact analysis 的公开 Contract

## 权限评估（Authority Assessment）

- 权限证据 ID：无；GitHub 官方项目文档入口已核验
- 本来源可支持的判断：绑定页面版本后，对 Spec Kit 官方公开的 artifact workflow 与 integration surface 形成 scoped Contract claim
- 本来源不可支持的判断：内部实现路径、旧 `converge` / `analyze` 命令仍存在、myharness Change 已收敛或 Agent review 更准确
- 已知限制：浮动文档不能形成可复现 Source Evidence；项目 workflow 不是通用 Change truth Contract
- 过期 / 重新验证触发条件：docs、workflow、command、template 或 integration statement 变化

## Host-specific Source Authority

- 是否适用（Applies?）：`NO`
- Policy / Gate：`NONE`
- 状态（Status）：`NOT APPLICABLE`
- 验证依据（Verification Basis）：该来源适用通用 Source Authority 规则，不需要额外 Host-specific gate

## 派生证据

- 证据 ID / 判断位置：无
- 备注：Batch 7 不派生 `EVD-*`。
