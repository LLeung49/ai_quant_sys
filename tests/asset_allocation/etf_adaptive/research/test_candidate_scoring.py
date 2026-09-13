"""Training evidence ranks candidates only after the stability gate."""

from dataclasses import asdict, replace
from itertools import permutations

import pytest

from asset_allocation.etf_adaptive.config import AdaptiveConfig, GridConfig, TrendConfig
from asset_allocation.etf_adaptive.research.candidate_scoring import (
    TrainingCandidateScore,
    select_stable_representative,
)


def _score(config: AdaptiveConfig = AdaptiveConfig(), **changes) -> TrainingCandidateScore:
    return replace(TrainingCandidateScore(
        config_hash=config.config_hash(), config=asdict(config),
        positive_subperiod_share=0.75, sortino_excess=0.2, sharpe_excess=0.1,
        drawdown_improvement=0.01, cvar5_improvement=0.001,
        cost_drag=0.002, exposure_ratio=0.5, stable=True, rejection_reason=None,
    ), **changes)


def test_select_stable_representative_rejects_high_score_outside_plateau() -> None:
    unstable_high_score = _score(
        AdaptiveConfig(grid=GridConfig(step_pct=0.01)),
        positive_subperiod_share=1.0, sortino_excess=100.0, sharpe_excess=100.0,
        stable=False, rejection_reason="outside_stable_plateau",
    )
    stable_lower_score = _score()

    assert select_stable_representative((unstable_high_score, stable_lower_score)) == stable_lower_score


def test_no_stable_representative_fails_closed() -> None:
    assert select_stable_representative(()) is None
    assert select_stable_representative((_score(stable=False),)) is None


@pytest.mark.parametrize("better,worse", (
    ({"positive_subperiod_share": 1.0, "sortino_excess": -1.0}, {"sortino_excess": 100.0}),
    ({"sortino_excess": 0.3, "sharpe_excess": -1.0}, {"sharpe_excess": 100.0}),
    ({"sharpe_excess": 0.2, "cost_drag": 0.9}, {"cost_drag": 0.0}),
    ({"cost_drag": 0.001}, {"cost_drag": 0.002}),
))
def test_stable_ranking_is_lexicographic_and_independent_of_input_order(better, worse) -> None:
    expected = _score(AdaptiveConfig(trend=TrendConfig(risk_per_unit=0.0075)), **better)
    other = _score(AdaptiveConfig(trend=TrendConfig(risk_per_unit=0.005)), **worse)

    for ordering in permutations((expected, other)):
        assert select_stable_representative(ordering) == expected


@pytest.mark.parametrize("conservative,riskier", (
    (AdaptiveConfig(trend=TrendConfig(risk_per_unit=0.005)),
     AdaptiveConfig(trend=TrendConfig(risk_per_unit=0.0075))),
    (AdaptiveConfig(trend=TrendConfig(max_units=2)),
     AdaptiveConfig(trend=TrendConfig(max_units=3))),
    (AdaptiveConfig(grid=GridConfig(unit_pct=0.05)),
     AdaptiveConfig(grid=GridConfig(unit_pct=0.10))),
    (AdaptiveConfig(grid=GridConfig(fixed_initial_pct=0.3)),
     AdaptiveConfig(grid=GridConfig(fixed_initial_pct=0.6))),
))
def test_equal_evidence_uses_conservative_config_order(conservative, riskier) -> None:
    expected, other = _score(conservative), _score(riskier)

    for ordering in permutations((expected, other)):
        assert select_stable_representative(ordering) == expected


def test_diagnostic_metrics_do_not_override_the_prescribed_ranking() -> None:
    expected = _score(AdaptiveConfig(trend=TrendConfig(risk_per_unit=0.005)))
    other = _score(
        AdaptiveConfig(trend=TrendConfig(risk_per_unit=0.0075)),
        drawdown_improvement=0.99, cvar5_improvement=0.99, exposure_ratio=0.99,
    )

    assert select_stable_representative((other, expected)) == expected
