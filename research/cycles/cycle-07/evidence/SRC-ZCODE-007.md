# 来源登记条目（Source Registry Entry）· SRC-ZCODE-007

## 身份（Identity）

- 来源 ID（Source ID）：`SRC-ZCODE-007`
- 来源角色（Source Role）：`OFFICIAL CONTRACT`
- 可产生的证据类别（May Produce Evidence Class）：`CONTRACT`
- 标题（Title）：版本发布与更新
- 权限所有者（Authority Owner）：ZCode / 北京智谱华章科技股份有限公司
- 来源类型（Source Type）：官方 release / changelog channel
- 官方状态（Official Status）：`VERIFIED`

## 位置与版本（Location and Revision）

- 规范网址或仓库（Canonical URL or Repository）：https://zcode.z.ai/cn/changelog
- 版本 / 发布（Version / Release）：浮动官方 release channel；执行时固定安装版本对应条目
- 提交（Commit）：不适用
- 发布日期（Published On）：多版本页面；执行时记录目标 release date
- 访问日期（Accessed On）：2026-07-14

## 范围（Scope）

- 宿主（Host）：ZCode
- 宿主版本（Host Version）：尚未绑定
- Provider Profile：尚未绑定
- 模型（Model）：尚未绑定
- Runtime / 组件范围（Runtime / Component Scope）：release identity、公开 feature / fix 说明、下载入口与版本变化风险

## 权限评估（Authority Assessment）

- 权限证据 ID（Authority Evidence IDs）：无；官方产品 release channel 已核验
- 本来源可支持的判断（Claim This Source May Support）：执行时对目标 release 明确列出的版本、发布日期与 change note 形成 scoped Contract claim
- 本来源不可支持的判断（Claim This Source Cannot Support）：完整 change set、长期支持、SLA、实际升级 / rollback、未列 Behavior、Runtime architecture 或 S1–S4
- 已知限制（Known Limitations）：浮动页面可新增或修订条目；网站下载版本与 changelog 展示可能存在时间差，必须以执行时 artifact 交叉核验
- 过期 / 重新验证触发条件（Staleness / Revalidation Trigger）：新 release、条目修订、download channel、platform support、update / rollback 说明变化

## ZCode 来源权限门禁（ZCode Source Authority Gate）

- 是否适用（Applies?）：`YES`
- 门禁状态（Gate Status）：`NOT VERIFIED`
- 验证依据（Verification Basis）：官方 Changelog 没有指认满足五项 Gate criteria 的 Runtime source repository

## 派生证据（Derived Evidence）

- 证据 ID（Evidence IDs）：无
- 证据判断位置（Evidence Claim Locations）：无
- 备注（Notes）：执行时绑定精确 Host version，不使用“最新版”作为可复现标识。
