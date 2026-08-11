"""P1 Score V2 预注册候选的纯评分构造。"""
from __future__ import annotations

import numpy as np
import pandas as pd


CANDIDATE_NAMES = ("h1_acceleration", "h2_trend_pruned", "h3_trend_reversed")

_REQUIRED_COMPONENTS = (
    "trend_level_score",
    "velocity_score",
    "acceleration_score",
    "participation_score",
)


def _weighted_available(frame: pd.DataFrame, weights: dict[str, float]) -> pd.Series:
    numerator = pd.Series(0.0, index=frame.index)
    denominator = pd.Series(0.0, index=frame.index)
    for column, weight in weights.items():
        values = pd.to_numeric(frame[column], errors="coerce")
        available = values.notna()
        numerator = numerator + values.fillna(0.0) * weight
        denominator = denominator + available.astype(float) * abs(weight)
    return numerator.div(denominator.where(denominator > 0.0))


def build_candidate_scores(snapshots: pd.DataFrame) -> pd.DataFrame:
    """按冻结公式构建 H1/H2/H3 研究候选，不修改输入快照。"""
    missing = [column for column in _REQUIRED_COMPONENTS if column not in snapshots]
    if missing:
        raise ValueError(f"快照缺少冻结候选分量列: {', '.join(missing)}")
    result = snapshots.copy()
    result["h1_acceleration"] = pd.to_numeric(result["acceleration_score"], errors="coerce")
    result["h2_trend_pruned"] = _weighted_available(
        result,
        {"acceleration_score": 0.15, "participation_score": 0.15},
    )
    result["h3_trend_reversed"] = _weighted_available(
        result,
        {
            "trend_level_score": -0.45,
            "velocity_score": -0.25,
            "acceleration_score": 0.15,
            "participation_score": 0.15,
        },
    )
    return result
