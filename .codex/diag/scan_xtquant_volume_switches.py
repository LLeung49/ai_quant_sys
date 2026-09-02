"""Read-only, high-confidence scan of 2026-08-12/13 stock volume-unit switches."""

from data_ingestion.db_config import get_connection


def main():
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(
            """SELECT COUNT(*) AS switched_stocks
                 FROM (
                    SELECT stock_code,
                           MAX(CASE WHEN trade_date='2026-08-12' THEN amount / NULLIF(volume * close_price, 0) END) AS before_multiple,
                           MAX(CASE WHEN trade_date='2026-08-13' THEN amount / NULLIF(volume * close_price, 0) END) AS after_multiple
                      FROM trade_stock_daily_raw
                     WHERE trade_date IN ('2026-08-12', '2026-08-13')
                     GROUP BY stock_code
                    HAVING before_multiple BETWEEN 0.5 AND 2 AND after_multiple BETWEEN 50 AND 150
                 ) AS switches"""
        )
        print("[switch_count]", cursor.fetchone())
        cursor.execute(
            """SELECT COALESCE(s.sector_1, '(unmapped)') AS sector_1,
                      COALESCE(s.sector_2, '(unmapped)') AS sector_2,
                      COUNT(*) AS switched_stocks,
                      GROUP_CONCAT(x.stock_code ORDER BY x.stock_code SEPARATOR ',') AS codes
                 FROM (
                    SELECT stock_code
                      FROM trade_stock_daily_raw
                     WHERE trade_date IN ('2026-08-12', '2026-08-13')
                     GROUP BY stock_code
                    HAVING MAX(CASE WHEN trade_date='2026-08-12' THEN amount / NULLIF(volume * close_price, 0) END) BETWEEN 0.5 AND 2
                       AND MAX(CASE WHEN trade_date='2026-08-13' THEN amount / NULLIF(volume * close_price, 0) END) BETWEEN 50 AND 150
                 ) AS x
                 LEFT JOIN trade_stock_status AS s ON s.stock_code=x.stock_code
                 GROUP BY s.sector_1, s.sector_2
                 ORDER BY switched_stocks DESC, sector_1, sector_2"""
        )
        print("[affected_sectors]")
        for row in cursor.fetchall():
            print(row)
    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    main()
