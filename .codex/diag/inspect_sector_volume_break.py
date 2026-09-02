"""Read-only diagnosis of sector volume discontinuities around 2026-08-13."""

from data_ingestion.db_config import get_connection


def main():
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(
            """SELECT sector_name, sector_level, trade_date, total_volume, total_amount,
                      close_idx
                 FROM trade_sector_daily
                WHERE sector_name LIKE %s
                  AND trade_date BETWEEN '2026-08-06' AND '2026-08-20'
                ORDER BY sector_name, sector_level, trade_date""",
            ("%煤炭%",),
        )
        for row in cursor.fetchall():
            print(row)
        cursor.execute(
            """SELECT d.stock_code, s.stock_name,
                      MAX(CASE WHEN d.trade_date='2026-08-12' THEN d.amount / NULLIF(d.volume * d.close_price, 0) END) AS multiple_0812,
                      MAX(CASE WHEN d.trade_date='2026-08-13' THEN d.amount / NULLIF(d.volume * d.close_price, 0) END) AS multiple_0813,
                      MAX(CASE WHEN d.trade_date='2026-08-13' THEN d.volume END) / NULLIF(MAX(CASE WHEN d.trade_date='2026-08-12' THEN d.volume END), 0) AS volume_ratio
                 FROM trade_stock_daily AS d
                 JOIN trade_stock_status AS s ON s.stock_code=d.stock_code
                WHERE s.sector_1 LIKE %s AND d.trade_date IN ('2026-08-12', '2026-08-13')
                GROUP BY d.stock_code, s.stock_name
                ORDER BY multiple_0813 / NULLIF(multiple_0812, 0) DESC""",
            ("%煤炭%",),
        )
        print("[coal_unit_switch_by_stock]")
        for row in cursor.fetchall():
            print(row)
        cursor.execute(
            """SELECT q.trade_date, SUM(q.volume) AS qfq_volume, SUM(raw.volume) AS raw_volume,
                      SUM(q.amount) AS qfq_amount, SUM(raw.amount) AS raw_amount
                 FROM trade_stock_daily_qfq AS q
                 JOIN trade_stock_daily AS raw ON raw.stock_code=q.stock_code AND raw.trade_date=q.trade_date
                 JOIN trade_stock_status AS s ON s.stock_code=q.stock_code
                WHERE s.sector_1 LIKE %s
                  AND q.trade_date IN ('2026-08-12', '2026-08-13', '2026-08-14')
                GROUP BY q.trade_date ORDER BY q.trade_date""",
            ("%煤炭%",),
        )
        print("[qfq_vs_raw]")
        for row in cursor.fetchall():
            print(row)
        cursor.execute(
            """SELECT d.trade_date, COUNT(*) AS row_count, COUNT(DISTINCT d.stock_code) AS stock_count,
                      SUM(d.volume) AS total_volume, SUM(d.amount) AS total_amount,
                      SUM(d.amount) / NULLIF(SUM(d.volume), 0) AS implied_price
                 FROM trade_stock_daily_qfq AS d
                 JOIN trade_stock_status AS s ON s.stock_code=d.stock_code
                WHERE s.sector_1 LIKE %s
                  AND d.trade_date IN ('2026-08-12', '2026-08-13', '2026-08-14')
                GROUP BY d.trade_date ORDER BY d.trade_date""",
            ("%煤炭%",),
        )
        print("[coal_constituent_raw]")
        for row in cursor.fetchall():
            print(row)
    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    main()
