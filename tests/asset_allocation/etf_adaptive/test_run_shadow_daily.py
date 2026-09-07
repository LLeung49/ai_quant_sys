"""Daily shadow runner: freshness, replay, no-broker-import safety."""

from __future__ import annotations

from datetime import date, datetime, timedelta
from decimal import Decimal
from typing import Sequence

import pytest

from asset_allocation.etf_adaptive.config import AdaptiveConfig
from asset_allocation.etf_adaptive.contracts import (
    DualPriceBar,
    ExecutionAvailability,
)
from asset_allocation.etf_adaptive.run_shadow_daily import (
    CutoffNotReachedError,
    DataFreshnessError,
    NonTradingDateError,
    next_trading_session,
    require_after_market_data_cutoff,
    require_fresh_bar,
    run_shadow_date,
)
import asset_allocation.etf_adaptive.run_shadow_daily as shadow_module
from asset_allocation.etf_adaptive.shadow_store import (
    FrozenConfigRecord,
    InMemoryShadowStore,
)


TARGET = date(2026, 9, 1)
EXECUTION_DATE = date(2026, 9, 2)
CALENDAR: tuple[date, ...] = tuple(date(2026, 8, day) for day in range(31, 32)) + (
    date(2026, 9, 1), date(2026, 9, 2), date(2026, 9, 3),
    date(2026, 9, 4), date(2026, 9, 5),
)
DATA_CUTOFF = date(2026, 9, 1)


def _after_close() -> datetime:
    return datetime(2026, 9, 1, 17, 0)


def _bar(trade_date, raw_open=1.00, raw_close=1.01, signal_open=1.00, signal_close=1.01):
    return DualPriceBar(
        stock_code="510300.SH",
        trade_date=trade_date,
        signal_open=signal_open,
        signal_high=max(signal_open, signal_close),
        signal_low=min(signal_open, signal_close),
        signal_close=signal_close,
        raw_open=raw_open,
        raw_high=max(raw_open, raw_close),
        raw_low=min(raw_open, raw_close),
        raw_close=raw_close,
        amount=15_000_000.0,
        suspended=False,
        adjustment_ratio=1.0,
        execution_availability=ExecutionAvailability(True, True, "test"),
    )


def _bars(start: date, end: date) -> tuple[DualPriceBar, ...]:
    return tuple(
        _bar(date(2026, 8, day) if day <= 31 else end) for day in range(30, 31)
    ) + (_bar(end),)


class _StubProvider:
    def __init__(self, *, include_target_bar: bool = True,
                 bars_by_code: dict[str, tuple[DualPriceBar, ...]] | None = None):
        self._include_target_bar = include_target_bar
        self._bars = bars_by_code or {}
        # Provide 252 historical bars up to the day before TARGET so require_fresh_bar reaches
        # the freshness check (the target date bar is added separately or omitted).
        self._historical = tuple(
            _bar(TARGET - timedelta(days=offset))
            for offset in range(260, 0, -1)
        )

    def load_calendar(self, around: date) -> Sequence[date]:
        return CALENDAR

    def load_bars(self, stock_code: str, start_date: date, end_date: date) -> Sequence[DualPriceBar]:
        full = self._bars.get(stock_code, self._historical)
        if self._include_target_bar:
            full = full + (_bar(end_date),)
        filtered = [bar for bar in full if start_date <= bar.trade_date <= end_date]
        return tuple(filtered)


def _store_with_selection() -> InMemoryShadowStore:
    store = InMemoryShadowStore()
    record = FrozenConfigRecord(
        config_hash="cfg-shadow-1",
        config=AdaptiveConfig.default(),
        selection_payload={
            "targets": [
                {
                    "stock_code": "510300.SH",
                    "weight": 1.0,
                    "layer": "core_broad",
                    "tracking_index_code": "000300.SH",
                },
            ],
        },
        data_cutoff=DATA_CUTOFF,
        activation_date=date(2026, 8, 1),
        review_date=date(2027, 2, 1),
        activated_at=datetime(2026, 8, 1, 17, 0),
    )
    store.activate_frozen_config(record)
    return store


def test_require_after_market_data_cutoff_rejects_pre_close_calls() -> None:
    try:
        require_after_market_data_cutoff(TARGET, datetime(2026, 9, 1, 14, 0))
    except CutoffNotReachedError as exc:
        assert "17:00" in str(exc)
    else:
        raise AssertionError("expected CutoffNotReachedError before 17:00")


def test_next_trading_session_returns_first_session_after_target() -> None:
    assert next_trading_session(TARGET, CALENDAR) == EXECUTION_DATE


def test_next_trading_session_rejects_non_trading_dates() -> None:
    try:
        next_trading_session(date(2026, 12, 25), CALENDAR)
    except NonTradingDateError as exc:
        assert "not a trading date" in str(exc)
    else:
        raise AssertionError("expected NonTradingDateError for non-trading date")


def test_require_fresh_bar_fails_closed_when_missing() -> None:
    bars = (_bar(date(2026, 8, 30)),)

    try:
        require_fresh_bar("510300.SH", bars, TARGET)
    except DataFreshnessError as exc:
        assert "510300.SH missing 2026-09-01 bar" in str(exc)
    else:
        raise AssertionError("expected DataFreshnessError for missing bar")


def test_require_fresh_bar_succeeds_when_target_bar_is_present() -> None:
    bars = (_bar(date(2026, 8, 30)), _bar(TARGET))

    bar = require_fresh_bar("510300.SH", bars, TARGET)

    assert bar.trade_date == TARGET


def test_shadow_runner_fails_closed_when_target_bar_is_stale() -> None:
    store = _store_with_selection()
    provider = _StubProvider(include_target_bar=False)

    try:
        run_shadow_date(TARGET, _after_close(), store, provider)
    except DataFreshnessError as exc:
        assert "510300.SH missing 2026-09-01 bar" in str(exc)
    else:
        raise AssertionError("expected DataFreshnessError when bar is stale")


def test_shadow_runner_replay_is_byte_equivalent() -> None:
    store = _store_with_selection()
    provider = _StubProvider()

    first = run_shadow_date(TARGET, _after_close(), store, provider)
    second = run_shadow_date(TARGET, _after_close(), store, provider)

    assert first.canonical_json() == second.canonical_json()


def test_shadow_runner_publishes_execution_eligible_date_and_run_id() -> None:
    store = _store_with_selection()
    provider = _StubProvider()

    summary = run_shadow_date(TARGET, _after_close(), store, provider)

    assert summary.as_of_date == TARGET
    assert summary.execution_eligible_date == EXECUTION_DATE
    assert summary.run_id
    assert summary.target_states
    target, state = summary.target_states[0]
    assert target.stock_code == "510300.SH"
    assert state.config_hash == "cfg-shadow-1"


def test_shadow_runner_requires_active_frozen_selection() -> None:
    store = InMemoryShadowStore()
    provider = _StubProvider()

    try:
        run_shadow_date(TARGET, _after_close(), store, provider)
    except Exception as exc:
        assert "no active frozen selection" in str(exc)
    else:
        raise AssertionError("expected error when no active selection exists")


def test_main_uses_injected_production_boundaries(monkeypatch, capsys) -> None:
    store = _store_with_selection()
    provider = _StubProvider()

    monkeypatch.setattr(shadow_module, "default_shadow_store", lambda: store, raising=False)
    monkeypatch.setattr(shadow_module, "default_shadow_provider", lambda: provider, raising=False)

    assert shadow_module.main([
        "--as-of-date", "2026-09-01", "--today", "2026-09-01T17:00:00",
    ]) == 0
    assert '"run_id"' in capsys.readouterr().out



