from __future__ import annotations

import json
from pathlib import Path

from data_ingestion.db_config import execute_query


root = Path(__file__).resolve().parent
source = json.loads(
    (root / "qmt-null-core-comparison-20261015.json").read_text(encoding="utf-8")
)
details = []
for finding in source["details"]:
    stock_code = finding["stock_code"]
    report_date = finding["report_date"]
    wide = execute_query(
        "SELECT revenue,net_profit,total_assets,total_equity,operating_cashflow,data_source "
        "FROM trade_stock_financial WHERE stock_code=%s AND report_date=%s",
        (stock_code, report_date),
    )
    pit = execute_query(
        "SELECT COUNT(*) AS n FROM trade_stock_financial_raw_pit "
        "WHERE stock_code=%s AND report_date=%s AND data_source='akshare' "
        "AND pit_status='pit_exact' AND announcement_date IS NOT NULL",
        (stock_code, report_date),
    )[0]["n"]
    quarantine = execute_query(
        "SELECT COUNT(*) AS n FROM trade_stock_financial_quarantine "
        "WHERE stock_code=%s AND report_date=%s "
        "AND reason_code='all_core_financials_null'",
        (stock_code, report_date),
    )[0]["n"]
    row = wide[0] if wide else {}
    values = {
        key: row.get(key)
        for key in (
            "revenue", "net_profit", "total_assets", "total_equity",
            "operating_cashflow",
        )
    }
    details.append({
        "stock_code": stock_code,
        "report_date": report_date,
        "data_source": row.get("data_source"),
        "resolved_fields": sum(value is not None for value in values.values()),
        "akshare_exact_pit_rows": pit,
        "quarantined_invalid_rows": quarantine,
        "values": values,
    })

result = {
    "target_count": len(details),
    "resolved_any_core": sum(item["resolved_fields"] > 0 for item in details),
    "resolved_all_core": sum(item["resolved_fields"] == 5 for item in details),
    "still_existing_all_core_empty": sum(
        item["resolved_fields"] == 0 and not item["quarantined_invalid_rows"]
        for item in details
    ),
    "quarantined_structural_rows": sum(
        item["quarantined_invalid_rows"] > 0 for item in details
    ),
    "with_akshare_exact_pit": sum(item["akshare_exact_pit_rows"] > 0 for item in details),
    "details": details,
}
(root / "akshare-targeted-recovery-20261018.json").write_text(
    json.dumps(result, ensure_ascii=False, default=str, indent=2), encoding="utf-8"
)
print(json.dumps(result, ensure_ascii=False, default=str, indent=2))
