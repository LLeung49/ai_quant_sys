"""Final candidate scoring, classification, and attribution for Trend Alpha V1."""

from __future__ import annotations

from typing import Mapping

import numpy as np
import pandas as pd

from .config import TrendAlphaConfig


def score_trend_candidates(
    frame: pd.DataFrame,
    *,
    config: TrendAlphaConfig,
    group_keys: tuple = ("as_of_date", "sector_name"),
) -> pd.DataFrame:
    """Compute ``candidate_score`` (clipped to [-1, 1]) for each row."""

    out = frame.copy()
    score_weights = dict(config.score_weights)
    if abs(sum(score_weights.values()) - 1.0) > 1e-9:
        raise ValueError("score_weights must sum to 1.0")

    if "risk_penalty" not in out.columns:
        out["risk_penalty"] = 0.0

    raw_scores = np.full(len(out), np.nan, dtype="float64")
    for idx in range(len(out)):
        row = out.iloc[idx]
        total_weight = 0.0
        weighted = 0.0
        for name, weight in score_weights.items():
            if name not in out.columns:
                continue
            value = row[name]
            if value is None or (isinstance(value, float) and np.isnan(value)):
                continue
            total_weight += weight
            weighted += float(value) * weight
        risk_penalty = row.get("risk_penalty")
        if risk_penalty is not None and not (isinstance(risk_penalty, float) and np.isnan(risk_penalty)):
            weighted -= float(risk_penalty)
            total_weight += sum(score_weights.values())
        if total_weight <= 0:
            raw_scores[idx] = np.nan
        else:
            raw_scores[idx] = max(-1.0, min(1.0, weighted / total_weight))
    out["candidate_score"] = raw_scores

    # Sector-local rank inside each (as_of_date, sector_name) group.
    if len(out) > 0:
        ranks = out.groupby(list(group_keys))["candidate_score"].rank(
            method="min", ascending=False, na_option="keep",
        )
        sector_size = out.groupby(list(group_keys))["candidate_score"].transform("count")
        out["rank_in_sector"] = ranks.where(sector_size > 0, other=np.nan).astype("float64")
    else:
        out["rank_in_sector"] = np.nan

    return out


def classify_candidate(
    features: Mapping,
    *,
    config: TrendAlphaConfig,
) -> str:
    """Return the candidate_status label for one row's feature bundle."""

    risk_penalty = float(features.get("risk_penalty") or 0.0)
    if risk_penalty > config.risk_penalty_threshold:
        return "risk_watch"

    score = features.get("candidate_score")
    if score is None or (isinstance(score, float) and np.isnan(score)):
        return "risk_watch"

    streak = features.get("limit_up_streak")
    hot_source = features.get("hot_leader_source", "unavailable")
    if (
        streak is not None
        and hot_source != "unavailable"
        and int(streak) >= config.hot_leader_streak
        and float(score) >= config.min_score_for_leader
        and float(features.get("alpha_strength") or 0.0) > 0
    ):
        return "hot_leader"

    if bool(features.get("strong_pullback")):
        return "trend_pullback"

    breakout = bool(features.get("breakout20")) or bool(features.get("breakout60"))
    alpha = float(features.get("alpha_strength") or 0.0)
    if breakout and alpha > 0 and float(score) >= config.min_score_for_leader:
        return "trend_leader"

    return "risk_watch"


def attach_attribution(
    frame: pd.DataFrame,
    *,
    config: TrendAlphaConfig,
) -> pd.DataFrame:
    """Persist the standardized classification onto the frame."""

    out = frame.copy()
    out["candidate_status"] = [
        classify_candidate(row, config=config)
        for _, row in out.iterrows()
    ]
    return out

