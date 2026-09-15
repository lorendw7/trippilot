# TripPilot

> A teaching-mode travel-planning Agent project for learning RAG, Agents, MCP, and Skills.
>
> 一个用于学习 RAG、Agent、MCP 与 Skill 的教学模式旅行策划项目。

[中文文档](docs/zh-CN/README.md) · [English docs](docs/en/README.md) · [Architecture / 架构](docs/architecture.md) · [Roadmap / 学习路线](docs/learning-roadmap.md)

## What is this? / 这是什么？

TripPilot is a documentation-first learning repository. You will build a travel-planning Agent that can understand constraints, retrieve trusted travel knowledge, call external tools, and produce explainable itineraries.

TripPilot 是一个文档优先的学习仓库。你将亲手构建一个旅行策划 Agent：理解约束、检索可信资料、调用外部工具，并生成可解释的行程。

This initial repository deliberately contains **no application implementation**. The learner writes every line of product code. Documentation, milestones, review questions, templates, and empty directories provide the learning path.

初始仓库刻意**不包含任何应用实现**。所有产品代码都由学习者编写；仓库只提供文档、里程碑、复盘问题、模板与空目录。

## Learning goals / 学习目标

- Build a minimal LLM application and define structured outputs / 构建最小 LLM 应用并定义结构化输出
- Implement a cited RAG pipeline / 实现带引用的 RAG 流程
- Design safe tool calling and an Agent loop / 设计安全的工具调用与 Agent 循环
- Expose and consume MCP tools and resources / 暴露并使用 MCP 工具与资源
- Package reusable capabilities as Skills / 将可复用能力封装为 Skill
- Evaluate quality, cost, latency, and safety / 评测质量、成本、延迟与安全性

## Start here / 从这里开始

1. Read the [project brief](docs/project-brief.md) / 阅读[项目说明](docs/project-brief.md)。
2. Review the [architecture](docs/architecture.md) and write your first ADR / 阅读[架构说明](docs/architecture.md)，并写第一份 ADR。
3. Follow the [learning roadmap](docs/learning-roadmap.md) / 按[学习路线](docs/learning-roadmap.md)推进。
4. Copy an issue template into a GitHub issue and complete one small task at a time / 使用 Issue 模板，每次完成一个小任务。
5. Use the [definition of done](docs/task-list.md) before merging / 合并前检查[任务清单](docs/task-list.md)中的完成标准。

## Repository map / 仓库结构

```text
apps/                 Future user-facing applications / 未来的用户端应用
packages/             Future reusable modules / 未来的可复用模块
data/                 Local sample data only / 仅存放本地样例数据
examples/             Future learning examples / 未来的学习示例
tests/                Future evaluation and tests / 未来的评测与测试
docs/                 Bilingual learning documentation / 双语学习文档
.github/               Issue and pull-request templates / Issue 与 PR 模板
```

The empty folders are boundaries, not required technology choices. Rename or remove them in an ADR when your design evolves.

空目录用于表达边界，并不代表强制技术选型。设计变化时，请先记录 ADR，再重命名或删除目录。

## Ground rules / 学习约定

- The learner writes all application code / 学习者编写全部应用代码。
- AI may explain, review, ask questions, or suggest tests, but should not silently implement milestones / AI 可以讲解、评审、提问或建议测试，但不应悄悄代写里程碑。
- Every generated itinerary must distinguish retrieved facts, model inference, and user preferences / 每份行程都应区分检索事实、模型推断与用户偏好。
- Never commit secrets, personal travel documents, or paid API responses / 不提交密钥、私人行程文件或付费 API 响应。

## Status / 当前状态

Documentation and empty scaffolding only. No runtime, dependency, framework, or provider has been selected.

当前仅包含文档与空脚手架，尚未选择运行时、依赖、框架或模型供应商。

## Contributing / 参与方式

See [CONTRIBUTING.md](CONTRIBUTING.md). This repository intentionally has no license yet; choose one before accepting outside contributions.

参见 [CONTRIBUTING.md](CONTRIBUTING.md)。仓库暂未选择开源许可证；接受外部贡献前请先确定许可证。
