"""Run the daily MACD pool scan for ETF and申万 sector entities."""
from __future__ import annotations

import argparse
from uuid import uuid4

from data_ingestion_qmt.db_config import execute_query

from .macd_pool import run_macd_daily_metrics
from .macd_pool_schema import ensure_macd_entity_daily_table, ensure_macd_pool_table
from .macd_pool_store import persist_macd_entity_daily, persist_macd_pool, sync_etf_status_names


def latest_trade_date() -> str:
    rows = execute_query("SELECT MAX(trade_date) AS latest FROM trade_stock_daily_qfq")
    if not rows or not rows[0].get("latest"):
        raise RuntimeError("trade_stock_daily_qfq has no trade date")
    return str(rows[0]["latest"])


def ensure_trade_date(as_of_date: str) -> None:
    rows = execute_query(
        "SELECT 1 AS present FROM trade_stock_daily_qfq WHERE trade_date=%s LIMIT 1",
        (as_of_date,),
    )
    if not rows:
        raise ValueError(f"{as_of_date} is not a trading date in trade_stock_daily_qfq")


def run(as_of_date: str | None = None, model_version: str = "v1", level: int = 2) -> dict[str, object]:
    date = as_of_date or latest_trade_date()
    ensure_trade_date(date)
    ensure_macd_pool_table()
    ensure_macd_entity_daily_table()
    run_id = str(uuid4())
    metrics = run_macd_daily_metrics(date)
    etf_codes = metrics.loc[metrics["entity_type"] == "etf", "stock_code"].tolist() if not metrics.empty else []
    etf_names_synced = sync_etf_status_names(etf_codes)
    if etf_codes:
        name_rows = execute_query(
            "SELECT stock_code, stock_name FROM trade_stock_status WHERE stock_code IN (" + ",".join(["%s"] * len(etf_codes)) + ")",
            tuple(etf_codes),
        )
        name_map = {row["stock_code"]: row["stock_name"] for row in name_rows}
        metrics.loc[metrics["entity_type"] == "etf", "stock_name"] = metrics.loc[metrics["entity_type"] == "etf", "stock_code"].map(name_map)
    frame = metrics[metrics["is_triggered"] == 1].drop(columns=["is_triggered"]) if not metrics.empty else metrics
    persisted_metrics = persist_macd_entity_daily(metrics, date, level, model_version, run_id)
    persisted = persist_macd_pool(frame, date, level, model_version, run_id)
    counts = frame["entity_type"].value_counts().to_dict() if not frame.empty else {}
    return {"as_of_date": date, "scanned_count": int(len(metrics)), "persisted_count": int(persisted), "metrics_persisted_count": int(persisted_metrics), "etf_names_synced": int(etf_names_synced), "counts": counts}


def main() -> None:
    parser = argparse.ArgumentParser(description="Scan and persist the daily MACD pool")
    parser.add_argument("--as-of-date", help="YYYY-MM-DD; defaults to latest trade date")
    parser.add_argument("--model-version", default="v1")
    parser.add_argument("--level", type=int, choices=(1, 2), default=2)
    args = parser.parse_args()
    print(run(args.as_of_date, args.model_version, args.level))


if __name__ == "__main__":
    main()

