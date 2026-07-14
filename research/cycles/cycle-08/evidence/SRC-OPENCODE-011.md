# 来源登记条目（Source Registry Entry）· SRC-OPENCODE-011

## 身份（Identity）

- 来源 ID（Source ID）：`SRC-OPENCODE-011`
- 来源角色（Source Role）：`OFFICIAL SOURCE`
- 可产生的证据类别（May Produce Evidence Class）：`SOURCE`
- 标题（Title）：anomalyco/opencode
- 权限所有者（Authority Owner）：Anomaly / OpenCode
- 来源类型（Source Type）：官方开源 Runtime / product repository 浮动锚点
- 官方状态（Official Status）：`VERIFIED`

## 位置与版本（Location and Revision）

- 规范网址或仓库（Canonical URL or Repository）：https://github.com/anomalyco/opencode
- 版本 / 发布（Version / Release）：浮动默认开发分支；执行时绑定 OpenCode release / installation 与 repository revision
- 提交（Commit）：`NOT PINNED`
- 发布日期（Published On）：不适用
- 访问日期（Accessed On）：2026-07-14

## 范围（Scope）

- 宿主（Host）：OpenCode
- 宿主版本（Host Version）：尚未绑定
- Provider Profile：尚未绑定
- 模型（Model）：尚未绑定
- Runtime / 组件范围（Runtime / Component Scope）：执行时针对 config、session / agent、tool / permission、provider / model 与 extension boundary 重新定位的官方源码候选

## 权限评估（Authority Assessment）

- 权限证据 ID（Authority Evidence IDs）：无；官方文档站点链接该仓库，仓库产品说明链接 `opencode.ai`
- 本来源可支持的判断（Claim This Source May Support）：只有固定完整 commit 并记录 capability question、source path、search term、stop point 与 limitation 后，才能对该 revision 的限定实现形成 Source Evidence
- 本来源不可支持的判断（Claim This Source Cannot Support）：未固定默认分支事实、当前安装采用、未来 Contract、Direct Behavior、所有 Provider / Model 组合、Model portability、企业结论或 S1–S4
- 已知限制（Known Limitations）：默认开发分支、package / module / function 与 docs 会变化；源码存在不表示发行版启用或 behavior 已观察
- 过期 / 重新验证触发条件（Staleness / Revalidation Trigger）：官方归属、repository relocation、license / provenance、default branch、release mapping 或目标 capability path 变化

## ZCode 来源权限门禁（ZCode Source Authority Gate）

- 是否适用（Applies?）：`NO`
- 门禁状态（Gate Status）：`NOT APPLICABLE`
- 验证依据（Verification Basis）：本来源只涉及 OpenCode；OpenCode 仍需遵守通用 Source authority 与 revision binding 规则

## 派生证据（Derived Evidence）

- 证据 ID（Evidence IDs）：无
- 证据判断位置（Evidence Claim Locations）：无
- 备注（Notes）：计划态官方 Source anchor；commit 未固定，因此 Batch 5 不从本条目派生 Source Evidence。
