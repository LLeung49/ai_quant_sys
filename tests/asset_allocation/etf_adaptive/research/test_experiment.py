from dataclasses import replace
from datetime import date

import pytest

from asset_allocation.etf_adaptive.research.strategy_specs import FULL_ADAPTIVE_SPEC, BUY_AND_HOLD_SPEC


def _spec(**changes):
    from asset_allocation.etf_adaptive.research import experiment
    values = dict(experiment_id="bounded", target_codes=("513330.SH",),
                  strategy=FULL_ADAPTIVE_SPEC, benchmarks=(BUY_AND_HOLD_SPEC,),
                  allowed_axes={"stop_n": (1.5, 2.0, 2.5)},
                  start_date=date(2020, 1, 1), as_of_date=date(2026, 9, 8))
    values.update(changes)
    return experiment.ExperimentSpec(**values)


@pytest.mark.parametrize("changes,match", [
    ({"target_codes": ("UNKNOWN",)}, "target"),
    ({"allowed_axes": {"unknown": (1,)}}, "allowed axis"),
    ({"allowed_axes": {"stop_n": (9.0,)}}, "allowed axis"),
    ({"allowed_axes": {"require_macd_bullish": (1,)}}, "allowed axis"),
    ({"allowed_axes": {"stop_n": ()}}, "allowed axis"),
    ({"target_codes": ()}, "target"),
    ({"benchmarks": ()}, "benchmark"),
    ({"start_date": date(2027, 1, 1)}, "date"),
])
def test_experiment_rejects_unapproved_target_or_axis(changes, match):
    with pytest.raises(ValueError, match=match):
        _spec(**changes)


def test_experiment_hash_is_canonical_and_immutable():
    axes = {"stop_n": (1.5, 2.0), "require_macd_bullish": (False, True)}
    spec = _spec(allowed_axes=axes)
    same = _spec(allowed_axes=dict(reversed(list(axes.items()))))
    assert spec.experiment_hash() == same.experiment_hash()
    axes["stop_n"] = (3.0,)
    assert spec.experiment_hash() == same.experiment_hash()
    with pytest.raises(TypeError):
        spec.allowed_axes["stop_n"] = (3.0,)
    assert replace(spec, as_of_date=date(2026, 9, 9)).experiment_hash() != spec.experiment_hash()
    assert replace(spec, strategy=replace(spec.strategy, version="2")).experiment_hash() != spec.experiment_hash()
    assert replace(spec, benchmarks=(replace(BUY_AND_HOLD_SPEC, target_weight=0.5),)).experiment_hash() != spec.experiment_hash()
