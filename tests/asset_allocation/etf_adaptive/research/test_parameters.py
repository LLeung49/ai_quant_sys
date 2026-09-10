"""Deterministic parameter families and stable-neighborhood selection."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Mapping

import pytest

from asset_allocation.etf_adaptive.config import AdaptiveConfig, GridConfig, TrendConfig
from asset_allocation.etf_adaptive.research.parameters import (
    GRID_ATR_STOP_MULTIPLES,
    GRID_COOLDOWN_SESSIONS,
    ParameterCandidate,
    TREND_REQUIRE_MACD_BULLISH,
    TREND_STOP_N,
    expand_candidate_axis,
    grid_candidates,
    stable_parameter_neighborhood,
    trend_candidates,
)


@dataclass(frozen=True)
class SurfacePoint:
    """Test-only marker for a single (config, axis_values, window-returns) record."""

    config_hash: str
    axis_values: Mapping[str, float]
    oos_returns: tuple[float, ...]
    positive_windows: tuple[bool, ...]

    @property
    def positive_window_share(self) -> float:
        if not self.positive_windows:
            return 0.0
        return sum(1 for value in self.positive_windows if value) / len(self.positive_windows)


def _surface(*, center_return: float, neighbor_returns: tuple[float, ...] = ()) -> dict[str, SurfacePoint]:
    """Build a 3x3 GRID surface where only the center has a positive return."""

    points: dict[str, SurfacePoint] = {}
    for step in (0.010, 0.015, 0.020):
        for unit in (0.05, 0.10, 0.15):
            candidate = ParameterCandidate(
                config=AdaptiveConfig(grid=GridConfig(step_pct=step, unit_pct=unit)),
            )
            if step == 0.015 and unit == 0.10:
                returns = (center_return, 0.10, 0.05)
                positives = (center_return > 0.0, True, True)
            else:
                returns = neighbor_returns + (-0.03,)
                positives = tuple(value > 0.0 for value in returns)
            points[candidate.config_hash] = SurfacePoint(
                config_hash=candidate.config_hash,
                axis_values={"step_pct": step, "unit_pct": unit},
                oos_returns=returns,
                positive_windows=positives,
            )
    return points


def test_grid_candidates_cover_exact_approved_space() -> None:
    candidates = grid_candidates()

    assert {candidate.config.grid.step_pct for candidate in candidates} == {
        value / 1000 for value in range(10, 65, 5)
    }
    assert {candidate.config.grid.unit_pct for candidate in candidates} == {0.05, 0.10, 0.15, 0.20}


def test_grid_candidates_include_only_approved_exit_axes() -> None:
    grids = {candidate.config.grid for candidate in grid_candidates()}

    assert GRID_ATR_STOP_MULTIPLES == (2.0, 3.0, 4.0)
    assert GRID_COOLDOWN_SESSIONS == (0, 3, 5, 10)
    assert len(grids) == 220
    assert {item.atr_stop_multiple for item in grids} == {3.0}
    assert {item.cooldown_sessions for item in grids} == {5}


def test_trend_candidates_cover_risk_grid() -> None:
    candidates = trend_candidates()

    assert {candidate.config.trend.risk_per_unit for candidate in candidates} == {
        0.0025, 0.0050, 0.0075, 0.0100
    }
    assert {candidate.config.trend.max_units for candidate in candidates} == {2, 3, 4}
    assert {candidate.config.trend.amount_ratio_min for candidate in candidates} == {None, 1.0, 1.2, 1.5}


def test_trend_candidates_include_only_approved_exit_and_filter_axes() -> None:
    trends = {candidate.config.trend for candidate in trend_candidates()}

    assert TREND_STOP_N == (1.5, 2.0, 2.5, 3.0)
    assert TREND_REQUIRE_MACD_BULLISH == (False, True)
    assert len(trends) == 144
    assert {item.stop_n for item in trends} == {2.0}
    assert {item.require_macd_bullish for item in trends} == {True}


@pytest.mark.parametrize(
    ("axis", "section", "field", "expected_values"),
    (
        ("atr_stop_multiple", "grid", "atr_stop_multiple", {2.0, 3.0, 4.0}),
        ("cooldown_sessions", "grid", "cooldown_sessions", {0, 3, 5, 10}),
        ("stop_n", "trend", "stop_n", {1.5, 2.0, 2.5, 3.0}),
        ("require_macd_bullish", "trend", "require_macd_bullish", {False, True}),
    ),
)
def test_one_axis_expansion_changes_only_its_requested_field(
    axis: str,
    section: str,
    field: str,
    expected_values: set[object],
) -> None:
    base = ParameterCandidate(
        config=AdaptiveConfig(
            grid=GridConfig(
                step_pct=0.035,
                unit_pct=0.15,
                fixed_initial_pct=0.60,
                atr_stop_multiple=3.0,
                cooldown_sessions=5,
            ),
            trend=TrendConfig(stop_n=2.5, require_macd_bullish=False),
        ),
        family="full",
    )

    expanded = expand_candidate_axis(base, axis=axis)

    assert {getattr(getattr(candidate.config, section), field) for candidate in expanded} == expected_values
    assert all(candidate.family == "full" for candidate in expanded)
    for candidate in expanded:
        base_payload = asdict(base.config)
        expanded_payload = asdict(candidate.config)
        del base_payload[section][field]
        del expanded_payload[section][field]
        assert expanded_payload == base_payload


def test_candidate_ids_are_deterministic_and_stable_under_reorder() -> None:
    first = grid_candidates()
    second = grid_candidates()

    ids_first = tuple(candidate.config_hash for candidate in first)
    ids_second = tuple(candidate.config_hash for candidate in second)

    assert ids_first == ids_second
    assert len(set(ids_first)) == len(ids_first)


def test_isolated_best_parameter_is_not_stable() -> None:
    results = _surface(center_return=0.20, neighbor_returns=(-0.01, -0.02))

    assert stable_parameter_neighborhood(
        results, axes=("step_pct", "unit_pct"), min_positive_window_share=0.60,
    ) == ()


def test_full_positive_neighborhood_returns_middle_candidate() -> None:
    points: dict[str, SurfacePoint] = {}
    for step in (0.010, 0.015, 0.020):
        for unit in (0.05, 0.10, 0.15):
            candidate = ParameterCandidate(
                config=AdaptiveConfig(grid=GridConfig(step_pct=step, unit_pct=unit)),
            )
            points[candidate.config_hash] = SurfacePoint(
                config_hash=candidate.config_hash,
                axis_values={"step_pct": step, "unit_pct": unit},
                oos_returns=(0.05, 0.04, 0.03),
                positive_windows=(True, True, True),
            )

    selected = stable_parameter_neighborhood(
        points, axes=("step_pct", "unit_pct"), min_positive_window_share=0.60,
    )

    assert len(selected) == 1
    assert selected[0].config.grid.step_pct == 0.015
    assert selected[0].config.grid.unit_pct == 0.10


def test_neighbor_must_match_every_other_axis() -> None:
    def point(step: float, stop: float) -> SurfacePoint:
        candidate = ParameterCandidate(
            config=AdaptiveConfig(
                grid=GridConfig(step_pct=step, atr_stop_multiple=stop),
            ),
            family="grid_only",
        )
        return SurfacePoint(
            config_hash=candidate.config_hash,
            axis_values={"step_pct": step, "atr_stop_multiple": stop},
            oos_returns=(0.05, 0.04, 0.03),
            positive_windows=(True, True, True),
        )

    points = {
        item.config_hash: item
        for item in (
            point(0.015, 3.0),
            point(0.010, 3.0),
            point(0.010, 2.0),
            point(0.020, 4.0),
        )
    }

    assert stable_parameter_neighborhood(
        points,
        axes=("step_pct", "atr_stop_multiple"),
        min_positive_window_share=0.75,
    ) == ()


def _positive_surface(candidates: tuple[ParameterCandidate, ...]) -> dict[str, SurfacePoint]:
    return {
        candidate.config_hash: SurfacePoint(
            config_hash=candidate.config_hash,
            axis_values={},
            oos_returns=(0.05, 0.04, 0.03),
            positive_windows=(True, True, True),
        )
        for candidate in candidates
    }


def test_expanded_three_point_surface_reaches_stability() -> None:
    base = ParameterCandidate(
        config=AdaptiveConfig(grid=GridConfig(atr_stop_multiple=3.0)),
        family="grid_only",
    )
    expanded = expand_candidate_axis(base, axis="atr_stop_multiple")

    selected = stable_parameter_neighborhood(
        _positive_surface(expanded),
        candidates=expanded,
        axes=("atr_stop_multiple",),
        min_positive_window_share=0.75,
    )

    assert selected == (expanded[1],)


@pytest.mark.parametrize(
    "unrelated_config",
    (
        AdaptiveConfig(grid=GridConfig(atr_stop_multiple=4.0, cooldown_sessions=10)),
        AdaptiveConfig(grid=GridConfig(atr_stop_multiple=4.0), trend=TrendConfig(stop_n=2.5)),
    ),
)
def test_neighbor_with_any_unrelated_grid_or_trend_change_is_not_stable(
    unrelated_config: AdaptiveConfig,
) -> None:
    center = ParameterCandidate(
        config=AdaptiveConfig(grid=GridConfig(atr_stop_multiple=3.0)),
        family="grid_only",
    )
    lower = ParameterCandidate(
        config=AdaptiveConfig(grid=GridConfig(atr_stop_multiple=2.0)),
        family="grid_only",
    )
    upper = ParameterCandidate(config=unrelated_config, family="grid_only")
    candidates = (center, lower, upper)

    assert stable_parameter_neighborhood(
        _positive_surface(candidates),
        candidates=candidates,
        axes=("atr_stop_multiple",),
        min_positive_window_share=0.75,
    ) == ()


def test_categorical_macd_axis_requires_both_observed_passing_values() -> None:
    candidates = tuple(
        ParameterCandidate(
            config=AdaptiveConfig(
                trend=TrendConfig(
                    stop_n=2.0,
                    risk_per_unit=0.005,
                    add_n=0.5,
                    max_units=4,
                    require_macd_bullish=value,
                    amount_ratio_min=None,
                ),
            ),
            family="trend_only",
        )
        for value in (False, True)
    )
    points = {
        candidate.config_hash: SurfacePoint(
            config_hash=candidate.config_hash,
            axis_values={"require_macd_bullish": float(candidate.config.trend.require_macd_bullish)},
            oos_returns=(0.05, 0.04, 0.03),
            positive_windows=(True, True, True),
        )
        for candidate in candidates
    }

    selected = stable_parameter_neighborhood(
        points,
        candidates=candidates,
        axes=("require_macd_bullish",),
        min_positive_window_share=0.75,
    )

    assert len(selected) == 1
    assert selected[0].config_hash in points

    failed_points = dict(points)
    failed_candidate = candidates[0]
    failed_points[failed_candidate.config_hash] = SurfacePoint(
        config_hash=failed_candidate.config_hash,
        axis_values={"require_macd_bullish": 0.0},
        oos_returns=(-0.03, -0.02, -0.01),
        positive_windows=(False, False, False),
    )
    assert stable_parameter_neighborhood(
        failed_points,
        candidates=candidates,
        axes=("require_macd_bullish",),
        min_positive_window_share=0.75,
    ) == ()


def test_plateau_picks_more_conservative_risk_when_even_cardinality() -> None:
    candidates = trend_candidates()

    points: dict[str, SurfacePoint] = {}
    for candidate in candidates:
        points[candidate.config_hash] = SurfacePoint(
            config_hash=candidate.config_hash,
            axis_values={
                "risk_per_unit": candidate.config.trend.risk_per_unit,
                "add_n": candidate.config.trend.add_n,
                "max_units": float(candidate.config.trend.max_units),
            },
            oos_returns=(0.10, 0.10),
            positive_windows=(True, True),
        )

    selected = stable_parameter_neighborhood(
        points,
        axes=("risk_per_unit", "add_n", "max_units"),
        min_positive_window_share=0.50,
    )

    assert len(selected) == 1
    assert selected[0].config.trend.risk_per_unit == 0.0050
    assert selected[0].config.trend.add_n == 0.75
    assert selected[0].config.trend.max_units == 3


def test_amount_ratio_none_is_a_valid_neighbor_axis_value() -> None:
    candidates = tuple(
        candidate for candidate in trend_candidates()
        if candidate.config.trend.risk_per_unit == 0.005
        and candidate.config.trend.add_n == 0.75
        and candidate.config.trend.max_units == 3
    )
    points = {
        candidate.config_hash: SurfacePoint(
            candidate.config_hash, {"amount_ratio_min": float("-inf") if candidate.config.trend.amount_ratio_min is None else candidate.config.trend.amount_ratio_min},
            (0.05, 0.04), (True, True),
        )
        for candidate in candidates
    }

    selected = stable_parameter_neighborhood(
        points, axes=("amount_ratio_min",), min_positive_window_share=0.5,
    )

    assert len(selected) == 1
    assert selected[0].config.trend.amount_ratio_min in {1.0, 1.2}
