from datetime import date, datetime
from zoneinfo import ZoneInfo

import pytest

from morning_conference.sector_rotation2.research.calendar import TradingCalendar
from morning_conference.sector_rotation2.research.availability import (
    AvailabilityBasis,
    as_shanghai_naive,
    resolve_availability,
)
from morning_conference.sector_rotation2.research.contracts import CandidateSnapshot
from morning_conference.sector_rotation2.research.status import SnapshotMode


def test_market_close_before_open_is_eligible_at_next_open() -> None:
    """A pre-open completed market-data run enters daily bars at that open."""
    calendar = TradingCalendar([date(2026, 8, 24), date(2026, 8, 25)])

    resolved = resolve_availability(
        date(2026, 8, 24),
        AvailabilityBasis.MARKET_CLOSE_1800,
        calendar,
        datetime(2026, 8, 25, 9, 10),
    )

    assert resolved.data_available_at == datetime(2026, 8, 24, 18, 0)
    assert resolved.execution_eligible_at == datetime(2026, 8, 25, 9, 30)
    assert resolved.daily_bar_entry_date == date(2026, 8, 25)


def test_report_after_open_defers_daily_bar_entry() -> None:
    """A report run completed after the open cannot claim an intraday daily-bar fill."""
    calendar = TradingCalendar([
        date(2026, 8, 24), date(2026, 8, 25), date(2026, 8, 26),
    ])

    resolved = resolve_availability(
        date(2026, 8, 24),
        AvailabilityBasis.NEXT_TRADE_DAY_0000,
        calendar,
        datetime(2026, 8, 25, 10, 0),
    )

    assert resolved.data_available_at == datetime(2026, 8, 25, 0, 0)
    assert resolved.execution_eligible_at == datetime(2026, 8, 25, 10, 0)
    assert resolved.daily_bar_entry_date == date(2026, 8, 26)


def test_run_completed_at_open_defers_daily_bar_entry() -> None:
    """At the opening timestamp the daily open is no longer safely tradable."""
    calendar = TradingCalendar([date(2026, 8, 24), date(2026, 8, 25), date(2026, 8, 26)])

    resolved = resolve_availability(
        date(2026, 8, 24), AvailabilityBasis.MARKET_CLOSE_1800, calendar, datetime(2026, 8, 25, 9, 30),
    )

    assert resolved.daily_bar_entry_date == date(2026, 8, 26)


def test_report_availability_skips_non_trading_days() -> None:
    """Report availability uses the calendar's next session rather than calendar midnight."""
    calendar = TradingCalendar([date(2026, 8, 28), date(2026, 8, 31)])

    resolved = resolve_availability(
        date(2026, 8, 28),
        AvailabilityBasis.NEXT_TRADE_DAY_0000,
        calendar,
        datetime(2026, 8, 31, 9, 0),
    )

    assert resolved.data_available_at == datetime(2026, 8, 31, 0, 0)
    assert resolved.execution_eligible_at == datetime(2026, 8, 31, 9, 30)


def test_run_multiple_sessions_late_uses_first_open_strictly_after_completion() -> None:
    """A delayed run skips every session that opened before it completed."""
    calendar = TradingCalendar([
        date(2026, 8, 21), date(2026, 8, 24), date(2026, 8, 25), date(2026, 8, 26),
    ])

    resolved = resolve_availability(
        date(2026, 8, 21),
        AvailabilityBasis.MARKET_CLOSE_1800,
        calendar,
        datetime(2026, 8, 25, 10, 0),
    )

    assert resolved.daily_bar_entry_date == date(2026, 8, 26)


def test_run_completed_on_non_trading_day_uses_next_trading_open() -> None:
    """A weekend completion waits for the first subsequent trading-day open."""
    calendar = TradingCalendar([
        date(2026, 8, 21), date(2026, 8, 24), date(2026, 8, 25),
        date(2026, 8, 28), date(2026, 8, 31),
    ])

    resolved = resolve_availability(
        date(2026, 8, 21),
        AvailabilityBasis.MARKET_CLOSE_1800,
        calendar,
        datetime(2026, 8, 29, 14, 0),
    )

    assert resolved.daily_bar_entry_date == date(2026, 8, 31)
    assert resolved.execution_eligible_at == datetime(2026, 8, 31, 9, 30)


def test_run_before_its_data_is_available_is_rejected() -> None:
    """A snapshot cannot report completion before its market inputs were allowed."""
    calendar = TradingCalendar([date(2026, 8, 24), date(2026, 8, 25)])

    with pytest.raises(ValueError, match="before data_available_at"):
        resolve_availability(
            date(2026, 8, 24),
            AvailabilityBasis.MARKET_CLOSE_1800,
            calendar,
            datetime(2026, 8, 24, 17, 59),
        )


def test_legacy_basis_cannot_resolve_new_snapshot_timing() -> None:
    """Legacy provenance is reserved for historical records, not new time resolution."""
    calendar = TradingCalendar([date(2026, 8, 24), date(2026, 8, 25)])

    with pytest.raises(ValueError, match="LEGACY_INFERRED"):
        resolve_availability(
            date(2026, 8, 24),
            AvailabilityBasis.LEGACY_INFERRED,
            calendar,
            datetime(2026, 8, 25, 9, 0),
        )


def test_candidate_snapshot_accepts_immutable_availability_metadata() -> None:
    """Delayed snapshots retain the resolved times alongside their identity fields."""
    snapshot = CandidateSnapshot(
        as_of_date=date(2026, 8, 24),
        entity_type="etf",
        entity_code="510300.SH",
        sector_level=None,
        sector_name=None,
        strategy_type="etf_core",
        candidate_status="candidate",
        candidate_score=0.9,
        model_version="v1",
        config_hash="hash",
        run_id="run-1",
        snapshot_mode=SnapshotMode.DELAYED_SHADOW,
        data_available_at=datetime(2026, 8, 24, 18, 0),
        run_at=datetime(2026, 8, 25, 9, 10),
        execution_eligible_at=datetime(2026, 8, 25, 9, 30),
        availability_basis=AvailabilityBasis.MARKET_CLOSE_1800,
    )

    assert snapshot.execution_eligible_at == datetime(2026, 8, 25, 9, 30)
    assert snapshot.availability_basis is AvailabilityBasis.MARKET_CLOSE_1800


def test_run_timestamp_is_normalized_to_naive_shanghai_time() -> None:
    normalized = as_shanghai_naive(datetime(2026, 8, 25, 1, 10, tzinfo=ZoneInfo("UTC")))

    assert normalized == datetime(2026, 8, 25, 9, 10)
    assert normalized.tzinfo is None
