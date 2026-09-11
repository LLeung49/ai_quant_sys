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
    InstrumentType,
    SubLayer,
)
from asset_allocation.etf_adaptive.run_shadow_daily import (
    ChinaAStockCostBoundary,
    CutoffNotReachedError,
    DataFreshnessError,
    ETFCostBoundary,
    NonTradingDateError,
    TargetSpec,
    cost_boundary_for,
    execution_cost_config_for,
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


def _approval(config_hash: str) -> dict[str, object]:
    return {
        "conclusion": "passed",
        "config_hash": config_hash,
        "universe_hash": "universe-hash",
        "data_cutoff": DATA_CUTOFF.isoformat(),
        "data_audit_passed": True,
    }


def _approved_layer_benchmarks(
    *, config_hash: str, universe_hash: str, data_cutoff: str,
) -> dict[str, object]:
    return {
        layer: {
            "passed": True,
            "decision": {"conclusion": "passed", "blockers": []},
            "config_hash": config_hash,
            "universe_hash": universe_hash,
            "data_cutoff": data_cutoff,
        }
        for layer in ("defensive", "broad_beta")
    }


def _approved_research_fields(config_hash: str) -> dict[str, object]:
    return {
        "research_approval": _approval(config_hash),
        "layer_benchmarks": _approved_layer_benchmarks(
            config_hash=config_hash,
            universe_hash="universe-hash",
            data_cutoff=DATA_CUTOFF.isoformat(),
        ),
    }


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
            **_approved_research_fields("cfg-shadow-1"),
            "targets": [
                {
                    "stock_code": "510300.SH",
                    "weight": "1",
                    "layer": "broad_beta",
                    "tracking_index_code": "000300.SH",
                    "sub_layer": "broad_domestic_core",
                    "sub_layer_budget": "100000",
                    "instrument_type": "etf",
                    "config_hash": "cfg-shadow-1",
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


def _store_with_layered_target_budgets() -> InMemoryShadowStore:
    store = InMemoryShadowStore()
    store.activate_frozen_config(FrozenConfigRecord(
        config_hash="cfg-layered-budget",
        config=AdaptiveConfig.default(),
        selection_payload={
            **_approved_research_fields("cfg-layered-budget"),
            "targets": [
                {
                    "stock_code": "510300.SH", "tracking_index_code": "000300.SH",
                    "layer": "broad_beta", "sub_layer": "broad_domestic_core",
                    "sub_layer_budget": "42000", "instrument_type": "etf", "weight": "0.6",
                    "config_hash": "cfg-layered-budget",
                },
                {
                    "stock_code": "510500.SH", "tracking_index_code": "000905.SH",
                    "layer": "broad_beta", "sub_layer": "broad_domestic_core",
                    "sub_layer_budget": "42000", "instrument_type": "etf", "weight": "0.4",
                    "config_hash": "cfg-layered-budget",
                },
            ],
        },
        data_cutoff=DATA_CUTOFF,
        activation_date=date(2026, 8, 1),
        review_date=date(2027, 2, 1),
        activated_at=datetime(2026, 8, 1, 17, 0),
    ))
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


def test_shadow_runner_initializes_each_target_from_its_weighted_sub_layer_budget() -> None:
    store = _store_with_layered_target_budgets()
    provider = _StubProvider()

    summary = run_shadow_date(TARGET, _after_close(), store, provider)

    assert {
        target.stock_code: state.cash for target, state in summary.target_states
    } == {
        "510300.SH": Decimal("25200.0"),
        "510500.SH": Decimal("16800.0"),
    }


def test_cost_boundary_dispatches_etf_and_china_a_stock_schedules() -> None:
    etf = TargetSpec(
        stock_code="510300.SH", tracking_index_code="000300.SH", layer="broad_beta",
        weight=Decimal("1"), sub_layer=SubLayer.DOMESTIC_CORE,
        sub_layer_budget=Decimal("42000"), instrument_type=InstrumentType.ETF,
    )
    stock = TargetSpec(
        stock_code="600000.SH", tracking_index_code="000922.SH", layer="defensive",
        weight=Decimal("1"), sub_layer=SubLayer.DEFENSIVE_BLUE_CHIP,
        sub_layer_budget=Decimal("18000"), instrument_type=InstrumentType.STOCK,
    )

    etf_cost = cost_boundary_for(etf, TARGET, AdaptiveConfig.default())
    stock_cost = cost_boundary_for(stock, TARGET, AdaptiveConfig.default())

    assert isinstance(etf_cost, ETFCostBoundary)
    assert isinstance(stock_cost, ChinaAStockCostBoundary)
    assert stock_cost.stamp_duty_sell_rate == Decimal("0.0005")
    assert stock_cost.transfer_fee_rate == Decimal("0.00001")
    stock_execution_cost = execution_cost_config_for(stock, TARGET, AdaptiveConfig.default())
    assert stock_execution_cost.sell_tax_rate == pytest.approx(0.0005)
    assert stock_execution_cost.transfer_fee_rate == pytest.approx(0.00001)


def test_active_selection_rejects_missing_or_mismatched_target_config_hash() -> None:
    frozen = FrozenConfigRecord(
        config_hash="parent-hash",
        config=AdaptiveConfig.default(),
        selection_payload={
            **_approved_research_fields("parent-hash"),
            "targets": [{
                "stock_code": "510300.SH", "tracking_index_code": "000300.SH",
                "layer": "broad_beta", "sub_layer": "broad_domestic_core",
                "sub_layer_budget": "42000", "instrument_type": "etf", "weight": "1",
            }],
        },
        data_cutoff=DATA_CUTOFF,
        activation_date=date(2026, 8, 1),
        review_date=date(2027, 2, 1),
        activated_at=datetime(2026, 8, 1, 17, 0),
    )

    with pytest.raises(ValueError, match="config_hash"):
        shadow_module._build_active_selection(frozen)

    mismatched = FrozenConfigRecord(
        **{
            **frozen.__dict__,
            "selection_payload": {
                **_approved_research_fields("parent-hash"),
                "targets": [{
                    **frozen.selection_payload["targets"][0], "config_hash": "another-hash",
                }],
            },
        },
    )
    with pytest.raises(ValueError, match="config_hash"):
        shadow_module._build_active_selection(mismatched)


def test_active_selection_rejects_a_recorded_failed_layer_benchmark() -> None:
    frozen = FrozenConfigRecord(
        config_hash="parent-hash",
        config=AdaptiveConfig.default(),
        selection_payload={
            "research_approval": _approval("parent-hash"),
            "layer_benchmarks": {
                "defensive": {"passed": False},
                "broad_beta": {"passed": True},
            },
            "targets": [{
                "stock_code": "510300.SH", "tracking_index_code": "000300.SH",
                "layer": "broad_beta", "sub_layer": "broad_domestic_core",
                "sub_layer_budget": "42000", "instrument_type": "etf", "weight": "1",
                "config_hash": "parent-hash",
            }],
        },
        data_cutoff=DATA_CUTOFF,
        activation_date=date(2026, 8, 1),
        review_date=date(2027, 2, 1),
        activated_at=datetime(2026, 8, 1, 17, 0),
    )

    with pytest.raises(ValueError, match="research approval"):
        shadow_module._build_active_selection(frozen)


def test_shadow_runner_requires_research_approval_for_every_advice_record() -> None:
    """Break caught: an approval-free legacy payload can still emit daily advice."""

    approved = _store_with_selection().load_active_frozen_config(TARGET)
    assert approved is not None
    legacy_store = InMemoryShadowStore()
    legacy_store.activate_frozen_config(FrozenConfigRecord(
        **{**approved.__dict__, "selection_payload": {
            "targets": approved.selection_payload["targets"],
        }},
    ))

    with pytest.raises(ValueError, match="research approval"):
        run_shadow_date(TARGET, _after_close(), legacy_store, _StubProvider())


def _frozen_with_research_approval(approval: object) -> FrozenConfigRecord:
    return FrozenConfigRecord(
        config_hash="parent-hash",
        config=AdaptiveConfig.default(),
        selection_payload={
            "research_approval": approval,
            "layer_benchmarks": _approved_layer_benchmarks(
                config_hash="parent-hash",
                universe_hash="universe-hash",
                data_cutoff=DATA_CUTOFF.isoformat(),
            ),
            "targets": [{
                "stock_code": "510300.SH", "tracking_index_code": "000300.SH",
                "layer": "broad_beta", "sub_layer": "broad_domestic_core",
                "sub_layer_budget": "42000", "instrument_type": "etf", "weight": "1",
                "config_hash": "parent-hash",
            }],
        },
        data_cutoff=DATA_CUTOFF,
        activation_date=date(2026, 8, 1),
        review_date=date(2027, 2, 1),
        activated_at=datetime(2026, 8, 1, 17, 0),
    )


@pytest.mark.parametrize("approval", [
    None,
    {"conclusion": "passed", "config_hash": "another-hash", "universe_hash": "universe-hash", "data_cutoff": "2026-09-01", "data_audit_passed": True},
    {"conclusion": "passed", "config_hash": "parent-hash", "universe_hash": "", "data_cutoff": "2026-09-01", "data_audit_passed": True},
    {"conclusion": "passed", "config_hash": "parent-hash", "universe_hash": "universe-hash", "data_cutoff": "2026-09-02", "data_audit_passed": True},
    {"conclusion": "continue_parameter_optimization", "config_hash": "parent-hash", "universe_hash": "universe-hash", "data_cutoff": "2026-09-01", "data_audit_passed": True},
])
def test_active_selection_rejects_missing_or_mismatched_research_approval(approval: object) -> None:
    """Break caught: a current approval payload can bypass immutable research identity checks."""

    with pytest.raises(ValueError, match="research approval"):
        shadow_module._build_active_selection(_frozen_with_research_approval(approval))


def test_active_selection_accepts_matching_passed_research_approval() -> None:
    approval = {
        "conclusion": "passed",
        "config_hash": "parent-hash",
        "universe_hash": "universe-hash",
        "data_cutoff": DATA_CUTOFF.isoformat(),
        "data_audit_passed": True,
    }

    selection = shadow_module._build_active_selection(
        _frozen_with_research_approval(approval)
    )

    assert selection.config_hash == "parent-hash"
    assert selection.data_cutoff == DATA_CUTOFF


def test_active_selection_rejects_layer_artifact_with_different_approval_identity() -> None:
    """Break caught: approval identity is accepted even when one layer artifact is from another universe."""

    approval = {
        "conclusion": "passed",
        "config_hash": "parent-hash",
        "universe_hash": "universe-hash",
        "data_cutoff": DATA_CUTOFF.isoformat(),
        "data_audit_passed": True,
    }
    frozen = _frozen_with_research_approval(approval)
    payload = dict(frozen.selection_payload)
    layer_benchmarks = dict(payload["layer_benchmarks"])
    layer_benchmarks["broad_beta"] = {
        **layer_benchmarks["broad_beta"],
        "universe_hash": "different-universe-hash",
    }
    payload["layer_benchmarks"] = layer_benchmarks

    with pytest.raises(ValueError, match="research approval"):
        shadow_module._build_active_selection(
            FrozenConfigRecord(**{**frozen.__dict__, "selection_payload": payload})
        )


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



