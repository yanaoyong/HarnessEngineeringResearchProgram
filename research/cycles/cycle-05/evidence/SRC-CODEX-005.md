# 来源登记条目（Source Registry Entry）· SRC-CODEX-005

## 身份（Identity）

- 来源 ID（Source ID）：`SRC-CODEX-005`
- 来源角色（Source Role）：`OFFICIAL SOURCE`
- 可产生的证据类别（May Produce Evidence Class）：`SOURCE`
- 标题（Title）：openai/codex
- 权限所有者（Authority Owner）：OpenAI
- 来源类型（Source Type）：官方开源仓库
- 官方状态（Official Status）：`VERIFIED`

## 位置与版本（Location and Revision）

- 规范网址或仓库（Canonical URL or Repository）：https://github.com/openai/codex
- 版本 / 发布（Version / Release）：默认分支浮动锚点；执行时固定 revision
- 提交（Commit）：`NOT PINNED — EXECUTION-TIME PIN REQUIRED`
- 发布日期（Published On）：不适用
- 访问日期（Accessed On）：2026-07-14

## 范围（Scope）

- 宿主（Host）：Codex
- 宿主版本（Host Version）：尚未绑定
- Provider Profile：尚未绑定
- 模型（Model）：尚未绑定
- Runtime / 组件范围（Runtime / Component Scope）：Cycle 5–6 已声明的 customization、execution、policy、sandbox、hook 与 state capability boundary；具体 path 尚未定位

## 权限评估（Authority Assessment）

- 权限证据 ID（Authority Evidence IDs）：无；官方组织与仓库身份已核验，revision 尚未固定
- 本来源可支持的判断（Claim This Source May Support）：固定 commit 后，对明确 source path 与 scope 的实现边界 claim
- 本来源不可支持的判断（Claim This Source Cannot Support）：当前安装版本行为、未来 Contract、所有客户端实现、未定位路径的架构、Provider / Model behavior 或支持等级
- 已知限制（Known Limitations）：当前未固定 commit，也未建立 Repository Map；目录、crate、module 与调用关系可能变化
- 过期 / 重新验证触发条件（Staleness / Revalidation Trigger）：默认分支、release、repository ownership、target Host version 或相关 capability 变化

## Host-specific Source Authority

- 是否适用（Applies?）：`NO`
- Policy / Gate：`NONE`
- 状态（Status）：`NOT APPLICABLE`
- 验证依据（Verification Basis）：该来源适用通用 Source Authority 规则，不需要额外 Host-specific gate

## 派生证据（Derived Evidence）

- 证据 ID（Evidence IDs）：无
- 证据判断位置（Evidence Claim Locations）：无
- 备注（Notes）：官方身份不等于可复现 revision。真正执行时必须固定完整 commit，并按 capability 重新定位 path、记录 search term 与 stop point 后才能派生 Source Evidence。
