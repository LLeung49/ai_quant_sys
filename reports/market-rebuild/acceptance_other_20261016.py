"""Read-only acceptance of 2026-10-16 features independent of stock trend."""

import json

from fastapi.testclient import TestClient

from data_ingestion.db_config import execute_query
from morning_conference.sector_rotation2.api.app import create_app


DAY = "2026-10-16"
client = TestClient(create_app())
result = {"date": DAY, "market": {}, "derived": {}, "api": {}, "checks": {}}


def get(name, path, params=None, list_key=None):
    response = client.get(path, params=params or {})
    body = response.json()
    result["api"][name] = {
        "status": response.status_code,
        "date": body.get("as_of_date") if isinstance(body, dict) else None,
        "rows": len(body.get(list_key, [])) if list_key and isinstance(body, dict) else None,
        "error": body.get("error") if isinstance(body, dict) else None,
    }
    return body


for table in ("trade_stock_daily_raw", "trade_stock_daily_qfq", "trade_stock_daily_bfq"):
    result["market"][table] = execute_query(
        f"""SELECT COUNT(*) AS rows_count, COUNT(DISTINCT stock_code) AS codes,
                   SUM(open_price IS NULL OR high_price IS NULL OR low_price IS NULL OR close_price IS NULL
                       OR open_price <= 0 OR high_price <= 0 OR low_price <= 0 OR close_price <= 0
                       OR high_price < GREATEST(open_price, close_price, low_price)
                       OR low_price > LEAST(open_price, close_price, high_price)
                       OR volume < 0 OR amount < 0) AS invalid_rows
              FROM {table} WHERE trade_date = %s""",
        (DAY,),
    )[0]

result["market"]["missing_projections"] = execute_query(
    """SELECT SUM(q.stock_code IS NULL) AS missing_qfq,
              SUM(b.stock_code IS NULL) AS missing_bfq
         FROM trade_stock_daily_raw r
         LEFT JOIN trade_stock_daily_qfq q
           ON q.stock_code = r.stock_code AND q.trade_date = r.trade_date
         LEFT JOIN trade_stock_daily_bfq b
           ON b.stock_code = r.stock_code AND b.trade_date = r.trade_date
        WHERE r.trade_date = %s""",
    (DAY,),
)[0]

for name, table, date_column in (
    ("sector_kline", "trade_sector_daily", "trade_date"),
    ("short_term", "sector_rotation_short_term_daily_snapshot", "as_of_date"),
    ("medium_term", "sector_rotation_sector_daily_snapshot", "as_of_date"),
):
    result["derived"][name] = execute_query(
        f"""SELECT sector_level, COUNT(*) AS rows_count FROM {table}
              WHERE {date_column} = %s GROUP BY sector_level ORDER BY sector_level""",
        (DAY,),
    )
result["derived"]["research"] = execute_query(
    """SELECT strategy_type, COUNT(*) AS rows_count
         FROM research_candidate_snapshot
        WHERE as_of_date = %s AND snapshot_mode = 'backfill'
          AND strategy_type IN ('etf_core', 'sector_opportunity')
        GROUP BY strategy_type ORDER BY strategy_type""",
    (DAY,),
)
result["derived"]["macd"] = execute_query(
    "SELECT COUNT(*) AS rows_count FROM sector_rotation_macd_pool WHERE as_of_date = %s",
    (DAY,),
)[0]

dates = get("available_dates", "/api/v1/sector-rotation/available-dates", list_key="dates")
calendar = get("calendar", "/api/v1/sector-rotation/calendar-availability", {"start_date": "2026-10-13", "end_date": DAY})
snapshot = get("snapshot", "/api/v1/sector-rotation/snapshot", {"as_of_date": DAY}, "sectors")
short = get("short_term", "/api/v1/sector-rotation/short-term/snapshot", {"as_of_date": DAY}, "sectors")
get("short_leaders", "/api/v1/sector-rotation/short-term/leaders", {"as_of_date": DAY}, "leaders")
get("macd_pool", "/api/v1/sector-rotation/macd-pool", {"as_of_date": DAY}, "stocks")
get("opportunities", "/api/v1/sector-rotation/research/opportunities", {"as_of_date": DAY, "snapshot_mode": "backfill"}, "opportunities")
get("etf_candidates", "/api/v1/sector-rotation/research/etf-candidates", {"as_of_date": DAY, "snapshot_mode": "backfill"}, "candidates")

sector = snapshot["sectors"][0]["sector_name"]
result["sample_sector"] = sector
get("sector_kline", "/api/v1/sector-rotation/sector-kline", {"sector_name": sector, "level": 2, "end_date": DAY}, "bars")
get("sector_history", "/api/v1/sector-rotation/sector-history", {"sector_name": sector, "start_date": "2026-10-13", "end_date": DAY}, "points")
get("short_history", "/api/v1/sector-rotation/short-term/history", {"sector_names": sector, "start_date": "2026-10-13", "end_date": DAY}, "points")
get("replay", "/api/v1/sector-rotation/replay", {"start_date": "2026-10-13", "end_date": DAY}, "points")

result["checks"] = {
    "market": all(row["rows_count"] == 6889 and row["codes"] == 6889 and int(row["invalid_rows"]) == 0 for key, row in result["market"].items() if key != "missing_projections"),
    "projection_coverage": all(int(value) == 0 for value in result["market"]["missing_projections"].values()),
    "sector_kline": {row["sector_level"]: row["rows_count"] for row in result["derived"]["sector_kline"]} == {1: 30, 2: 131},
    "short_term": {row["sector_level"]: row["rows_count"] for row in result["derived"]["short_term"]} == {1: 30, 2: 130},
    "medium_term": {row["sector_level"]: row["rows_count"] for row in result["derived"]["medium_term"]} == {1: 30, 2: 130},
    "research": {row["strategy_type"]: row["rows_count"] for row in result["derived"]["research"]} == {"etf_core": 390, "sector_opportunity": 130},
    "macd": result["derived"]["macd"]["rows_count"] == 54,
    "api_status": all(row["status"] == 200 for row in result["api"].values()),
    "api_content": all(result["api"][name]["rows"] > 0 for name in ("snapshot", "short_term", "short_leaders", "macd_pool", "opportunities", "etf_candidates", "sector_kline", "sector_history", "short_history", "replay")),
    "date_available": DAY in dates.get("dates", []) and DAY in calendar.get("snapshot_dates", []) and DAY in calendar.get("trade_dates", []),
    "date_identity": snapshot.get("as_of_date") == DAY and short.get("as_of_date") == DAY,
}
print(json.dumps(result, ensure_ascii=False, default=str, indent=2))
if not all(result["checks"].values()):
    raise SystemExit(1)
