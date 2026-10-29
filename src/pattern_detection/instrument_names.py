"""Resolve scanned instrument names from local metadata, with cache fallback."""

from data_ingestion.db_config import execute_query
from data_ingestion.utils import get_instrument_names


def get_scan_names(codes):
    """Return display names for scan hits, preferring trade_stock_status."""
    codes = list(dict.fromkeys(codes))
    if not codes:
        return {}

    names = {}
    try:
        for offset in range(0, len(codes), 500):
            batch = codes[offset:offset + 500]
            placeholders = ", ".join(["%s"] * len(batch))
            sql = ("SELECT stock_code, stock_name FROM trade_stock_status "
                   f"WHERE stock_code IN ({placeholders})")
            for row in execute_query(sql, batch):
                name = row.get("stock_name")
                if isinstance(name, str) and name.strip():
                    names[row["stock_code"]] = name.strip()
    except Exception as exc:
        print(f"  [名称] 本地标的名称查询失败 ({exc}), 使用名称缓存")

    missing = [code for code in codes if code not in names]
    if missing:
        fallback = get_instrument_names(missing)
        names.update({code: fallback.get(code, code) for code in missing})
    return names
