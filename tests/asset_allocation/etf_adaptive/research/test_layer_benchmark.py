"""Fixed-weight defensive and broad-Beta layer benchmark aggregation."""

from __future__ import annotations

from datetime import date
from decimal import Decimal

import pytest

from asset_allocation.etf_adaptive.contracts import AssetLayer, SubLayer
from asset_allocation.etf_adaptive.research.baselines import BaselineKind
from asset_allocation.etf_adaptive.research.benchmark_contracts import (
    StrategicPortfolio,
    WhitelistEntry,
)
from asset_allocation.etf_adaptive.research.execution_evidence import (
    ExecutionCostTurnover,
    StitchedNavPoint,
    TargetEvidence,
)
from asset_allocation.etf_adaptive.research.bluechip_basket import (
    BlueChipBasket,
    BlueChipConstituent,
)
from asset_allocation.etf_adaptive.research.bluechip_execution import (
    BlueChipBasketEvidence,
    BlueChipPath,
)
from asset_allocation.etf_adaptive.research.layer_benchmark import (
    _window_excess_returns,
    aggregate_defensive_evidence,
    aggregate_layer_evidence,
    layer_benchmark_artifact,
)


def _evidence(sub_layer: SubLayer, strategy: tuple[float, ...], benchmark: tuple[float, ...]) -> TargetEvidence:
    dates = tuple(date(2024, 1, 2 + offset) for offset in range(len(strategy)))
    entry = WhitelistEntry(
        exposure_id=sub_layer.value,
        sub_layer=sub_layer,
        primary_code="510300.SH",
        backup_code="510310.SH",
        effective_from=date(2020, 1, 1),
        effective_to=None,
        source_hash="d" * 64,
        valuation_multiplier=1.0,
    )
    return TargetEvidence(
        entry=entry,
        initial_cash=Decimal("100"),
        paths={
            BaselineKind.FULL_ADAPTIVE: (),
            BaselineKind.BUY_AND_HOLD: (),
        },
        stitched_paths={
            BaselineKind.FULL_ADAPTIVE: tuple(
                StitchedNavPoint("wf_000", day, nav) for day, nav in zip(dates, strategy)
            ),
            BaselineKind.BUY_AND_HOLD: tuple(
                StitchedNavPoint("wf_000", day, nav) for day, nav in zip(dates, benchmark)
            ),
        },
        execution_evidence={
            BaselineKind.FULL_ADAPTIVE: ExecutionCostTurnover(0.01, 0.25),
            BaselineKind.BUY_AND_HOLD: ExecutionCostTurnover(0.005, 0.05),
        },
    )


def test_defensive_layer_uses_fixed_weights_and_can_pass_with_one_lagging_target() -> None:
    portfolio = StrategicPortfolio(
        "defensive_strategy",
        AssetLayer.DEFENSIVE,
        {
            SubLayer.DEFENSIVE_DIVIDEND_ETF: 0.6429,
            SubLayer.DEFENSIVE_BLUE_CHIP: 0.3571,
        },
    )

    result = aggregate_layer_evidence(
        portfolio,
        {
            SubLayer.DEFENSIVE_DIVIDEND_ETF: _evidence(
                SubLayer.DEFENSIVE_DIVIDEND_ETF, (1.0, 1.2, 1.3), (1.0, 1.1, 1.2)
            ),
            SubLayer.DEFENSIVE_BLUE_CHIP: _evidence(
                SubLayer.DEFENSIVE_BLUE_CHIP, (1.0, 0.9, 0.95), (1.0, 1.0, 1.0)
            ),
        },
    )

    assert result.strategy_nav[-1] == pytest.approx(1.175015)
    assert result.benchmark_nav[-1] == pytest.approx(1.12858)
    assert result.strategy_metrics.total_cost == pytest.approx(0.01)
    assert result.strategy_metrics.turnover == pytest.approx(0.25)
    assert result.benchmark_metrics.total_cost == pytest.approx(0.005)
    assert result.benchmark_metrics.turnover == pytest.approx(0.05)
    assert result.gate.passed is True
    assert result.marginal_excess_contribution[SubLayer.DEFENSIVE_BLUE_CHIP] < 0
    artifact = layer_benchmark_artifact(result)
    assert artifact["passed"] is False
    assert artifact["decision"]["conclusion"] != "passed"
    assert artifact["strategy_nav"] == pytest.approx((1.0, 1.09287, 1.175015))
    assert artifact["benchmark_nav"] == pytest.approx((1.0, 1.06429, 1.12858))
    assert artifact["marginal_excess_contribution"] == {
        "defensive_dividend_etf": pytest.approx(0.06429),
        "defensive_blue_chip": pytest.approx(-0.017855),
    }


def test_layer_artifact_requires_a_passing_risk_adjusted_decision() -> None:
    """Break caught: a legacy return/drawdown gate alone authorizes a layer."""

    portfolio = StrategicPortfolio(
        "defensive_strategy",
        AssetLayer.DEFENSIVE,
        {
            SubLayer.DEFENSIVE_DIVIDEND_ETF: 0.6429,
            SubLayer.DEFENSIVE_BLUE_CHIP: 0.3571,
        },
    )
    result = aggregate_layer_evidence(
        portfolio,
        {
            SubLayer.DEFENSIVE_DIVIDEND_ETF: _evidence(
                SubLayer.DEFENSIVE_DIVIDEND_ETF,
                (1.0, 1.1, 1.0, 0.93, 1.3, 1.5),
                (1.0, 1.1, 0.8, 0.6, 1.0, 1.2),
            ),
            SubLayer.DEFENSIVE_BLUE_CHIP: _evidence(
                SubLayer.DEFENSIVE_BLUE_CHIP,
                (1.0, 1.1, 1.0, 0.93, 1.3, 1.5),
                (1.0, 1.1, 0.8, 0.6, 1.0, 1.2),
            ),
        },
    )

    artifact = layer_benchmark_artifact(result)

    assert result.gate.passed is True
    assert artifact["passed"] is False
    assert artifact["decision"] == {
        "conclusion": "continue_parameter_optimization",
        "blockers": ["oos_evidence"],
    }
    assert artifact["strategy_metrics"]["sortino"] == pytest.approx(
        result.strategy_metrics.sortino
    )
    assert artifact["benchmark_metrics"]["cvar5"] == pytest.approx(
        result.benchmark_metrics.cvar5
    )


def test_layer_aggregation_rejects_misaligned_dates() -> None:
    portfolio = StrategicPortfolio(
        "beta_strategy",
        AssetLayer.BROAD_BETA,
        {SubLayer.DOMESTIC_CORE: 1.0},
    )
    evidence = _evidence(SubLayer.DOMESTIC_CORE, (1.0, 1.1, 1.2), (1.0, 1.1, 1.15))
    bad = TargetEvidence(
        entry=evidence.entry,
        initial_cash=evidence.initial_cash,
        paths=evidence.paths,
        stitched_paths={
            BaselineKind.FULL_ADAPTIVE: evidence.stitched_paths[BaselineKind.FULL_ADAPTIVE][1:],
            BaselineKind.BUY_AND_HOLD: evidence.stitched_paths[BaselineKind.BUY_AND_HOLD],
        },
        execution_evidence=evidence.execution_evidence,
    )

    with pytest.raises(ValueError, match="aligned"):
        aggregate_layer_evidence(portfolio, {SubLayer.DOMESTIC_CORE: bad})


def test_layer_aggregation_rejects_missing_recorded_execution_evidence() -> None:
    """Break caught: missing fills turn cost and turnover into invented zeroes."""

    portfolio = StrategicPortfolio(
        "beta_strategy", AssetLayer.BROAD_BETA, {SubLayer.DOMESTIC_CORE: 1.0},
    )

    with pytest.raises(ValueError, match="execution evidence"):
        aggregate_layer_evidence(
            portfolio,
            {SubLayer.DOMESTIC_CORE: TargetEvidence(
                entry=_evidence(SubLayer.DOMESTIC_CORE, (1.0, 1.1, 1.2), (1.0, 1.05, 1.1)).entry,
                initial_cash=Decimal("100"),
                paths={},
                stitched_paths=_evidence(
                    SubLayer.DOMESTIC_CORE, (1.0, 1.1, 1.2), (1.0, 1.05, 1.1),
                ).stitched_paths,
            )},
        )


def test_layer_window_excess_uses_the_prior_compounded_capital_basis() -> None:
    """Break caught: a later window drops its opening-session return from excess."""

    portfolio = StrategicPortfolio(
        "beta_strategy", AssetLayer.BROAD_BETA, {SubLayer.DOMESTIC_CORE: 1.0},
    )
    evidence = _evidence(SubLayer.DOMESTIC_CORE, (1.0, 1.1, 1.21), (1.0, 0.95, 1.2))
    dates = (date(2024, 1, 2), date(2024, 1, 3), date(2024, 1, 4))
    aligned = TargetEvidence(
        entry=evidence.entry,
        initial_cash=evidence.initial_cash,
        paths=evidence.paths,
        stitched_paths={
            BaselineKind.FULL_ADAPTIVE: tuple(
                StitchedNavPoint(window_id, day, nav)
                for window_id, day, nav in zip(("wf_000", "wf_001", "wf_001"), dates, (1.0, 1.1, 1.21))
            ),
            BaselineKind.BUY_AND_HOLD: tuple(
                StitchedNavPoint(window_id, day, nav)
                for window_id, day, nav in zip(("wf_000", "wf_001", "wf_001"), dates, (1.0, 0.95, 1.2))
            ),
        },
        execution_evidence=evidence.execution_evidence,
    )

    result = aggregate_layer_evidence(portfolio, {SubLayer.DOMESTIC_CORE: aligned})

    assert result.gate.non_lagging_windows == 2
    assert result.gate.passed is True


def test_first_window_excess_uses_normalized_pre_window_capital() -> None:
    """Break caught: the benchmark's first observed NAV becomes its opening capital."""

    excess = _window_excess_returns(
        (1.00, 1.05),
        (1.10, 1.12),
        {
            SubLayer.DOMESTIC_CORE: (
                StitchedNavPoint("wf_000", date(2024, 1, 2), 1.00),
                StitchedNavPoint("wf_000", date(2024, 1, 3), 1.05),
            ),
        },
    )

    assert excess == pytest.approx((-0.07,))


def test_layer_aggregation_rejects_window_boundary_misalignment() -> None:
    """Break caught: strategy and benchmark windows can describe different OOS boundaries."""

    portfolio = StrategicPortfolio(
        "beta_strategy", AssetLayer.BROAD_BETA, {SubLayer.DOMESTIC_CORE: 1.0},
    )
    evidence = _evidence(SubLayer.DOMESTIC_CORE, (1.0, 1.1, 1.2), (1.0, 1.05, 1.1))
    misaligned = TargetEvidence(
        entry=evidence.entry,
        initial_cash=evidence.initial_cash,
        paths=evidence.paths,
        stitched_paths={
            BaselineKind.FULL_ADAPTIVE: evidence.stitched_paths[BaselineKind.FULL_ADAPTIVE],
            BaselineKind.BUY_AND_HOLD: tuple(
                StitchedNavPoint("different_window", point.nav_date, point.nav_total)
                for point in evidence.stitched_paths[BaselineKind.BUY_AND_HOLD]
            ),
        },
        execution_evidence=evidence.execution_evidence,
    )

    with pytest.raises(ValueError, match="window"):
        aggregate_layer_evidence(portfolio, {SubLayer.DOMESTIC_CORE: misaligned})


def test_defensive_adapter_uses_basket_weight_and_reports_stock_contribution() -> None:
    dates = (date(2024, 1, 2), date(2024, 1, 3), date(2024, 1, 4))
    basket = BlueChipBasket(
        "H30269.CSI",
        dates[0],
        (
            BlueChipConstituent("600900.SH", 0.6, "a" * 64),
            BlueChipConstituent("601088.SH", 0.4, "b" * 64),
        ),
    )
    bluechip = BlueChipBasketEvidence(
        basket=basket,
        member_evidence={},
        paths={
            BaselineKind.FULL_ADAPTIVE: BlueChipPath(
                tuple(StitchedNavPoint("wf_000", day, nav) for day, nav in zip(dates, (1.0, 0.9, 0.95))),
                {"600900.SH": 0.03, "601088.SH": -0.08},
            ),
            BaselineKind.BUY_AND_HOLD: BlueChipPath(
                tuple(StitchedNavPoint("wf_000", day, nav) for day, nav in zip(dates, (1.0, 1.0, 1.0))),
                {"600900.SH": 0.01, "601088.SH": -0.02},
            ),
        },
        initial_cash=Decimal("100"),
        execution_evidence={
            BaselineKind.FULL_ADAPTIVE: ExecutionCostTurnover(0.01, 0.25),
            BaselineKind.BUY_AND_HOLD: ExecutionCostTurnover(0.005, 0.05),
        },
    )

    result = aggregate_defensive_evidence(
        _evidence(SubLayer.DEFENSIVE_DIVIDEND_ETF, (1.0, 1.2, 1.3), (1.0, 1.1, 1.2)),
        bluechip,
    )

    assert result.strategy_nav[-1] == pytest.approx(1.175015)
    assert result.bluechip_member_contribution == {
        "600900.SH": pytest.approx(0.007142),
        "601088.SH": pytest.approx(-0.021426),
    }
    assert layer_benchmark_artifact(result)["bluechip_member_contribution"] == {
        "600900.SH": pytest.approx(0.007142),
        "601088.SH": pytest.approx(-0.021426),
    }
