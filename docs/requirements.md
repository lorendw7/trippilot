# Phase 0 requirements / 阶段 0 需求

## Product boundary / 产品边界

TripPilot turns a traveler's stated preferences and constraints into an explainable draft
itinerary. It is a decision-support tool: the traveler reviews the output before making any
booking or purchase.

TripPilot 将旅行者明确表达的偏好和约束转化为可解释的行程草案。它是决策辅助工具：
旅行者必须先审阅输出，再进行任何预订或购买。

## Functional requirements / 功能需求

1. Accept a destination, date range, traveler counts, budget, interests, pace, accessibility
   needs, and exclusions / 接收目的地、日期、人数、预算、兴趣、节奏、无障碍需求和排除项。
2. Reject invalid or contradictory structured input instead of silently correcting it /
   拒绝无效或矛盾的结构化输入，不静默修正。
3. Produce a day-by-day draft containing rationale, estimated cost, evidence, assumptions,
   warnings, and unresolved questions / 输出逐日草案，并包含理由、费用估算、依据、假设、
   警告和待确认问题。
4. Preserve source identity and retrieval time for externally verifiable claims /
   为可外部验证的事实保留来源标识和检索时间。
5. Normalize tool success and failure into one stable result contract /
   将工具成功与失败结果统一为稳定的数据契约。
6. Save representative requests as future regression fixtures /
   将代表性请求保存为后续回归测试样例。

## Representative scenarios / 代表性场景

### 1. Standard request / 标准请求

A couple visits Shanghai for three days, has a moderate CNY budget, enjoys architecture,
prefers a balanced pace, and wants rainy-day alternatives.

两人到上海旅行三天，人民币预算适中，喜欢建筑，节奏适中，并希望获得雨天备选方案。

### 2. Accessibility-sensitive request / 无障碍敏感请求

A family with one child visits Hangzhou for two days and needs step-free routes and frequent
rest stops. The plan must expose unknown accessibility facts rather than infer them.

一家三口（含一名儿童）到杭州旅行两天，需要无台阶路线和频繁休息点。对于未知的无障碍
信息，行程必须明确标记未知，而不能自行推断。

### 3. Contradictory request / 矛盾请求

A traveler asks for a one-day Beijing plan containing six distant attractions, no transit,
little walking, and a very low budget. TripPilot must return unresolved questions or warnings
instead of pretending all constraints can be met.

旅行者希望一天内游览北京六个相距较远的景点，同时不乘车、少步行且预算极低。
TripPilot 必须返回待确认问题或警告，不能假装所有约束均可满足。

## Non-functional requirements / 非功能需求

- **Explainability / 可解释性:** recommendations distinguish evidence, assumptions, and
  preferences / 推荐结果区分依据、假设和用户偏好。
- **Safety / 安全:** no booking, payment, messaging, or calendar write in the MVP /
  MVP 不执行预订、支付、发消息或写日历。
- **Privacy / 隐私:** do not accept or store passport, payment, or other sensitive identifiers /
  不接收或存储护照、支付信息等敏感标识。
- **Testability / 可测试性:** domain validation is deterministic and does not require network
  access / 领域校验确定且不依赖网络。
- **Observability / 可观测性:** later provider calls must expose latency, cost, source time,
  and normalized errors / 后续供应商调用必须暴露延迟、成本、来源时间和标准化错误。
- **Cost / 成本:** local development uses free tooling; paid APIs remain optional and bounded /
  本地开发使用免费工具；付费 API 保持可选且有预算上限。

## Phase 0 acceptance criteria / 阶段 0 验收标准

- The runtime and dependency workflow are recorded in ADR-0001 / 运行时和依赖流程记录于
  ADR-0001。
- Input, output, evidence, money, and tool-result contracts reject unknown fields /
  输入、输出、依据、金额和工具结果契约拒绝未知字段。
- The three scenarios above include one conflicting case / 上述三个场景包含一个冲突案例。
- A clean checkout can create `.venv`, install locked dependencies, and run all checks /
  全新检出可创建 `.venv`、安装锁定依赖并运行全部检查。

## Explicit non-goals / 明确不做

- Real booking, purchasing, or reservation changes / 真实预订、购买或修改订单。
- A promise of real-time accuracy without a live source / 无实时来源时承诺实时准确。
- Multi-user accounts, long-term personal profiles, or sensitive document storage /
  多用户账号、长期个人画像或敏感证件存储。
- Microservices, distributed queues, or production-scale infrastructure in early phases /
  早期阶段不采用微服务、分布式队列或生产级基础设施。
