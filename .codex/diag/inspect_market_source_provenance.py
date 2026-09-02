"""Read-only source-provenance inspection for the 2026-08-13 volume anomaly."""

from data_ingestion.db_config import get_connection


def main():
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("SHOW COLUMNS FROM trade_stock_daily_raw")
        print("[raw_columns]", [row[0] for row in cursor.fetchall()])
        cursor.execute("SHOW COLUMNS FROM trade_stock_daily")
        print("[legacy_columns]", [row[0] for row in cursor.fetchall()])
        cursor.execute(
            """SELECT trade_date, data_source, COUNT(*) AS rows_count
                 FROM trade_stock_daily_raw
                WHERE trade_date BETWEEN '2026-08-11' AND '2026-08-14'
                GROUP BY trade_date, data_source ORDER BY trade_date, data_source"""
        )
        print("[raw_source_counts]")
        for row in cursor.fetchall():
            print(row)
        cursor.execute(
            """SELECT legacy.trade_date,
                      SUM(legacy.volume) AS legacy_volume, SUM(raw.volume) AS raw_volume,
                      SUM(legacy.amount) AS legacy_amount, SUM(raw.amount) AS raw_amount
                 FROM trade_stock_daily AS legacy
                 JOIN trade_stock_daily_raw AS raw ON raw.stock_code=legacy.stock_code AND raw.trade_date=legacy.trade_date
                 JOIN trade_stock_status AS s ON s.stock_code=legacy.stock_code
                WHERE s.sector_1 LIKE %s AND legacy.trade_date IN ('2026-08-12', '2026-08-13', '2026-08-14')
                GROUP BY legacy.trade_date ORDER BY legacy.trade_date""",
            ("%煤炭%",),
        )
        print("[legacy_vs_raw_coal]")
        for row in cursor.fetchall():
            print(row)
    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    main()
