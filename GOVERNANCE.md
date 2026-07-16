# 仓库治理（Governance）

## 维护角色

- Repository owner / current maintainer：[@yanaoyong](https://github.com/yanaoyong)
- Code ownership：由 [.github/CODEOWNERS](.github/CODEOWNERS) 声明。

CODEOWNERS 用于自动请求审查；它本身不代表 GitHub branch protection 或 ruleset 已启用。平台级保护规则需要 owner 在 GitHub 设置中单独配置。

## 决策分层

| 变更类型 | 最低治理要求 |
|---|---|
| 导航、拼写、断链、无语义格式修正 | PR、内容完整性 CI、maintainer review |
| Source Registry 或 Experiment plan 修订 | 上述要求 + authority / ID / scope 说明 + baseline diff |
| Cycle、Batch、Host set、Evidence 或 Support 协议变化 | repository owner 明确批准 + Changelog / Amendment + baseline revision |
| 真实研究执行与结果 | 预注册协议、Run metadata、Evidence 绑定、限制与人工干预记录 |
| 安全事件 | 私有报告；协调修复前不进入公开 Issue |
| 项目许可证 | repository owner 的独立明确决策 |

## 合并原则

- PR 必须范围单一、可逆、无未解释的内容基线变化。
- `Content integrity` 必须通过；校验通过不替代人工语义审查。
- Research plan、execution、evidence、finding、decision 与 implementation 必须保持分层。
- 未解决矛盾进入 Open Questions，不通过模糊措辞强行收敛。
- Draft、Issue、PR description 和 Source ID 不得被描述为已验证研究结论。

## 公共讨论入口

- 内容与导航问题：Content correction Issue Form。
- 研究执行建议：Research execution proposal Issue Form。
- 安全问题：[Security Policy](SECURITY.md) 的私有渠道。
- 贡献流程：[Contributing](CONTRIBUTING.md)。

## 变更本治理文件

治理变更必须由 repository owner 审查。影响协议、执行权限、许可证或安全报告方式的变化需要在 Changelog 中单独说明。
