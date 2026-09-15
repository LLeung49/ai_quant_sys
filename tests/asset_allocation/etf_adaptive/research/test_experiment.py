from dataclasses import replace
from datetime import date
import json

import pytest

from asset_allocation.etf_adaptive.research.experiment import ExperimentSpec, targeted_study
from asset_allocation.etf_adaptive.research.strategy_profiles import (
    GRID_CORE_PROFILE,
    GRID_PLUS_OPTIONAL_TREND_PROFILE,
)


def test_experiment_serializes_the_declared_profile_and_hash() -> None:
    spec = ExperimentSpec("industry-grid", ("515450.SH",), GRID_CORE_PROFILE,
                          {"step_pct": (0.02,)}, date(2021, 1, 1), date(2026, 9, 11))

    payload = json.loads(json.dumps(spec.to_dict()))

    assert payload["profile"]["profile_id"] == "grid_core"
    assert payload["profile_hash"] == GRID_CORE_PROFILE.profile_hash()
    assert ExperimentSpec.from_dict(payload) == spec


def test_experiment_rejects_axis_not_owned_by_its_profile() -> None:
    with pytest.raises(ValueError, match="profile does not permit axis"):
        ExperimentSpec("bad", ("515450.SH",), GRID_CORE_PROFILE,
                       {"stop_n": (2.0,)}, date(2021, 1, 1), date(2026, 9, 11))


def test_targeted_study_manifest_cannot_include_nonprioritized_code():
    from asset_allocation.etf_adaptive.research import experiment

    assert hasattr(experiment, "targeted_study"), "targeted study boundary is not implemented"
    study = experiment.targeted_study("hk_internet")
    assert study.target_codes == ("513330.SH",)
    with pytest.raises(ValueError, match="target code"):
        experiment.targeted_study("hk_internet", target_codes=("513100.SH",))


@pytest.mark.parametrize("name,code,axes", [
    ("hk_internet", "513330.SH", {"step_pct", "unit_pct", "atr_stop_multiple", "cooldown_sessions"}),
    ("chinext_reentry", "159915.SZ", {"cooldown_sessions", "atr_stop_multiple"}),
    ("star50_extreme_window", "588000.SH", {"atr_stop_multiple", "cooldown_sessions"}),
])
def test_targeted_candidates_keep_undeclared_fields_frozen(name, code, axes):
    from dataclasses import asdict
    from asset_allocation.etf_adaptive.research import experiment

    study = experiment.targeted_study(name)
    assert study.target_codes == (code,)
    assert set(study.allowed_axes) == axes
    plans = experiment.study_training_plan(study)
    for family, (candidates, initial_axes, expansion_axes) in plans.items():
        assert set(initial_axes) | set(expansion_axes) <= axes
        for candidate in candidates:
            for section in ("grid", "trend", "cost"):
                defaults = asdict(getattr(study.strategy.config, section))
                for field, value in asdict(getattr(candidate.config, section)).items():
                    if field in initial_axes:
                        assert value in study.allowed_axes[field]
                    else:
                        assert value == defaults[field]


def test_star50_cli_missing_diagnostic_stops_before_provider(tmp_path, monkeypatch):
    import json
    from asset_allocation.etf_adaptive import run_instrument_validation as cli

    monkeypatch.chdir(tmp_path)
    def unexpected_provider():
        pytest.fail("parameter runner must not read data before the diagnostic gate")
    monkeypatch.setattr(cli, "default_validation_provider", unexpected_provider)
    output = tmp_path / "study"
    assert cli.main(["--experiment", "star50_extreme_window", "--start-date", "2021-01-01",
                     "--as-of-date", "2026-09-11", "--output-dir", str(output)]) == 4
    diagnostic = json.loads((output / "diagnostic.json").read_text(encoding="utf-8"))
    assert diagnostic["parameter_execution_allowed"] is False
    assert diagnostic["largest_contributor"] is None
    assert diagnostic["research_only"] is True
    assert not list(output.rglob("*operation*"))


def test_star50_diagnostic_records_extreme_window_but_cannot_infer_contributor(tmp_path):
    import json
    from asset_allocation.etf_adaptive.research.experiment import targeted_study, star50_diagnostic

    (tmp_path / "summary.json").write_text(json.dumps({
        "stock_code": "588000.SH",
        "data_provenance": {"run_manifest": {"data_cutoff": "2026-09-10"}},
        "windows": [
            {"window_id": "wf_000", "validation_start": "2023-01-03", "excess_return": -0.1},
            {"window_id": "wf_003", "validation_start": "2024-08-22", "excess_return": -0.5},
        ],
        "largest_contributor": "cash_opportunity_cost",
    }), encoding="utf-8")
    diagnostic = star50_diagnostic(targeted_study("star50_extreme_window"), tmp_path)
    assert diagnostic["window_id"] == "wf_003"
    assert diagnostic["excess_return"] == -0.5
    assert diagnostic["largest_contributor"] is None
    assert diagnostic["parameter_execution_allowed"] is False


def _spec(**changes):
    from asset_allocation.etf_adaptive.research import experiment
    values = dict(experiment_id="bounded", target_codes=("513330.SH",),
                  profile=GRID_CORE_PROFILE,
                  allowed_axes={"step_pct": (0.01, 0.02, 0.03)},
                  start_date=date(2020, 1, 1), as_of_date=date(2026, 9, 8))
    values.update(changes)
    return experiment.ExperimentSpec(**values)


@pytest.mark.parametrize("changes,match", [
    ({"target_codes": ("UNKNOWN",)}, "target"),
    ({"allowed_axes": {"unknown": (1,)}}, "allowed axis"),
    ({"allowed_axes": {"step_pct": (9.0,)}}, "allowed axis"),
    ({"allowed_axes": {"step_pct": (False,)}}, "allowed axis"),
    ({"allowed_axes": {"step_pct": ()}}, "allowed axis"),
    ({"target_codes": ()}, "target"),
    ({"start_date": date(2027, 1, 1)}, "date"),
])
def test_experiment_rejects_unapproved_target_or_axis(changes, match):
    with pytest.raises(ValueError, match=match):
        _spec(**changes)


def test_experiment_hash_is_canonical_and_immutable():
    axes = {"step_pct": (0.01, 0.02), "unit_pct": (0.05, 0.1)}
    spec = _spec(allowed_axes=axes)
    same = _spec(allowed_axes=dict(reversed(list(axes.items()))))
    assert spec.experiment_hash() == same.experiment_hash()
    axes["step_pct"] = (0.03,)
    assert spec.experiment_hash() == same.experiment_hash()
    with pytest.raises(TypeError):
        spec.allowed_axes["step_pct"] = (0.03,)
    assert replace(spec, as_of_date=date(2026, 9, 9)).experiment_hash() != spec.experiment_hash()
    assert replace(spec, profile=replace(spec.profile, version="2")).experiment_hash() != spec.experiment_hash()


def test_targeted_study_explicitly_selects_optional_trend_profile() -> None:
    study = ExperimentSpec.from_dict(targeted_study("hk_internet").to_dict())

    assert study.profile == GRID_PLUS_OPTIONAL_TREND_PROFILE
    assert study.strategy == study.profile.strategy
    assert study.benchmarks == study.profile.benchmarks
