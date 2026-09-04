"""60-session readiness verification: every gate must be evaluated independently."""

from __future__ import annotations

from datetime import date, datetime, timedelta
from decimal import Decimal

import pytest

from asset_allocation.etf_adaptive.run_shadow_daily import run_shadow_date
from asset_allocation.etf_adaptive.shadow_store import (
    AdviceRecord,
    FillObservation,
    FrozenConfigRecord,
    HealthCheck,
    InMemoryShadowStore,
    ShadowRunIdentity,
    ShadowRunRecord,
    StateRecord,
    build_run_record,
)
from asset_allocation.etf_adaptive.state import (
    OrderIntent,
    OrderReason,
    Regime,
    Side,
    StrategyState,
)
from asset_allocation.etf_adaptive.verify_shadow import (
    READINESS_GATES,
    verify_shadow_period,
)


START = date(2026, 1, 1)
END = date(2026, 6, 30)


def _stub_provider():
    class _Provider:
        def __init__(self):
            self._calendar = [START + timedelta(days=offset) for offset in range(365)]

        def load_calendar(self, around):
            return self._calendar

        def load_bars(self, stock_code, start_date, end_date):
            return tuple(
                _bar(stock_code, date(2025, 1, 1) + timedelta(days=index))
                for index in range(800)
            )

    return _Provider()


def _bar(stock_code, trade_date):
    from asset_allocation.etf_adaptive.contracts import (
        DualPriceBar,
        ExecutionAvailability,
    )
    return DualPriceBar(
        stock_code=stock_code,
        trade_date=trade_date,
        signal_open=1.0,
        signal_high=1.0,
        signal_low=1.0,
        signal_close=1.0,
        raw_open=1.0,
        raw_high=1.0,
        raw_low=1.0,
        raw_close=1.0,
        amount=15_000_000.0,
        suspended=False,
        adjustment_ratio=1.0,
        execution_availability=ExecutionAvailability(True, True, "test"),
    )


def _store_with_n_sessions(n: int, *, config_hash: str = "cfg-shadow-1") -> InMemoryShadowStore:
    store = InMemoryShadowStore()
    store.activate_frozen_config(FrozenConfigRecord(
        config_hash=config_hash,
        config=__import__("asset_allocation.etf_adaptive.config", fromlist=["AdaptiveConfig"]).AdaptiveConfig.default(),
        selection_payload={
            "targets": [{"stock_code": "510300.SH", "weight": 1.0,
                         "layer": "core_broad", "tracking_index_code": "000300.SH"}],
        },
        data_cutoff=START,
        activation_date=START,
        review_date=START + timedelta(days=183),
        activated_at=datetime(2026, 1, 1, 17, 0),
    ))
    return store


def _store_with_n_runs(n: int) -> InMemoryShadowStore:
    store = _store_with_n_sessions(n)
    for offset in range(n):
        as_of = START + timedelta(days=offset)
        identity = ShadowRunIdentity(
            as_of_date=as_of,
            model_version="shadow-v1",
            stock_code="510300.SH",
        )
        record = build_run_record(
            run_id=f"run-{offset:03d}",
            identity=identity,
            config_hash="cfg-shadow-1",
            execution_eligible_date=as_of + timedelta(days=1),
            state=StrategyState(cash=Decimal("100000"), position_shares=offset % 10),
            orders=(),
        )
        store.persist_run(record)
    return store


def test_readiness_requires_sixty_complete_sessions() -> None:
    store = _store_with_n_runs(59)

    result = verify_shadow_period(START, END, store)

    assert result.ready is False
    assert "complete_sessions_gte_60" in result.failures


def test_readiness_passes_when_six_gate_clear() -> None:
    store = _store_with_n_runs(80)

    result = verify_shadow_period(START, END, store)

    assert result.ready is True
    assert result.failures == ()


def test_readiness_reports_every_gate_independently() -> None:
    store = _store_with_n_runs(60)
    store.record_fill_observation(FillObservation(
        execution_eligible_date=START + timedelta(days=1),
        stock_code="510300.SH",
        config_hash="cfg-shadow-1",
        raw_open=1.0, raw_close=1.0,
        slippage_bps=10.0,
        fill_complete=True,
        notes="over 5bp",
    ))

    result = verify_shadow_period(START, END, store, observations=store.fill_observations)

    assert "observed_slippage_within_5bp_scenario" in result.failures
    assert "complete_sessions_gte_60" not in result.failures
    gate_results = result.gate_results()
    assert gate_results["complete_sessions_gte_60"] is True
    assert gate_results["observed_slippage_within_5bp_scenario"] is False


def test_readiness_rejects_future_data_in_health_check() -> None:
    store = _store_with_n_sessions(60)
    identity = ShadowRunIdentity(
        as_of_date=START + timedelta(days=10),
        model_version="shadow-v1",
        stock_code="510300.SH",
    )
    record = build_run_record(
        run_id="run-future",
        identity=identity,
        config_hash="cfg-shadow-1",
        execution_eligible_date=START + timedelta(days=11),
        state=StrategyState(cash=Decimal("100000")),
        orders=(),
    )
    record = _replace(record, health_checks=(
        HealthCheck(
            run_id="run-future",
            check_name="data_freshness",
            passed=True,
            detail={"bar_trade_date": (START + timedelta(days=20)).isoformat()},
        ),
    ))
    store.persist_run(record)

    result = verify_shadow_period(START, END, store)

    assert "future_data_violations_eq_0" in result.failures


def _replace(record, **fields):
    from dataclasses import replace as _replace
    return _replace(record, **fields)


def test_readiness_rejects_window_inversion() -> None:
    store = _store_with_n_sessions(60)

    try:
        verify_shadow_period(END, START, store)
    except ValueError as exc:
        assert "start_date" in str(exc)
    else:
        raise AssertionError("expected ValueError for inverted window")


def test_readiness_checked_gates_match_spec() -> None:
    store = _store_with_n_runs(60)

    result = verify_shadow_period(START, END, store)

    assert set(result.checked_gates) == set(READINESS_GATES)
