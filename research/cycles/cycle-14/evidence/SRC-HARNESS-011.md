# 来源登记条目（Source Registry Entry）· SRC-HARNESS-011

## 身份（Identity）

- 来源 ID：`SRC-HARNESS-011`
- 来源角色：`OFFICIAL SOURCE`
- 可产生的证据类别：`SOURCE`
- 标题：SWE-agent/mini-swe-agent canonical repository
- 权限所有者：SWE-agent project maintainers
- 来源类型：项目自身公开源码与文档
- 官方状态：`VERIFIED`

## 位置与版本（Location and Revision）

- 规范网址或仓库：https://github.com/SWE-agent/mini-swe-agent
- 版本 / 发布：浮动 `main`；执行时固定完整 commit
- 提交：`NOT PINNED`
- 发布日期：不适用
- 访问日期：2026-07-15

## 范围（Scope）

- 宿主：mini-swe-agent 自身 scaffold
- 宿主版本 / Provider Profile / 模型：尚未绑定
- Runtime / 组件范围：Agent、Environment、Model、Run 与 minimal scaffold boundary；执行时按 current tree 重新定位

## 权限评估（Authority Assessment）

- 权限证据 ID：无；canonical repository 已核验
- 本来源可支持的判断：固定 commit 后，对 mini-swe-agent 自身 scaffold / interface 形成 scoped Source claim
- 本来源不可支持的判断：更小 scaffold 普遍更好；benchmark 排名；myharness 应删除哪些 primitive
- 已知限制：项目结构和实现会变化；minimality 与 task capability 必须绑定
- 过期 / 重新验证触发条件：release、repository layout、Agent / Environment / Model interface 变化

## ZCode 来源权限门禁

- 是否适用：`NO`
- 门禁状态：`NOT APPLICABLE`
- 验证依据：不是 ZCode Runtime Source

## 派生证据

- 证据 ID / 判断位置：无
- 备注：Batch 7 不使用公开 benchmark 结果。
