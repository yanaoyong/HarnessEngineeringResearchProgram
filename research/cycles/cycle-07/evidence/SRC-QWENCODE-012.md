# 来源登记条目（Source Registry Entry）· SRC-QWENCODE-012

## 身份（Identity）

- 来源 ID（Source ID）：`SRC-QWENCODE-012`
- 来源角色（Source Role）：`OFFICIAL SOURCE`
- 可产生的证据类型（May Produce Evidence Class）：`SOURCE`
- 标题（Title）：QwenLM/qwen-code official repository
- 权限所有者（Authority Owner）：Qwen / QwenLM
- 来源类型（Source Type）：Official Git repository
- 官方状态（Official Status）：`VERIFIED`

## 位置与版本（Location and Revision）

- 规范网址或仓库（Canonical URL or Repository）：https://github.com/QwenLM/qwen-code
- 版本 / 发布（Version / Release）：浮动官方锚点；执行时绑定 Qwen Code release / surface
- 提交（Commit）：`NOT PINNED`
- 发布日期（Published On）：未固定
- 访问日期（Accessed On）：2026-07-15

## 范围（Scope）

- 宿主（Host）：Qwen Code
- 宿主版本（Host Version）：未绑定
- Provider Profile：未绑定
- Model：未绑定
- Runtime / Component Scope：QwenLM/qwen-code official repository
- 相关来源 ID 与关系（Related Source IDs and Relationship）：`SRC-QWENCODE-001..013` 共同组成 Cycle 7 计划来源集；各 ID 仍是独立 canonical artifact

## 权限评估（Authority Assessment）

- 权限证据 ID（Authority Evidence IDs）：无；官方身份核验尚未派生 `EVD-*`
- 本来源可支持的判断（Claim This Source May Support）：固定 revision 中限定 capability 的实现与 repository provenance
- 本来源不可支持的判断（Claim This Source Cannot Support）：未固定默认分支事实、当前安装 Behavior、未来 Contract、跨 surface / Provider / Model portability
- 已知限制（Known Limitations）：内容、release 与默认分支会变化；当前没有绑定 Host version / source commit / Behavior Run，也没有派生 `EVD-*`
- 过期 / 重新验证触发条件（Staleness / Revalidation Trigger）：页面、repository identity、license、release、surface、path 或相关 Contract 变化

## Host-specific Source Authority

- 是否适用（Applies?）：`YES`
- Policy / Gate：`QWEN_CODE_OFFICIAL_SOURCE_VERIFICATION`
- 状态（Status）：`VERIFIED`
- 验证依据（Verification Basis）：QwenLM 官方组织、官方文档回链、公开 repository / license 已核验；repository identity 为 VERIFIED，但 revision 为 NOT PINNED，尚不能派生 revision-bound EVD

## 派生证据（Derived Evidence）

- 证据 ID（Evidence IDs）：无
- 证据判断位置（Evidence Claim Locations）：无
- 备注（Notes）：计划态来源；Contract / Source / Behavior 必须分开登记。形成 Source Evidence 前必须固定完整 commit；解释 Behavior 前还需 execution artifact provenance。
