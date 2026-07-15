# 来源登记条目（Source Registry Entry）· SRC-CROSSHOST-005

## 身份（Identity）

- 来源 ID（Source ID）：`SRC-CROSSHOST-005`
- 来源角色（Source Role）：`OFFICIAL SOURCE`
- 可产生的证据类别（May Produce Evidence Class）：`SOURCE`
- 标题（Title）：mifunedev/openharness
- 权限所有者（Authority Owner）：mifunedev / Open Harness project
- 来源类型（Source Type）：项目 canonical repository 与 current README
- 官方状态（Official Status）：`VERIFIED`

## 位置与版本（Location and Revision）

- 规范网址或仓库（Canonical URL or Repository）：https://github.com/mifunedev/openharness
- 版本 / 发布（Version / Release）：浮动默认分支锚点；执行时固定 commit 并重新定位 current capability
- 提交（Commit）：`NOT PINNED`
- 发布日期（Published On）：不适用
- 访问日期（Accessed On）：2026-07-15

## 范围（Scope）

- 宿主（Host）：Open Harness project；不是本计划四个主要 Coding Agent Host 之一
- 宿主版本（Host Version）：尚未绑定
- Provider Profile：不适用
- 模型（Model）：不适用
- Runtime / 组件范围（Runtime / Component Scope）：current README 所述 Docker sandbox、long-lived per-project workspace、agent installation / selection 与 tracked configuration

## 权限评估（Authority Assessment）

- 权限证据 ID（Authority Evidence IDs）：无；canonical repository 与 current README 已核验
- 本来源可支持的判断（Claim This Source May Support）：固定完整 commit 后，对该 revision 的 Open Harness project scope、documented workspace / sandbox boundary 与 repository artifacts 形成 scoped Source claim
- 本来源不可支持的判断（Claim This Source Cannot Support）：四宿主 Portable Semantic Contract、shared primitive pack 的当前存在、任一 Host 官方 capability、Provider / Model portability、myharness Adapter 设计或 S1–S4
- 已知限制（Known Limitations）：V4.1 Atlas 将其作为 `.oh` primitive / provider surface 参考；当前 README 主要定位已转向 Docker sandbox / long-lived workspace，旧路径和角色不能沿用。该变化只说明 reference anchor drift，不证明旧 revision 或当前 implementation 的完整事实
- 过期 / 重新验证触发条件（Staleness / Revalidation Trigger）：project positioning、README、`.oh` structure、supported agent、configuration、sandbox 或 distribution mechanism 变化

## ZCode 来源权限门禁（ZCode Source Authority Gate）

- 是否适用（Applies?）：`NO`
- 门禁状态（Gate Status）：`NOT APPLICABLE`
- 验证依据（Verification Basis）：Open Harness 不是 ZCode Runtime Source；其支持启动某 Agent 也不能证明该 Agent 内部架构

## 派生证据（Derived Evidence）

- 证据 ID（Evidence IDs）：无
- 证据判断位置（Evidence Claim Locations）：无
- 备注（Notes）：计划态浮动 Official Source anchor；Batch 6 仅将其作为 V4.1 source-role drift 对照，不作为 Cycle 9 portability 主锚点。
