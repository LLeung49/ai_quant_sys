"""60-session readiness verification: every gate must be evaluated independently."""

from __future__ import annotations

from datetime import date, datetime, timedelta
from decimal import Decimal
import json

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
import asset_allocation.etf_adaptive.verify_shadow as verify_module


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


def _store_with_n_runs(n: int, *, changing_holdings: bool = False) -> InMemoryShadowStore:
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
            state=StrategyState(cash=Decimal("100000"), position_shares=offset % 10 if changing_holdings else 0),
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


def test_readiness_rejects_unexplained_holdings_changes() -> None:
    store = _store_with_n_runs(60, changing_holdings=True)

    result = verify_shadow_period(START, END, store)

    assert result.ready is False
    assert "state_continuity_eq_1" in result.failures


@pytest.mark.parametrize("mutation", (
    None, "missing_order", "missing_fill", "wrong_side", "wrong_fill_date",
    "wrong_config", "incomplete_fill", "wrong_quantity", "wrong_cash", "unsupported_intent",
    "changed_run_config", "changed_model",
))
def test_state_continuity_reconciles_prior_grid_advice_and_observed_fill(mutation) -> None:
    store = _store_with_n_sessions(2)
    first_state = StrategyState(cash=Decimal("100000"))
    order = OrderIntent(
        signal_date=START, side=Side.SELL if mutation == "wrong_side" else Side.BUY,
        reason=OrderReason.TREND_ENTRY if mutation == "unsupported_intent" else OrderReason.GRID_INITIALIZE,
        signal_atr20=None, signal_thresholds=(), target_budget=1005.0,
        risk_per_unit=0.005, quantity_rationale="recorded allocation",
    )
    second_state = StrategyState(
        cash=Decimal("98994.70") if mutation != "wrong_cash" else Decimal("98900"),
        position_shares=100 if mutation != "wrong_quantity" else 200,
    )
    for index, state in enumerate((first_state, second_state)):
        as_of = START + timedelta(days=index)
        store.persist_run(build_run_record(
            run_id=f"run-{index}", identity=ShadowRunIdentity(
                as_of, "shadow-v2" if index and mutation == "changed_model" else "shadow-v1", "510300.SH",
            ),
            config_hash="other-config" if index and mutation == "changed_run_config" else "cfg-shadow-1",
            execution_eligible_date=as_of + timedelta(days=1),
            state=state, orders=(order,) if index == 0 and mutation != "missing_order" else (),
        ))
    observation = FillObservation(
        execution_eligible_date=START + timedelta(days=2 if mutation == "wrong_fill_date" else 1),
        stock_code="510300.SH", config_hash="wrong" if mutation == "wrong_config" else "cfg-shadow-1",
        raw_open=10.0, raw_close=10.0, slippage_bps=3.0,
        fill_complete=mutation != "incomplete_fill", notes=None,
    )

    result = verify_shadow_period(
        START, END, store, observations=() if mutation == "missing_fill" else (observation,),
    )

    assert result.gate_results()["state_continuity_eq_1"] is (mutation is None)


def test_state_continuity_allows_regime_change_without_balance_change() -> None:
    store = _store_with_n_sessions(2)
    for index, regime in enumerate((Regime.GRID, Regime.TREND)):
        as_of = START + timedelta(days=index)
        store.persist_run(build_run_record(
            run_id=f"run-{index}", identity=ShadowRunIdentity(as_of, "shadow-v1", "510300.SH"),
            config_hash="cfg-shadow-1", execution_eligible_date=as_of + timedelta(days=1),
            state=StrategyState(cash=Decimal("100000"), regime=regime), orders=(),
        ))

    assert verify_shadow_period(START, END, store).gate_results()["state_continuity_eq_1"] is True


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


def test_main_uses_injected_durable_store(monkeypatch, capsys) -> None:
    store = _store_with_n_runs(60)
    monkeypatch.setattr(verify_module, "default_shadow_store", lambda: store, raising=False)
    assert verify_module.main(["--start-date", START.isoformat(), "--end-date", END.isoformat()]) == 0
    assert '"ready": true' in capsys.readouterr().out


def test_main_loads_observations_from_json_file(tmp_path, monkeypatch) -> None:
    store = _store_with_n_runs(60)
    observation_file = tmp_path / "observations.json"
    observation_file.write_text(json.dumps([{
        "execution_eligible_date": START.isoformat(), "stock_code": "510300.SH",
        "config_hash": "cfg-shadow-1", "raw_open": 1.0, "raw_close": 1.0,
        "slippage_bps": 10.0, "fill_complete": True, "notes": "test",
    }]), encoding="utf-8")
    monkeypatch.setattr(verify_module, "default_shadow_store", lambda: store, raising=False)

    assert verify_module.main([
        "--start-date", START.isoformat(), "--end-date", END.isoformat(),
        "--observation-file", str(observation_file),
    ]) == 2


@pytest.mark.parametrize("field,value", (("fill_complete", "false"), ("slippage_bps", float("nan"))))
def test_main_rejects_malformed_observation_values(tmp_path, monkeypatch, field, value) -> None:
    store = _store_with_n_runs(60)
    observation_file = tmp_path / "observations.json"
    row = {
        "execution_eligible_date": START.isoformat(), "stock_code": "510300.SH",
        "config_hash": "cfg-shadow-1", "raw_open": 1.0, "raw_close": 1.0,
        "slippage_bps": 1.0, "fill_complete": True, "notes": "test",
    }
    row[field] = value
    observation_file.write_text(json.dumps([row]), encoding="utf-8")
    monkeypatch.setattr(verify_module, "default_shadow_store", lambda: store, raising=False)

    with pytest.raises(ValueError):
        verify_module.main([
            "--start-date", START.isoformat(), "--end-date", END.isoformat(),
            "--observation-file", str(observation_file),
        ])


@pytest.mark.parametrize("field,value", (("execution_eligible_date", 1), ("notes", {"bad": "type"})))
def test_main_rejects_invalid_observation_date_and_notes(tmp_path, monkeypatch, field, value) -> None:
    store = _store_with_n_runs(60)
    observation_file = tmp_path / "observations.json"
    row = {
        "execution_eligible_date": START.isoformat(), "stock_code": "510300.SH",
        "config_hash": "cfg-shadow-1", "raw_open": 1.0, "raw_close": 1.0,
        "slippage_bps": 1.0, "fill_complete": True, "notes": "test",
    }
    row[field] = value
    observation_file.write_text(json.dumps([row]), encoding="utf-8")
    monkeypatch.setattr(verify_module, "default_shadow_store", lambda: store, raising=False)

    with pytest.raises(ValueError):
        verify_module.main([
            "--start-date", START.isoformat(), "--end-date", END.isoformat(),
            "--observation-file", str(observation_file),
        ])
