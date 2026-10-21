import json
from dataclasses import asdict
from datetime import date
from pathlib import Path

from data_ingestion.akshare_market_provider import AKShareMarketProvider
from data_ingestion.db_config import execute_query
from data_ingestion.market_rebuild_audit import (
    assess_rebuild_metrics,
    build_stratified_sample,
    compare_source_batches,
)
from data_ingestion.qmt_bootstrap_provider import QMTBootstrapProvider
from data_ingestion.run_market_rebuild import _load_legacy_history_starts


BATCH_ID = "market-full-qmt-20261014"
START = date(2026, 9, 1)
END = date(2026, 10, 13)
ABNORMAL_CODES = {
    "000596.SZ", "000651.SZ", "000830.SZ", "000933.SZ", "000937.SZ",
    "002110.SZ", "002432.SZ", "600096.SH", "600132.SH", "600346.SH",
    "600585.SH", "600660.SH", "600971.SH", "601088.SH", "601666.SH",
}


def security_type(code: str) -> str:
    number = code.split(".", 1)[0]
    return "fund" if number.startswith(("15", "16", "50", "51", "52", "56", "58")) else "stock"


def listing_era(value: object) -> str:
    year = int(str(value)[:4])
    if year < 2015:
        return "pre_2015"
    if year < 2021:
        return "2015_2020"
    return "post_2020"


catalog_rows = execute_query(
    """
    SELECT b.stock_code, b.start_date, b.source, b.gap_count,
           s.is_suspended, s.is_tradable
      FROM trade_market_rebuild_batch b
      LEFT JOIN trade_market_rebuild_excluded_code x
        ON x.batch_id=b.batch_id AND x.stock_code=b.stock_code
      LEFT JOIN trade_stock_status s ON s.stock_code=b.stock_code
     WHERE b.batch_id=%s AND b.status='complete' AND x.stock_code IS NULL
    """,
    (BATCH_ID,),
)
catalog = []
for row in catalog_rows:
    code = str(row["stock_code"])
    catalog.append({
        "stock_code": code,
        "security_type": security_type(code),
        "listing_era": listing_era(row["start_date"]),
        "has_action": code in ABNORMAL_CODES,
        "abnormal": bool(row.get("gap_count")) or code in ABNORMAL_CODES,
    })

stock_catalog = [row for row in catalog if row["security_type"] == "stock"]
fund_catalog = [row for row in catalog if row["security_type"] == "fund"]
sample = (
    build_stratified_sample(stock_catalog, seed=20261014, target_size=15)
    + build_stratified_sample(fund_catalog, seed=20261015, target_size=15)
)
qmt = QMTBootstrapProvider(expected_start_dates=_load_legacy_history_starts())
akshare = AKShareMarketProvider(max_attempts=3, request_timeout=20.0)
qmt_batches = qmt.fetch_batches(sample, START, END)
comparisons = []
for position, code in enumerate(sample, start=1):
    print(f"[source-comparison] {position}/{len(sample)} {code}", flush=True)
    ak_batch = akshare.fetch_batch(code, START, END)
    comparisons.append(compare_source_batches(
        qmt_batches[code],
        ak_batch,
        price_relative_tolerance=0.10,
        volume_relative_tolerance=0.50,
    ))

audit = json.loads(Path(
    "reports/market-rebuild/full-audit-20261015.json"
).read_text(encoding="utf-8"))
combined = assess_rebuild_metrics(audit["metrics"], comparisons)
report = {
    "batch_id": BATCH_ID,
    "window": {"start": START.isoformat(), "end": END.isoformat()},
    "seed": 20261014,
    "price_relative_tolerance": 0.10,
    "volume_relative_tolerance": 0.50,
    "sample": sample,
    "comparisons": [asdict(item) for item in comparisons],
    "combined_assessment": asdict(combined),
}
output = Path("reports/market-rebuild/source-comparison-20261015.json")
output.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(report, ensure_ascii=False, indent=2))
