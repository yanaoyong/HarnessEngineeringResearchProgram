# 来源登记条目（Source Registry Entry）· SRC-HARNESS-003

## 身份（Identity）

- 来源 ID：`SRC-HARNESS-003`
- 来源角色：`OFFICIAL SOURCE`
- 可产生的证据类别：`SOURCE`
- 标题：obra/superpowers canonical repository
- 权限所有者：obra/superpowers maintainers
- 来源类型：项目自身公开源码仓库
- 官方状态：`VERIFIED`

## 位置与版本（Location and Revision）

- 规范网址或仓库：https://github.com/obra/superpowers
- 版本 / 发布：浮动 `main`；执行时固定完整 commit
- 提交：`NOT PINNED`
- 发布日期：不适用
- 访问日期：2026-07-15

## 范围（Scope）

- 宿主：该项目声明支持的 integrations；执行时逐项核验
- 宿主版本 / Provider Profile / 模型：尚未绑定
- Runtime / 组件范围：README、`skills/writing-skills/`、`skills/verification-before-completion/` 与相关 Skill tests

## 权限评估（Authority Assessment）

- 权限证据 ID：无；canonical repository 已核验
- 本来源可支持的判断：固定 commit 后，对 Superpowers 自身 Skill structure、procedure、verification 与 testing pattern 形成 scoped Source claim
- 本来源不可支持的判断：四个主要 Host 的官方 Contract / Runtime；myharness Skill 有效；跨 Host behavior parity
- 已知限制：项目方法带有自身规范立场；source path 与 integration 会漂移
- 过期 / 重新验证触发条件：默认分支、Skill path、integration、license 或 behavior contract 变化

## ZCode 来源权限门禁

- 是否适用：`NO`
- 门禁状态：`NOT APPLICABLE`
- 验证依据：不是 ZCode Runtime Source

## 派生证据

- 证据 ID / 判断位置：无
- 备注：`NOT PINNED` 时不能产生可复现 Source Evidence。
