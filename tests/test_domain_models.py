from datetime import UTC, date, datetime
from decimal import Decimal

import pytest
from pydantic import ValidationError

from trippilot.domain import (
    Evidence,
    ItineraryDay,
    ItineraryItem,
    Money,
    ToolResult,
    ToolStatus,
    TripPlan,
    TripRequest,
)


def make_request() -> TripRequest:
    return TripRequest(
        destination="Shanghai",
        start_date=date(2026, 10, 1),
        end_date=date(2026, 10, 3),
        budget=Money(amount=Decimal("3000.00"), currency="cny"),
        interests=["architecture"],
    )


def test_trip_request_normalizes_currency_and_counts_travelers() -> None:
    request = make_request()

    assert request.budget is not None
    assert request.budget.currency == "CNY"
    assert request.travelers.total == 1


def test_trip_request_rejects_reversed_dates() -> None:
    with pytest.raises(ValidationError, match="end_date"):
        TripRequest(
            destination="Shanghai",
            start_date=date(2026, 10, 3),
            end_date=date(2026, 10, 1),
        )


def test_contracts_reject_unknown_fields() -> None:
    with pytest.raises(ValidationError, match="extra_forbidden"):
        TripRequest(
            destination="Shanghai",
            start_date=date(2026, 10, 1),
            end_date=date(2026, 10, 3),
            passport_number="must-not-be-accepted",  # type: ignore[call-arg]
        )


def test_failed_tool_result_requires_error() -> None:
    with pytest.raises(ValidationError, match="must contain an error"):
        ToolResult(
            tool_name="weather",
            status=ToolStatus.FAILURE,
            observed_at=datetime.now(UTC),
            duration_ms=20,
        )


def test_successful_tool_result_rejects_error() -> None:
    with pytest.raises(ValidationError, match="cannot contain an error"):
        ToolResult(
            tool_name="weather",
            status=ToolStatus.SUCCESS,
            error="unexpected",
            observed_at=datetime.now(UTC),
            duration_ms=20,
        )


def test_timestamps_must_include_timezone() -> None:
    with pytest.raises(ValidationError, match="timezone"):
        ToolResult(
            tool_name="weather",
            status=ToolStatus.SUCCESS,
            payload={},
            observed_at=datetime(2026, 9, 15),
            duration_ms=20,
        )


def test_evidence_timestamp_must_include_timezone() -> None:
    with pytest.raises(ValidationError, match="timezone"):
        Evidence(
            claim="The museum opens at 09:00",
            source_title="Museum hours",
            source_url="https://example.com/hours",
            retrieved_at=datetime(2026, 9, 15),
            confidence=0.9,
        )


def test_trip_plan_rejects_non_sequential_days() -> None:
    request = make_request()
    item = ItineraryItem(place="The Bund", rationale="Architecture walk")

    with pytest.raises(ValidationError, match="sequential"):
        TripPlan(
            request=request,
            days=[ItineraryDay(day_number=2, date=request.start_date, items=[item])],
            generated_at=datetime.now(UTC),
        )


def test_trip_plan_rejects_dates_outside_request() -> None:
    request = make_request()
    item = ItineraryItem(place="The Bund", rationale="Architecture walk")

    with pytest.raises(ValidationError, match="requested date range"):
        TripPlan(
            request=request,
            days=[ItineraryDay(day_number=1, date=date(2026, 10, 4), items=[item])],
            generated_at=datetime.now(UTC),
        )


def test_trip_plan_timestamp_must_include_timezone() -> None:
    request = make_request()
    item = ItineraryItem(place="The Bund", rationale="Architecture walk")

    with pytest.raises(ValidationError, match="timezone"):
        TripPlan(
            request=request,
            days=[ItineraryDay(day_number=1, date=request.start_date, items=[item])],
            generated_at=datetime(2026, 9, 15),
        )
