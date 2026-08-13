from datetime import date
from fastapi import APIRouter, Query
from data_ingestion.db_config import execute_query
from .router import _invalid_parameter, _not_found
from .schemas import normalize_json_numbers
from ..macd_pool_store import load_macd_pool
macd_router = APIRouter(prefix="/api/v1/sector-rotation", tags=["MACD pool"])
@macd_router.get("/macd-pool")
def get_macd_pool(as_of_date: str | None = Query(None), level: int = Query(2, ge=1, le=2), model_version: str = Query("v1")):
    if not as_of_date:
        latest = execute_query("SELECT MAX(as_of_date) AS latest FROM sector_rotation_macd_pool WHERE sector_level=%s AND model_version=%s", (level, model_version))
        as_of_date = str(latest[0]["latest"]) if latest and latest[0].get("latest") else ""
    if not as_of_date:
        raise _not_found("MACD_POOL_NOT_FOUND", "No MACD pool data")
    try:
        date.fromisoformat(as_of_date)
    except ValueError as exc:
        raise _invalid_parameter("Date must use YYYY-MM-DD") from exc
    rows = normalize_json_numbers(load_macd_pool(as_of_date, level, model_version))
    if not rows:
        raise _not_found("MACD_POOL_NOT_FOUND", "No MACD pool data for date")
    groups = {}
    for row in rows:
        groups.setdefault(row.get("entity_type", "unknown"), []).append(row)
    return {"as_of_date": as_of_date, "sector_level": level, "model_version": model_version, "meta": {"run_status": "succeeded", "field_version": "v1", "hit_count": len(rows)}, "groups": groups, "stocks": rows}

@macd_router.get("/macd-pool-dates")
def get_macd_pool_dates(level: int = Query(2, ge=1, le=2), model_version: str = Query("v1")):
    rows = execute_query("SELECT DISTINCT as_of_date FROM sector_rotation_macd_pool WHERE sector_level=%s AND model_version=%s ORDER BY as_of_date DESC", (level, model_version))
    return {"dates": [str(row["as_of_date"]) for row in rows]}

@macd_router.get("/macd-pool-trajectory")
def get_macd_pool_trajectory(as_of_date: str, entity_type: str = Query(..., pattern="^(etf|sector_l1|sector_l2)$"), stock_code: str = Query(..., min_length=1), level: int = Query(2, ge=1, le=2), model_version: str = Query("v1"), days: int = Query(5, ge=2, le=5)):
    try:
        date.fromisoformat(as_of_date)
    except ValueError as exc:
        raise _invalid_parameter("Date must use YYYY-MM-DD") from exc
    dates = execute_query("SELECT DISTINCT as_of_date FROM sector_rotation_macd_entity_daily WHERE sector_level=%s AND model_version=%s AND entity_type=%s AND stock_code=%s AND as_of_date<=%s ORDER BY as_of_date DESC LIMIT %s", (level, model_version, entity_type, stock_code, as_of_date, days))
    selected = [str(row["as_of_date"]) for row in reversed(dates)]
    placeholders = ",".join(["%s"] * len(selected))
    rows = execute_query(f"SELECT as_of_date, entity_type, stock_code, stock_name, kama_efficiency, adx_14 FROM sector_rotation_macd_entity_daily WHERE sector_level=%s AND model_version=%s AND entity_type=%s AND stock_code=%s AND as_of_date IN ({placeholders}) ORDER BY as_of_date", (level, model_version, entity_type, stock_code, *selected)) if selected else []
    points = [{"as_of_date": str(row["as_of_date"]), "er": row.get("kama_efficiency"), "adx": row.get("adx_14")} for row in rows]
    return {"as_of_date": as_of_date, "dates": selected, "trajectory": {"entity_type": entity_type, "stock_code": stock_code, "stock_name": rows[-1].get("stock_name") if rows else None, "points": points}}
