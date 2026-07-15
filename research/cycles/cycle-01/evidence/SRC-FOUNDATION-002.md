# 来源登记条目（Source Registry Entry）· SRC-FOUNDATION-002

## 身份（Identity）

- 来源 ID（Source ID）：`SRC-FOUNDATION-002`
- 来源角色（Source Role）：`OFFICIAL SOURCE`
- 可产生的证据类别（May Produce Evidence Class）：`SOURCE`
- 标题（Title）：SWE-agent/mini-swe-agent
- 权限所有者（Authority Owner）：SWE-agent GitHub 组织
- 来源类型（Source Type）：官方开源项目仓库
- 官方状态（Official Status）：`VERIFIED`

## 位置与版本（Location and Revision）

- 规范网址或仓库（Canonical URL or Repository）：https://github.com/SWE-agent/mini-swe-agent
- 版本 / 发布（Version / Release）：浮动 `main` 计划锚点；v2 状态在执行时重新核验
- 提交（Commit）：`NOT PINNED`——派生源码证据前必须固定
- 发布日期（Published On）：尚未评估
- 访问日期（Accessed On）：2026-07-14

## 范围（Scope）

- 宿主（Host）：不适用；参考 Agent 实现
- 宿主版本（Host Version）：不适用
- Provider Profile：不适用
- 模型（Model）：不适用
- Runtime / 组件范围（Runtime / Component Scope）：未来固定 revision 中的 `src/minisweagent/agents/`、`environments/`、`models/`、`run/`

## 权限评估（Authority Assessment）

- 权限证据 ID（Authority Evidence IDs）：无；这里只登记仓库归属，版本与目录在执行时重新核验
- 本来源可支持的判断（Claim This Source May Support）：固定项目 revision 实现的 Agent、Environment、Model 与 Run 边界
- 本来源不可支持的判断（Claim This Source Cannot Support）：普遍最小性、商业 Host 内部实现、本计划的 Provider / Model benchmark 判断或生产就绪性
- 已知限制（Known Limitations）：v2 默认分支可变；路径和行为可能变化；benchmark 判断不在 Cycle 1 范围内
- 过期 / 重新验证触发条件（Staleness / Revalidation Trigger）：版本、默认分支、目录结构、所有权或范围发生变化

## ZCode 来源权限门禁（ZCode Source Authority Gate）

- 是否适用（Applies?）：`NO`
- 门禁状态（Gate Status）：`NOT APPLICABLE`
- 验证依据（Verification Basis）：该来源与 ZCode Runtime 无关

## 派生证据（Derived Evidence）

- 证据 ID（Evidence IDs）：无
- 证据判断位置（Evidence Claim Locations）：无
- 备注（Notes）：为 Cycle 1 登记，并由 Cycle 14 复用；尚未派生行为或源码证据判断。跨 Cycle 复用不创建新的 Source ID。
