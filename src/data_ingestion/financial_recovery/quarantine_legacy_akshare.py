"""Preserve and isolate incomplete AKShare rows predating the strict collector."""

from datetime import date
import json

from data_ingestion.audit_financial_pit import quarantine_rows
from data_ingestion.db_config import execute_query, get_connection


def quarantine() -> dict:
    rows = execute_query(
        "SELECT id,stock_code FROM trade_stock_financial_raw_pit "
        "WHERE data_source='akshare' AND first_seen_at<'2026-10-20' "
        "AND (revenue IS NULL OR net_profit IS NULL OR total_assets IS NULL "
        "OR total_assets<=0 OR total_equity IS NULL OR operating_cash_flow IS NULL)"
    )
    findings = [{**row, "reasons": ["legacy_incomplete_core"]} for row in rows]
    connection = get_connection()
    try:
        count = quarantine_rows(connection, findings, batch_id="legacy-akshare-core-20261020")
    finally:
        connection.close()
    return {"as_of_date": date(2026, 10, 20).isoformat(), "quarantined": count}


if __name__ == "__main__":
    print(json.dumps(quarantine()))
