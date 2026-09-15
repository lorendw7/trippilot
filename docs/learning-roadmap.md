# Learning roadmap / 学习路线

Work sequentially. Each phase produces evidence of understanding, not just working code.

请按顺序推进。每个阶段都要产出“理解的证据”，而不只是能运行的代码。

## Phase 0 — Problem framing / 问题定义

**Learn / 学习：** scope, user stories, constraints, success metrics.

**Build yourself / 亲手完成：** choose one traveler scenario, define structured input/output, write ADR-0001 for language and runtime.

**Evidence / 验收证据：** three example requests, including one contradictory request; a written explanation of non-goals.

## Phase 1 — Minimal LLM call / 最小模型调用

**Learn / 学习：** messages, tokens, temperature, structured output, retries, cost and latency.

**Build yourself / 亲手完成：** turn one validated request into a structured draft with no tools or RAG.

**Evidence / 验收证据：** schema validation; captured latency/token metrics; a failure case; explanation of why the result is not yet trustworthy.

## Phase 2 — RAG / 检索增强生成

**Learn / 学习：** ingestion, chunking, embeddings, metadata, retrieval, reranking, citations, prompt injection.

**Build yourself / 亲手完成：** a tiny curated destination corpus and cited retrieval path.

**Evidence / 验收证据：** retrieval tests with expected sources; citations that map back to exact records; an adversarial document test.

## Phase 3 — Tool calling / 工具调用

**Learn / 学习：** schemas, deterministic tools, validation, timeouts, retries, idempotency, fresh data.

**Build yourself / 亲手完成：** one read-only tool, such as weather or travel-time estimation, behind a narrow adapter.

**Evidence / 验收证据：** success, timeout, malformed response, and unavailable-provider tests; clear freshness labels.

## Phase 4 — Agent loop / Agent 循环

**Learn / 学习：** planning vs. acting, state, stopping conditions, budgets, human approval, traceability.

**Build yourself / 亲手完成：** a bounded loop that selects retrieval, a tool, clarification, or final response.

**Evidence / 验收证据：** maximum-step and maximum-cost limits; tool trace; graceful recovery; a case where the Agent chooses to ask rather than act.

## Phase 5 — MCP / MCP 协议

**Learn / 学习：** clients, servers, tools, resources, prompts, capability discovery, trust boundaries.

**Build yourself / 亲手完成：** expose one existing read-only capability through an MCP server and consume it through an MCP client.

**Evidence / 验收证据：** capability listing; schema validation; disconnected-server behavior; written comparison with a direct function call.

## Phase 6 — Skills / Skill 封装

**Learn / 学习：** reusable instructions, tool composition, progressive disclosure, context management, evaluation.

**Build yourself / 亲手完成：** package a narrow workflow such as “rainy-day alternative planner” as a reusable Skill.

**Evidence / 验收证据：** explicit trigger and non-trigger examples; versioned instructions; tests showing the Skill improves consistency.

## Phase 7 — Evaluation and safety / 评测与安全

**Learn / 学习：** golden datasets, rubric scoring, groundedness, task completion, regression testing, red teaming, privacy.

**Build yourself / 亲手完成：** a small, versioned evaluation set spanning normal, ambiguous, conflicting, stale-data, injection, and tool-failure cases.

**Evidence / 验收证据：** baseline report; regression threshold; cost/latency summary; documented limitations.

## Phase 8 — Product polish / 产品化

**Learn / 学习：** UX for uncertainty, observability, caching, rate limits, deployment, feedback loops.

**Build yourself / 亲手完成：** a simple interface that shows sources, assumptions, warnings, and tool status.

**Evidence / 验收证据：** end-to-end demo from a clean environment; accessibility check; operations and rollback notes.

## Suggested pacing / 建议节奏

Treat each phase as one or more small pull requests. Do not advance until you can explain the current phase without reading the implementation.

每个阶段拆成一个或多个小 PR。只有当你不看实现也能解释当前阶段时，再进入下一阶段。
