from __future__ import annotations
from typing import Any
import pandas as pd
from data_ingestion_qmt.db_config import execute_query, get_connection
WATCHLIST_COLUMNS = ('as_of_date','sector_level','model_version','run_id','entity_type','stock_code','stock_name','sector_1','sector_2','close','change_pct','dif','dea','macd_hist','vol_ratio','vol_ratio_gc','gc_offset','gc_label','gc_dif','gc_dea','adx_14','rsi_14','hurst_60','kama_efficiency','above_ma60','sector_2_5d_return','main_capital_net_inflow_20d','chan_first_buy')
ENTITY_DAILY_COLUMNS = WATCHLIST_COLUMNS[:25] + ('is_triggered',)


def sync_etf_status_names(codes: list[str]) -> int:
    """Write ETF names into the shared instrument status table without replacing other metadata."""
    unique_codes = sorted({str(code) for code in codes if code})
    if not unique_codes:
        return 0
    from data_ingestion_qmt.utils import get_instrument_names

    names = get_instrument_names(unique_codes)
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




