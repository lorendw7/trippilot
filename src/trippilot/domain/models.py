"""Validated, provider-independent contracts for TripPilot."""

from __future__ import annotations

from datetime import date, datetime
from decimal import Decimal
from enum import StrEnum
from typing import Annotated, Any, Self

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl,
    StringConstraints,
    field_validator,
    model_validator,
)

NonEmptyText = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
CurrencyCode = Annotated[
    str,
    StringConstraints(strip_whitespace=True, to_upper=True, pattern=r"^[A-Z]{3}$"),
]


class DomainModel(BaseModel):
    """Base policy shared by every trusted domain contract."""

    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)


class Pace(StrEnum):
    SLOW = "slow"
    BALANCED = "balanced"
    FAST = "fast"


class Freshness(StrEnum):
    STABLE = "stable"
    TIME_SENSITIVE = "time_sensitive"
    UNKNOWN = "unknown"


class ToolStatus(StrEnum):
    SUCCESS = "success"
    FAILURE = "failure"


class Travelers(DomainModel):
    adults: int = Field(default=1, ge=1, le=20)
    children: int = Field(default=0, ge=0, le=20)

    @property
    def total(self) -> int:
        return self.adults + self.children


class Money(DomainModel):
    amount: Decimal = Field(ge=0, max_digits=12, decimal_places=2)
    currency: CurrencyCode

    @field_validator("currency", mode="before")
    @classmethod
    def normalize_currency(cls, value: object) -> object:
        return value.upper() if isinstance(value, str) else value


class TripRequest(DomainModel):
    destination: NonEmptyText = Field(max_length=200)
    start_date: date
    end_date: date
    travelers: Travelers = Field(default_factory=Travelers)
    budget: Money | None = None
    interests: list[NonEmptyText] = Field(default_factory=list, max_length=20)
    pace: Pace = Pace.BALANCED
    accessibility_needs: list[NonEmptyText] = Field(default_factory=list, max_length=20)
    exclusions: list[NonEmptyText] = Field(default_factory=list, max_length=20)
    special_requests: list[NonEmptyText] = Field(default_factory=list, max_length=20)

    @model_validator(mode="after")
    def validate_date_range(self) -> Self:
        if self.end_date < self.start_date:
            raise ValueError("end_date must be on or after start_date")
        return self


class Evidence(DomainModel):
    claim: NonEmptyText
    source_title: NonEmptyText
    source_url: HttpUrl
    retrieved_at: datetime
    freshness: Freshness = Freshness.UNKNOWN
    confidence: float = Field(ge=0, le=1)

    @model_validator(mode="after")
    def require_timezone(self) -> Self:
        if self.retrieved_at.tzinfo is None or self.retrieved_at.utcoffset() is None:
            raise ValueError("retrieved_at must include a timezone")
        return self


class ToolResult(DomainModel):
    tool_name: NonEmptyText
    status: ToolStatus
    payload: dict[str, Any] | None = None
    error: NonEmptyText | None = None
    observed_at: datetime
    duration_ms: int = Field(ge=0)

    @model_validator(mode="after")
    def validate_status_fields(self) -> Self:
        if self.observed_at.tzinfo is None or self.observed_at.utcoffset() is None:
            raise ValueError("observed_at must include a timezone")
        if self.status is ToolStatus.SUCCESS and self.error is not None:
            raise ValueError("a successful tool result cannot contain an error")
        if self.status is ToolStatus.FAILURE and self.error is None:
            raise ValueError("a failed tool result must contain an error")
        return self


class ItineraryItem(DomainModel):
    time_window: NonEmptyText | None = None
    place: NonEmptyText
    rationale: NonEmptyText
    estimated_cost: Money | None = None
    evidence: list[Evidence] = Field(default_factory=list)
    alternatives: list[NonEmptyText] = Field(default_factory=list, max_length=10)


class ItineraryDay(DomainModel):
    day_number: int = Field(ge=1)
    date: date
    items: list[ItineraryItem] = Field(min_length=1)


class TripPlan(DomainModel):
    request: TripRequest
    assumptions: list[NonEmptyText] = Field(default_factory=list)
    days: list[ItineraryDay] = Field(min_length=1)
    estimated_total: Money | None = None
    warnings: list[NonEmptyText] = Field(default_factory=list)
    unresolved_questions: list[NonEmptyText] = Field(default_factory=list)
    generated_at: datetime

    @model_validator(mode="after")
    def validate_plan_dates(self) -> Self:
        expected_day_numbers = list(range(1, len(self.days) + 1))
        actual_day_numbers = [day.day_number for day in self.days]
        if actual_day_numbers != expected_day_numbers:
            raise ValueError("day numbers must be unique and sequential from 1")
        if any(
            day.date < self.request.start_date or day.date > self.request.end_date
            for day in self.days
        ):
            raise ValueError("itinerary dates must be inside the requested date range")
        if self.generated_at.tzinfo is None or self.generated_at.utcoffset() is None:
            raise ValueError("generated_at must include a timezone")
        return self
