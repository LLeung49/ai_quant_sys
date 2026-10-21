import json
from pathlib import Path

from data_ingestion.db_config import execute_query


sector_daily = execute_query(
    """SELECT trade_date, sector_level, COUNT(*) AS sector_count,
              SUM(close_idx IS NULL OR close_idx=0) AS zero_close_sectors,
              SUM(total_volume IS NULL OR total_volume=0) AS zero_volume_sectors,
              SUM(kline_stock_count IS NULL OR kline_stock_count=0) AS zero_constituent_sectors,
              ROUND(AVG(kline_stock_count / NULLIF(stock_count, 0)), 4) AS avg_coverage
       FROM trade_sector_daily
       WHERE trade_date >= '2026-04-01'
       GROUP BY trade_date, sector_level ORDER BY trade_date, sector_level"""
)
sector_bad_dates = [
    row for row in sector_daily
    if any(int(row[name] or 0) for name in (
        "zero_close_sectors", "zero_volume_sectors", "zero_constituent_sectors"
    ))
    or float(row["avg_coverage"] or 0) < 0.8
]
report = {
    "sector_date_level_count": len(sector_daily),
    "sector_bad_date_level_count": len(sector_bad_dates),
    "sector_first_bad": sector_bad_dates[0] if sector_bad_dates else None,
    "sector_latest": sector_daily[-2:] if sector_daily else [],
    "sector_bad_sample": sector_bad_dates[:20],
}
output = Path("reports/market-rebuild/existing-derived-market-audit-20261015.json")
output.write_text(json.dumps(report, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
print(json.dumps(report, ensure_ascii=False, default=str, indent=2))
