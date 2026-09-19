"""Bounded experiment identity and recorded research evidence (no execution)."""

from __future__ import annotations

from dataclasses import InitVar, asdict, dataclass, replace
from datetime import date
from hashlib import sha256
import json
from math import isfinite
from pathlib import Path
from types import MappingProxyType
from typing import TYPE_CHECKING, Mapping

from ..config import AdaptiveConfig, CostConfig, GridConfig, TrendConfig
from . import parameters
from .instrument_validation import FIXED_VALIDATION_TARGETS, InstrumentValidationResult
from .strategy_specs import BenchmarkSpec, StrategySpec, benchmark_provenance_hash

if TYPE_CHECKING:
    from .strategy_profiles import StrategyProfileSpec


APPROVED_EXPERIMENT_AXES = MappingProxyType({
    "step_pct": parameters.GRID_STEPS,
    "unit_pct": parameters.GRID_UNITS,
    "fixed_initial_pct": parameters.FIXED_INITIAL,
    "risk_per_unit": parameters.RISK_PER_UNIT,
    "add_n": parameters.ADD_N,
    "max_units": parameters.MAX_UNITS,
    "amount_ratio_min": parameters.AMOUNT_RATIO,
    "atr_stop_multiple": parameters.GRID_ATR_STOP_MULTIPLES,
    "cooldown_sessions": parameters.GRID_COOLDOWN_SESSIONS,
    "stop_n": parameters.TREND_STOP_N,
    "require_macd_bullish": parameters.TREND_REQUIRE_MACD_BULLISH,
})


def _json(payload) -> str:
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), allow_nan=False)


def _config(payload: Mapping[str, object]) -> AdaptiveConfig:
    return AdaptiveConfig(grid=GridConfig(**payload["grid"]),
                          trend=TrendConfig(**payload["trend"]),
                          cost=CostConfig(**payload["cost"]))


def _profile_payload(profile) -> dict[str, object]:
    return {
        "profile_id": profile.profile_id,
        "version": profile.version,
        "strategy": asdict(profile.strategy) if profile.strategy is not None else None,
        "benchmarks": [asdict(item) for item in profile.benchmarks],
        "selection_families": list(profile.selection_families),
        "required_evidence": sorted(profile.required_evidence),
    }


_LEGACY_READ = object()


@dataclass(frozen=True)
class ExperimentSpec:
    experiment_id: str
    target_codes: tuple[str, ...]
    profile: StrategyProfileSpec
    allowed_axes: Mapping[str, tuple[object, ...]]
    start_date: date
    as_of_date: date
    _legacy_read: InitVar[object] = None

    def __post_init__(self, _legacy_read: object) -> None:
        from .strategy_profiles import StrategyProfileSpec, profile_for_id, profile_training_plan

        if not isinstance(self.experiment_id, str) or not self.experiment_id.strip():
            raise ValueError("experiment_id must be non-empty")
        targets = tuple(self.target_codes)
        if not targets or len(set(targets)) != len(targets) or not set(targets).issubset(
            target.stock_code for target in FIXED_VALIDATION_TARGETS
        ):
            raise ValueError("experiment target must belong to fixed validation targets")
        if not isinstance(self.profile, StrategyProfileSpec):
            raise ValueError("experiment requires a strategy profile")
        if _legacy_read is _LEGACY_READ:
            if self.profile.profile_id != "legacy_unprofiled":
                raise ValueError("legacy experiment read requires legacy_unprofiled")
        else:
            try:
                registered = profile_for_id(self.profile.profile_id)
            except ValueError as exc:
                raise ValueError("experiment requires a registered strategy profile") from exc
            if self.profile != registered:
                raise ValueError("experiment requires a registered strategy profile")
        if self.start_date > self.as_of_date:
            raise ValueError("start date must not be after as-of date")
        axes: dict[str, tuple[object, ...]] = {}
        for axis, values in self.allowed_axes.items():
            values = tuple(values)
            config = self.profile.strategy.config if self.profile.strategy is not None else AdaptiveConfig.default()
            profile_training_plan(self.profile, config, {axis: values})
            axes[axis] = values
        object.__setattr__(self, "target_codes", targets)
        object.__setattr__(self, "allowed_axes", MappingProxyType(axes))

    @property
    def strategy(self) -> StrategySpec | None:
        return self.profile.strategy

    @property
    def benchmarks(self) -> tuple[BenchmarkSpec, ...]:
        return self.profile.benchmarks

    def to_dict(self) -> dict[str, object]:
        return {
            "experiment_id": self.experiment_id, "target_codes": list(self.target_codes),
            "profile": _profile_payload(self.profile), "profile_hash": self.profile.profile_hash(),
            "allowed_axes": {axis: list(values) for axis, values in self.allowed_axes.items()},
            "start_date": self.start_date.isoformat(), "as_of_date": self.as_of_date.isoformat(),
        }

    def experiment_hash(self) -> str:
        return sha256(_json(self.to_dict()).encode("utf-8")).hexdigest()

    @classmethod
    def from_dict(cls, payload: Mapping[str, object]) -> "ExperimentSpec":
        from .strategy_profiles import StrategyProfileSpec, profile_for_id

        if "profile" in payload:
            declared = payload["profile"]
            if not isinstance(declared, Mapping):
                raise ValueError("experiment profile provenance must be a mapping")
            profile = profile_for_id(declared.get("profile_id"))
            if (dict(declared) != _profile_payload(profile)
                    or payload.get("profile_hash") != profile.profile_hash()):
                raise ValueError("experiment profile provenance differs from registry")
        else:
            strategy = dict(payload["strategy"])
            strategy["config"] = _config(strategy["config"])
            profile = StrategyProfileSpec(
                "legacy_unprofiled", "0", StrategySpec(**strategy),
                tuple(BenchmarkSpec(**item) for item in payload["benchmarks"]),
                ("grid_only", "trend_only"), frozenset({"legacy_manifest"}),
            )
        return cls(payload["experiment_id"], tuple(payload["target_codes"]), profile,
                   payload["allowed_axes"], date.fromisoformat(payload["start_date"]),
                   date.fromisoformat(payload["as_of_date"]),
                   _legacy_read=_LEGACY_READ if "profile" not in payload else None)


_TARGETED_STUDIES = MappingProxyType({
    "hk_internet": ("513330.SH", ("step_pct", "unit_pct", "atr_stop_multiple", "cooldown_sessions")),
    "chinext_reentry": ("159915.SZ", ("cooldown_sessions", "atr_stop_multiple")),
    "star50_extreme_window": ("588000.SH", ("atr_stop_multiple", "cooldown_sessions")),
})


def targeted_study(name: str, *, target_codes=None, start_date=date(2021, 1, 1),
                   as_of_date=date(2026, 9, 11)) -> ExperimentSpec:
    """Construct one immutable, single-ETF study without universe overrides."""
    from .strategy_profiles import GRID_PLUS_OPTIONAL_TREND_PROFILE

    if name not in _TARGETED_STUDIES:
        raise ValueError("unknown targeted study")
    code, axes = _TARGETED_STUDIES[name]
    if target_codes is not None and tuple(target_codes) != (code,):
        raise ValueError("target code does not match the targeted study")
    return ExperimentSpec(name, (code,), GRID_PLUS_OPTIONAL_TREND_PROFILE,
                          {axis: APPROVED_EXPERIMENT_AXES[axis] for axis in axes},
                          start_date, as_of_date)


def study_training_plan(spec: ExperimentSpec) -> dict:
    """Screen each family's bounded Cartesian surface; freeze every other field."""
    from .strategy_profiles import profile_training_plan

    canonical = targeted_study(spec.experiment_id, target_codes=spec.target_codes,
                               start_date=spec.start_date, as_of_date=spec.as_of_date)
    if spec != canonical:
        raise ValueError("targeted study configuration differs from its declaration")
    return profile_training_plan(spec.profile, spec.strategy.config, spec.allowed_axes)


def star50_diagnostic(spec: ExperimentSpec, source: Path) -> dict:
    """Identify an extreme-window contributor only from persisted excess evidence."""
    diagnostic = {
        "experiment_hash": spec.experiment_hash(), "stock_code": "588000.SH",
        "source": str(source), "source_hashes": {}, "window_id": None,
        "largest_contributor": None, "parameter_execution_allowed": False,
        "research_only": True, "activation_eligible": False,
        "decision": "do_not_trade", "blocker": "missing_largest_contributor_evidence",
    }
    try:
        summary_path = source / "summary.json"
        summary = json.loads(summary_path.read_text(encoding="utf-8"))
        diagnostic["source_hashes"]["summary.json"] = sha256(summary_path.read_bytes()).hexdigest()
        manifest = summary["data_provenance"]["run_manifest"]
        source_cutoff = date.fromisoformat(manifest["data_cutoff"])
        if summary["stock_code"] != "588000.SH" or not spec.start_date <= source_cutoff <= spec.as_of_date:
            raise ValueError("diagnostic source identity mismatch")
        diagnostic["source_data_cutoff"] = source_cutoff.isoformat()
        windows = summary["windows"]
        if not windows or any(not isfinite(float(row["excess_return"])) for row in windows):
            raise ValueError("invalid diagnostic window evidence")
        worst = min(windows, key=lambda row: float(row["excess_return"]))
        diagnostic.update(window_id=worst["window_id"], excess_return=float(worst["excess_return"]),
                          validation_start=worst["validation_start"])
        if float(worst["excess_return"]) >= 0:
            raise ValueError("no lagging diagnostic window")
        excess_path = source / "excess_attribution.json"
        rows = json.loads(excess_path.read_text(encoding="utf-8"))
        matching = [row for row in rows if row["window_id"] == worst["window_id"]]
        recorded = [row["excess_attribution"] for row in manifest["experiment_windows"]
                    if row["window_id"] == worst["window_id"]]
        if len(matching) != 1 or len(recorded) != 1:
            raise ValueError("missing or ambiguous persisted attribution")
        row = matching[0]
        values = {name: row[name] for name in ("grid_return", "trend_return", "transition_return", "cash_opportunity_cost")}
        if any(type(value) not in (int, float) or not isfinite(value) for value in values.values()):
            raise ValueError("nonfinite contributor")
        if {key: value for key, value in row.items() if key != "window_id"} != recorded[0]:
            raise ValueError("persisted attribution differs from experiment manifest")
        if not isfinite(row["reconciliation_error"]) or abs(row["reconciliation_error"]) > 1e-9:
            raise ValueError("unreconciled contributor")
        if not any(abs(value) > 0 for value in values.values()):
            raise ValueError("no nonzero contributor")
        # Both files are required: legacy trade counts cannot fill missing daily-state evidence.
        for filename in ("excess_attribution.json", "daily_state.csv", "daily_nav.csv"):
            content = (source / filename).read_bytes()
            if len(content.splitlines()) < 2:
                raise ValueError("empty daily evidence")
            diagnostic["source_hashes"][filename] = sha256(content).hexdigest()
        largest = max(values, key=lambda name: abs(values[name]))
        diagnostic.update(largest_contributor=largest, contribution=values[largest],
                          parameter_execution_allowed=True, blocker=None)
    except (OSError, ValueError, KeyError, TypeError, IndexError) as exc:
        diagnostic["detail"] = str(exc)
    return diagnostic


def experiment_evidence(result: InstrumentValidationResult, spec: ExperimentSpec) -> dict[str, object]:
    """Serialize stored score surfaces via their explicit immutable boundary."""
    windows = []
    for window in result.windows:
        config = (window.execution_config if spec.strategy is None else
                  _config(window.selected_config) if window.selected_config else None)
        strategy = replace(spec.strategy, config=config) if config and spec.strategy is not None else None
        windows.append({
            "window_id": window.window_id,
            "execution_cost_config": asdict(window.cost_config) if window.cost_config else None,
            "screened_axes": window.screened_axes,
            "strategy_spec": {**asdict(strategy), "spec_hash": strategy.spec_hash(),
                              "config_hash": config.config_hash()} if strategy else None,
            "benchmark_specs": [
                {**asdict(item), "spec_hash": item.spec_hash(),
                 "config": asdict(config), "provenance_hash": benchmark_provenance_hash(item, config)}
                for item in spec.benchmarks
            ] if config else [],
            "selected_scores": {family: score.to_dict() for family, score in (window.selected_scores or {}).items()},
            "candidate_scores": [score.to_dict() for score in window.candidate_scores],
            "excess_attribution": asdict(window.excess_attribution) if window.excess_attribution else None,
        })
    return json.loads(_json({"experiment": spec.to_dict(), "experiment_hash": spec.experiment_hash(),
                            "run_mode": result.run_mode.value,
                            "research_only": True,
                            "activation_eligible": False if result.run_mode.value == "research_diagnostic" else result.activation_eligible,
                            "shadow_run_eligible": False if result.run_mode.value == "research_diagnostic" else None,
                            "trading_authorized": False,
                            "strategy_spec": asdict(spec.strategy) if spec.strategy is not None else None,
                            "benchmark_specs": [asdict(item) for item in spec.benchmarks],
                            "experiment_windows": windows}))


def bind_experiment(result: InstrumentValidationResult, spec: ExperimentSpec) -> InstrumentValidationResult:
    """Attach declared boundaries; never fill in missing provider/data evidence."""
    if result.target.stock_code not in spec.target_codes or result.as_of_date != spec.as_of_date:
        raise ValueError("experiment target or date does not match result")
    manifest = dict(result.run_manifest or {})
    manifest.update(experiment_evidence(result, spec))
    return replace(result, run_manifest=manifest)
