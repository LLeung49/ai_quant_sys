"""Read-only market-data provider factory for ETF validation."""

from datetime import date
from dataclasses import dataclass, replace
from typing import Callable, Mapping, Sequence

from ..market_data import AdaptiveMarketDataProvider
from ..contracts import ExecutionAvailability
from .validation_eligibility import validation_eligibility


@dataclass(frozen=True)
class ResolvedValidationRange:
    requested_start: date
    requested_end: date
    start_date: date
    end_date: date
    adjustments: tuple[str, ...]


def resolve_validation_range(
    requested_start: date,
    requested_end: date,
    sessions: Sequence[date],
) -> ResolvedValidationRange:
    """Resolve requested calendar boundaries and preserve every adjustment."""
    if requested_start > requested_end:
        raise ValueError("requested_start must not be after requested_end")
    ordered = tuple(sorted(set(sessions)))
    if not ordered:
        raise ValueError("sessions must not be empty")
    start = next((session for session in ordered if session >= requested_start), None)
    end = next((session for session in reversed(ordered) if session <= requested_end), None)
    if start is None or end is None or start > end:
        raise ValueError("requested range has no available trading sessions")
    adjustments: list[str] = []
    if start != requested_start:
        adjustments.append("start_forward")
    if end != requested_end:
        adjustments.append("end_backward")
    return ResolvedValidationRange(
        requested_start, requested_end, start, end, tuple(adjustments),
    )


LATEST_ACTION_AS_OF_SQL = """
SELECT MAX(ex_date) AS latest_action_date
FROM trade_corporate_action
WHERE stock_code = %s AND ex_date <= %s
  AND event_status = 'effective' AND data_source = 'xtquant'
"""


def adjustment_provenance_loader(
    query: Callable[[str, tuple[object, ...]], Sequence[Mapping[str, object]]],
    stock_code: str,
    as_of_date: date,
) -> dict[str, object]:
    rows = tuple(query(LATEST_ACTION_AS_OF_SQL, (stock_code, as_of_date)))
    if len(rows) != 1:
        raise ValueError("adjustment provenance query must return exactly one row")
    latest = rows[0].get("latest_action_date")
    if latest is not None and not isinstance(latest, date):
        raise ValueError("latest_action_date must be a date or null")
    return {"stock_code": stock_code, "as_of_date": as_of_date,
            "source": "trade_corporate_action:xtquant", "complete": True,
            "latest_action_date": latest}


class ValidationMarketDataProvider:
    """Add fixed-manifest tradability to the aligned read-only price provider."""

    def __init__(self, prices: AdaptiveMarketDataProvider) -> None:
        self._prices = prices

    def load_bars(self, stock_code, start_date, end_date):
        bars = self._prices.load_bars(stock_code, start_date, end_date)
        return tuple(
            replace(bar, execution_availability=ExecutionAvailability(False, False, "daily_bar_assumption"))
            if bar.execution_availability.provenance == "unavailable" else bar
            for bar in bars
        )

    def first_aligned_session(self, stock_code, start_date, end_date):
        return self._prices.first_aligned_session(stock_code, start_date, end_date)

    def load_actions(self, stock_code, start_date, end_date):
        return self._prices.load_actions(stock_code, start_date, end_date)

    def load_eligibility(self, stock_code, bars):
        return validation_eligibility(stock_code, bars)


def default_validation_provider() -> ValidationMarketDataProvider:
    from data_ingestion.db_config import execute_query
    from morning_conference.sector_rotation2.research.evaluation.prices import load_authoritative_market_calendar
    return ValidationMarketDataProvider(AdaptiveMarketDataProvider(
        query=execute_query,
        calendar_loader=lambda start, end: load_authoritative_market_calendar(start, end, execute_query),
        adjustment_provenance_loader=lambda code, cutoff: adjustment_provenance_loader(execute_query, code, cutoff),
    ))
