# 来源登记条目（Source Registry Entry）· SRC-CROSSHOST-004

## 身份（Identity）

- 来源 ID（Source ID）：`SRC-CROSSHOST-004`
- 来源角色（Source Role）：`OFFICIAL SOURCE`
- 可产生的证据类别（May Produce Evidence Class）：`SOURCE`
- 标题（Title）：Porting Superpowers to a New Harness
- 权限所有者（Authority Owner）：obra / Superpowers project
- 来源类型（Source Type）：项目维护者的 porting guide 与同仓库 live integration reference
- 官方状态（Official Status）：`VERIFIED`

## 位置与版本（Location and Revision）

- 规范网址或仓库（Canonical URL or Repository）：https://github.com/obra/superpowers
- 版本 / 发布（Version / Release）：浮动默认分支锚点；目标路径 `docs/porting-to-a-new-harness.md`，执行时按 capability 重新定位
- 提交（Commit）：`NOT PINNED`
- 发布日期（Published On）：不适用
- 访问日期（Accessed On）：2026-07-15

## 范围（Scope）

- 宿主（Host）：Superpowers supported harness integrations
- 宿主版本（Host Version）：尚未绑定
- Provider Profile：不适用
- 模型（Model）：不适用
- Runtime / 组件范围（Runtime / Component Scope）：shared skill body、per-harness tool mapping、bootstrap injection、capability checklist、integration shape、tests 与 definition of done reference pattern

## 权限评估（Authority Assessment）

- 权限证据 ID（Authority Evidence IDs）：无；canonical repository ownership 与 guide path 已核验
- 本来源可支持的判断（Claim This Source May Support）：固定完整 commit 后，对该 revision 的 Superpowers porting architecture、declared invariant、tool mapping / bootstrap mechanism、test boundary 与 known degradation 形成 scoped Source claim
- 本来源不可支持的判断（Claim This Source Cannot Support）：其 invariant 是所有 Harness 的普遍真理；Claude Code、Codex、Qwen Code 或 OpenCode 的官方 Contract / Runtime；myharness 应复制该 bootstrap；未执行 port 的 behavior 或 support
- 已知限制（Known Limitations）：默认分支与 guide 会变化；guide 明确要求参考 live code，文档与 implementation 可能漂移；项目自身的 support definition 不等于本计划 Portable Semantic Contract
- 过期 / 重新验证触发条件（Staleness / Revalidation Trigger）：guide path、supported harness、bootstrap、tool mapping、capability gate、test / transcript requirement 或 integration implementation 变化

## Host-specific Source Authority

- 是否适用（Applies?）：`NO`
- Policy / Gate：`NONE`
- 状态（Status）：`NOT APPLICABLE`
- 验证依据（Verification Basis）：该来源适用通用 Source Authority 规则，不需要额外 Host-specific gate

## 派生证据（Derived Evidence）

- 证据 ID（Evidence IDs）：无
- 证据判断位置（Evidence Claim Locations）：无
- 备注（Notes）：计划态浮动 Official Source anchor，由 Cycle 9 与 Cycle 10 复用；固定 commit 前不派生可复现 Source Evidence，只作为 Reference Pattern / research question source。跨 Cycle 复用不创建新的 Source ID。
