# 来源登记条目（Source Registry Entry）· SRC-CLAUDE-005

## 身份（Identity）

- 来源 ID（Source ID）：`SRC-CLAUDE-005`
- 来源角色（Source Role）：`OFFICIAL SOURCE`
- 可产生的证据类别（May Produce Evidence Class）：`SOURCE`
- 标题（Title）：shareAI-lab/learn-claude-code
- 权限所有者（Authority Owner）：shareAI-lab GitHub 组织
- 来源类型（Source Type）：教学重实现的官方项目源码
- 官方状态（Official Status）：`VERIFIED`

## 位置与版本（Location and Revision）

- 规范网址或仓库（Canonical URL or Repository）：https://github.com/shareAI-lab/learn-claude-code
- 版本 / 发布（Version / Release）：浮动 `main` 计划锚点；执行时重新核验 current / legacy track
- 提交（Commit）：`NOT PINNED`——派生 Source Evidence 前必须固定
- 发布日期（Published On）：尚未评估
- 访问日期（Accessed On）：2026-07-14

## 范围（Scope）

- 宿主（Host）：不适用；教学重实现
- 宿主版本（Host Version）：不适用
- Provider Profile：不适用
- 模型（Model）：不适用
- Runtime / 组件范围（Runtime / Component Scope）：按 capability 重新定位 context compact、memory、system prompt、error recovery 与 task system 教学章节

## 权限评估（Authority Assessment）

- 权限证据 ID（Authority Evidence IDs）：无；项目归属和当前双轨教程状态已核验，revision 尚未固定
- 本来源可支持的判断（Claim This Source May Support）：固定教学 revision 中的机制实现
- 本来源不可支持的判断（Claim This Source Cannot Support）：Claude Code 官方 Contract、Runtime architecture、内部 prompt / event、实际 Host behavior 或支持等级
- 已知限制（Known Limitations）：章节编号与 current / legacy track 已变化；V4.1 `s08`–`s12` 路径不能当永久 Contract
- 过期 / 重新验证触发条件（Staleness / Revalidation Trigger）：默认分支、教程 track、目录、所有权或目标 capability 变化

## ZCode 来源权限门禁（ZCode Source Authority Gate）

- 是否适用（Applies?）：`NO`
- 门禁状态（Gate Status）：`NOT APPLICABLE`
- 验证依据（Verification Basis）：该来源与 ZCode Runtime 无关

## 派生证据（Derived Evidence）

- 证据 ID（Evidence IDs）：无
- 证据判断位置（Evidence Claim Locations）：无
- 备注（Notes）：计划态 floating anchor；执行时必须固定 commit 和 track。
