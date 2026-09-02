"""Resolve immutable operational availability times for research snapshots."""

from dataclasses import dataclass
from datetime import date, datetime, time
from enum import Enum
from zoneinfo import ZoneInfo

from .calendar import TradingCalendar


class AvailabilityBasis(str, Enum):
    """The input-data rule used to determine when a signal became available."""

    MARKET_CLOSE_1800 = "market_close_1800"
    NEXT_TRADE_DAY_0000 = "next_trade_day_0000"
    LEGACY_INFERRED = "legacy_inferred"


_SHANGHAI = ZoneInfo("Asia/Shanghai")


def as_shanghai_naive(value: datetime | None = None) -> datetime:
    """Return a MySQL-DATETIME-safe timestamp in the fixed Shanghai timezone."""
    source = value or datetime.now(_SHANGHAI)
    if source.tzinfo is not None:
        source = source.astimezone(_SHANGHAI).replace(tzinfo=None)
    return source


@dataclass(frozen=True)
class AvailabilityMetadata:
    """Operational times resolved once and persisted with a candidate snapshot."""

    data_available_at: datetime
    run_at: datetime
    execution_eligible_at: datetime
    daily_bar_entry_date: date
    availability_basis: AvailabilityBasis


def resolve_availability(
    as_of_date: date,
    basis: AvailabilityBasis,
    calendar: TradingCalendar,
    run_at: datetime,
) -> AvailabilityMetadata:
    """Resolve availability and daily-bar-safe entry timing in Asia/Shanghai time."""
    if basis is AvailabilityBasis.LEGACY_INFERRED:
        raise ValueError("LEGACY_INFERRED cannot resolve new snapshot timing")

    next_trade_date = calendar.shift(as_of_date, 1)
    scheduled_open = datetime.combine(next_trade_date, time(9, 30))
    data_available_at = (
        datetime.combine(as_of_date, time(18))
        if basis is AvailabilityBasis.MARKET_CLOSE_1800
        else datetime.combine(next_trade_date, time())
    )
    if run_at < data_available_at:
        raise ValueError("run_at cannot be before data_available_at")

    if run_at.date() in calendar:
        execution_eligible_at = max(datetime.combine(run_at.date(), time(9, 30)), run_at)
    else:
        execution_eligible_at = scheduled_open
        while execution_eligible_at < run_at:
            execution_eligible_at = datetime.combine(
                calendar.shift(execution_eligible_at.date(), 1), time(9, 30),
            )
    daily_bar_entry_date = next_trade_date
    while datetime.combine(daily_bar_entry_date, time(9, 30)) <= run_at:
        daily_bar_entry_date = calendar.shift(daily_bar_entry_date, 1)
    return AvailabilityMetadata(
        data_available_at=data_available_at,
        run_at=run_at,
        execution_eligible_at=execution_eligible_at,
        daily_bar_entry_date=daily_bar_entry_date,
        availability_basis=basis,
    )
