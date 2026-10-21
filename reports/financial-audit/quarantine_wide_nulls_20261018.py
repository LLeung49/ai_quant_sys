"""Quarantine all-core-null rows from the legacy financial wide table."""

from __future__ import annotations

import argparse
from datetime import date, datetime
from decimal import Decimal
import json
from pathlib import Path

import pymysql

from data_ingestion.db_config import get_connection


SELECT_NULLS = """
SELECT * FROM trade_stock_financial
WHERE revenue IS NULL
  AND net_profit IS NULL
  AND total_assets IS NULL
  AND total_equity IS NULL
  AND operating_cashflow IS NULL
ORDER BY id
"""


def _json_default(value):
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, Decimal):
        return str(value)
    return str(value)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("reports/financial-audit/financial-wide-null-audit-20261018.json"),
    )
    args = parser.parse_args(argv)

    connection = get_connection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    try:
        cursor.execute(SELECT_NULLS)
        rows = list(cursor.fetchall())
        if args.apply and rows:
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS trade_stock_financial_quarantine (
                       quarantine_id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                       source_id BIGINT NOT NULL,
                       stock_code VARCHAR(32) NOT NULL,
                       report_date DATE NOT NULL,
                       reason_code VARCHAR(64) NOT NULL,
                       batch_id VARCHAR(96) NOT NULL,
                       quarantined_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                       row_payload JSON NOT NULL,
                       UNIQUE KEY uq_financial_wide_quarantine_batch (source_id, batch_id)
                   ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4"""
            )
            connection.commit()
            connection.begin()
            ids = []
            for row in rows:
                source_id = int(row["id"])
                cursor.execute(
                    "SELECT * FROM trade_stock_financial WHERE id=%s FOR UPDATE",
                    (source_id,),
                )
                locked = cursor.fetchone()
                if locked is None or any(
                    locked[field] is not None
                    for field in (
                        "revenue", "net_profit", "total_assets", "total_equity",
                        "operating_cashflow",
                    )
                ):
                    raise RuntimeError(f"wide row changed before quarantine: id={source_id}")
                cursor.execute(
                    """INSERT INTO trade_stock_financial_quarantine
                           (source_id, stock_code, report_date, reason_code,
                            batch_id, row_payload)
                       VALUES (%s, %s, %s, %s, %s, %s)""",
                    (
                        source_id,
                        locked["stock_code"],
                        locked["report_date"],
                        "all_core_financials_null",
                        "financial-wide-null-audit-20261018",
                        json.dumps(locked, ensure_ascii=False, default=_json_default),
                    ),
                )
                ids.append(source_id)
            placeholders = ",".join(["%s"] * len(ids))
            cursor.execute(
                f"DELETE FROM trade_stock_financial WHERE id IN ({placeholders})",
                tuple(ids),
            )
            if cursor.rowcount != len(ids):
                raise RuntimeError(
                    f"wide delete mismatch: expected={len(ids)} actual={cursor.rowcount}"
                )
            connection.commit()
        report = {
            "batch_id": "financial-wide-null-audit-20261018",
            "mode": "apply" if args.apply else "dry-run",
            "candidate_count": len(rows),
            "quarantined_count": len(rows) if args.apply else 0,
            "rows": [
                {
                    "id": int(row["id"]),
                    "stock_code": row["stock_code"],
                    "report_date": str(row["report_date"]),
                    "data_source": row["data_source"],
                }
                for row in rows
            ],
        }
        args.output.write_text(
            json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        print(json.dumps(report, ensure_ascii=False))
        return 0
    except Exception:
        connection.rollback()
        raise
    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    raise SystemExit(main())
