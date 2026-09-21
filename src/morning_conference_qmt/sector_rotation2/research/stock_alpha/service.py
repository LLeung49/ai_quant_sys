"""Build immutable Trend Alpha SHADOW stock candidates from upstream sources.

This module is the orchestration layer.  It joins the upstream
``sector_opportunity`` snapshots (which gate by ``playbook='trend_follow'``)
with the stock universe and pre-computed features to build one
``CandidateSnapshot`` per eligible stock per sector per date.
"""

from __future__ import annotations

from collections.abc import Callable, Iterable, Mapping
from dataclasses import dataclass
from datetime import date
from typing import Any

import numpy as np
import pandas as pd

from ..config_hash import build_config_hash
from ..contracts import CandidateSnapshot
from ..snapshot import (
    SnapshotStore, persist_backfill_snapshot, persist_delayed_shadow_snapshot,
    persist_live_shadow_snapshot,
)
from ..status import ExecutionStatus, ResearchStatus, SnapshotMode, ValidationStatus
from .common import (
    StockEligibilityRow,
    load_sector_close_series,
    load_stock_close_series,
    load_stock_universe,
)
from .config import TrendAlphaConfig
from .trend import classify_candidate, score_trend_candidates
from .trend_features import (
    calc_adx14,
    calc_alpha_persistence,
    calc_kama_er,
    calc_relative_returns,
    calc_volatility,
    score_alpha_strength,
    score_trend_quality,
)
from .trend_risk import (
    calc_extension_penalty,
    calc_hot_leader_bonus,
    calc_stock_liquidity,
    calc_volatility_penalty,
    total_risk_penalty,
)
from .trend_structure import (
    calc_breakout_flags,
    calc_ma,
    calc_ma_slope,
    calc_ma_stack,
    calc_prev_high,
    calc_strong_pullback,
    score_trend_structure,
)


@dataclass(frozen=True)
class SectorTrendContext:
    """Identity of the upstream sector_opportunity snapshot feeding Trend Alpha."""

    as_of_date: date
    sector_level: int
    sector_name: str
    model_version: str
    config_hash: str
    snapshot_mode: SnapshotMode


def load_trend_follow_sectors(
    as_of_date: str,
    sector_level: int,
    snapshot_mode: SnapshotMode,
    query: Callable[[str, tuple[object, ...]], list[dict[str, Any]]],
) -> list[Mapping[str, Any]]:
    """Return canonical sector_opportunity snapshots with ``playbook='trend_follow'``.

    The ``feature_json.playbook`` filter is applied in Python because the
    upstream sector_opportunity snapshot stores the playbook as JSON, not a
    dedicated column.  Backed by ``research_candidate_snapshot``.
    """

    rows = query(
        """SELECT sector_name, candidate_status, model_version, config_hash, snapshot_mode, feature_json
             FROM (
                SELECT sector_name, candidate_status, model_version, config_hash, snapshot_mode, feature_json,
                       ROW_NUMBER() OVER (
                           PARTITION BY sector_name ORDER BY created_at DESC, id DESC
                       ) AS canonical_rank
                FROM research_candidate_snapshot
                WHERE as_of_date=%s AND sector_level=%s AND entity_type='sector'
                  AND strategy_type='sector_opportunity' AND snapshot_mode=%s
             ) AS canonical_sector_snapshot
             WHERE canonical_rank=1
             ORDER BY sector_name ASC""",
        (as_of_date, sector_level, snapshot_mode.value),
    )
    trend_sectors: list[Mapping[str, Any]] = []
    for row in rows:
        feature_json = row.get("feature_json")
        if isinstance(feature_json, str):
            try:
                import json
                feature_json = json.loads(feature_json)
            except (TypeError, ValueError):
                feature_json = {}
        if not isinstance(feature_json, Mapping):
            continue
        if feature_json.get("playbook") != "trend_follow":
            continue
        trend_sectors.append(row)
    return trend_sectors


def build_features_frame(
    *,
    as_of_date: date,
    sector_level: int,
    sector_name: str,
    universe: list[StockEligibilityRow],
    sector_close_series: Mapping[date, float],
    stock_close_series: Mapping[str, Mapping[date, float]],
    config: TrendAlphaConfig,
) -> pd.DataFrame:
    """Compute the per-stock feature frame for one (as_of_date, sector)."""

    if not universe:
        return pd.DataFrame()
    sector_close = pd.Series(sector_close_series).sort_index()
    rows: list[dict[str, Any]] = []
    for stock in universe:
        stock_close_dict = stock_close_series.get(stock.stock_code)
        if not stock_close_dict:
            continue
        stock_close = pd.Series(stock_close_dict).sort_index()
        aligned = pd.concat([stock_close.rename("close"), sector_close.rename("sector")], axis=1).dropna()
        if aligned.empty:
            continue
        rr = calc_relative_returns(aligned["close"], aligned["sector"], windows=config.windows)
        er = calc_kama_er(aligned["close"], window=10)
        adx = None  # OHLC required; populated separately when full features available.
        ma20 = calc_ma(aligned["close"], window=20)
        ma60 = calc_ma(aligned["close"], window=60)
        ma20_slope = calc_ma_slope(ma20, window=5)
        prev_high_20 = calc_prev_high(aligned["close"].rename("close"), window=20)
        prev_high_60 = calc_prev_high(aligned["close"].rename("close"), window=60)
        breakout20, breakout60 = calc_breakout_flags(aligned["close"].rename("high"), prev_high_20, prev_high_60)
        ma_stack = calc_ma_stack(aligned["close"], ma20, ma60 if ma60.notna().any() else ma20, ma20_slope)
        ret_1d = aligned["close"].pct_change().dropna()
        vol20 = calc_volatility(ret_1d, window=config.liquidity_window)
        distance_ma20 = (
            float(aligned["close"].iloc[-1] / ma20.iloc[-1] - 1.0)
            if ma20.notna().any() else None
        )
        amount_median_20 = None  # Populated by service from upstream volume feed.
        rows.append({
            "stock_code": stock.stock_code,
            "as_of_date": as_of_date,
            "sector_name": sector_name,
            "sector_level": sector_level,
            "rr_5": rr.get("rr_5"),
            "rr_10": rr.get("rr_10"),
            "rr_20": rr.get("rr_20"),
            "er": er,
            "adx": adx,
            "ma_stack": ma_stack,
            "breakout20": breakout20,
            "breakout60": breakout60,
            "strong_pullback": False,  # populated by run_trend_alpha_for with full OHLCV.
            "distance_ma20": distance_ma20,
            "volatility_20d": vol20,
            "amount_20d_median": amount_median_20,
            "limit_up_streak": None,
            "hot_leader_source": "unavailable",
            "mapping_quality": stock.mapping_quality,
            "eligibility_unknown": list(stock.eligibility_unknown),
        })
    return pd.DataFrame(rows)


def build_trend_candidate(
    *,
    row: Mapping[str, Any],
    sector_context: SectorTrendContext,
    config: TrendAlphaConfig,
    run_id: str,
) -> CandidateSnapshot:
    """Construct the ``CandidateSnapshot`` for one scored feature row."""

    features = {
        "candidate_score": row.get("candidate_score"),
        "risk_penalty": row.get("risk_penalty"),
        "alpha_strength": row.get("alpha_strength"),
        "breakout20": row.get("breakout20"),
        "breakout60": row.get("breakout60"),
        "strong_pullback": row.get("strong_pullback"),
        "limit_up_streak": row.get("limit_up_streak"),
        "hot_leader_source": row.get("hot_leader_source", "unavailable"),
    }
    candidate_status = classify_candidate(features, config=config)
    config_payload = {
        "model_version": config.model_version,
        "sector_level": sector_context.sector_level,
        "windows": list(config.windows),
        "alpha_weights": list(config.alpha_weights),
        "structure_weights": dict(config.structure_weights),
        "score_weights": dict(config.score_weights),
    }
    config_hash = build_config_hash(config_payload)
    risk_flags: list[str] = []
    if bool(row.get("data_quality_blocked")):
        risk_flags.append("data_quality_blocked")
    if row.get("hot_leader_source") == "unavailable" and row.get("limit_up_streak") is not None:
        risk_flags.append("hot_leader_unavailable")
    feature_json = {
        "alpha_strength": row.get("alpha_strength"),
        "rr_5": row.get("rr_5"),
        "rr_10": row.get("rr_10"),
        "rr_20": row.get("rr_20"),
        "alpha_persistence": row.get("alpha_persistence"),
        "trend_quality": row.get("trend_quality"),
        "er": row.get("er"),
        "adx": row.get("adx"),
        "ma_stack": row.get("ma_stack"),
        "breakout20": row.get("breakout20"),
        "breakout60": row.get("breakout60"),
        "strong_pullback": row.get("strong_pullback"),
        "trend_structure": row.get("trend_structure"),
        "liquidity": row.get("liquidity"),
        "amount_20d_median": row.get("amount_20d_median"),
        "distance_ma20": row.get("distance_ma20"),
        "volatility_20d": row.get("volatility_20d"),
        "hot_leader_bonus": row.get("hot_leader_bonus"),
        "hot_leader_unavailable": row.get("hot_leader_source") == "unavailable",
        "risk_penalty": row.get("risk_penalty"),
        "mapping_quality": row.get("mapping_quality"),
        "eligibility_unknown": row.get("eligibility_unknown"),
        "sector_playbook": "trend_follow",
        "upstream_sector_snapshot": {
            "as_of_date": sector_context.as_of_date.isoformat(),
            "entity_type": "sector",
            "entity_code": sector_context.sector_name,
            "strategy_type": "sector_opportunity",
            "model_version": sector_context.model_version,
            "config_hash": sector_context.config_hash,
            "snapshot_mode": sector_context.snapshot_mode.value,
        },
    }
    reasons: list[str] = []
    if bool(row.get("data_quality_blocked")):
        reasons.extend(f"missing:{name}" for name in row.get("data_quality_reasons", []))
    if row.get("alpha_strength") is not None and not (isinstance(row["alpha_strength"], float) and np.isnan(row["alpha_strength"])):
        reasons.append(f"alpha_strength={float(row['alpha_strength']):.3f}")
    if row.get("breakout20"):
        reasons.append("breakout20")
    if row.get("breakout60"):
        reasons.append("breakout60")
    if row.get("strong_pullback"):
        reasons.append("strong_pullback")
    if row.get("ma_stack"):
        reasons.append("ma_stack")
    return CandidateSnapshot(
        as_of_date=sector_context.as_of_date,
        entity_type="stock",
        entity_code=str(row["stock_code"]),
        sector_level=sector_context.sector_level,
        sector_name=sector_context.sector_name,
        strategy_type="stock_trend",
        candidate_status=candidate_status,
        candidate_score=None if pd.isna(row.get("candidate_score")) else float(row["candidate_score"]),
        model_version=config.model_version,
        config_hash=config_hash,
        run_id=run_id,
        research_status=ResearchStatus.SHADOW,
        validation_status=ValidationStatus.NOT_EVALUATED,
        execution_status=ExecutionStatus.MANUAL_ONLY,
        snapshot_mode=sector_context.snapshot_mode,
        rank_in_sector=None if pd.isna(row.get("rank_in_sector")) else int(row["rank_in_sector"]),
        feature_json=feature_json,
        reasons_json=tuple(reasons),
        risk_flags_json=tuple(risk_flags),
    )


def persist_trend_candidates(
    store: SnapshotStore,
    snapshots: Iterable[CandidateSnapshot],
) -> list[CandidateSnapshot]:
    """Persist Trend Alpha snapshots under the appropriate snapshot mode rules."""

    persisted: list[CandidateSnapshot] = []
    for snapshot in snapshots:
        if snapshot.snapshot_mode is SnapshotMode.LIVE_SHADOW:
            persisted.append(persist_live_shadow_snapshot(store, snapshot))
        elif snapshot.snapshot_mode is SnapshotMode.DELAYED_SHADOW:
            persisted.append(persist_delayed_shadow_snapshot(store, snapshot))
        elif snapshot.snapshot_mode is SnapshotMode.BACKFILL:
            persisted.append(persist_backfill_snapshot(store, snapshot))
        else:
            raise ValueError("Trend Alpha only supports LIVE_SHADOW or BACKFILL (or DELAYED_SHADOW) modes")
    return persisted


def assemble_features_frame(
    *,
    as_of_date: date,
    sector_level: int,
    sector_name: str,
    universe: list[StockEligibilityRow],
    sector_close_series: Mapping[date, float],
    stock_close_series: Mapping[str, Mapping[date, float]],
    config: TrendAlphaConfig,
    amount_feed: Mapping[str, float] | None = None,
    volume_3d_mean_feed: Mapping[str, float] | None = None,
    volume_20d_mean_feed: Mapping[str, float] | None = None,
    high_feed: Mapping[str, pd.Series] | None = None,
    ohlcv_feed: Mapping[str, Mapping] | None = None,
) -> pd.DataFrame:
    """Compute the per-stock feature frame including structure components.

    Extended variant used by the daily runner so that ``strong_pullback`` and
    ``ma_stack`` can be evaluated with the full OHLCV inputs.
    """

    if not universe:
        return pd.DataFrame()
    sector_close = pd.Series(sector_close_series).sort_index()
    amount_feed = amount_feed or {}
    volume_3d_mean_feed = volume_3d_mean_feed or {}
    volume_20d_mean_feed = volume_20d_mean_feed or {}
    high_feed = high_feed or {}
    ohlcv_feed = ohlcv_feed or {}
    rows: list[dict[str, Any]] = []
    for stock in universe:
        stock_close_dict = stock_close_series.get(stock.stock_code)
        if not stock_close_dict:
            continue
        stock_close = pd.Series(stock_close_dict).sort_index()
        aligned = pd.concat([stock_close.rename("close"), sector_close.rename("sector")], axis=1).dropna()
        if aligned.empty:
            continue
        rr = calc_relative_returns(aligned["close"], aligned["sector"], windows=config.windows)
        er = calc_kama_er(aligned["close"], window=10)
        ohlcv = pd.DataFrame.from_dict(ohlcv_feed.get(stock.stock_code, {}), orient="index").sort_index()
        required_ohlcv = {"high", "low", "close"}
        if not required_ohlcv.issubset(ohlcv.columns):
            ohlcv = pd.DataFrame(index=aligned.index, columns=sorted(required_ohlcv))
        else:
            ohlcv = ohlcv.reindex(aligned.index).dropna(subset=["high", "low", "close"])
        adx = calc_adx14(ohlcv["high"], ohlcv["low"], ohlcv["close"]) if not ohlcv.empty else None
        ma20 = calc_ma(aligned["close"], window=20)
        ma60 = calc_ma(aligned["close"], window=60)
        ma20_slope = calc_ma_slope(ma20, window=5)
        prev_high_20 = calc_prev_high(aligned["close"].rename("close"), window=20)
        prev_high_60 = calc_prev_high(aligned["close"].rename("close"), window=60)
        breakout20, breakout60 = calc_breakout_flags(aligned["close"].rename("high"), prev_high_20, prev_high_60)
        ma_stack = calc_ma_stack(aligned["close"], ma20, ma60 if ma60.notna().any() else ma20, ma20_slope)
        # strong_pullback requires high + volume 3d/20d mean.
        strong_pullback = False
        high_series = high_feed.get(stock.stock_code)
        vol_3d = volume_3d_mean_feed.get(stock.stock_code)
        vol_20d = volume_20d_mean_feed.get(stock.stock_code)
        if high_series is not None and vol_3d is not None and vol_20d is not None:
            vol_3d_series = pd.Series([vol_3d], index=[aligned.index[-1]])
            vol_20d_series = pd.Series([vol_20d], index=[aligned.index[-1]])
            strong_pullback = calc_strong_pullback(
                aligned["close"], high_series, ma20, vol_3d_series, vol_20d_series,
            )
        ret_1d = aligned["close"].pct_change().dropna()
        vol20 = calc_volatility(ret_1d, window=config.liquidity_window)
        distance_ma20 = (
            float(aligned["close"].iloc[-1] / ma20.iloc[-1] - 1.0)
            if ma20.notna().any() else None
        )
        rows.append({
            "stock_code": stock.stock_code,
            "as_of_date": as_of_date,
            "sector_name": sector_name,
            "sector_level": sector_level,
            "rr_5": rr.get("rr_5"),
            "rr_10": rr.get("rr_10"),
            "rr_20": rr.get("rr_20"),
            "er": er,
            "adx": adx,
            "ma_stack": ma_stack,
            "breakout20": breakout20,
            "breakout60": breakout60,
            "strong_pullback": strong_pullback,
            "distance_ma20": distance_ma20,
            "volatility_20d": vol20,
            "amount_20d_median": amount_feed.get(stock.stock_code),
            "limit_up_streak": None,
            "hot_leader_source": "unavailable",
            "mapping_quality": stock.mapping_quality,
            "eligibility_unknown": list(stock.eligibility_unknown),
        })
    return pd.DataFrame(rows)


def score_features_frame(
    frame: pd.DataFrame,
    *,
    config: TrendAlphaConfig,
) -> pd.DataFrame:
    """Score a feature frame and return the final per-row scores.

    The function expects a frame with at least ``as_of_date`` and
    ``sector_name`` columns so sector-local ranks are computed correctly.
    Missing alpha components keep the row in the frame but with NaN score.
    """

    if frame.empty:
        frame = frame.copy()
        frame["candidate_score"] = []
        frame["rank_in_sector"] = []
        return frame
    out = frame.copy()
    # Sector-local relative strength and persistence.
    out = score_alpha_strength(
        out,
        windows=config.windows,
        alpha_weights=config.alpha_weights,
        min_alpha_weight=config.min_alpha_weight,
    )
    # Persistence is computed from the rr_<n>_pct history if provided in
    # ``alpha_persistence_history`` (per-stock list).  The default is NaN.
    if "alpha_persistence_history" in out.columns:
        out["alpha_persistence"] = [
            calc_alpha_persistence(
                {"self": history},
                top_threshold=config.persistence_top_threshold,
                min_dates=config.persistence_min_dates,
            ) if history is not None else None
            for history in out["alpha_persistence_history"]
        ]
    else:
        out["alpha_persistence"] = None
    # ER/ADX trend quality (ADX requires OHLC; here we only have ER).
    if "er" in out.columns:
        out["trend_quality"] = score_trend_quality(out, weights=config.trend_quality_weights)["trend_quality"]
    # Structure score.
    structure_cols = [name for name in config.structure_weights if name in out.columns]
    out = score_trend_structure(out)
    # Liquidity percentile.
    if "amount_20d_median" in out.columns:
        out["liquidity"] = calc_stock_liquidity(out, amount_column="amount_20d_median")
    # Hot-leader bonus + flag.
    bonuses: list[float] = []
    unavailable_flags: list[bool] = []
    for _, row in out.iterrows():
        bonus, unavailable = calc_hot_leader_bonus(
            streak=row.get("limit_up_streak"),
            source=row.get("hot_leader_source", "unavailable"),
            cap=config.hot_leader_cap,
            streak_threshold=config.hot_leader_streak,
        )
        bonuses.append(bonus)
        unavailable_flags.append(unavailable)
    out["hot_leader_bonus"] = bonuses
    # Risk components.
    extension_penalties: list[float | None] = []
    volatility_pcts: list[float | None] = []
    for _, row in out.iterrows():
        extension_penalties.append(calc_extension_penalty(
            row.get("distance_ma20"),
            start=config.extension_start,
            end=config.extension_max,
            max_penalty=config.extension_max_penalty,
        ))
        volatility_pcts.append(row.get("volatility_20d"))  # already computed
    out["_extension_penalty"] = extension_penalties
    out["_volatility_pct"] = volatility_pcts
    if "volatility_20d" in out.columns:
        out["volatility_pct"] = calc_volatility_penalty(out, column="volatility_20d")
    risk_penalties: list[float] = []
    for _, row in out.iterrows():
        risk_penalties.append(total_risk_penalty(
            row.get("_extension_penalty"),
            row.get("volatility_pct"),
        ))
    out["risk_penalty"] = risk_penalties
    # Final score.
    out = score_trend_candidates(out, config=config)
    # Core trend evidence is fail-closed. Keep a row for auditability, but do
    # not classify or rank it as a usable candidate when the required inputs
    # are unavailable.
    required = ("alpha_strength", "persistence", "trend_quality", "liquidity")
    blocked: list[list[str]] = []
    for _, row in out.iterrows():
        missing = [name for name in required if name not in out.columns or pd.isna(row.get(name))]
        blocked.append(missing)
    out["data_quality_blocked"] = [bool(items) for items in blocked]
    out["data_quality_reasons"] = blocked
    out.loc[out["data_quality_blocked"], "candidate_score"] = np.nan
    out.loc[out["data_quality_blocked"], "candidate_status"] = "data_quality_blocked"
    return out

