from __future__ import annotations

import json

from data_ingestion.db_config import execute_query


codes = [
    "000016.SZ", "002388.SZ", "002731.SZ", "300773.SZ", "512390.SH",
    "560650.SH", "600293.SH", "601059.SH", "601198.SH", "688496.SH",
    "689009.SH",
]
placeholders = ",".join(["%s"] * len(codes))
status = execute_query(
    f"SELECT stock_code, stock_name, is_suspended, is_tradable "
    f"FROM trade_stock_status WHERE stock_code IN ({placeholders}) "
    "ORDER BY stock_code",
    tuple(codes),
)
history = execute_query(
    f"SELECT stock_code, trade_date, open_price, high_price, low_price, "
    f"close_price, volume, amount, suspend_flag, data_source "
    f"FROM trade_stock_daily_raw WHERE stock_code IN ({placeholders}) "
    "AND trade_date >= %s ORDER BY stock_code, trade_date",
    (*codes, "2026-09-28"),
)
print(json.dumps({"status": status, "history": history}, ensure_ascii=True, default=str, indent=2))
