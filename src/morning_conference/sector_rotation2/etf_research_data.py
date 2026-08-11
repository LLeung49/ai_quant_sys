"""Read-only ETF research data transformations."""
from __future__ import annotations

import pandas as pd

from data_ingestion.db_config import execute_query


def load_qfq_etf_panel(
    etf_codes: list[str], start_date: str, as_of_date: str
) -> pd.DataFrame:
    """Load ETF price and turnover observations from the QFQ table only."""
    columns = ["stock_code", "trade_date", "close_price", "amount"]
    if not etf_codes:
        return pd.DataFrame(columns=columns)
    placeholders = ", ".join(["%s"] * len(etf_codes))
    sql = f"""
        SELECT stock_code, trade_date, close_price, amount
        FROM trade_stock_daily_qfq
        WHERE stock_code IN ({placeholders})
          AND trade_date >= %s AND trade_date <= %s
        ORDER BY stock_code, trade_date
    """
    rows = execute_query(sql, [*etf_codes, start_date, as_of_date])
    frame = pd.DataFrame(rows, columns=columns)
    if not frame.empty:
        frame["trade_date"] = pd.to_datetime(frame["trade_date"])
        frame[["close_price", "amount"]] = frame[["close_price", "amount"]].apply(pd.to_numeric, errors="coerce")
    return frame


def load_current_stock_industries(stock_codes: list[str], level: int) -> pd.DataFrame:
    """Load the explicitly current Shenwan membership snapshot for holdings."""
    if level not in (1, 2):
        raise ValueError("level must be 1 or 2")
    field = f"sector_{level}"
    if not stock_codes:
        return pd.DataFrame(columns=["stock_code", field, "membership_asof_mode"])
    placeholders = ", ".join(["%s"] * len(stock_codes))
    rows = execute_query(
        f"SELECT stock_code, {field} FROM trade_stock_status WHERE stock_code IN ({placeholders})",
        stock_codes,
    )
    result = pd.DataFrame(rows, columns=["stock_code", field])
    result["membership_asof_mode"] = "current_mapping"
    return result


def calculate_holdings_industry_exposure(
    holdings: pd.DataFrame, industries: pd.DataFrame, level: int
) -> pd.DataFrame:
    """Aggregate disclosed stock weights into current Shenwan industry exposure."""
    if level not in (1, 2):
        raise ValueError("level must be 1 or 2")
    sector_column = f"sector_{level}"
    left = holdings.copy()
    left["stock_code"] = left["股票代码"].astype(str).str.zfill(6)
    left["weight"] = pd.to_numeric(left["占净值比例"], errors="coerce").fillna(0.0)
    right = industries[["stock_code", sector_column]].copy()
    right["stock_code"] = right["stock_code"].astype(str).str.zfill(6)
    merged = left.merge(right, on="stock_code", how="left")
    total = merged.groupby("etf_code", as_index=False)["weight"].sum().rename(columns={"weight": "disclosed_weight"})
    grouped = merged.dropna(subset=[sector_column]).groupby(["etf_code", sector_column], as_index=False).agg(
        industry_weight=("weight", "sum"), report_period=("季度", "first")
    )
    grouped = grouped.merge(total, on="etf_code", how="left")
    grouped["industry_exposure"] = grouped["industry_weight"] / grouped["disclosed_weight"]
    mapped = merged.loc[merged[sector_column].notna()].groupby("etf_code")["weight"].sum()
    grouped["unmapped_weight"] = (grouped["disclosed_weight"] - grouped["etf_code"].map(mapped).fillna(0.0)) / grouped["disclosed_weight"]
    grouped["sector_name"] = grouped.pop(sector_column)
    grouped["membership_asof_mode"] = "current_mapping"
    return grouped
