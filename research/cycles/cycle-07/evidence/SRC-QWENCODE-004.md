# 来源登记条目（Source Registry Entry）· SRC-QWENCODE-004

## 身份（Identity）

- 来源 ID（Source ID）：`SRC-QWENCODE-004`
- 来源角色（Source Role）：`OFFICIAL CONTRACT`
- 可产生的证据类型（May Produce Evidence Class）：`CONTRACT`
- 标题（Title）：Qwen Code Memory
- 权限所有者（Authority Owner）：Qwen / QwenLM
- 来源类型（Source Type）：Official documentation page
- 官方状态（Official Status）：`VERIFIED`

## 位置与版本（Location and Revision）

- 规范网址或仓库（Canonical URL or Repository）：https://qwenlm.github.io/qwen-code-docs/en/users/features/memory/
- 版本 / 发布（Version / Release）：浮动官方锚点；执行时绑定 Qwen Code release / surface
- 提交（Commit）：`NOT PINNED`
- 发布日期（Published On）：未固定
- 访问日期（Accessed On）：2026-07-15

## 范围（Scope）

- 宿主（Host）：Qwen Code
- 宿主版本（Host Version）：未绑定
- Provider Profile：未绑定
- Model：未绑定
- Runtime / Component Scope：Qwen Code Memory
- 相关来源 ID 与关系（Related Source IDs and Relationship）：`SRC-QWENCODE-001..013` 共同组成 Cycle 7 计划来源集；各 ID 仍是独立 canonical artifact

## 权限评估（Authority Assessment）

- 权限证据 ID（Authority Evidence IDs）：无；官方身份核验尚未派生 `EVD-*`
- 本来源可支持的判断（Claim This Source May Support）：QWEN.md、memory、cross-session knowledge 与相关 command Contract
- 本来源不可支持的判断（Claim This Source Cannot Support）：特定 Session 实际加载、记忆准确性、freshness、Behavior improvement 或 universal retention
- 已知限制（Known Limitations）：内容、release 与默认分支会变化；当前没有绑定 Host version / source commit / Behavior Run，也没有派生 `EVD-*`
- 过期 / 重新验证触发条件（Staleness / Revalidation Trigger）：页面、repository identity、license、release、surface、path 或相关 Contract 变化

## Host-specific Source Authority

- 是否适用（Applies?）：`YES`
- Policy / Gate：`QWEN_CODE_OFFICIAL_CONTRACT`
- 状态（Status）：`VERIFIED`
- 验证依据（Verification Basis）：Qwen Code 官方文档或 release channel 归属已核验；页面为浮动 Contract anchor，执行时重新核验

## 派生证据（Derived Evidence）

- 证据 ID（Evidence IDs）：无
- 证据判断位置（Evidence Claim Locations）：无
- 备注（Notes）：计划态来源；Contract / Source / Behavior 必须分开登记。
