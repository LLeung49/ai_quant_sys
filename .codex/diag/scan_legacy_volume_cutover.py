"""Read-only scan of legacy-table volume unit cutover on 2026-08-13.

A stock is considered affected when its legacy volume was roughly 100 times the
new XtQuant raw volume on 2026-08-12, then roughly equal on 2026-08-13.  Since
amount and price agree, that pattern means the legacy table switched from
shares to lots rather than that trading activity collapsed.
"""

import json

from data_ingestion.db_config import get_connection


SWITCHES_SQL = """
SELECT l12.stock_code
FROM trade_stock_daily AS l12
JOIN trade_stock_daily_raw AS r12
  ON r12.stock_code = l12.stock_code AND r12.trade_date = l12.trade_date
JOIN trade_stock_daily AS l13
  ON l13.stock_code = l12.stock_code AND l13.trade_date = '2026-08-13'
JOIN trade_stock_daily_raw AS r13
  ON r13.stock_code = l12.stock_code AND r13.trade_date = l13.trade_date
WHERE l12.trade_date = '2026-08-12'
  AND l12.volume / NULLIF(r12.volume, 0) BETWEEN 50 AND 150
  AND l13.volume / NULLIF(r13.volume, 0) BETWEEN 0.5 AND 2
"""


def main():
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT COUNT(*) FROM (" + SWITCHES_SQL + ") AS x")
        print("[affected_stock_count]", cursor.fetchone()[0])

        cursor.execute(
            """SELECT
                      SUM(q12.volume / NULLIF(r12.volume, 0) BETWEEN 50 AND 150)
                        AS qfq_share_unit_on_0812,
                      SUM(q13.volume / NULLIF(r13.volume, 0) BETWEEN 0.5 AND 2)
                        AS qfq_lot_unit_on_0813,
                      COUNT(*) AS affected_stocks
                 FROM (""" + SWITCHES_SQL + """) AS x
                 JOIN trade_stock_daily_qfq AS q12
                   ON q12.stock_code=x.stock_code AND q12.trade_date='2026-08-12'
                 JOIN trade_stock_daily_raw AS r12
                   ON r12.stock_code=q12.stock_code AND r12.trade_date=q12.trade_date
                 JOIN trade_stock_daily_qfq AS q13
                   ON q13.stock_code=x.stock_code AND q13.trade_date='2026-08-13'
                 JOIN trade_stock_daily_raw AS r13
                   ON r13.stock_code=q13.stock_code AND r13.trade_date=q13.trade_date"""
        )
        print("[sector_input_qfq_unit_check]", cursor.fetchone())

        cursor.execute(
            """SELECT q.stock_code, MIN(q.trade_date) AS first_share_unit_date,
                      MAX(q.trade_date) AS last_share_unit_date,
                      COUNT(*) AS share_unit_rows
                 FROM (""" + SWITCHES_SQL + """) AS x
                 JOIN trade_stock_daily_qfq AS q ON q.stock_code=x.stock_code
                WHERE q.amount / NULLIF(q.volume * q.close_price, 0) BETWEEN 0.5 AND 2
                GROUP BY q.stock_code
                ORDER BY first_share_unit_date, q.stock_code"""
        )
        histories = cursor.fetchall()
        print("[qfq_share_unit_history_count]", len(histories))
        print("[qfq_share_unit_row_count]", sum(row[3] for row in histories))
        for row in histories:
            print(json.dumps(row, ensure_ascii=True, default=str))

        for table_name in ("trade_stock_daily", "trade_stock_daily_qfq", "trade_stock_daily_bfq"):
            cursor.execute(
                """SELECT COUNT(*) AS share_unit_rows,
                          COUNT(DISTINCT d.stock_code) AS affected_stocks,
                          MIN(d.trade_date) AS first_date,
                          MAX(d.trade_date) AS last_date
                     FROM (""" + SWITCHES_SQL + """) AS x
                     JOIN """ + table_name + """ AS d ON d.stock_code=x.stock_code
                    WHERE d.amount / NULLIF(d.volume * d.close_price, 0) BETWEEN 0.5 AND 2"""
            )
            print("[share_unit_table_check]", table_name, cursor.fetchone())

        cursor.execute(
            """SELECT COALESCE(s.sector_1, '(unmapped)') AS sector_1,
                      COALESCE(s.sector_2, '(unmapped)') AS sector_2,
                      COUNT(*) AS affected_stock_count
                 FROM (""" + SWITCHES_SQL + """) AS x
                 LEFT JOIN trade_stock_status AS s ON s.stock_code = x.stock_code
                 GROUP BY s.sector_1, s.sector_2
                 ORDER BY affected_stock_count DESC, sector_1, sector_2"""
        )
        print("[affected_sector_count]")
        for row in cursor.fetchall():
            print(json.dumps(row, ensure_ascii=True, default=str))

        cursor.execute(
            """SELECT x.stock_code, s.stock_name, s.sector_1, s.sector_2,
                      l12.volume AS legacy_0812, r12.volume AS raw_0812,
                      l13.volume AS legacy_0813, r13.volume AS raw_0813
                 FROM (""" + SWITCHES_SQL + """) AS x
                 JOIN trade_stock_daily AS l12
                   ON l12.stock_code=x.stock_code AND l12.trade_date='2026-08-12'
                 JOIN trade_stock_daily_raw AS r12
                   ON r12.stock_code=l12.stock_code AND r12.trade_date=l12.trade_date
                 JOIN trade_stock_daily AS l13
                   ON l13.stock_code=x.stock_code AND l13.trade_date='2026-08-13'
                 JOIN trade_stock_daily_raw AS r13
                   ON r13.stock_code=l13.stock_code AND r13.trade_date=l13.trade_date
                 LEFT JOIN trade_stock_status AS s ON s.stock_code=x.stock_code
                 ORDER BY x.stock_code
                 LIMIT 30"""
        )
        print("[examples]")
        for row in cursor.fetchall():
            print(json.dumps(row, ensure_ascii=True, default=str))
    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    main()
