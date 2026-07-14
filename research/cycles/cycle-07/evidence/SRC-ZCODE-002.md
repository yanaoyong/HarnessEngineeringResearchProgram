# 来源登记条目（Source Registry Entry）· SRC-ZCODE-002

## 身份（Identity）

- 来源 ID（Source ID）：`SRC-ZCODE-002`
- 来源角色（Source Role）：`OFFICIAL CONTRACT`
- 可产生的证据类别（May Produce Evidence Class）：`CONTRACT`
- 标题（Title）：ZCode Agent
- 权限所有者（Authority Owner）：ZCode / 北京智谱华章科技股份有限公司
- 来源类型（Source Type）：官方产品文档
- 官方状态（Official Status）：`VERIFIED`

## 位置与版本（Location and Revision）

- 规范网址或仓库（Canonical URL or Repository）：https://zcode.z.ai/cn/docs/agent-framework
- 版本 / 发布（Version / Release）：浮动官方文档锚点；执行时与安装的 ZCode release 重新核验
- 提交（Commit）：不适用
- 发布日期（Published On）：页面未提供稳定发布日期
- 访问日期（Accessed On）：2026-07-14

## 范围（Scope）

- 宿主（Host）：ZCode
- 宿主版本（Host Version）：尚未绑定
- Provider Profile：尚未绑定
- 模型（Model）：尚未绑定
- Runtime / 组件范围（Runtime / Component Scope）：Agent、workspace、task、context surface、tool、permission mode、Review 与 Git state 的公开产品 Contract

## 权限评估（Authority Assessment）

- 权限证据 ID（Authority Evidence IDs）：无；官方 ZCode 文档导航与产品域名已核验
- 本来源可支持的判断（Claim This Source May Support）：执行时绑定 Host version 后，对页面明确声明的 Agent / workspace surface 形成 scoped Contract claim
- 本来源不可支持的判断（Claim This Source Cannot Support）：本地 capability 已启用、内部 context lifecycle、tool implementation、Provider / Model behavior、enterprise readiness 或 S1–S4
- 已知限制（Known Limitations）：产品文档是浮动页面；产品描述可能覆盖多个 platform / release，且不能替代 Direct Behavior
- 过期 / 重新验证触发条件（Staleness / Revalidation Trigger）：Agent identity、workspace / task surface、permission mode、Review、navigation 或产品版本变化

## ZCode 来源权限门禁（ZCode Source Authority Gate）

- 是否适用（Applies?）：`YES`
- 门禁状态（Gate Status）：`NOT VERIFIED`
- 验证依据（Verification Basis）：官方产品文档没有指认可固定 revision 的 ZCode Runtime source repository

## 派生证据（Derived Evidence）

- 证据 ID（Evidence IDs）：无
- 证据判断位置（Evidence Claim Locations）：无
- 备注（Notes）：计划态浮动 Contract anchor；页面中的“自研”产品表述不能替代 Runtime Source Evidence。
