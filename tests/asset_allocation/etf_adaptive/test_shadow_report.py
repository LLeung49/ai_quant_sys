"""Chinese daily shadow report must surface state, risk, and order trace."""

from __future__ import annotations

from datetime import date, datetime
from decimal import Decimal

import pytest

from asset_allocation.etf_adaptive.run_shadow_daily import (
    ShadowRunSummary,
    TargetSpec,
)
from asset_allocation.etf_adaptive.shadow_report import render_daily_report
from asset_allocation.etf_adaptive.shadow_store import (
    AdviceRecord,
    HealthCheck,
    StateRecord,
)
from asset_allocation.etf_adaptive.state import (
    OrderIntent,
    OrderReason,
    Regime,
    Side,
    StrategyState,
)


def _summary_with_buy_advice() -> ShadowRunSummary:
    target = TargetSpec(
        stock_code="510300.SH",
        tracking_index_code="000300.SH",
        layer="core_broad",
        weight=0.5,
    )
    state = StrategyState(
        regime=Regime.GRID,
        position_shares=0,
        cash=Decimal("100000"),
        grid_anchor=1.0,
        cycle_entry_price=1.0,
        grid_stop_price=0.95,
    )
    state_record = StateRecord(
        run_id="run-1",
        as_of_date=date(2026, 9, 1),
        stock_code=target.stock_code,
        config_hash="cfg-shadow-1",
        state=state,
        cash=state.cash,
        position_shares=state.position_shares,
        regime=state.regime.value,
    )
    advice = AdviceRecord(
        run_id="run-1",
        stock_code=target.stock_code,
        as_of_date=date(2026, 9, 1),
        execution_eligible_date=date(2026, 9, 2),
        signal_date=date(2026, 9, 1),
        order=OrderIntent(
            signal_date=date(2026, 9, 1),
            side=Side.BUY,
            reason=OrderReason.GRID_INITIALIZE,
            signal_atr20=0.05,
            signal_thresholds=(("grid_anchor", 1.0),),
            target_budget=0.5,
            risk_per_unit=0.005,
            quantity_rationale="initial GRID unit",
        ),
        config_hash="cfg-shadow-1",
    )
    return ShadowRunSummary(
        as_of_date=date(2026, 9, 1),
        model_version="shadow-v1",
        config_hash="cfg-shadow-1",
        execution_eligible_date=date(2026, 9, 2),
        run_id="run-1",
        target_states=((target, state_record),),
        advices=(advice,),
        health_checks=(
            HealthCheck(run_id="run-1", check_name="data_freshness", passed=True,
                        detail={"bar_trade_date": "2026-09-01"}),
        ),
    )


def test_daily_report_contains_state_risk_and_order_trace() -> None:
    report = render_daily_report(_summary_with_buy_advice())

    assert "GRID" in report
    assert "grid_anchor" in report
    assert "execution_eligible_date" in report
    assert "config_hash" in report
    assert "cfg-shadow-1" in report
    assert "grid_initialize" in report


def test_daily_report_includes_no_advice_section_when_idle() -> None:
    summary = ShadowRunSummary(
        as_of_date=date(2026, 9, 1),
        model_version="shadow-v1",
        config_hash="cfg-shadow-1",
        execution_eligible_date=date(2026, 9, 2),
        run_id="run-1",
        target_states=(),
        advices=(),
        health_checks=(),
    )

    report = render_daily_report(summary)

    assert "无新订单建议" in report


def test_daily_report_records_failed_health_check_with_marker() -> None:
    summary = ShadowRunSummary(
        as_of_date=date(2026, 9, 1),
        model_version="shadow-v1",
        config_hash="cfg-shadow-1",
        execution_eligible_date=date(2026, 9, 2),
        run_id="run-1",
        target_states=(),
        advices=(),
        health_checks=(
            HealthCheck(run_id="run-1", check_name="data_freshness", passed=False,
                        detail={"missing": "bar"}),
        ),
    )

    report = render_daily_report(summary)

    assert "❌" in report
    assert "data_freshness" in report


def test_daily_report_displays_run_id_and_execution_eligible_date() -> None:
    report = render_daily_report(_summary_with_buy_advice())

    assert "run-1" in report
    assert "2026-09-01" in report
    assert "2026-09-02" in report
