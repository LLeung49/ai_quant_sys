import json
from datetime import date, datetime
from decimal import Decimal
from pathlib import Path

from data_ingestion.db_config import execute_query
from data_ingestion_qmt.qmt_data_gateway import QMTDataGateway


BATCH_ID = "market-full-qmt-20261014"
VOLUME_CODES = {"511920.SH", "511930.SH", "511950.SH", "511970.SH"}


def default(value):
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, Decimal):
        return str(value)
    return str(value)


failed = execute_query(
    """SELECT b.stock_code, b.error_detail
       FROM trade_market_rebuild_batch b
       LEFT JOIN trade_market_rebuild_excluded_code x
         ON x.batch_id=b.batch_id AND x.stock_code=b.stock_code
       WHERE b.batch_id=%s AND b.status='failed' AND x.stock_code IS NULL
       ORDER BY b.stock_code""",
    (BATCH_ID,),
)
codes = [row["stock_code"] for row in failed if row["stock_code"] not in VOLUME_CODES]
details = QMTDataGateway.from_env().get_instrument_detail(codes, iscomplete=True)

old_stats = execute_query(
    """SELECT stock_code, COUNT(*) AS row_count,
              SUM(open_price<>0 AND high_price<>0 AND low_price<>0 AND close_price<>0) AS nonzero_rows,
              MIN(trade_date) AS min_date, MAX(trade_date) AS max_date
       FROM trade_stock_daily_raw
       WHERE stock_code IN %s
       GROUP BY stock_code""",
    (codes,),
) if codes else []
stats_by_code = {row["stock_code"]: row for row in old_stats}

records = []
for code in codes:
    detail = details.get(code) or {}
    selected_detail = {
        key: detail.get(key)
        for key in (
            "InstrumentName", "ProductID", "ExchangeID", "OpenDate", "ExpireDate",
            "InstrumentStatus", "FloatVolume", "TotalVolume", "PreClose",
        )
        if key in detail
    }
    records.append(
        {
            "stock_code": code,
            "error_detail": next(row["error_detail"] for row in failed if row["stock_code"] == code),
            "instrument_detail_found": bool(detail),
            "instrument_detail": selected_detail,
            "old_table": stats_by_code.get(code),
        }
    )

report = {
    "batch_id": BATCH_ID,
    "remaining_non_volume_failure_count": len(codes),
    "instrument_detail_found_count": sum(row["instrument_detail_found"] for row in records),
    "records": records,
}
report["old_nonzero_codes"] = [
    row["stock_code"]
    for row in records
    if int((row["old_table"] or {}).get("nonzero_rows") or 0) > 0
]
report["old_zero_only_codes"] = [
    row["stock_code"]
    for row in records
    if int((row["old_table"] or {}).get("row_count") or 0) > 0
    and int((row["old_table"] or {}).get("nonzero_rows") or 0) == 0
]
output = Path("reports/market-rebuild/remaining-failure-evidence-20261015.json")
output.write_text(json.dumps(report, ensure_ascii=False, indent=2, default=default), encoding="utf-8")
print(json.dumps({**report, "records": f"{len(records)} rows"}, ensure_ascii=False, default=default))
print(f"report={output.resolve()}")
