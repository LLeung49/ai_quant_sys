"""Read-only acceptance check for the 2026-10-19 daily pipeline."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path

from fastapi.testclient import TestClient

from data_ingestion.db_config import execute_query
from data_ingestion.run_daily_market_pipeline import market_date_issue
from morning_conference.sector_rotation2.api.app import create_app


DATE = "2026-10-19"
OUT = Path(__file__).with_name("daily-update-20261019") / "acceptance.json"


def query(sql: str):
    return execute_query(sql, (DATE,))


def main() -> None:
    market = {}
    for table in ("trade_stock_daily_raw", "trade_stock_daily_qfq", "trade_stock_daily_bfq"):
        market[table] = query(
            f"SELECT COUNT(*) AS rows_count, COUNT(DISTINCT stock_code) AS codes, "
            "SUM(open_price IS NULL OR high_price IS NULL OR low_price IS NULL OR close_price IS NULL "
            "OR open_price <= 0 OR high_price <= 0 OR low_price <= 0 OR close_price <= 0) AS bad_ohlc "
            f"FROM {table} WHERE trade_date=%s"
        )[0]
    derived = {}
    for key, table, date_column in (
        ("sector_kline", "trade_sector_daily", "trade_date"),
        ("short_term", "sector_rotation_short_term_daily_snapshot", "as_of_date"),
        ("medium_term", "sector_rotation_sector_daily_snapshot", "as_of_date"),
    ):
        derived[key] = query(
            f"SELECT sector_level, COUNT(*) AS rows_count FROM {table} "
            f"WHERE {date_column}=%s GROUP BY sector_level ORDER BY sector_level"
        )
    for key, table in (
        ("macd_entities", "sector_rotation_macd_entity_daily"),
        ("macd_pool", "sector_rotation_macd_pool"),
    ):
        derived[key] = query(f"SELECT COUNT(*) AS rows_count FROM {table} WHERE as_of_date=%s")[0]
    derived["research"] = query(
        "SELECT strategy_type, snapshot_mode, COUNT(*) AS rows_count "
        "FROM research_candidate_snapshot WHERE as_of_date=%s "
        "GROUP BY strategy_type, snapshot_mode ORDER BY strategy_type, snapshot_mode"
    )
    derived["run_log"] = query(
        "SELECT model_version, status, COUNT(*) AS run_count FROM sector_rotation_run_log "
        "WHERE as_of_date=%s GROUP BY model_version, status ORDER BY model_version, status"
    )

    client = TestClient(create_app())
    api = {}
    for name, path in (
        ("snapshot", "/api/v1/sector-rotation/snapshot"),
        ("short_term", "/api/v1/sector-rotation/short-term/snapshot"),
        ("macd_pool", "/api/v1/sector-rotation/macd-pool"),
        ("research_summary", "/api/v1/sector-rotation/research/today-summary"),
        ("opportunities", "/api/v1/sector-rotation/research/opportunities"),
        ("etf_candidates", "/api/v1/sector-rotation/research/etf-candidates"),
        ("stock_candidates", "/api/v1/sector-rotation/research/stock-candidates"),
    ):
        response = client.get(path, params={"as_of_date": DATE})
        body = response.json()
        api[name] = {
            "status": response.status_code,
            "as_of_date": body.get("as_of_date") if isinstance(body, dict) else None,
            "snapshot_mode": body.get("snapshot_mode") if isinstance(body, dict) else None,
            "rows": next(
                (len(body[key]) for key in ("sectors", "stocks", "opportunities", "candidates") if key in body),
                None,
            ) if isinstance(body, dict) else None,
            "summary": body.get("summary") if name == "research_summary" and isinstance(body, dict) else None,
            "error": body.get("error") if isinstance(body, dict) else None,
        }

    issue = market_date_issue(date.fromisoformat(DATE))
    checks = {
        "market": issue is None and all(
            row["rows_count"] == 6885 and row["codes"] == 6885 and int(row["bad_ohlc"]) == 0
            for row in market.values()
        ),
        "sector_kline": {row["sector_level"]: row["rows_count"] for row in derived["sector_kline"]} == {1: 30, 2: 131},
        "short_term": {row["sector_level"]: row["rows_count"] for row in derived["short_term"]} == {1: 30, 2: 130},
        "medium_term": {row["sector_level"]: row["rows_count"] for row in derived["medium_term"]} == {1: 30, 2: 130},
        "macd": derived["macd_entities"]["rows_count"] > 0 and derived["macd_pool"]["rows_count"] > 0,
        "research": {row["strategy_type"] for row in derived["research"]} >= {"sector_opportunity", "etf_core", "stock_trend"},
        "api": all(row["status"] == 200 and str(row["as_of_date"]) == DATE for row in api.values()),
    }
    result = {"date": DATE, "market": market, "market_issue": issue, "derived": derived, "api": api, "checks": checks}
    OUT.write_text(json.dumps(result, ensure_ascii=False, default=str, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, default=str, indent=2))
    if not all(checks.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
