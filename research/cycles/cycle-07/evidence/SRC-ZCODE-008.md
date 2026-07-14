# 来源登记条目（Source Registry Entry）· SRC-ZCODE-008

## 身份（Identity）

- 来源 ID（Source ID）：`SRC-ZCODE-008`
- 来源角色（Source Role）：`OFFICIAL CONTRACT`
- 可产生的证据类别（May Produce Evidence Class）：`CONTRACT`
- 标题（Title）：用户反馈与支持
- 权限所有者（Authority Owner）：ZCode / 北京智谱华章科技股份有限公司
- 来源类型（Source Type）：官方 feedback、diagnostic log 与 support route 文档
- 官方状态（Official Status）：`VERIFIED`

## 位置与版本（Location and Revision）

- 规范网址或仓库（Canonical URL or Repository）：https://zcode.z.ai/cn/docs/feedback
- 版本 / 发布（Version / Release）：浮动官方文档锚点；执行时与 Host version / platform 重新核验
- 提交（Commit）：不适用
- 发布日期（Published On）：页面未提供稳定发布日期
- 访问日期（Accessed On）：2026-07-14

## 范围（Scope）

- 宿主（Host）：ZCode
- 宿主版本（Host Version）：尚未绑定
- Provider Profile：执行时绑定实际 profile
- 模型（Model）：执行时绑定实际 Model ID
- Runtime / 组件范围（Runtime / Component Scope）：feedback entry、diagnostic log export / upload、ticket identity 与公开 support route

## 权限评估（Authority Assessment）

- 权限证据 ID（Authority Evidence IDs）：无；官方文档导航与产品域名已核验
- 本来源可支持的判断（Claim This Source May Support）：执行时对明确记录的 feedback / log / ticket surface 形成 scoped Contract claim
- 本来源不可支持的判断（Claim This Source Cannot Support）：日志完整性、审计不可抵赖、组织 retention / access control、SLA、incident response outcome、合规或 S1–S4
- 已知限制（Known Limitations）：用户反馈 route 不等于 enterprise support contract；日志内容、脱敏、位置和 upload behavior 需要绑定版本实际验证
- 过期 / 重新验证触发条件（Staleness / Revalidation Trigger）：feedback channel、log path / export、redaction、upload、ticket status、support contact 或 platform 变化

## ZCode 来源权限门禁（ZCode Source Authority Gate）

- 是否适用（Applies?）：`YES`
- 门禁状态（Gate Status）：`NOT VERIFIED`
- 验证依据（Verification Basis）：support 文档不提供可固定 revision 的 ZCode Runtime source authority

## 派生证据（Derived Evidence）

- 证据 ID（Evidence IDs）：无
- 证据判断位置（Evidence Claim Locations）：无
- 备注（Notes）：实验不得上传真实项目日志；Enterprise Fact 必须另有组织证据与 owner。
