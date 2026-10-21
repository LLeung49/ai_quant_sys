"""Read-only database and API smoke checks for the 2026-10-16 recovery."""

import json

from fastapi.testclient import TestClient

from data_ingestion.db_config import execute_query
from morning_conference.sector_rotation2.api.app import create_app


DATE = "2026-10-16"


def main() -> None:
    result = {"date": DATE, "market": {}, "derived": {}, "api": {}}
    for table in (
        "trade_stock_daily_raw",
        "trade_stock_daily_qfq",
        "trade_stock_daily_bfq",
    ):
        result["market"][table] = execute_query(
            f"""SELECT COUNT(*) AS rows_count, COUNT(DISTINCT stock_code) AS codes,
                SUM(open_price IS NULL OR high_price IS NULL OR low_price IS NULL OR
                    close_price IS NULL OR open_price <= 0 OR high_price <= 0 OR
                    low_price <= 0 OR close_price <= 0) AS bad_ohlc
                FROM {table} WHERE trade_date = %s""",
            (DATE,),
        )[0]
    for table, date_column in (
        ("trade_sector_daily", "trade_date"),
        ("sector_rotation_short_term_daily_snapshot", "as_of_date"),
        ("sector_rotation_macd_entity_daily", "as_of_date"),
        ("sector_rotation_macd_pool", "as_of_date"),
    ):
        result["derived"][table] = execute_query(
            f"SELECT COUNT(*) AS rows_count FROM {table} WHERE {date_column} = %s",
            (DATE,),
        )[0]
    result["derived"]["research_candidate_snapshot"] = execute_query(
        """SELECT strategy_type, COUNT(*) AS rows_count
           FROM research_candidate_snapshot WHERE as_of_date = %s
           GROUP BY strategy_type ORDER BY strategy_type""",
        (DATE,),
    )

    client = TestClient(create_app())
    endpoints = (
        ("available_dates", "/api/v1/sector-rotation/available-dates", {}),
        ("snapshot", "/api/v1/sector-rotation/snapshot", {"as_of_date": DATE}),
        ("short_term", "/api/v1/sector-rotation/short-term/snapshot", {"as_of_date": DATE}),
        ("macd_pool", "/api/v1/sector-rotation/macd-pool", {"as_of_date": DATE}),
        ("research_latest", "/api/v1/sector-rotation/research/latest-date", {}),
        ("research_summary", "/api/v1/sector-rotation/research/today-summary", {"as_of_date": DATE, "snapshot_mode": "backfill"}),
        ("opportunities", "/api/v1/sector-rotation/research/opportunities", {"as_of_date": DATE, "snapshot_mode": "backfill"}),
        ("etf_candidates", "/api/v1/sector-rotation/research/etf-candidates", {"as_of_date": DATE, "snapshot_mode": "backfill"}),
        ("stock_candidates", "/api/v1/sector-rotation/research/stock-candidates", {"as_of_date": DATE, "snapshot_mode": "backfill"}),
    )
    for name, path, params in endpoints:
        response = client.get(path, params=params)
        body = response.json()
        result["api"][name] = {
            "status": response.status_code,
            "keys": sorted(body) if isinstance(body, dict) else None,
            "as_of_date": body.get("as_of_date") if isinstance(body, dict) else None,
            "snapshot_mode": body.get("snapshot_mode") if isinstance(body, dict) else None,
            "row_count": next((len(body[key]) for key in ("sectors", "stocks", "opportunities", "candidates", "dates") if key in body), None) if isinstance(body, dict) else None,
            "summary": body.get("summary") if name == "research_summary" else None,
            "error": body.get("error") if isinstance(body, dict) else None,
        }
    expected_api_rows = {
        "snapshot": 130,
        "short_term": 130,
        "macd_pool": 54,
        "opportunities": 130,
        "etf_candidates": 161,
        "stock_candidates": 1011,
    }
    result["checks"] = {
        "market": all(row["rows_count"] == 6889 and row["codes"] == 6889 and int(row["bad_ohlc"]) == 0 for row in result["market"].values()),
        "api_status": all(row["status"] == 200 for row in result["api"].values()),
        "api_rows": all(result["api"][key]["row_count"] == count for key, count in expected_api_rows.items()),
        "research_latest": str(result["api"]["research_latest"]["as_of_date"]) == DATE,
        "research_summary": result["api"]["research_summary"]["summary"]["trend_candidates"] == 1011,
        "research_quality": result["api"]["research_summary"]["summary"]["data_quality_blocked"] == 0,
    }
    print(json.dumps(result, ensure_ascii=False, default=str, indent=2))
    if not all(result["checks"].values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
