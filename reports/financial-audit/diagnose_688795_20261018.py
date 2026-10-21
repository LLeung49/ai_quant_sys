"""Collect read-only evidence for the unresolved 688795.SH financial row."""

from __future__ import annotations

from datetime import date
import json

import akshare as ak

from data_ingestion.akshare_financial_provider import AKShareFinancialProvider
from data_ingestion.db_config import execute_query


def _dates(frame):
    return sorted({str(value)[:10] for value in frame.get("REPORT_DATE", [])})


def main() -> None:
    symbol = "SH688795"
    frames = {
        "balance": ak.stock_balance_sheet_by_report_em(symbol=symbol),
        "income": ak.stock_profit_sheet_by_report_em(symbol=symbol),
        "cash": ak.stock_cash_flow_sheet_by_report_em(symbol=symbol),
    }
    provider_rows = AKShareFinancialProvider(
        fetch_balance=lambda _symbol: frames["balance"],
        fetch_income=lambda _symbol: frames["income"],
        fetch_cash=lambda _symbol: frames["cash"],
    ).fetch("688795.SH", as_of_date=date(2026, 10, 16))
    db_wide = execute_query(
        """SELECT report_date, data_source, revenue, net_profit, total_assets,
                  total_equity, operating_cashflow
             FROM trade_stock_financial
            WHERE stock_code=%s ORDER BY report_date""",
        ("688795.SH",),
    )
    db_pit = execute_query(
        """SELECT report_date, announcement_date, data_source, pit_status,
                  revenue, net_profit, total_assets, total_equity,
                  operating_cash_flow
             FROM trade_stock_financial_raw_pit
            WHERE stock_code=%s ORDER BY report_date, announcement_date""",
        ("688795.SH",),
    )
    security_rows = execute_query(
        """SELECT stock_code, MIN(trade_date) AS first_market_date,
                  MAX(trade_date) AS last_market_date
             FROM trade_stock_daily_raw
            WHERE stock_code=%s
            GROUP BY stock_code""",
        ("688795.SH",),
    )
    payload = {
        "raw_dates": {name: _dates(frame) for name, frame in frames.items()},
        "raw_shapes": {name: list(frame.shape) for name, frame in frames.items()},
        "provider_dates": [str(row["report_date"]) for row in provider_rows],
        "db_wide": db_wide,
        "db_pit": db_pit,
        "security": security_rows,
        "capital_coverage": execute_query(
            """SELECT data_source, COUNT(*) AS rows_count,
                      COUNT(DISTINCT stock_code) AS code_count,
                      MIN(report_date) AS first_date, MAX(report_date) AS last_date
                 FROM trade_stock_capital_pit
                GROUP BY data_source ORDER BY data_source"""
        ),
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2, default=str))


if __name__ == "__main__":
    main()
