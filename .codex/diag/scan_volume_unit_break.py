"""Read-only scan for volume-unit discontinuities in raw stock daily data."""

from data_ingestion.db_config import get_connection


def main():
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(
            """SELECT trade_date, COUNT(*) AS rows_total,
                      SUM(amount > 0 AND volume > 0 AND close_price > 0
                          AND amount / volume / close_price > 5) AS suspicious_rows,
                      SUM(amount > 0 AND volume > 0 AND close_price > 0
                          AND amount / volume / close_price > 5) / COUNT(*) AS suspicious_ratio
                 FROM trade_stock_daily
                WHERE trade_date BETWEEN '2026-08-11' AND '2026-08-20'
                GROUP BY trade_date ORDER BY trade_date"""
        )
        print("[daily_scope]")
        for row in cursor.fetchall():
            print(row)
        cursor.execute(
            """SELECT d.stock_code, s.stock_name, d.trade_date, d.close_price, d.volume, d.amount,
                      d.amount / NULLIF(d.volume * d.close_price, 0) AS implied_volume_multiple
                 FROM trade_stock_daily AS d
                 LEFT JOIN trade_stock_status AS s ON s.stock_code=d.stock_code
                WHERE d.trade_date='2026-08-13' AND d.amount > 0 AND d.volume > 0 AND d.close_price > 0
                  AND d.amount / d.volume / d.close_price > 5
                ORDER BY implied_volume_multiple DESC LIMIT 30"""
        )
        print("[examples_20260813]")
        for row in cursor.fetchall():
            print(row)
    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    main()
