"""v2_short_term 异动标签的单元测试：覆盖 ``short_rebound_candidate`` /
``short_breakdown_candidate`` 在 ``rs_5`` 缺失 / 满足阈值时的行为。"""
from __future__ import annotations

import numpy as np
import pandas as pd

from morning_conference.sector_rotation2.short_term.config import DEFAULT_SHORT_TERM_CONFIG
from morning_conference.sector_rotation2.short_term.labels import classify_short_term_labels


def _row(**overrides) -> pd.Series:
    base = {
        "sector_name": "半导体",
        "score_eligible": True,
        "rs_1": np.nan,
        "rs_5": np.nan,
        "breadth_up": np.nan,
        "rvol_1_20": np.nan,
        "share_impulse_1d": np.nan,
        "limit_up_ratio": np.nan,
        "limit_down_ratio": np.nan,
        "ret_1": np.nan,
    }
    base.update(overrides)
    return pd.Series(base)


def _has(label_csv: str, target: str) -> bool:
    if not label_csv:
        return False
    return target in label_csv.split(",")


def test_short_rebound_triggers_when_rs1_positive_and_rs5_negative():
    labels, _ = classify_short_term_labels(
        _row(rs_1=0.012, rs_5=-0.005, breadth_up=0.6), DEFAULT_SHORT_TERM_CONFIG,
    )
    assert _has(labels, "short_rebound_candidate")


def test_short_rebound_does_not_trigger_when_rs5_is_missing():
    labels, _ = classify_short_term_labels(
        _row(rs_1=0.02, rs_5=np.nan, breadth_up=0.6), DEFAULT_SHORT_TERM_CONFIG,
    )
    assert not _has(labels, "short_rebound_candidate")


def test_short_rebound_does_not_trigger_when_rs1_below_threshold():
    labels, _ = classify_short_term_labels(
        _row(rs_1=0.005, rs_5=-0.01, breadth_up=0.6), DEFAULT_SHORT_TERM_CONFIG,
    )
    assert not _has(labels, "short_rebound_candidate")


def test_short_rebound_does_not_trigger_when_rs5_is_positive():
    labels, _ = classify_short_term_labels(
        _row(rs_1=0.02, rs_5=0.01, breadth_up=0.6), DEFAULT_SHORT_TERM_CONFIG,
    )
    assert not _has(labels, "short_rebound_candidate")


def test_short_breakdown_triggers_when_rs1_negative_and_rs5_positive():
    labels, _ = classify_short_term_labels(
        _row(rs_1=-0.012, rs_5=0.005, breadth_up=0.6), DEFAULT_SHORT_TERM_CONFIG,
    )
    assert _has(labels, "short_breakdown_candidate")


def test_short_breakdown_does_not_trigger_when_rs5_is_missing():
    labels, _ = classify_short_term_labels(
        _row(rs_1=-0.02, rs_5=np.nan, breadth_up=0.6), DEFAULT_SHORT_TERM_CONFIG,
    )
    assert not _has(labels, "short_breakdown_candidate")


def test_short_breakdown_does_not_trigger_when_rs1_above_threshold():
    labels, _ = classify_short_term_labels(
        _row(rs_1=-0.005, rs_5=0.01, breadth_up=0.6), DEFAULT_SHORT_TERM_CONFIG,
    )
    assert not _has(labels, "short_breakdown_candidate")


def test_short_breakdown_does_not_trigger_when_rs5_is_negative():
    labels, _ = classify_short_term_labels(
        _row(rs_1=-0.02, rs_5=-0.01, breadth_up=0.6), DEFAULT_SHORT_TERM_CONFIG,
    )
    assert not _has(labels, "short_breakdown_candidate")


def test_score_ineligible_sector_never_triggers_rebound_or_breakdown():
    labels, _ = classify_short_term_labels(
        _row(score_eligible=False, rs_1=0.02, rs_5=-0.01), DEFAULT_SHORT_TERM_CONFIG,
    )
    assert labels == ""


def test_limit_cluster_triggers_when_up_ratio_above_threshold_and_down_ratio_low():
    labels, intensity = classify_short_term_labels(
        _row(limit_up_ratio=0.08, limit_down_ratio=0.005), DEFAULT_SHORT_TERM_CONFIG,
    )
    assert _has(labels, "limit_cluster")
    assert intensity == "intense"


def test_limit_cluster_does_not_trigger_when_up_ratio_below_threshold():
    labels, _ = classify_short_term_labels(
        _row(limit_up_ratio=0.04, limit_down_ratio=0.0), DEFAULT_SHORT_TERM_CONFIG,
    )
    assert not _has(labels, "limit_cluster")


def test_limit_cluster_does_not_trigger_when_down_ratio_too_high():
    labels, _ = classify_short_term_labels(
        _row(limit_up_ratio=0.10, limit_down_ratio=0.03), DEFAULT_SHORT_TERM_CONFIG,
    )
    assert not _has(labels, "limit_cluster")


def test_limit_panic_triggers_when_down_ratio_above_threshold_and_up_ratio_low():
    labels, intensity = classify_short_term_labels(
        _row(limit_up_ratio=0.005, limit_down_ratio=0.09), DEFAULT_SHORT_TERM_CONFIG,
    )
    assert _has(labels, "limit_panic")
    assert intensity == "intense"


def test_limit_panic_does_not_trigger_when_down_ratio_below_threshold():
    labels, _ = classify_short_term_labels(
        _row(limit_up_ratio=0.0, limit_down_ratio=0.04), DEFAULT_SHORT_TERM_CONFIG,
    )
    assert not _has(labels, "limit_panic")


def test_limit_labels_skip_when_ratios_missing():
    labels, intensity = classify_short_term_labels(_row(), DEFAULT_SHORT_TERM_CONFIG)
    assert not _has(labels, "limit_cluster")
    assert not _has(labels, "limit_panic")
    assert intensity == "none"
