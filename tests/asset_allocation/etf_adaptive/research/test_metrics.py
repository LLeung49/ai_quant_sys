"""Performance metrics, baselines, and mode attribution for research."""

from __future__ import annotations

from datetime import date
from decimal import Decimal
from typing import Sequence

import pytest

from asset_allocation.etf_adaptive.research.metrics import (
    AttributionEvent,
    ModeAttribution,
    PerformanceMetrics,
    Trade,
    attribute_by_mode,
    calculate_performance,
    max_drawdown,
    recovery_sessions,
    session_returns,
)


def _nav(values: Sequence[float]) -> tuple[float, ...]:
    return tuple(values)


def _trades(*, cost: float = 0.0, fill_count: int = 1) -> tuple[Trade, ...]:
    return tuple(
        Trade(
            signal_date=date(2026, 9, offset + 1),
            fill_date=date(2026, 9, offset + 2),
            side="BUY",
            shares=100,
            raw_price=1.0,
            commission=Decimal(str(cost / max(fill_count, 1))),
            slippage_cost=Decimal("0"),
            minimum_commission_applied=False,
            is_unfilled=False,
        )
        for offset in range(fill_count)
    )


def test_max_drawdown_matches_nadir_relative_to_running_peak() -> None:
    assert max_drawdown(_nav([1.0, 1.1, 0.9, 1.0])) == pytest.approx(0.9 / 1.1 - 1.0)
    assert max_drawdown(_nav([1.0, 0.8, 0.9, 1.01])) == pytest.approx(-0.20)


def test_recovery_sessions_returns_index_of_first_new_high() -> None:
    assert recovery_sessions(_nav([1.0, 0.8, 0.9, 1.01])) == 3
    assert recovery_sessions(_nav([1.0, 1.2, 1.3])) == 1
    assert recovery_sessions(_nav([1.0, 0.95, 0.90])) == len((1.0, 0.95, 0.90))


def test_session_returns_drop_the_first_nav_observation() -> None:
    returns = session_returns(_nav([1.0, 1.1, 0.99]))

    assert returns == pytest.approx([0.10, -0.10])


def test_metrics_use_cost_net_nav_and_report_recovery_sessions() -> None:
    metrics = calculate_performance(_nav([1.0, 0.8, 0.9, 1.01]), _trades(cost=0.01))

    assert metrics.max_drawdown == pytest.approx(-0.20)
    assert metrics.recovery_sessions == 3
    assert metrics.total_cost == pytest.approx(0.01)


def test_metrics_report_annualized_return_and_sharpe_from_net_returns() -> None:
    nav = _nav([1.0, 1.01, 1.02, 1.03, 1.05])
    trades = _trades(cost=0.0, fill_count=4)

    metrics = calculate_performance(nav, trades)

    assert metrics.annual_return > 0.0
    assert metrics.annual_volatility >= 0.0
    assert metrics.sharpe == metrics.annual_return / metrics.annual_volatility
    assert metrics.worst_126_session_return == pytest.approx(0.05, rel=1e-6)


def test_worst_window_return_finds_most_negative_rolling_window() -> None:
    nav = [1.0]
    for offset in range(1, 260):
        if 80 <= offset < 110:
            nav.append(nav[-1] * 0.97)
        else:
            nav.append(nav[-1] * 1.001)

    metrics = calculate_performance(_nav(nav), _trades(cost=0.0, fill_count=0))

    assert metrics.worst_126_session_return < -0.10


def test_metrics_capture_unfilled_share_and_minimum_commission() -> None:
    nav = _nav([1.0, 1.0, 1.0])
    trades = (
        Trade(
            signal_date=date(2026, 9, 1), fill_date=date(2026, 9, 2),
            side="BUY", shares=100, raw_price=1.0,
            commission=Decimal("5.00"), slippage_cost=Decimal("0"),
            minimum_commission_applied=True, is_unfilled=False,
        ),
        Trade(
            signal_date=date(2026, 9, 3), fill_date=date(2026, 9, 4),
            side="BUY", shares=0, raw_price=1.0,
            commission=Decimal("0"), slippage_cost=Decimal("0"),
            minimum_commission_applied=False, is_unfilled=True,
        ),
    )

    metrics = calculate_performance(nav, trades)

    assert metrics.minimum_commission_share == pytest.approx(0.5)
    assert metrics.unfilled_share == pytest.approx(0.5)


def test_metrics_compute_slippage_degradation_from_slippage_cost() -> None:
    nav = _nav([1.0, 1.0, 1.0])
    trades = (
        Trade(
            signal_date=date(2026, 9, 1), fill_date=date(2026, 9, 2),
            side="BUY", shares=100, raw_price=1.0,
            commission=Decimal("0.10"), slippage_cost=Decimal("0.20"),
            minimum_commission_applied=False, is_unfilled=False,
        ),
    )

    metrics = calculate_performance(nav, trades)

    assert metrics.slippage_degradation == pytest.approx(2.0)


def test_mode_attribution_reconciles_to_total_pnl() -> None:
    attribution = attribute_by_mode((
        AttributionEvent(mode="grid", amount=10.0),
        AttributionEvent(mode="trend", amount=20.0),
        AttributionEvent(mode="transition", amount=-2.0),
        AttributionEvent(mode="cost", amount=3.0),
    ))

    assert attribution.net_total == pytest.approx(25.0)


def test_mode_attribution_is_zero_when_no_events() -> None:
    attribution = attribute_by_mode(())

    assert attribution.grid_pnl == 0.0
    assert attribution.trend_pnl == 0.0
    assert attribution.transition_pnl == 0.0
    assert attribution.costs == 0.0
    assert attribution.net_total == 0.0


def test_mode_attribution_rejects_unknown_mode() -> None:
    try:
        attribute_by_mode((AttributionEvent(mode="invalid", amount=1.0),))
    except ValueError as exc:
        assert "invalid" in str(exc) or "mode" in str(exc)
    else:
        raise AssertionError("expected ValueError for unknown mode")
