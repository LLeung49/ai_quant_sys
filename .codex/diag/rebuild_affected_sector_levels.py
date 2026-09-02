"""Rebuild only sector aggregates affected by one audited volume-repair run."""

import sys

from data_ingestion.db_config import get_connection
from morning_conference.sector_rotation import sector_index_builder as builder


run_id = sys.argv[1]
connection = get_connection()
cursor = connection.cursor()
try:
    cursor.execute(
        """SELECT DISTINCT s.sector_1, s.sector_2
             FROM trade_market_volume_repair_audit AS audit
             JOIN trade_stock_status AS s ON s.stock_code=audit.stock_code
            WHERE audit.run_id=%s""",
        (run_id,),
    )
    mappings = cursor.fetchall()
finally:
    cursor.close()
    connection.close()

all_dates = builder.get_all_trade_dates()
for level, column in ((1, 0), (2, 1)):
    sectors = sorted({row[column] for row in mappings if row[column]})
    total = 0
    print(f"[sector-rebuild] level={level} sectors={len(sectors)}", flush=True)
    for index, sector_name in enumerate(sectors, 1):
        rows = builder.rebuild_one_sector(sector_name, level, all_dates, all_dates)
        total += rows
        print(
            f"[sector-rebuild] level={level} {index}/{len(sectors)} "
            f"sector={sector_name} changed={rows} total={total}",
            flush=True,
        )
    print(f"[sector-rebuild] level={level} complete changed={total}", flush=True)
