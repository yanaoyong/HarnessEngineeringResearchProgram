# Cycle 17 证据准备（Evidence Preparation）

> 状态：PREPARED · NO EVIDENCE CLAIMS

本目录当前没有 implementation artifact、Run 或 `EVD-*`。实际执行必须分别登记 H0 / H1 Harness revisions、one-time build / preflight / rollback artifacts，以及每个候选的 A0 / A1 task Run、diff、test、trace、acceptance 与 Human intervention。Run 的 `repository.commit` 绑定共同 task-fixture baseline；`harness_under_test` block 绑定 A0 / A1、H0 / H1、Harness repository / distribution revision 和 implementation artifact IDs；Harness effect 还必须绑定 Host、surface、Provider、endpoint / protocol、Model 与 Configuration。

代码存在、实现完成、测试通过与 Hypothesis 获得 `SUPPORT` 是不同命题；未运行时不得创建结果占位或推断 Evidence。
