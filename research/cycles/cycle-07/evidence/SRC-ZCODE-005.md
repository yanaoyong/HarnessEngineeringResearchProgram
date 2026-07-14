# 来源登记条目（Source Registry Entry）· SRC-ZCODE-005

## 身份（Identity）

- 来源 ID（Source ID）：`SRC-ZCODE-005`
- 来源角色（Source Role）：`OFFICIAL CONTRACT`
- 可产生的证据类别（May Produce Evidence Class）：`CONTRACT`
- 标题（Title）：远程开发
- 权限所有者（Authority Owner）：ZCode / 北京智谱华章科技股份有限公司
- 来源类型（Source Type）：官方 remote workspace 文档
- 官方状态（Official Status）：`VERIFIED`

## 位置与版本（Location and Revision）

- 规范网址或仓库（Canonical URL or Repository）：https://zcode.z.ai/cn/docs/remote-development
- 版本 / 发布（Version / Release）：浮动官方文档锚点；执行时与 Host version、platform 与 remote type 重新核验
- 提交（Commit）：不适用
- 发布日期（Published On）：页面未提供稳定发布日期
- 访问日期（Accessed On）：2026-07-14

## 范围（Scope）

- 宿主（Host）：ZCode
- 宿主版本（Host Version）：尚未绑定
- Provider Profile：尚未绑定
- 模型（Model）：尚未绑定
- Runtime / 组件范围（Runtime / Component Scope）：local、SSH 与 Docker workspace 的 execution location、desktop / target responsibility 与 remote resource preparation Contract

## 权限评估（Authority Assessment）

- 权限证据 ID（Authority Evidence IDs）：无；官方文档导航与产品域名已核验
- 本来源可支持的判断（Claim This Source May Support）：执行时对明确记录的 remote connection surface 与 execution-location responsibility 形成 scoped Contract claim
- 本来源不可支持的判断（Claim This Source Cannot Support）：实际网络流量、credential storage、安全隔离、远端 runtime implementation、组织批准、data residency 或 S1–S4
- 已知限制（Known Limitations）：remote resource、platform、connection method 与下载路径可能变化；页面不能替代网络 / deployment record
- 过期 / 重新验证触发条件（Staleness / Revalidation Trigger）：SSH / Docker / WSL support、resource preparation、execution location、credential、network 或 platform 说明变化

## ZCode 来源权限门禁（ZCode Source Authority Gate）

- 是否适用（Applies?）：`YES`
- 门禁状态（Gate Status）：`NOT VERIFIED`
- 验证依据（Verification Basis）：页面描述公开 remote Contract，但没有指认可固定 revision 的 ZCode remote Runtime source repository

## 派生证据（Derived Evidence）

- 证据 ID（Evidence IDs）：无
- 证据判断位置（Evidence Claim Locations）：无
- 备注（Notes）：remote workspace availability 不等于 private deployment、network compliance 或 enterprise approval。
