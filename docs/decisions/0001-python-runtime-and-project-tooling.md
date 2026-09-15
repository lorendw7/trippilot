# ADR-0001: Python runtime and project tooling / Python 运行时与项目工具

- Status / 状态: Accepted / 已接受
- Date / 日期: 2026-09-15
- Owners / 负责人: TripPilot maintainers
- Related issues / 关联 Issue: Phase 0 repository foundation

## Context / 背景

TripPilot begins as a single-developer learning project and later adds RAG, tool calling, an
agent loop, MCP, evaluation, and a small interface. The first decision must favor readable data
contracts, strong AI/data ecosystem support, reproducible setup, and low operational overhead.

TripPilot 起步阶段是单人学习项目，后续会加入 RAG、工具调用、Agent 循环、MCP、评测和
简单界面。首个决策应优先考虑易读的数据契约、成熟的 AI/数据生态、可复现安装和较低运维
成本。

## Decision drivers / 决策因素

- One-command, cross-platform local setup / 跨平台的一条命令本地安装。
- Runtime validation for model and tool payloads / 对模型和工具载荷进行运行时校验。
- Compatibility with AI, retrieval, evaluation, and MCP libraries / 兼容 AI、检索、评测和 MCP 生态。
- Fast feedback from formatting, linting, typing, and tests / 格式、检查、类型和测试反馈迅速。
- Avoid premature distributed-system or framework commitments / 避免过早绑定分布式系统或 Web 框架。

## Options considered / 候选方案

### Option A: Python 3.13, uv, and Pydantic v2

| Dimension / 维度 | Assessment / 评估 |
|---|---|
| Complexity / 复杂度 | Low / 低 |
| Ecosystem / 生态 | Strong for AI and data / AI 与数据生态成熟 |
| Type safety / 类型安全 | Static checks plus runtime validation / 静态检查加运行时校验 |
| Setup speed / 安装速度 | Fast, with a committed lockfile / 快，提交锁文件 |

Benefits: direct access to the Python AI ecosystem; concise schemas; `uv` manages the environment
and lockfile; the required interpreter is already available locally.

Costs: Python's static guarantees are weaker than TypeScript's; Python 3.13 compatibility must be
checked when adding older dependencies.

### Option B: TypeScript, Node.js, and Zod

| Dimension / 维度 | Assessment / 评估 |
|---|---|
| Complexity / 复杂度 | Low to medium / 低到中 |
| Ecosystem / 生态 | Strong for web and SDK integration / Web 与 SDK 集成成熟 |
| Type safety / 类型安全 | Strong compile-time types plus Zod / 强静态类型加 Zod |
| Setup speed / 安装速度 | Good, with a package manager lockfile / 良好 |

Benefits: excellent full-stack sharing and strong compile-time types.

Costs: the data and evaluation ecosystem is less direct for this learning path, and sharing types
does not yet matter because the UI contract has not been selected.

### Option C: Python service plus TypeScript web app from day one

| Dimension / 维度 | Assessment / 评估 |
|---|---|
| Complexity / 复杂度 | High for Phase 0 / 对阶段 0 而言较高 |
| Ecosystem / 生态 | Best of both ecosystems / 兼得两种生态 |
| Type safety / 类型安全 | Requires schema generation across languages / 需要跨语言生成结构 |
| Setup speed / 安装速度 | Slowest / 最慢 |

Benefits: clear frontend/backend specialization and independent deployment.

Costs: two toolchains, duplicated configuration, contract generation, and deployment complexity
before those costs produce user value.

## Decision / 决策

Use Python 3.13, `uv`, Pydantic v2, pytest, Ruff, and mypy. Begin as a modular monolith with
provider-independent domain contracts. Defer the HTTP framework, UI framework, model provider,
retrieval store, and deployment platform until their respective milestones provide evidence.

采用 Python 3.13、`uv`、Pydantic v2、pytest、Ruff 和 mypy。先构建具有供应商无关领域契约
的模块化单体；HTTP 框架、UI 框架、模型供应商、检索存储和部署平台推迟到对应里程碑，
基于实验依据再选择。

## Consequences / 影响

### Positive / 正面

- A clean checkout has one dependency and environment workflow / 全新检出只有一套依赖与环境流程。
- Domain contracts can generate JSON Schema for later LLM structured output and APIs /
  领域契约可生成 JSON Schema，供后续模型结构化输出和 API 使用。
- Early tests run without network access or paid services / 早期测试不依赖网络或付费服务。

### Negative / 负面

- A future browser UI may introduce a second TypeScript toolchain / 未来浏览器界面可能引入第二套 TypeScript 工具链。
- Libraries added later must explicitly support Python 3.13 / 后续依赖必须明确支持 Python 3.13。
- The modular boundaries rely on review discipline until separate packages are justified /
  在有必要拆包前，模块边界依赖评审纪律维护。

## Validation / 验证方式

Run `uv sync`, followed by `uv run ruff check .`, `uv run mypy`, and `uv run pytest`. Revisit this
decision if a required MCP, retrieval, or model SDK does not support Python 3.13, or if the web UI
needs to share contracts frequently enough to justify schema generation or TypeScript ownership.

运行 `uv sync`，再运行 `uv run ruff check .`、`uv run mypy` 和 `uv run pytest`。如果必需的
MCP、检索或模型 SDK 不支持 Python 3.13，或 Web UI 频繁共享契约以至于值得引入结构生成或
由 TypeScript 管理契约，则重新评估本决策。
