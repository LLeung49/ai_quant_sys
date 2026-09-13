"""Training evidence ranks candidates only after the stability gate."""

from dataclasses import asdict, replace
from hashlib import sha256
from itertools import permutations
import json

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
    ({"sharpe_excess": 0.2, "cost_drag": 0.019}, {"cost_drag": 0.0}),
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


@pytest.mark.parametrize("field", (
    "positive_subperiod_share", "sortino_excess", "sharpe_excess",
    "drawdown_improvement", "cvar5_improvement", "cost_drag", "exposure_ratio",
))
@pytest.mark.parametrize("value", (None, float("nan"), float("inf"), float("-inf"), True, "0.1"))
def test_invalid_or_unavailable_metrics_are_recorded_as_rejected(field, value) -> None:
    rejected = _score(**{field: value})
    valid = _score(AdaptiveConfig(trend=TrendConfig(risk_per_unit=0.0075)))

    assert rejected.stable is False
    assert rejected.rejection_reason is not None
    assert field in rejected.rejection_reason
    for ordering in permutations((rejected, valid)):
        assert select_stable_representative(ordering) == valid
    assert select_stable_representative((rejected,)) is None
    # Rejected evidence must remain serializable without non-standard NaN/Inf.
    json.dumps(asdict(rejected), allow_nan=False)


@pytest.mark.parametrize("field,value,reason", (
    ("positive_subperiod_share", -0.01, "positive_subperiod_share_out_of_bounds"),
    ("positive_subperiod_share", 1.01, "positive_subperiod_share_out_of_bounds"),
    ("exposure_ratio", -0.01, "exposure_ratio_out_of_bounds"),
    ("exposure_ratio", 1.01, "exposure_ratio_out_of_bounds"),
    ("cost_drag", -0.001, "cost_drag_out_of_bounds"),
    ("cost_drag", 0.020001, "cost_drag_out_of_bounds"),
    ("cost_drag", 1.01, "cost_drag_out_of_bounds"),
))
def test_training_execution_and_share_bounds_reject_scores(field, value, reason) -> None:
    rejected = _score(**{field: value})

    assert rejected.stable is False
    assert rejected.rejection_reason == reason
    assert select_stable_representative((rejected,)) is None


@pytest.mark.parametrize("cost_drag", (0.0, 0.02))
def test_training_cost_gate_includes_its_boundaries(cost_drag) -> None:
    score = _score(cost_drag=cost_drag)

    assert select_stable_representative((score,)) == score


@pytest.mark.parametrize("stable,reason", (
    (True, "outside_stable_plateau"),
    (True, "unavailable_training_ratios"),
    (False, None),
    (False, "outside_stable_plateau"),
    (1, None),
    ("true", None),
))
def test_inconsistent_or_rejected_state_cannot_select(stable, reason) -> None:
    score = _score(stable=stable, rejection_reason=reason)

    assert score.stable is False
    assert score.rejection_reason is not None
    assert select_stable_representative((score,)) is None


@pytest.mark.parametrize("changes", (
    {"sortino_excess": None}, {"sortino_excess": float("nan")},
    {"sortino_excess": float("inf")}, {"cost_drag": 0.020001},
    {"positive_subperiod_share": 1.01}, {"exposure_ratio": -0.1},
    {"rejection_reason": "outside_stable_plateau"}, {"stable": 1},
))
def test_selector_rechecks_evidence_even_if_constructor_validation_was_bypassed(changes) -> None:
    corrupted = _score(sortino_excess=100.0, sharpe_excess=100.0)
    for field, value in changes.items():
        object.__setattr__(corrupted, field, value)
    valid = _score(AdaptiveConfig(trend=TrendConfig(risk_per_unit=0.0075)))

    for ordering in permutations((corrupted, valid)):
        assert select_stable_representative(ordering) == valid


def test_config_hash_must_match_the_complete_configuration() -> None:
    with pytest.raises(ValueError, match="config_hash"):
        replace(_score(), config_hash="0" * 64)


@pytest.mark.parametrize("malformation", (
    "missing_section", "missing_field", "extra_field", "wrong_boolean", "wrong_integer",
    "wrong_string", "nonfinite_optional_number", "wrong_section_type",
))
def test_incomplete_or_noncanonical_config_is_rejected_even_with_its_matching_hash(malformation) -> None:
    payload = asdict(AdaptiveConfig())
    if malformation == "missing_section":
        del payload["cost"]
    elif malformation == "missing_field":
        del payload["grid"]["cooldown_sessions"]
    elif malformation == "extra_field":
        payload["trend"]["future_flag"] = True
    elif malformation == "wrong_boolean":
        payload["trend"]["require_macd_bullish"] = "true"
    elif malformation == "wrong_integer":
        payload["trend"]["max_units"] = True
    elif malformation == "wrong_string":
        payload["grid"]["initial_model"] = 42
    elif malformation == "nonfinite_optional_number":
        payload["trend"]["amount_ratio_min"] = float("nan")
    else:
        payload["cost"] = []
    matching_hash = sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

    with pytest.raises(ValueError, match="config"):
        replace(_score(), config=payload, config_hash=matching_hash)


def test_config_is_an_independent_deeply_immutable_serializable_snapshot() -> None:
    source = asdict(AdaptiveConfig())
    score = replace(_score(), config=source)
    source["grid"]["unit_pct"] = 0.9
    source["cost"].clear()

    assert score.config["grid"]["unit_pct"] == 0.10
    assert score.config["cost"]["slippage_bps"] == 3.0
    with pytest.raises(TypeError):
        score.config["grid"]["unit_pct"] = 0.8
    with pytest.raises(TypeError):
        score.config["trend"] = {}
    # Existing dataclass/JSON evidence consumers get an independent payload.
    serialized = json.loads(json.dumps(asdict(score), allow_nan=False))
    assert serialized["config"] == asdict(AdaptiveConfig())
    serialized["config"]["grid"]["unit_pct"] = 0.7
    assert score.config_hash == AdaptiveConfig().config_hash()
    assert score.config["grid"]["unit_pct"] == 0.10


def test_frozen_config_cannot_be_reinitialized_after_hash_binding() -> None:
    score = _score()

    with pytest.raises(TypeError):
        score.config["grid"].__init__({"unit_pct": 0.9})
    assert score.config["grid"]["unit_pct"] == 0.10


def test_selector_rejects_a_config_hash_changed_after_construction() -> None:
    corrupted = _score(sortino_excess=100.0)
    object.__setattr__(corrupted, "config_hash", "0" * 64)
    valid = _score()

    for ordering in permutations((corrupted, valid)):
        assert select_stable_representative(ordering) == valid
