from datetime import date
from decimal import Decimal

import pytest

from asset_allocation.etf_adaptive.research.attribution import (
    build_excess_attribution,
    build_result_attribution,
)
from asset_allocation.etf_adaptive.state import (
    BacktestEvent,
    BacktestRequest,
    BacktestResult,
    DailyNav,
    DailyStrategyObservation,
    Regime,
)


def test_attribution_uses_only_recorded_events_and_nav() -> None:
    result = BacktestResult(
        BacktestRequest("510300.SH", Decimal("100000"), date(2026, 9, 1), date(2026, 9, 2)),
        (
            BacktestEvent(date(2026, 9, 1), "fill", (("reason", "trend_entry"), ("shares", "1000"), ("raw_price", "4.0"))),
            BacktestEvent(date(2026, 9, 2), "rejected_order", (("reason", "buy_locked"),)),
        ),
        (
            DailyNav(date(2026, 9, 1), Decimal("96000"), Decimal("4000")),
            DailyNav(date(2026, 9, 2), Decimal("100000"), Decimal("0")),
        ),
    )

    attribution = build_result_attribution("wf_000", result)

    assert attribution.invested_sessions == 1
    assert attribution.cash_sessions == 1
    assert attribution.by_reason["trend_entry"].fill_count == 1
    assert attribution.rejected_order_count == 1
    assert attribution.trade_points[0].event_date == date(2026, 9, 1)


def test_attribution_reconciles_recorded_strategy_minus_benchmark_nav() -> None:
    # Break caught: including execution costs in the net reconciliation would
    # double count costs that are already reflected in the recorded strategy NAV.
    days = tuple(date(2026, 9, day) for day in range(1, 5))
    recorded_strategy = (
        DailyNav(days[0], Decimal("100"), Decimal("0")),
        DailyNav(days[1], Decimal("55"), Decimal("55")),
        DailyNav(days[2], Decimal("50"), Decimal("49")),
        DailyNav(days[3], Decimal("99"), Decimal("0")),
    )
    recorded_benchmark = (
        DailyNav(days[0], Decimal("100"), Decimal("0")),
        DailyNav(days[1], Decimal("0"), Decimal("105")),
        DailyNav(days[2], Decimal("0"), Decimal("100")),
        DailyNav(days[3], Decimal("0"), Decimal("102")),
    )
    observations = (
        DailyStrategyObservation(days[0], Regime.GRID, 0.5, 0.0, 0, 0, "grid"),
        DailyStrategyObservation(days[1], Regime.GRID, 0.5, 0.5, 0, 0, "grid"),
        DailyStrategyObservation(days[2], Regime.TREND, 0.5, 0.5, 0, 0, "trend"),
        DailyStrategyObservation(days[3], Regime.TREND, 0.0, 0.0, 0, 0, "cash"),
    )

    attribution = build_excess_attribution(
        recorded_strategy,
        recorded_benchmark,
        observations,
        (BacktestEvent(days[1], "fill", (("commission", "7"),)),),
    )

    assert attribution.grid_return == pytest.approx(0.05)
    assert attribution.transition_return == pytest.approx(-0.0523809523809524)
    assert attribution.cash_opportunity_cost == pytest.approx(-0.02)
    assert attribution.execution_cost == pytest.approx(7.0)
    assert attribution.reconciliation_error == pytest.approx(0.0, abs=1e-9)


def test_attribution_rejects_observation_date_not_in_recorded_nav() -> None:
    # Break caught: an observation outside the recorded NAV path can fabricate
    # a mode attribution that never occurred in the backtest.
    days = (date(2026, 9, 1), date(2026, 9, 2))
    strategy = tuple(DailyNav(day, Decimal("100"), Decimal("0")) for day in days)
    benchmark = tuple(DailyNav(day, Decimal("0"), Decimal("100")) for day in days)
    foreign_date_observation = DailyStrategyObservation(
        date(2026, 9, 3), Regime.GRID, 0.0, 0.0, 0, 0, "foreign",
    )

    with pytest.raises(ValueError, match="observation date"):
        build_excess_attribution(strategy, benchmark, (foreign_date_observation,))


def test_attribution_marks_the_first_return_after_a_regime_switch_as_transition() -> None:
    # Break caught: starting transition tracking at the first return, rather
    # than the first observation, mislabels an immediate GRID-to-TREND switch.
    days = tuple(date(2026, 9, day) for day in range(1, 4))
    strategy = tuple(
        DailyNav(day, Decimal("0"), Decimal(str(total)))
        for day, total in zip(days, (100, 110, 112))
    )
    benchmark = tuple(
        DailyNav(day, Decimal("0"), Decimal(str(total)))
        for day, total in zip(days, (100, 105, 107))
    )
    observations = (
        DailyStrategyObservation(days[0], Regime.GRID, 1.0, 1.0, 0, 0, "grid"),
        DailyStrategyObservation(days[1], Regime.TREND, 1.0, 1.0, 0, 0, "trend"),
        DailyStrategyObservation(days[2], Regime.TREND, 1.0, 1.0, 0, 0, "trend"),
    )

    attribution = build_excess_attribution(strategy, benchmark, observations)

    assert attribution.transition_return == pytest.approx(0.05)


def test_attribution_rejects_cash_series_that_cannot_reconcile_to_benchmark_opportunity_cost() -> None:
    # Break caught: treating an unexplained cash-NAV gain as cash opportunity
    # cost hides a malformed recorded series instead of rejecting it.
    days = (date(2026, 9, 1), date(2026, 9, 2))
    strategy = (
        DailyNav(days[0], Decimal("100"), Decimal("0")),
        DailyNav(days[1], Decimal("101"), Decimal("0")),
    )
    benchmark = tuple(DailyNav(day, Decimal("0"), Decimal("100")) for day in days)
    observations = tuple(
        DailyStrategyObservation(day, None, 0.0, 0.0, 0, 0, "cash") for day in days
    )

    with pytest.raises(ValueError, match="does not reconcile"):
        build_excess_attribution(strategy, benchmark, observations)


def test_attribution_marks_first_invested_session_after_cash_regime_switch_as_transition() -> None:
    # Break caught: clearing the transition marker on an uninvested switch
    # misattributes the first executable TREND session as ordinary trend P&L.
    days = tuple(date(2026, 9, day) for day in range(1, 4))
    strategy = tuple(
        DailyNav(day, Decimal("0"), Decimal(str(total)))
        for day, total in zip(days, (100, 100, 110))
    )
    benchmark = tuple(
        DailyNav(day, Decimal("0"), Decimal(str(total)))
        for day, total in zip(days, (100, 100, 105))
    )
    observations = (
        DailyStrategyObservation(days[0], Regime.GRID, 0.0, 0.0, 0, 0, "grid"),
        DailyStrategyObservation(days[1], Regime.TREND, 0.0, 0.0, 0, 0, "trend_entry"),
        DailyStrategyObservation(days[2], Regime.TREND, 1.0, 1.0, 0, 0, "trend_entry"),
    )

    attribution = build_excess_attribution(strategy, benchmark, observations)

    assert attribution.transition_return == pytest.approx(0.05)
    assert attribution.trend_return == pytest.approx(0.0)
