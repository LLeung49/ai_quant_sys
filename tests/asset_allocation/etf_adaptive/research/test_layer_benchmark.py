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
    aggregate_defensive_evidence,
    aggregate_layer_evidence,
    layer_benchmark_artifact,
)


def _evidence(sub_layer: SubLayer, strategy: tuple[float, ...], benchmark: tuple[float, ...]) -> TargetEvidence:
    dates = (date(2024, 1, 2), date(2024, 1, 3), date(2024, 1, 4))
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
    assert result.gate.passed is True
    assert result.marginal_excess_contribution[SubLayer.DEFENSIVE_BLUE_CHIP] < 0
    assert layer_benchmark_artifact(result) == {
        "passed": True,
        "return_passed": True,
        "drawdown_passed": True,
        "majority_windows_passed": True,
        "strategy_nav": pytest.approx((1.0, 1.09287, 1.175015)),
        "benchmark_nav": pytest.approx((1.0, 1.06429, 1.12858)),
        "marginal_excess_contribution": {
            "defensive_dividend_etf": pytest.approx(0.06429),
            "defensive_blue_chip": pytest.approx(-0.017855),
        },
    }


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
    )

    with pytest.raises(ValueError, match="aligned"):
        aggregate_layer_evidence(portfolio, {SubLayer.DOMESTIC_CORE: bad})


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
