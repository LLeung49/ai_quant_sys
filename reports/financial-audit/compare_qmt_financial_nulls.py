import importlib
import json
from datetime import date, datetime
from decimal import Decimal
from pathlib import Path

from data_ingestion.db_config import execute_query
from data_ingestion_qmt.qmt_data_gateway import QMTDataGateway


def default(value):
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, Decimal):
        return str(value)
    return str(value)


suspects = execute_query(
    """SELECT stock_code, report_date, revenue, net_profit, total_assets,
              total_equity, operating_cashflow
       FROM trade_stock_financial
       WHERE COALESCE(revenue, 0) = 0
         AND COALESCE(net_profit, 0) = 0
         AND COALESCE(total_assets, 0) = 0
         AND COALESCE(total_equity, 0) = 0
         AND COALESCE(operating_cashflow, 0) = 0
       ORDER BY stock_code, report_date"""
)
codes = sorted({row["stock_code"] for row in suspects})
gateway = QMTDataGateway.from_env()
data = gateway.get_financial_data(
    stock_list=codes,
    table_list=["Balance", "Income", "CashFlow", "PershareIndex"],
    start_time="20150101",
    end_time="20261015",
    report_type="report_time",
)
collector = importlib.import_module("data_ingestion.2-财务数据采集")
parsed = {
    code: {record["report_date"]: record for record in collector.extract_periods(data, code)}
    for code in codes
}

details = []
counts = {"qmt_nonzero_available": 0, "qmt_still_empty": 0, "qmt_row_missing": 0}
fields = ("revenue", "net_profit", "total_assets", "total_equity", "operating_cashflow")
for row in suspects:
    report_key = row["report_date"].strftime("%Y%m%d")
    cached = parsed.get(row["stock_code"], {}).get(report_key)
    if cached is None:
        status = "qmt_row_missing"
    elif any(cached.get(field) not in (None, 0, 0.0) for field in fields):
        status = "qmt_nonzero_available"
    else:
        status = "qmt_still_empty"
    counts[status] += 1
    details.append(
        {
            "stock_code": row["stock_code"],
            "report_date": row["report_date"],
            "status": status,
            "qmt_values": {field: cached.get(field) for field in fields} if cached else None,
        }
    )

report = {
    "as_of_date": "2026-10-15",
    "suspect_count": len(suspects),
    "stock_count": len(codes),
    "counts": counts,
    "details": details,
}
output = Path("reports/financial-audit/qmt-null-core-comparison-20261015.json")
output.write_text(json.dumps(report, ensure_ascii=False, indent=2, default=default), encoding="utf-8")
print(json.dumps({**report, "details": f"{len(details)} rows"}, ensure_ascii=False, default=default))
print(f"report={output.resolve()}")
