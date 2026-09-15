# Project brief / 项目说明

## Vision / 愿景

**EN:** TripPilot helps a traveler turn preferences and constraints into an explainable draft itinerary. It retrieves supporting knowledge and uses tools when freshness or computation matters.

**中文：** TripPilot 帮助旅行者把偏好与约束转化为可解释的行程草案；当信息时效性或计算准确性重要时，系统通过检索与工具获得依据。

## Primary learning scenario / 核心学习场景

Given a destination, dates, budget, interests, pace, and constraints, the system should produce a day-by-day draft with assumptions, sources, estimated costs, and unresolved questions.

给定目的地、日期、预算、兴趣、节奏与约束，系统应输出逐日行程草案，并列出假设、来源、估算费用和待确认问题。

## Intended users / 目标用户

- The learner building the system / 构建系统的学习者
- A traveler reviewing a draft plan, not blindly following it / 审阅行程草案、而非盲目执行的旅行者

## MVP capabilities / 最小可行能力

1. Capture and validate travel constraints / 收集并校验旅行约束。
2. Retrieve relevant, cited knowledge / 检索相关知识并提供引用。
3. Call a small set of explicit tools / 调用少量、边界明确的工具。
4. Produce structured itinerary output / 生成结构化行程。
5. Explain assumptions and uncertainty / 解释假设与不确定性。
6. Evaluate a saved set of scenarios / 使用固定场景进行评测。

## Non-goals for early versions / 早期版本非目标

- Booking, purchasing, or modifying real reservations / 真实预订、支付或修改订单
- Autonomous messaging or calendar writes / 自主发送消息或写入日历
- Claiming real-time accuracy without a live source / 没有实时来源却声称信息实时准确
- Storing passports, payment data, or sensitive personal data / 保存护照、支付信息或敏感个人数据
- A general-purpose autonomous assistant / 通用自主 Agent

## Success criteria / 成功标准

- A user can tell why each major recommendation was made / 用户能理解主要推荐的原因。
- Time-sensitive facts show a source and retrieval time / 时效性事实附带来源和检索时间。
- Invalid or conflicting constraints produce questions instead of fabricated certainty / 约束无效或冲突时，系统提出问题而不是编造确定答案。
- The same evaluation set can compare changes over time / 固定评测集能用于比较迭代效果。
- The learner can diagram and explain the complete flow without assistance / 学习者能独立画出并解释完整流程。

## Example user story / 用户故事示例

> As a traveler visiting Shanghai for three days with a moderate budget and an interest in architecture, I want a walkable draft itinerary with rainy-day alternatives, so I can review the trade-offs before booking.
>
> 作为一名计划在上海旅行三天、预算适中且喜欢建筑的游客，我希望得到步行友好的行程草案和雨天备选方案，以便在预订前审阅取舍。
