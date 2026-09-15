# Architecture Decision Records / 架构决策记录

Use an ADR for a decision that changes system boundaries, data contracts, providers, security posture, or a dependency that is costly to reverse.

当某项决定会改变系统边界、数据契约、供应商、安全策略，或引入难以撤销的依赖时，请使用 ADR。

## Process / 流程

1. Copy `0000-template.md` and assign the next four-digit number / 复制模板并使用下一个四位编号。
2. Keep one decision per file / 每个文件只记录一个决策。
3. Start with `Proposed / 提议中` / 初始状态设为 `Proposed / 提议中`。
4. Link evidence or experiments / 链接实验与证据。
5. When replaced, mark it `Superseded / 已取代` and link the new ADR / 被替代时更新状态并链接新 ADR。

Suggested first ADRs: language/runtime, model provider, orchestration style, retrieval store, and MCP boundary.

建议最先记录：语言/运行时、模型服务商、编排方式、检索存储和 MCP 边界。
