from __future__ import annotations
from typing import Any
import numpy as np
import pandas as pd
from data_ingestion.db_config import execute_query, get_connection
WATCHLIST_COLUMNS = ('as_of_date','sector_level','model_version','run_id','entity_type','stock_code','stock_name','sector_1','sector_2','close','change_pct','dif','dea','macd_hist','vol_ratio','vol_ratio_gc','gc_offset','gc_label','gc_dif','gc_dea','adx_14','rsi_14','hurst_60','kama_efficiency','above_ma60','sector_2_5d_return','main_capital_net_inflow_20d','chan_first_buy')
ENTITY_DAILY_COLUMNS = WATCHLIST_COLUMNS[:25] + ('is_triggered',)


def replace_macd_daily(frame: pd.DataFrame, as_of_date: str, sector_level: int,
                       model_version: str, run_id: str) -> tuple[int, int]:
    """Replace both MACD outputs for one date in one transaction.

    A rerun must remove entities and triggers that disappeared after source repair.
    Reject invalid prices before touching either table.
    """
    if frame is None or frame.empty:
        raise ValueError(f"No MACD metrics for {as_of_date}")
    closes = pd.to_numeric(frame['close'], errors='coerce')
    if closes.isna().any() or (closes <= 0).any():
        raise ValueError(f"Invalid MACD close for {as_of_date}")
    triggered = frame[frame['is_triggered'] == 1]

    def values(row: dict, columns: tuple[str, ...]) -> tuple:
        return (as_of_date, sector_level, model_version, run_id) + tuple(
            None if pd.isna(row.get(column)) or (
                isinstance(row.get(column), (float, np.floating))
                and not np.isfinite(row.get(column))
            ) else row.get(column)
            for column in columns[4:]
        )

    entity_rows = [values(row, ENTITY_DAILY_COLUMNS) for row in frame.to_dict('records')]
    pool_rows = [values(row, WATCHLIST_COLUMNS) for row in triggered.to_dict('records')]
    conn = get_connection()
    cur = conn.cursor()
    try:
        for table in ('sector_rotation_macd_entity_daily', 'sector_rotation_macd_pool'):
            cur.execute(
                f'DELETE FROM {table} WHERE as_of_date=%s AND sector_level=%s AND model_version=%s',
                (as_of_date, sector_level, model_version),
            )
        cur.executemany(
            f"INSERT INTO sector_rotation_macd_entity_daily ({', '.join(ENTITY_DAILY_COLUMNS)}) "
            f"VALUES ({', '.join(['%s'] * len(ENTITY_DAILY_COLUMNS))})",
            entity_rows,
        )
        if pool_rows:
            cur.executemany(
                f"INSERT INTO sector_rotation_macd_pool ({', '.join(WATCHLIST_COLUMNS)}) "
                f"VALUES ({', '.join(['%s'] * len(WATCHLIST_COLUMNS))})",
                pool_rows,
            )
        conn.commit()
        return len(entity_rows), len(pool_rows)
    except Exception:
        conn.rollback()
        raise
    finally:
        cur.close()
        conn.close()


def sync_etf_status_names(codes: list[str]) -> int:
    """Write ETF names into the shared instrument status table without replacing other metadata."""
    unique_codes = sorted({str(code) for code in codes if code})
    if not unique_codes:
        return 0
    existing = execute_query(
        "SELECT stock_code FROM trade_stock_status WHERE stock_code IN (" + ",".join(["%s"] * len(unique_codes)) + ") "
        "AND stock_name IS NOT NULL AND stock_name<>''",
        tuple(unique_codes),
    )
    named_codes = {row['stock_code'] for row in existing}
    unresolved = [code for code in unique_codes if code not in named_codes]
    if not unresolved:
        return 0
    from data_ingestion.utils import get_instrument_names

    names = get_instrument_names(unresolved)
    rows = [(code, name) for code, name in names.items() if name and name != code]
    if not rows:
        return 0
    sql = "INSERT INTO trade_stock_status (stock_code, stock_name) VALUES (%s, %s) ON DUPLICATE KEY UPDATE stock_name=VALUES(stock_name)"
    conn = get_connection(); cur = conn.cursor()
    try:
        cur.executemany(sql, rows); conn.commit(); return cur.rowcount
    except Exception:
        conn.rollback(); raise
    finally:
        cur.close(); conn.close()
def persist_macd_pool(frame: pd.DataFrame, as_of_date: str, sector_level: int, model_version: str, run_id: str) -> int:
    if frame is None or frame.empty: return 0
    rows=[]
    for row in frame.to_dict('records'):
        rows.append((as_of_date, sector_level, model_version, run_id, row.get('entity_type', 'stock')) + tuple(None if pd.isna(row.get(c)) else row.get(c) for c in WATCHLIST_COLUMNS[5:]))
    sql=f"INSERT INTO sector_rotation_macd_pool ({', '.join(WATCHLIST_COLUMNS)}) VALUES ({', '.join(['%s']*len(WATCHLIST_COLUMNS))}) ON DUPLICATE KEY UPDATE " + ', '.join(f'{c}=VALUES({c})' for c in WATCHLIST_COLUMNS[4:])
    conn=get_connection(); cur=conn.cursor()
    try: cur.executemany(sql, rows); conn.commit(); return cur.rowcount
    except Exception: conn.rollback(); raise
    finally: cur.close(); conn.close()
def load_macd_pool(as_of_date: str, sector_level: int, model_version: str) -> list[dict[str, Any]]:
    return list(execute_query(f"SELECT {', '.join(WATCHLIST_COLUMNS[4:])} FROM sector_rotation_macd_pool WHERE as_of_date=%s AND sector_level=%s AND model_version=%s ORDER BY sector_2, stock_code", (as_of_date, sector_level, model_version)))


def persist_macd_entity_daily(frame: pd.DataFrame, as_of_date: str, sector_level: int, model_version: str, run_id: str) -> int:
    if frame is None or frame.empty:
        return 0
    rows = []
    for row in frame.to_dict('records'):
        rows.append((as_of_date, sector_level, model_version, run_id) + tuple(None if pd.isna(row.get(c)) else row.get(c) for c in ENTITY_DAILY_COLUMNS[4:]))
    sql = f"INSERT INTO sector_rotation_macd_entity_daily ({', '.join(ENTITY_DAILY_COLUMNS)}) VALUES ({', '.join(['%s'] * len(ENTITY_DAILY_COLUMNS))}) ON DUPLICATE KEY UPDATE " + ', '.join(f'{c}=VALUES({c})' for c in ENTITY_DAILY_COLUMNS[4:])
    conn=get_connection(); cur=conn.cursor()
    try: cur.executemany(sql, rows); conn.commit(); return cur.rowcount
    except Exception: conn.rollback(); raise
    finally: cur.close(); conn.close()


# Backward-compatible aliases during migration
persist_personal_watchlist = persist_macd_pool
load_personal_watchlist = load_macd_pool



