# Core data contracts / 核心数据契约

The executable source of truth is `src/trippilot/domain/models.py`. All models reject unknown
fields so provider responses and tool payloads cannot silently expand the trusted contract.

可执行的事实来源是 `src/trippilot/domain/models.py`。所有模型都拒绝未知字段，避免供应商
响应或工具载荷静默扩大可信边界。

| Contract / 契约 | Purpose / 用途 | Key invariants / 关键约束 |
|---|---|---|
| `TripRequest` | Validated traveler intent / 已校验的旅行意图 | End date is not before start date; traveler count is positive / 结束日期不早于开始日期；旅行人数为正 |
| `Money` | Currency-safe estimate / 带币种的金额估算 | Amount is non-negative; currency is a three-letter uppercase code / 金额非负；币种为三位大写代码 |
| `Evidence` | Support for a claim / 事实依据 | Retrieval timestamp has a timezone; confidence is 0–1 / 检索时间包含时区；置信度为 0–1 |
| `ToolResult` | Provider-independent tool response / 与供应商无关的工具响应 | Success has no error; failure has an error / 成功时无错误；失败时必须有错误 |
| `ItineraryDay` | One dated group of itinerary items / 某日行程组 | Contains one or more items / 至少包含一个行程项 |
| `TripPlan` | Structured final draft / 结构化最终草案 | Day numbers are unique, ordered, and inside the request date range / 日期序号唯一、有序且处于请求范围内 |

## Trust boundary / 信任边界

External text is never promoted directly into a trusted model. Retrieval and tool adapters must
first normalize it into `Evidence` or `ToolResult`; the planner then constructs `TripPlan`.

外部文本不能直接成为可信模型。检索和工具适配器必须先将其标准化为 `Evidence` 或
`ToolResult`，再由规划器构造 `TripPlan`。
