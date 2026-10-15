# -*- coding: utf-8 -*-
"""兼容的个股 K 线只读接口。

行情写入统一由 ``data_ingestion/8-原始行情与复权数据采集.py`` 负责。
本模块只保留旧板块研究代码使用的读取函数，数据来自正式 QFQ 表。
"""

from __future__ import annotations

from pathlib import Path
from typing import List, Optional

import pandas as pd

from data_ingestion.db_config import execute_query


def sync_all_kline(*args, **kwargs) -> int:
    """拒绝旧行情写入入口，防止再次污染行情层。"""
    raise RuntimeError(
        "已废弃：请使用 data_ingestion/8-原始行情与复权数据采集.py；"
        "正式前复权行情表为 trade_stock_daily_qfq。"
    )


def load_stock_kline(
    stock_code: str,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
) -> pd.DataFrame:
    """从正式 QFQ 表加载单只证券日线，返回以交易日为索引的数据框。"""
    conditions = ["stock_code = %s"]
    params: list = [stock_code]
    if start_date:
        conditions.append("trade_date >= %s")
        params.append(start_date)
    if end_date:
        conditions.append("trade_date <= %s")
        params.append(end_date)

    rows = execute_query(
        f"""
        SELECT trade_date, open_price, high_price, low_price, close_price, volume, amount
        FROM trade_stock_daily_qfq
        WHERE {' AND '.join(conditions)}
        ORDER BY trade_date ASC
        """,
        params,
    )
    if not rows:
        return pd.DataFrame()

    frame = pd.DataFrame(rows)
    frame["trade_date"] = pd.to_datetime(frame["trade_date"])
    frame.set_index("trade_date", inplace=True)
    frame.columns = ["open", "high", "low", "close", "volume", "amount"]
    for column in frame.columns:
        frame[column] = pd.to_numeric(frame[column], errors="coerce")
    return frame


def load_multi_stock_kline(
    stock_codes: List[str],
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
) -> dict[str, pd.DataFrame]:
    result: dict[str, pd.DataFrame] = {}
    for code in stock_codes:
        frame = load_stock_kline(code, start_date, end_date)
        if not frame.empty:
            result[code] = frame
    return result


def main() -> int:
    sync_all_kline()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
