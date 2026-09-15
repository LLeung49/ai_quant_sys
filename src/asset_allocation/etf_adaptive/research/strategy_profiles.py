"""Immutable, explicit ETF research profile declarations.

Profiles define a research boundary above the existing executable strategy and
benchmark specifications.  They do not dispatch execution or imply authority
to trade.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, replace
from hashlib import sha256
from itertools import product
import json
from types import MappingProxyType
from typing import Mapping

from ..config import AdaptiveConfig
from . import parameters
from .experiment import APPROVED_EXPERIMENT_AXES
from .strategy_specs import (
    BUY_AND_HOLD_SPEC,
    FIXED_HALF_SPEC,
    FULL_ADAPTIVE_SPEC,
    GRID_ONLY_SPEC,
    BenchmarkSpec,
    StrategySpec,
)


_SELECTION_FAMILIES = frozenset({"grid_only", "trend_only"})
_GRID_AXES = frozenset(asdict(AdaptiveConfig.default().grid))
_TREND_AXES = frozenset(asdict(AdaptiveConfig.default().trend))


@dataclass(frozen=True)
class StrategyProfileSpec:
    """A versioned, non-inferable research selection and evidence policy."""

    profile_id: str
    version: str
    strategy: StrategySpec | None
    benchmarks: tuple[BenchmarkSpec, ...]
    selection_families: tuple[str, ...]
    required_evidence: frozenset[str]

    def __post_init__(self) -> None:
        if not isinstance(self.profile_id, str) or not self.profile_id.strip():
            raise ValueError("profile_id must be non-empty")
        if not isinstance(self.version, str) or not self.version.strip():
            raise ValueError("profile version must be non-empty")
        if self.strategy is not None and not isinstance(self.strategy, StrategySpec):
            raise ValueError("profile strategy must be a StrategySpec or None")

        benchmarks = tuple(self.benchmarks)
        if not benchmarks or any(not isinstance(item, BenchmarkSpec) for item in benchmarks):
            raise ValueError("profile requires benchmark specs")

        families = tuple(self.selection_families)
        if len(set(families)) != len(families) or any(family not in _SELECTION_FAMILIES for family in families):
            raise ValueError("profile has an unsupported selection family")
        if self.strategy is None and families:
            raise ValueError("benchmark-only profile cannot select adaptive candidates")

        evidence = frozenset(self.required_evidence)
        if not evidence or any(not isinstance(item, str) or not item for item in evidence):
            raise ValueError("profile requires non-empty evidence declarations")

        object.__setattr__(self, "benchmarks", benchmarks)
        object.__setattr__(self, "selection_families", families)
        object.__setattr__(self, "required_evidence", evidence)

    def profile_hash(self) -> str:
        """Return the canonical reproducibility identity of the profile policy."""
        return _hash_profile(asdict(self))


GRID_CORE_PROFILE = StrategyProfileSpec(
    "grid_core",
    "1",
    GRID_ONLY_SPEC,
    (BUY_AND_HOLD_SPEC, FIXED_HALF_SPEC),
    ("grid_only",),
    frozenset({"integrated_oos", "execution", "provenance"}),
)

GRID_PLUS_OPTIONAL_TREND_PROFILE = StrategyProfileSpec(
    "grid_plus_optional_trend",
    "1",
    FULL_ADAPTIVE_SPEC,
    (BUY_AND_HOLD_SPEC, FIXED_HALF_SPEC),
    ("grid_only",),
    frozenset({"integrated_oos", "execution", "provenance", "mode_attribution"}),
)

CORE_HOLD_REBALANCE_PROFILE = StrategyProfileSpec(
    "core_hold_rebalance",
    "1",
    None,
    (BUY_AND_HOLD_SPEC, FIXED_HALF_SPEC),
    (),
    frozenset({"integrated_oos", "execution", "provenance"}),
)


_PROFILES = MappingProxyType({
    profile.profile_id: profile
    for profile in (
        GRID_CORE_PROFILE,
        GRID_PLUS_OPTIONAL_TREND_PROFILE,
        CORE_HOLD_REBALANCE_PROFILE,
    )
})


def profile_for_id(profile_id: str) -> StrategyProfileSpec:
    """Return an explicitly declared profile; never infer one from an ETF."""
    try:
        return _PROFILES[profile_id]
    except (KeyError, TypeError) as exc:
        raise ValueError(f"unknown strategy profile: {profile_id!r}") from exc


def profile_training_plan(
    profile: StrategyProfileSpec,
    config: AdaptiveConfig,
    allowed_axes: Mapping[str, tuple[object, ...]],
) -> Mapping[str, tuple]:
    """Build each declared frozen candidate surface without cross-mode tuning."""
    if not isinstance(profile, StrategyProfileSpec):
        raise ValueError("profile must be a StrategyProfileSpec")
    if not isinstance(config, AdaptiveConfig):
        raise ValueError("config must be an AdaptiveConfig")
    if not isinstance(allowed_axes, Mapping):
        raise ValueError("allowed_axes must be a mapping")

    axes_by_family: dict[str, tuple[str, ...]] = {
        family: () for family in profile.selection_families
    }
    for axis, values in allowed_axes.items():
        family = _family_for_axis(axis)
        if family not in profile.selection_families:
            raise ValueError(f"profile does not permit axis: {axis}")
        values = tuple(values)
        approved = APPROVED_EXPERIMENT_AXES[axis]
        if not values or any(
            not any(type(value) is type(item) and value == item for item in approved)
            for value in values
        ):
            raise ValueError(f"invalid allowed axis: {axis}")
        axes_by_family[family] += (axis,)

    plans: dict[str, tuple] = {}
    for family in profile.selection_families:
        section = "grid" if family == "grid_only" else "trend"
        baseline = getattr(config, section)
        axes = axes_by_family[family]
        candidates = tuple(
            parameters.ParameterCandidate(
                replace(config, **{section: replace(baseline, **dict(zip(axes, values)))}),
                family,
            )
            for values in product(*(allowed_axes[axis] for axis in axes))
        )
        plans[family] = (candidates, axes, ())
    return MappingProxyType(plans)


def _family_for_axis(axis: str) -> str:
    if axis not in APPROVED_EXPERIMENT_AXES:
        raise ValueError(f"invalid allowed axis: {axis}")
    if axis in _GRID_AXES:
        return "grid_only"
    if axis in _TREND_AXES:
        return "trend_only"
    raise ValueError(f"axis has no selection family: {axis}")


def _hash_profile(payload: object) -> str:
    encoded = json.dumps(_jsonable(payload), sort_keys=True, separators=(",", ":"), allow_nan=False)
    return sha256(encoded.encode("utf-8")).hexdigest()


def _jsonable(value: object) -> object:
    if isinstance(value, Mapping):
        return {str(key): _jsonable(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [_jsonable(item) for item in value]
    if isinstance(value, (frozenset, set)):
        return sorted((_jsonable(item) for item in value), key=lambda item: json.dumps(item, sort_keys=True))
    return value
