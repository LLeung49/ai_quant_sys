from dataclasses import replace

import pytest

from asset_allocation.etf_adaptive.config import AdaptiveConfig
from asset_allocation.etf_adaptive.research.strategy_profiles import (
    CORE_HOLD_REBALANCE_PROFILE,
    GRID_CORE_PROFILE,
    GRID_PLUS_OPTIONAL_TREND_PROFILE,
    StrategyProfileSpec,
    profile_for_id,
    profile_training_plan,
)
from asset_allocation.etf_adaptive.research.strategy_specs import (
    BUY_AND_HOLD_SPEC,
    FIXED_HALF_SPEC,
    FULL_ADAPTIVE_SPEC,
    GRID_ONLY_SPEC,
)


def test_grid_core_profile_uses_grid_policy_and_never_plans_trend_candidates() -> None:
    """A GRID profile must not create a TREND candidate-selection surface."""
    profile = profile_for_id("grid_core")

    plan = profile_training_plan(profile, AdaptiveConfig.default(), {"step_pct": (0.02,)})

    assert profile.strategy == GRID_ONLY_SPEC
    assert set(plan) == {"grid_only"}
    candidates, axes, expansion_axes = plan["grid_only"]
    assert axes == ("step_pct",)
    assert expansion_axes == ()
    assert {candidate.config.grid.step_pct for candidate in candidates} == {0.02}


def test_optional_trend_profile_freezes_trend_configuration() -> None:
    """Removing GRID selection must fail this profile's plan without adding TREND tuning."""
    profile = profile_for_id("grid_plus_optional_trend")
    default_trend = AdaptiveConfig.default().trend

    plan = profile_training_plan(profile, AdaptiveConfig.default(), {"step_pct": (0.02,)})

    assert profile.strategy == FULL_ADAPTIVE_SPEC
    assert "trend_only" not in plan
    candidates, _, _ = plan["grid_only"]
    assert {candidate.config.trend for candidate in candidates} == {default_trend}


def test_core_hold_profile_has_no_adaptive_strategy_or_parameter_surface() -> None:
    """Adding any adaptive axis would turn a deterministic reference into a sweep."""
    profile = profile_for_id("core_hold_rebalance")

    assert profile.strategy is None
    assert profile_training_plan(profile, AdaptiveConfig.default(), {}) == {}
    with pytest.raises(ValueError, match="does not permit axis"):
        profile_training_plan(profile, AdaptiveConfig.default(), {"step_pct": (0.02,)})


def test_profiles_are_frozen_and_hash_their_complete_policy() -> None:
    """A changed evidence policy must have a different reproducibility identity."""
    assert GRID_CORE_PROFILE.benchmarks == (BUY_AND_HOLD_SPEC, FIXED_HALF_SPEC)
    with pytest.raises(AttributeError):
        GRID_CORE_PROFILE.version = "2"  # type: ignore[misc]

    changed = replace(GRID_CORE_PROFILE, required_evidence=frozenset({"provenance"}))
    assert changed.profile_hash() != GRID_CORE_PROFILE.profile_hash()


def test_profile_spec_rejects_an_empty_benchmark_declaration() -> None:
    """Deleting the reference benchmark would leave research comparison undefined."""
    with pytest.raises(ValueError, match="benchmark"):
        StrategyProfileSpec(
            "invalid", "1", GRID_ONLY_SPEC, (), ("grid_only",), frozenset({"provenance"}),
        )


def test_profile_rejects_selection_axes_not_owned_by_declared_family() -> None:
    """A TREND axis in a GRID-only profile would silently tune an undeclared strategy mode."""
    with pytest.raises(ValueError, match="does not permit axis"):
        profile_training_plan(
            GRID_PLUS_OPTIONAL_TREND_PROFILE,
            AdaptiveConfig.default(),
            {"stop_n": (2.0,)},
        )


def test_profile_lookup_rejects_unknown_profile_id() -> None:
    """A typo must not receive an inferred strategy profile."""
    with pytest.raises(ValueError, match="unknown strategy profile"):
        profile_for_id("implied_industry_profile")


@pytest.mark.parametrize(
    ("profile", "expected_strategy", "expected_families"),
    (
        (GRID_CORE_PROFILE, GRID_ONLY_SPEC, ("grid_only",)),
        (GRID_PLUS_OPTIONAL_TREND_PROFILE, FULL_ADAPTIVE_SPEC, ("grid_only",)),
        (CORE_HOLD_REBALANCE_PROFILE, None, ()),
    ),
)
def test_registry_profiles_have_the_declared_executable_boundary(
    profile: StrategyProfileSpec,
    expected_strategy,
    expected_families: tuple[str, ...],
) -> None:
    """A registry entry must keep its declared execution and selection boundaries."""
    assert profile.strategy == expected_strategy
    assert profile.selection_families == expected_families
