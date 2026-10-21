import hashlib
import json
from collections import Counter
from datetime import date
from pathlib import Path

from data_ingestion.db_config import execute_query, get_connection


BATCH_ID = "market-full-qmt-20261014"
TARGET_END = date(2026, 10, 13)

rows = execute_query(
    """
    SELECT b.stock_code, b.start_date, b.end_date,
           b.raw_rows, b.qfq_rows, b.hfq_rows,
           r.first_date AS raw_first, r.last_date AS raw_last, r.n AS raw_actual,
           q.first_date AS qfq_first, q.last_date AS qfq_last, q.n AS qfq_actual,
           h.first_date AS hfq_first, h.last_date AS hfq_last, h.n AS hfq_actual
    FROM trade_market_rebuild_batch b
    LEFT JOIN trade_market_rebuild_excluded_code x
      ON x.batch_id=b.batch_id AND x.stock_code=b.stock_code
    JOIN (
      SELECT stock_code, MIN(trade_date) first_date, MAX(trade_date) last_date, COUNT(*) n
      FROM trade_stock_daily_raw_rebuild WHERE rebuild_batch_id=%s GROUP BY stock_code
    ) r ON r.stock_code=b.stock_code
    JOIN (
      SELECT stock_code, MIN(trade_date) first_date, MAX(trade_date) last_date, COUNT(*) n
      FROM trade_stock_daily_qfq_rebuild WHERE rebuild_batch_id=%s GROUP BY stock_code
    ) q ON q.stock_code=b.stock_code
    JOIN (
      SELECT stock_code, MIN(trade_date) first_date, MAX(trade_date) last_date, COUNT(*) n
      FROM trade_stock_daily_bfq_rebuild WHERE rebuild_batch_id=%s GROUP BY stock_code
    ) h ON h.stock_code=b.stock_code
    WHERE b.batch_id=%s AND b.status='complete' AND x.stock_code IS NULL
      AND b.stock_code LIKE '68%%.SH' AND b.end_date < b.start_date
      AND b.end_date < '1990-01-01' AND b.start_date <= %s
    ORDER BY b.stock_code
    """,
    (BATCH_ID, BATCH_ID, BATCH_ID, BATCH_ID, TARGET_END),
)
if not rows:
    raise RuntimeError("no malformed STAR Market expiry metadata found")

for row in rows:
    ranges = {
        (row["raw_first"], row["raw_last"]),
        (row["qfq_first"], row["qfq_last"]),
        (row["hfq_first"], row["hfq_last"]),
    }
    counts = (row["raw_actual"], row["qfq_actual"], row["hfq_actual"])
    expected_counts = (row["raw_rows"], row["qfq_rows"], row["hfq_rows"])
    if len(ranges) != 1 or counts != expected_counts:
        raise RuntimeError(f"projection evidence mismatch: {row}")
    actual_first, actual_last = next(iter(ranges))
    if actual_first < row["start_date"] or actual_last > TARGET_END:
        raise RuntimeError(f"actual rows outside repaired range: {row}")

codes = [row["stock_code"] for row in rows]
conn = get_connection()
cursor = conn.cursor()
try:
    affected = cursor.execute(
        """
        UPDATE trade_market_rebuild_batch b
        LEFT JOIN trade_market_rebuild_excluded_code x
          ON x.batch_id=b.batch_id AND x.stock_code=b.stock_code
        SET b.end_date=%s
        WHERE b.batch_id=%s AND b.status='complete' AND x.stock_code IS NULL
          AND b.stock_code LIKE '68%%.SH' AND b.end_date < b.start_date
          AND b.end_date < '1990-01-01' AND b.start_date <= %s
        """,
        (TARGET_END, BATCH_ID, TARGET_END),
    )
    if affected != len(rows):
        raise RuntimeError(f"expected to update {len(rows)} rows, updated {affected}")
    conn.commit()
except Exception:
    conn.rollback()
    raise
finally:
    cursor.close()
    conn.close()

report = {
    "batch_id": BATCH_ID,
    "target_end_date": TARGET_END.isoformat(),
    "repaired_codes": len(codes),
    "code_sha256": hashlib.sha256("".join(f"{code}\n" for code in codes).encode()).hexdigest(),
    "old_end_date_counts": dict(Counter(str(row["end_date"]) for row in rows)),
    "rows_per_projection": sum(row["raw_actual"] for row in rows),
    "first_code": codes[0],
    "last_code": codes[-1],
}
path = Path("reports/market-rebuild/star-expiry-metadata-repair-pass2-20261016.json")
path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(report, ensure_ascii=False, indent=2))
