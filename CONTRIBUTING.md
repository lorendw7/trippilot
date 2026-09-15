# Contributing / 贡献指南

TripPilot is a learner-owned project. Contributions should protect the teaching-mode constraint: guide the learner without replacing their work.

TripPilot 是学习者主导的项目。贡献应遵守教学模式：帮助学习者思考，而不是替学习者完成代码。

## Workflow / 工作流

1. Create or choose one focused issue / 创建或选择一个范围明确的 Issue。
2. Write acceptance criteria before implementation / 实现前写清验收标准。
3. For architectural choices, add an ADR using `docs/decisions/0000-template.md` / 架构决策使用该 ADR 模板记录。
4. Keep pull requests small and link the issue / PR 保持小而清晰，并关联 Issue。
5. Complete the PR checklist and record what you learned / 完成 PR 检查项并记录学习收获。

## Teaching-mode review / 教学模式评审

Reviewers should prefer questions and evidence:

- What assumption does this change make? / 这个改动依赖什么假设？
- How can the learner verify it? / 学习者如何验证？
- What is the smallest experiment? / 最小实验是什么？
- What failure mode is still untested? / 哪种失败模式尚未测试？

Do not merge generated application code that the learner cannot explain. Documentation, feedback, test ideas, and small illustrative snippets are welcome.

不要合并学习者无法解释的生成式应用代码。欢迎文档、反馈、测试思路和小型说明片段。

## Commit suggestions / 提交建议

Use clear prefixes such as `docs:`, `chore:`, `feat:`, `test:`, and `fix:`. Keep each commit
focused on one explainable learning outcome.

使用 `docs:`、`chore:`、`feat:`、`test:`、`fix:` 等清晰前缀。每个提交只聚焦一个可解释、
可验证的学习成果。
