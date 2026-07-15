# 来源登记条目（Source Registry Entry）· SRC-OPENCODE-008

## 身份（Identity）

- 来源 ID（Source ID）：`SRC-OPENCODE-008`
- 来源角色（Source Role）：`OFFICIAL CONTRACT`
- 可产生的证据类别（May Produce Evidence Class）：`CONTRACT`
- 标题（Title）：Agent Skills | OpenCode
- 权限所有者（Authority Owner）：Anomaly / OpenCode
- 来源类型（Source Type）：官方 Skill discovery 与 load 文档
- 官方状态（Official Status）：`VERIFIED`

## 位置与版本（Location and Revision）

- 规范网址或仓库（Canonical URL or Repository）：https://opencode.ai/docs/skills/
- 版本 / 发布（Version / Release）：浮动官方文档锚点；执行时与 OpenCode version / working directory 重新核验
- 提交（Commit）：不适用
- 发布日期（Published On）：页面未提供稳定发布日期
- 访问日期（Accessed On）：2026-07-14

## 范围（Scope）

- 宿主（Host）：OpenCode
- 宿主版本（Host Version）：尚未绑定
- Provider Profile：尚未绑定
- 模型（Model）：尚未绑定
- Runtime / 组件范围（Runtime / Component Scope）：`SKILL.md` location、frontmatter、project traversal、discovery、on-demand `skill` tool load 与 permission surface

## 权限评估（Authority Assessment）

- 权限证据 ID（Authority Evidence IDs）：无；官方文档站点归属已核验
- 本来源可支持的判断（Claim This Source May Support）：执行时对页面明确声明的 Skill format、discovery location、load trigger 与 permission Contract 形成 scoped claim
- 本来源不可支持的判断（Claim This Source Cannot Support）：Skill 实际被发现 / 加载 / 执行、procedure adherence、outcome、跨 Host behavior parity 或 portability
- 已知限制（Known Limitations）：location、compatibility path、frontmatter、permission 与 discovery semantics 可变化；format compatibility 不等于 behavior equivalence
- 过期 / 重新验证触发条件（Staleness / Revalidation Trigger）：Skill path、frontmatter、walk boundary、tool invocation、permission 或 compatibility support 变化

## Host-specific Source Authority

- 是否适用（Applies?）：`NO`
- Policy / Gate：`NONE`
- 状态（Status）：`NOT APPLICABLE`
- 验证依据（Verification Basis）：该来源适用通用 Source Authority 规则，不需要额外 Host-specific gate

## 派生证据（Derived Evidence）

- 证据 ID（Evidence IDs）：无
- 证据判断位置（Evidence Claim Locations）：无
- 备注（Notes）：完整 Skill outcome evaluation 属于 Cycle 10；本 Cycle 只追 architecture boundary。
