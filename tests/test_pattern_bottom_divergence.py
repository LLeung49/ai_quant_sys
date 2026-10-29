import importlib.util
from pathlib import Path

import numpy as np
import pytest


@pytest.fixture(scope="module")
def radar():
    path = (Path(__file__).resolve().parents[1] / "src" / "pattern_detection"
            / "9-形态选股雷达.py")
    spec = importlib.util.spec_from_file_location("radar_divergence_test", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def detect(radar, prev=-1.0, recent=-0.8, recent_price=9.0, **kwargs):
    close = np.full(60, 12.0)
    close[20], close[55] = 10.0, recent_price
    dif = np.full(60, -0.5)
    dif[20], dif[55] = prev, recent
    # Boundary rejection must not rely on a divide-by-zero or invalid warning.
    with np.errstate(divide="raise", invalid="raise"):
        return radar.detect_bottom_divergence(close, dif, **kwargs)


@pytest.mark.parametrize("prev,recent,expected", [
    (-1.0, -0.8, True),
    (-1.0, -1.2, False),
    (-1.0, -0.98, False),
    (-1.0, -1.0, False),
    (-2.0, -1.92, False),  # Absolute gain > .05, relative gain < 5%.
    (-2.0, -1.875, True),
    (-2.5, -2.375, False),  # Exactly 5% is excluded (binary-exact inputs).
])
def test_relative_improvement(radar, prev, recent, expected):
    found, info = detect(radar, prev, recent)
    assert bool(found) is expected
    if expected:
        assert info["prev_macd"] == prev
        assert info["recent_macd"] == recent
    else:
        assert info == {}


@pytest.mark.parametrize("prev,recent", [
    (0.0, -0.8), (1e-8, -0.8), (-1e-8, -0.8), (-1e-10, -0.8),
    (np.nan, -0.8), (-1.0, np.nan),
    (np.inf, -0.8), (-np.inf, -0.8),
    (-1.0, np.inf), (-1.0, -np.inf),
])
def test_invalid_or_near_zero_dif_is_rejected(radar, prev, recent):
    assert detect(radar, prev, recent) == (False, {})


def test_equal_price_low_is_allowed(radar):
    assert detect(radar, recent_price=10.0)[0]


def test_higher_price_low_is_rejected(radar):
    assert detect(radar, recent_price=10.5) == (False, {})


def test_below_zero_filter_remains_optional(radar):
    assert detect(radar, recent=0.2) == (False, {})
    assert detect(radar, recent=0.2, require_macd_below_zero=False)[0]


def test_previous_downtrend_filter_remains_optional(radar):
    assert detect(radar, min_prev_decline_pct=0.2) == (False, {})
    assert detect(radar, min_prev_decline_pct=0.2, require_prev_downtrend=False)[0]


def test_explicit_rise_required_even_with_negative_threshold(radar):
    assert detect(radar, recent=-1.2, min_macd_diff=-0.5) == (False, {})
