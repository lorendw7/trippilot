# TripPilot English learning entry

Welcome to TripPilot. The goal is not to ship a chat box as quickly as possible. It is to use a verifiable travel-planning scenario to understand the important building blocks of an LLM application.

## Suggested reading order

1. [Project brief](../project-brief.md): define the users, scope, and non-goals.
2. [Architecture](../architecture.md): understand component boundaries and end-to-end request flow.
3. [Learning roadmap](../learning-roadmap.md): progress through LLM basics, RAG, tools, Agents, MCP, Skills, and evaluation.
4. [Task list](../task-list.md): turn milestones into small, verifiable tasks.
5. [ADR guide](../decisions/README.md): record important choices and trade-offs.

## Teaching mode

You write all application code. When asking AI for help, prefer explanations, Socratic questions, design review, test design, and risk identification. Unless you explicitly change the rule, do not ask AI to implement a milestone for you.

At the end of each phase, explain in your own words:

1. Where did the data come from, and which steps transformed it?
2. Which outputs are grounded facts, and which are model inferences?
3. If the system fails, can the user understand the failure and recover safely?
