# 贡献指南（Contributing）

感谢参与 Harness Engineering Research Program。本仓库当前是 V4.3 计划态研究内容：Batch 1–8 / Cycle 1–18 已生成，研究执行尚未开始。

开始前请阅读 [文档导航](docs/README.md)、[研究计划总纲](docs/00-研究计划总纲.md)、[有效协议](docs/10-V4.3-Qwen-Code-Host-Amendment.md) 和 [Source Authority](research/source-authority.md)。

## 可接受的贡献类型

- 导航、拼写、断链和内部一致性修正；
- Source Registry 的官方入口、版本或浮动锚点维护；
- 不越过证据权限的 Research Question、Open Question 或实验设计改进；
- 已获授权且符合协议的真实研究执行制品；
- 自动校验、模板和公共仓库治理改进。

内容修正和研究执行必须分开。Issue、草案或计划实验不表示实验已经运行，也不能创建 `EVD-*`、`ENT-*`、Support Assessment 或产品排名。

## 工作流程

1. 先检查现有 Issue、Open Questions 和对应 Cycle，避免重复 ID 或重复来源。
2. 使用 `agent/<short-description>` 分支；一个 PR 只处理一个可审查目标。
3. 保留 V4.2 frozen baseline 与 V4.1 historical mapping；当前效力变化必须写入 Changelog 或 Amendment。
4. 对所有受管文件变化重建并审查 Manifest：

   ```bash
   python3 scripts/validate_content.py --write-manifest
   ```

5. 提交前运行：

   ```bash
   python3 scripts/validate_content.py
   git diff --check
   git status --short
   ```

6. 在 PR 中说明 What、Why、Impact / Boundary、Validation，以及是否改变内容基线。

## 内容与证据规则

- 使用冻结的 Cycle 名称、Batch 边界、T01–T03、`EXP-Cxx-yy`、Evidence taxonomy 和 S0–S4。
- 分离 Host、surface、Provider、endpoint / protocol、Model、Configuration 与 deployment effect。
- Source ID 不是 Evidence Claim；计划来源不得自动升级为 `EVD-*`。
- 未固定 commit 的源码或文档必须标记为浮动锚点，并说明 pin / revalidation boundary。
- Community Claim 只能形成 Open Question，不能证明官方 Contract、Architecture 或 Support Level。
- 研究执行前必须预注册 Experiment / Run identity、controlled variables、known confounders、evidence 和 human intervention。

## 内容基线变更

`validation/content-baseline.json` 是 owner-approved repository state，不是方便消除 CI 失败的快照。只有以下变化才能更新它：

- 明确批准的 Program / Amendment 决策；
- Cycle、Batch、Experiment 或 Source Registry 的可追溯内容修订；
- 按协议产生的真实研究执行制品与状态变化。

普通 Markdown 编辑只需要更新 `MANIFEST.txt`；不要为了通过校验器而删除检查、扩大忽略范围或顺手改变 `research_execution`。

## 安全与敏感信息

不要在 Issue、PR、Run metadata 或配置快照中提交 token、credential、private endpoint、客户数据或组织身份信息。安全问题使用 [Security Policy](SECURITY.md) 中的私有报告渠道。

## 行为与治理

参与者应遵循 [Code of Conduct](CODE_OF_CONDUCT.md)。维护权限、合并边界和决策分层见 [Governance](GOVERNANCE.md)。

## 许可证状态

仓库当前没有项目级 `LICENSE`。贡献者不应把仓库公开可见解释为复制、修改或再分发许可；repository owner 需要另行作出许可证决策。本贡献指南本身不授予许可证。
