"""Read-only API for the SHADOW research cockpit."""

from __future__ import annotations

import json
from datetime import date
from typing import Any

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field

from data_ingestion.db_config import execute_query
from ..research.watchlist import service as watchlist_service
from ..research.human_decision import service as decision_service


research_router = APIRouter(prefix="/api/v1/sector-rotation/research", tags=["Research cockpit"])


class WatchlistRequest(BaseModel):
    user_id: str = Field(default="default", min_length=1, max_length=64)
    snapshot_id: int = Field(gt=0)
    note: str | None = Field(default=None, max_length=2000)
    watch_status: str = Field(default="watch", max_length=32)


class DecisionRequest(BaseModel):
    user_id: str = Field(default="default", min_length=1, max_length=64)
    snapshot_id: int = Field(gt=0)
    decision: str = Field(max_length=16)
    note: str | None = Field(default=None, max_length=2000)


@research_router.get("/latest-date")
def latest_date(
    level: int = Query(2, ge=1, le=2),
    snapshot_mode: str | None = Query(None, pattern="^(live_shadow|delayed_shadow|backfill)$"),
) -> dict[str, Any]:
    if snapshot_mode:
        rows = execute_query(
            "SELECT MAX(as_of_date) AS as_of_date, %s AS snapshot_mode "
            "FROM research_candidate_snapshot WHERE sector_level=%s AND snapshot_mode=%s",
            (snapshot_mode, level, snapshot_mode),
        )
        if rows and rows[0].get("as_of_date"):
            return {"as_of_date": rows[0].get("as_of_date"), "sector_level": level, "snapshot_mode": snapshot_mode}
        return {"as_of_date": None, "sector_level": level, "snapshot_mode": snapshot_mode}

    # Auto mode: find the absolute latest date across all modes, preferring live_shadow if dates match
    rows = execute_query(
        """SELECT as_of_date, snapshot_mode
             FROM research_candidate_snapshot
            WHERE sector_level=%s
            ORDER BY as_of_date DESC, (CASE WHEN snapshot_mode='live_shadow' THEN 1 ELSE 2 END) ASC
            LIMIT 1""",
        (level,),
    )
    if rows and rows[0].get("as_of_date"):
        return {"as_of_date": rows[0].get("as_of_date"), "sector_level": level, "snapshot_mode": rows[0].get("snapshot_mode")}
    return {"as_of_date": None, "sector_level": level, "snapshot_mode": snapshot_mode or "live_shadow"}


def _parse_date(value: str) -> str:
    try:
        return date.fromisoformat(value).isoformat()
    except ValueError as exc:
        raise HTTPException(422, detail={"code": "INVALID_DATE", "message": "日期必须使用 YYYY-MM-DD 格式"}) from exc


def _decode_json(row: dict[str, Any]) -> dict[str, Any]:
    row["entity_name"] = str(row.get("entity_name") or row.get("entity_code") or "")
    for name in ("feature_json", "reasons_json", "risk_flags_json"):
        if isinstance(row.get(name), str):
            try:
                row[name] = json.loads(row[name])
            except ValueError:
                row[name] = {} if name == "feature_json" else []
    row["is_data_quality_blocked"] = (
        row.get("candidate_status") == "data_quality_blocked"
        or "data_quality_blocked" in (row.get("risk_flags_json") or [])
    )
    if row.get("snapshot_mode") == "delayed_shadow" and row.get("daily_bar_entry_date") is None:
        row["daily_bar_entry_reason"] = "trading_calendar_unavailable"
    else:
        row["daily_bar_entry_reason"] = None
    return row


def _load_candidates(
    as_of_date: str,
    level: int,
    snapshot_mode: str | None,
    strategies: tuple[str, ...],
    sector_name: str | None = None,
) -> list[dict[str, Any]]:
    placeholders = ", ".join(["%s"] * len(strategies))
    sector_filter = " AND sector_name=%s" if sector_name else ""

    # A requested mode is an isolation boundary. Legacy callers default to
    # live snapshots, but no request may silently fall back across modes.
    mode = snapshot_mode or "live_shadow"
    sql = f"""
            SELECT id, as_of_date, entity_type, entity_code,
                   COALESCE(NULLIF(stock_status.stock_name, ''), entity_code) AS entity_name,
                   sector_level, sector_name,
                   strategy_type, candidate_status, candidate_score, rank_in_sector,
                   research_status, validation_status, execution_status, model_version,
                   config_hash, snapshot_mode, feature_json, reasons_json, risk_flags_json,
                   data_available_at, run_at, execution_eligible_at, availability_basis,
                   CASE
                     WHEN current_snapshot.snapshot_mode = 'delayed_shadow' AND current_snapshot.run_at IS NOT NULL THEN (
                       SELECT MIN(calendar_dates.trade_date)
                         FROM trade_sector_daily AS calendar_dates
                        WHERE calendar_dates.sector_level = current_snapshot.sector_level
                          AND calendar_dates.trade_date >= CASE
                            WHEN TIME(current_snapshot.run_at) < '09:30:00' THEN DATE(current_snapshot.run_at)
                            ELSE DATE_ADD(DATE(current_snapshot.run_at), INTERVAL 1 DAY)
                          END
                     )
                   END AS daily_bar_entry_date,
                   created_at
              FROM (
                  SELECT s.*, ROW_NUMBER() OVER (
                      PARTITION BY entity_type, entity_code, strategy_type
                      ORDER BY created_at DESC, id DESC
                  ) AS current_rank
                  FROM research_candidate_snapshot AS s
                 WHERE as_of_date=%s AND sector_level=%s AND snapshot_mode=%s
                   AND strategy_type IN ({placeholders}) {sector_filter}
              ) AS current_snapshot
              LEFT JOIN trade_stock_status AS stock_status
                ON stock_status.stock_code=current_snapshot.entity_code
             WHERE current_rank=1
             ORDER BY sector_name, strategy_type, rank_in_sector, candidate_score DESC, entity_code
    """
    params: tuple[object, ...] = (as_of_date, level, mode, *strategies)
    if sector_name:
        params += (sector_name,)
    return [_decode_json(dict(row)) for row in execute_query(sql, params)]


@research_router.get("/opportunities")
def opportunities(
    as_of_date: str = Query(...), level: int = Query(2, ge=1, le=2),
    snapshot_mode: str | None = Query(None, pattern="^(live_shadow|delayed_shadow|backfill)$"), sector_name: str | None = Query(None),
) -> dict[str, Any]:
    target = _parse_date(as_of_date)
    rows = _load_candidates(target, level, snapshot_mode, ("sector_opportunity",), sector_name)
    mode = rows[0]["snapshot_mode"] if rows else (snapshot_mode or "live_shadow")
    return {"as_of_date": target, "sector_level": level, "snapshot_mode": mode, "research_status": "shadow", "opportunities": rows}


@research_router.get("/etf-candidates")
def etf_candidates(
    as_of_date: str = Query(...), level: int = Query(2, ge=1, le=2),
    snapshot_mode: str | None = Query(None, pattern="^(live_shadow|delayed_shadow|backfill)$"), sector_name: str | None = Query(None),
) -> dict[str, Any]:
    target = _parse_date(as_of_date)
    rows = _load_candidates(target, level, snapshot_mode, ("etf_core",), sector_name)
    mode = rows[0]["snapshot_mode"] if rows else (snapshot_mode or "live_shadow")
    return {"as_of_date": target, "sector_level": level, "snapshot_mode": mode, "candidates": rows}


@research_router.get("/stock-candidates")
def stock_candidates(
    as_of_date: str = Query(...), level: int = Query(2, ge=1, le=2),
    snapshot_mode: str | None = Query(None, pattern="^(live_shadow|delayed_shadow|backfill)$"), sector_name: str | None = Query(None),
    strategy_type: str | None = Query(None, pattern="^(stock_trend|stock_repair)$"),
) -> dict[str, Any]:
    target = _parse_date(as_of_date)
    strategies = (strategy_type,) if strategy_type else ("stock_trend", "stock_repair")
    rows = _load_candidates(target, level, snapshot_mode, strategies, sector_name)
    mode = rows[0]["snapshot_mode"] if rows else (snapshot_mode or "live_shadow")
    return {"as_of_date": target, "sector_level": level, "snapshot_mode": mode, "candidates": rows}


@research_router.get("/today-summary")
def today_summary(
    as_of_date: str = Query(...), level: int = Query(2, ge=1, le=2),
    snapshot_mode: str | None = Query(None, pattern="^(live_shadow|delayed_shadow|backfill)$"),
) -> dict[str, Any]:
    target = _parse_date(as_of_date)
    rows = _load_candidates(target, level, snapshot_mode, ("sector_opportunity", "etf_core", "stock_trend", "stock_repair"))
    grouped: dict[str, int] = {"core_etf_ready": 0, "trend_candidates": 0, "repair_candidates": 0, "reduce_or_avoid": 0, "data_quality_blocked": 0}
    for row in rows:
        if row["strategy_type"] == "etf_core" and row["candidate_status"] == "ready": grouped["core_etf_ready"] += 1
        elif row["strategy_type"] == "stock_trend": grouped["trend_candidates"] += 1
        elif row["strategy_type"] == "stock_repair": grouped["repair_candidates"] += 1
        if row["candidate_status"] in {"avoid", "risk_reduce"}: grouped["reduce_or_avoid"] += 1
        if row.get("is_data_quality_blocked"):
            grouped["data_quality_blocked"] += 1
    versions = sorted({(str(row.get("strategy_type")), str(row.get("model_version")), str(row.get("config_hash"))) for row in rows})
    mode = rows[0]["snapshot_mode"] if rows else (snapshot_mode or "live_shadow")
    return {"as_of_date": target, "sector_level": level, "snapshot_mode": mode, "research_status": "shadow", "summary": grouped, "source_versions": [{"strategy_type": s, "model_version": v, "config_hash": h} for s, v, h in versions]}


@research_router.get("/evaluation")
def evaluation(
    signal_family: str = Query(..., min_length=1, max_length=64),
    horizon: int = Query(..., ge=1, le=1000),
    label_type: str = Query(..., pattern="^(close_to_close|tradable)$"),
    sampling_mode: str = Query("snapshot", pattern="^(snapshot|event)$"),
    sample_scope: str = Query("full", pattern="^(full|train|validation|test)$"),
    snapshot_mode: str = Query("backfill", pattern="^(live_shadow|delayed_shadow|backfill)$"),
) -> dict[str, Any]:
    """Read-only aggregate evaluation result; modes are never combined."""
    rows = execute_query(
        """SELECT e.*, m.metric_name, m.metric_value, m.sample_count, m.ci_low, m.ci_high
           FROM sector_rotation_research_evaluation e
           LEFT JOIN sector_rotation_research_evaluation_metric m ON m.evaluation_id=e.id
          WHERE e.signal_family=%s AND e.horizon=%s AND e.label_type=%s
            AND e.event_sampling_mode=%s AND e.sample_scope=%s AND e.snapshot_mode=%s
          ORDER BY e.created_at DESC, m.metric_name""",
        (signal_family, horizon, label_type, sampling_mode, sample_scope, snapshot_mode),
    )
    if not rows:
        raise HTTPException(404, detail={"code": "RESEARCH_EVALUATION_NOT_FOUND", "message": "evaluation result not found"})
    first = dict(rows[0])
    metrics = [{key: row.get(key) for key in ("metric_name", "metric_value", "sample_count", "ci_low", "ci_high")} for row in rows if row.get("metric_name")]
    for key in ("metric_name", "metric_value", "sample_count", "ci_low", "ci_high"):
        first.pop(key, None)
    first["metrics"] = metrics
    return first


@research_router.get("/watchlist")
def get_watchlist(user_id: str = Query("default", min_length=1, max_length=64)) -> dict[str, Any]:
    return {"user_id": user_id, "items": watchlist_service.list_items(user_id=user_id)}


@research_router.post("/watchlist")
def add_watchlist(request: WatchlistRequest) -> dict[str, Any]:
    try:
        return watchlist_service.add(**request.model_dump())
    except LookupError as exc:
        raise HTTPException(404, detail={"code": "SNAPSHOT_NOT_FOUND", "message": str(exc)}) from exc
    except ValueError as exc:
        raise HTTPException(422, detail={"code": "INVALID_WATCHLIST", "message": str(exc)}) from exc


@research_router.patch("/watchlist/{snapshot_id}")
def update_watchlist(snapshot_id: int, request: WatchlistRequest) -> dict[str, Any]:
    try:
        return watchlist_service.update(user_id=request.user_id, snapshot_id=snapshot_id, note=request.note, watch_status=request.watch_status)
    except ValueError as exc:
        raise HTTPException(422, detail={"code": "INVALID_WATCHLIST", "message": str(exc)}) from exc


@research_router.delete("/watchlist/{snapshot_id}", status_code=204)
def delete_watchlist(snapshot_id: int, user_id: str = Query("default", min_length=1, max_length=64)) -> None:
    watchlist_service.remove(user_id=user_id, snapshot_id=snapshot_id)


@research_router.get("/decisions")
def get_decisions(user_id: str = Query("default", min_length=1, max_length=64), snapshot_id: int | None = Query(None, gt=0)) -> dict[str, Any]:
    return {"user_id": user_id, "decisions": decision_service.list_items(user_id=user_id, snapshot_id=snapshot_id)}


@research_router.post("/decisions")
def add_decision(request: DecisionRequest) -> dict[str, Any]:
    try:
        return decision_service.append(**request.model_dump())
    except LookupError as exc:
        raise HTTPException(404, detail={"code": "SNAPSHOT_NOT_FOUND", "message": str(exc)}) from exc
    except ValueError as exc:
        raise HTTPException(422, detail={"code": "INVALID_DECISION", "message": str(exc)}) from exc
