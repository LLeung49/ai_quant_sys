from datetime import date

import pandas as pd
import pytest

from morning_conference.sector_rotation2.research.evaluation.calendar import TradingCalendar
from morning_conference.sector_rotation2.research.evaluation.prices import (
    MySQLPriceBarProvider,
    load_authoritative_market_calendar,
    load_exchange_schedule,
)


def test_shift_uses_market_calendar_not_entity_rows() -> None:
    calendar = TradingCalendar([date(2026, 1, 5), date(2026, 1, 6), date(2026, 1, 7), date(2026, 1, 9)])
    assert calendar.shift(date(2026, 1, 5), 1) == date(2026, 1, 6)
    assert calendar.shift(date(2026, 1, 5), 2) == date(2026, 1, 7)
    assert calendar.shift(date(2026, 1, 9), -2) == date(2026, 1, 6)


def test_calendar_rejects_date_outside_master_calendar() -> None:
    calendar = TradingCalendar([date(2026, 1, 5)])
    with pytest.raises(ValueError, match="not a trading date"):
        calendar.shift(date(2026, 1, 4), 1)


def test_mysql_provider_keeps_sector_close_only_and_uses_adjusted_ohlc() -> None:
    calls: list[tuple[str, tuple[object, ...]]] = []

    def query(sql: str, params: tuple[object, ...]) -> list[dict[str, object]]:
        calls.append((sql, params))
        return [{"trade_date": date(2026, 1, 5), "open": 10, "high": 11, "low": 9, "close": 10.5}]

    provider = MySQLPriceBarProvider(query)
    bars = provider.load_bars("stock", "000001.SZ", date(2026, 1, 5), date(2026, 1, 5))
    assert bars[date(2026, 1, 5)].high == 11.0
    assert provider.supports_open("sector_l2") is False
    assert provider.supports_ohlc("sector_l2") is False
    assert "trade_stock_daily_qfq" in calls[0][0]


def test_authoritative_calendar_is_loaded_from_shared_sector_dates() -> None:
    def query(sql: str, params: tuple[object, ...]) -> list[dict[str, object]]:
        assert "SELECT DISTINCT trade_date FROM trade_sector_daily" in sql
        assert params == (1, date(2026, 1, 5), date(2026, 1, 6))
        return [{"trade_date": date(2026, 1, 5)}, {"trade_date": date(2026, 1, 6)}]

    assert load_authoritative_market_calendar(date(2026, 1, 5), date(2026, 1, 6), query) == (date(2026, 1, 5), date(2026, 1, 6))


def test_authoritative_calendar_uses_exchange_schedule_for_future_sessions() -> None:
    """A completed-price table ending at T must not hide scheduled T+1/T+2 sessions."""
    def query(_sql: str, _params: tuple[object, ...]) -> list[dict[str, object]]:
        return [{"trade_date": date(2026, 8, 24)}]

    def exchange_schedule(start: date, end: date) -> tuple[date, ...]:
        assert (start, end) == (date(2026, 8, 24), date(2026, 8, 26))
        return (date(2026, 8, 24), date(2026, 8, 25), date(2026, 8, 26))

    assert load_authoritative_market_calendar(
        date(2026, 8, 24), date(2026, 8, 26), query, schedule_loader=exchange_schedule,
    ) == (date(2026, 8, 24), date(2026, 8, 25), date(2026, 8, 26))


def test_authoritative_calendar_fails_clearly_when_future_schedule_is_unavailable() -> None:
    def query(_sql: str, _params: tuple[object, ...]) -> list[dict[str, object]]:
        return [{"trade_date": date(2026, 8, 24)}]

    def unavailable(_start: date, _end: date) -> tuple[date, ...]:
        raise OSError("schedule endpoint down")

    with pytest.raises(RuntimeError, match="authoritative exchange schedule unavailable"):
        load_authoritative_market_calendar(
            date(2026, 8, 24), date(2026, 8, 26), query, schedule_loader=unavailable,
        )


def test_exchange_schedule_normalizes_timestamp_rows_to_dates(monkeypatch) -> None:
    frame = pd.DataFrame({"trade_date": pd.to_datetime(["2026-08-24", "2026-08-25", "2026-08-26"])})
    monkeypatch.setattr("akshare.tool_trade_date_hist_sina", lambda: frame)

    assert load_exchange_schedule(date(2026, 8, 25), date(2026, 8, 26)) == (
        date(2026, 8, 25), date(2026, 8, 26),
    )
