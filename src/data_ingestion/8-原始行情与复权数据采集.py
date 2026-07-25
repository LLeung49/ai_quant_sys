# -*- coding: utf-8 -*-
"""独立的 QMT 原始、前复权和后复权日线采集任务。

这是与既有行情采集脚本并行运行的第二条数据链路：它不导入旧脚本，
也绝不写入旧的 ``trade_stock_daily``。三种 QMT ``dividend_type`` 分别落入
``trade_stock_daily_raw``、``trade_stock_daily_qfq``、``trade_stock_daily_bfq``，
因此旧前复权结果可以作为对账基准，而不是被新任务覆盖。

每次运行先保存近期权益因子快照，再增量拉取三类价格，最后执行权益事件生成的
派生价格刷新任务。任一代码的 QMT 响应为空会被视为失败，避免把“供应商未返回数据”
误当成“当天没有行情”。
"""

import sys
from datetime import date, timedelta

from xtquant import xtdata

from db_config import execute_query
from price_corporate_actions import run_due_refresh_tasks, sync_qmt_factor_snapshot
from price_projection_store import get_existing_latest_dates, write_daily_rows


DATA_START = "20150101"
DATA_START_DATE = date(2015, 1, 1)
A_SHARE_SECTOR = "沪深A股"
ETF_SECTOR = "沪深ETF"
SECTORS = (A_SHARE_SECTOR, ETF_SECTOR)
DIVIDEND_TYPES = ("none", "front", "back")  # QMT 原始、前复权、后复权三种投影。
# 每日重复读取最近窗口：即使权益公告在之后被修订/撤回，也能被快照比较发现。
ACTION_LOOKBACK_DAYS = 10
MARKET_FIELDS = (
    "open", "high", "low", "close", "volume", "amount", "preClose", "suspendFlag",
)

SELECT_ADJUSTMENT_ASOF_SQL = """
-- 投影中已纳入的最新有效除权日，仅作数据血缘标记，不参与价格计算。
SELECT MAX(ex_date) AS adjustment_asof
FROM trade_corporate_action
WHERE stock_code = %s
  AND data_source = 'xtquant'
  AND event_status = 'effective'
"""

MODE_LABELS = {
    "none": "raw",
    "front": "front-adjusted",
    "back": "back-adjusted",
}


def _as_trade_date(index_value) -> str:
    """将 QMT DataFrame 索引统一成 MySQL DATE 可识别的 ``YYYY-MM-DD`` 字符串。"""
    value = str(index_value)
    if len(value) < 8:
        raise ValueError(f"Unexpected QMT trading-date index: {index_value!r}")
    return f"{value[:4]}-{value[4:6]}-{value[6:8]}"


def _optional_number(row, key):
    """读取可空数值，并将 pandas/NumPy 的 NaN 统一为 ``None``。"""
    value = row.get(key) if hasattr(row, "get") else row[key]
    if value is None:
        return None
    try:
        if value != value:  # NaN without adding a pandas dependency.
            return None
    except TypeError:
        pass
    return float(value)


def _rows_from_dataframe(stock_code: str, dataframe, dividend_type: str) -> list[dict]:
    """把 QMT 行转为固定库表字段，保留原始行情特有的昨收和停牌标记。

    三个模式共享 OHLCV/成交额字段；只有 ``none`` 是交易事实，因而额外保存
    ``preClose`` 和 ``suspendFlag``。复权表的换手率目前没有 QMT 对应字段，显式写
    ``None``，避免把原始表字段误复制到派生表。
    """
    rows = []
    for index_value, row in dataframe.iterrows():
        item = {
            "stock_code": stock_code,
            "trade_date": _as_trade_date(index_value),
            "open_price": float(row["open"]),
            "high_price": float(row["high"]),
            "low_price": float(row["low"]),
            "close_price": float(row["close"]),
            "volume": int(row["volume"]),
            "amount": float(row["amount"]),
        }
        if dividend_type == "none":
            item["pre_close"] = _optional_number(row, "preClose")
            suspend = _optional_number(row, "suspendFlag")
            item["suspend_flag"] = int(suspend) if suspend is not None else None
        else:
            item["turnover_rate"] = None
        rows.append(item)
    return rows


def download_and_save_mode(
    stock_code: str,
    dividend_type: str,
    start_date: str,
    adjustment_asof: date | None,
) -> int:
    """下载并幂等写入一个价格模式，返回实际写入的行数。

    ``start_date`` 由三张表中最早的游标决定，保证它们日期对齐。供应商返回空表、
    或转换后没有有效行，都抛出异常：调用者会保留该股票失败记录，后续运行可重试。
    ``adjustment_asof`` 只随前/后复权行写入，表示该投影使用的权益事件版本。
    """
    if dividend_type not in DIVIDEND_TYPES:
        raise ValueError(f"Unsupported dividend type: {dividend_type}")
    xtdata.download_history_data(stock_code, "1d", start_time=start_date)
    data = xtdata.get_market_data_ex(
        field_list=list(MARKET_FIELDS),
        stock_list=[stock_code],
        period="1d",
        start_time=start_date,
        dividend_type=dividend_type,
    )
    dataframe = data.get(stock_code) if data else None
    if dataframe is None or len(dataframe) == 0:
        raise RuntimeError(
            f"empty QMT {MODE_LABELS[dividend_type]} market response for {stock_code}"
        )
    rows = _rows_from_dataframe(stock_code, dataframe, dividend_type)
    if not rows:
        raise RuntimeError(
            f"QMT returned no valid {MODE_LABELS[dividend_type]} rows for {stock_code}"
        )
    write_daily_rows(dividend_type, rows, adjustment_asof)
    return len(rows)


def download_and_save_all_modes(
    stock_code: str, start_date: str, adjustment_asof: date | None = None,
) -> dict[str, int]:
    """按固定顺序拉取原始、前复权、后复权；三者从同一起点重新对齐。"""
    counts = {}
    for dividend_type in DIVIDEND_TYPES:
        counts[dividend_type] = download_and_save_mode(
            stock_code,
            dividend_type,
            start_date,
            adjustment_asof,
        )
    return counts


def get_adjustment_asof(stock_code: str) -> date | None:
    """返回该股票已生效权益事件的最新除权日，作为复权行的可追溯版本标记。"""
    rows = execute_query(SELECT_ADJUSTMENT_ASOF_SQL, (stock_code,))
    return rows[0]["adjustment_asof"] if rows and rows[0]["adjustment_asof"] else None


def sync_stock_actions(stock_code: str, today: date):
    """保存最近完整权益窗口，并把需要重刷的前/后复权范围写入持久任务表。

    仅 A 股调用此方法；ETF 仍采集三种价格，但不假定其可从此 QMT 权益因子接口获得
    同一语义的公司行为。这里不直接重刷价格，任务会在本轮普通采集结束后统一执行。
    """
    snapshot_start = today - timedelta(days=ACTION_LOOKBACK_DAYS)
    factor_frame = xtdata.get_divid_factors(
        stock_code,
        start_time=snapshot_start.strftime("%Y%m%d"),
        end_time=today.strftime("%Y%m%d"),
    )
    if factor_frame is None:
        raise RuntimeError(f"empty QMT corporate-action response for {stock_code}")
    return sync_qmt_factor_snapshot(
        stock_code,
        factor_frame,
        snapshot_start,
        today,
        DATA_START_DATE,
    )


def get_code_universe() -> tuple[list[str], set[str]]:
    """返回去重且稳定顺序的 A 股/ETF 代码，并单独标记需要同步权益事件的 A 股集合。"""
    codes = []
    seen = set()
    a_share_codes = set()
    for sector in SECTORS:
        for stock_code in xtdata.get_stock_list_in_sector(sector) or []:
            if "." in str(stock_code) and stock_code not in seen:
                seen.add(stock_code)
                codes.append(stock_code)
            if sector == A_SHARE_SECTOR and "." in str(stock_code):
                a_share_codes.add(stock_code)
    return codes, a_share_codes


def get_all_codes() -> list[str]:
    return get_code_universe()[0]


def _earliest_start(latest_dates: dict[str, dict[str, str]], stock_code: str) -> str:
    """取三张投影表中最早游标，缺任意一种则从 ``DATA_START`` 回补。

    这里宁愿多拉少量重叠数据，也不让原始、前复权、后复权的起始日产生不可解释的缺口；
    存储层的 UPSERT 使重叠写入安全。
    """
    starts = [latest_dates[mode].get(stock_code) for mode in DIVIDEND_TYPES]
    if any(value is None for value in starts):
        return DATA_START
    return min(starts)


def main() -> int:
    """执行完整日任务：权益事实 → 三类价格投影 → 待执行的派生刷新。

    单只股票失败不会中断全市场采集；失败代码会汇总并导致非零退出码，供调度器告警。
    任务队列在所有普通增量写入后才执行，避免权益事件触发的历史重刷与本轮增量写入竞争。
    """
    xtdata.connect()
    latest_dates = {mode: get_existing_latest_dates(mode) for mode in DIVIDEND_TYPES}
    total_rows = {mode: 0 for mode in DIVIDEND_TYPES}
    failures = []
    action_counts = {"new": 0, "corrected": 0, "cancelled": 0, "tasks": 0}
    codes, a_share_codes = get_code_universe()
    today = date.today()
    for number, stock_code in enumerate(codes, start=1):
        start_date = _earliest_start(latest_dates, stock_code)
        try:
            if stock_code in a_share_codes:
                plan = sync_stock_actions(stock_code, today)
                for change in plan.changes:
                    action_counts[change.kind] += 1
                action_counts["tasks"] += len(plan.refresh_tasks)
            counts = download_and_save_all_modes(
                stock_code,
                start_date,
                adjustment_asof=get_adjustment_asof(stock_code),
            )
            for mode, count in counts.items():
                total_rows[mode] += count
            print(f"[{number}/{len(codes)}] {stock_code}: {counts}")
        except Exception as exc:
            failures.append(stock_code)
            print(f"[{number}/{len(codes)}] {stock_code}: failed - {type(exc).__name__}: {exc}")
    # 任务执行器只认识“股票、模式、起点”；闭包负责把它适配为本文件的 QMT 下载函数。
    def refresh_projection(stock_code: str, price_mode: str, refresh_from: date) -> int:
        return download_and_save_mode(
            stock_code,
            price_mode,
            refresh_from.strftime("%Y%m%d"),
            get_adjustment_asof(stock_code),
        )

    refresh = run_due_refresh_tasks(refresh_projection)
    print("[行情] raw=%(none)s qfq=%(front)s bfq=%(back)s" % total_rows)
    print(
        "[权益] 新增=%(new)s 修订=%(corrected)s 撤回=%(cancelled)s 刷新任务=%(tasks)s"
        % action_counts
    )
    print(
        "[刷新] 成功=%(done)s 失败=%(failed)s 重试=%(retried)s "
        "回收=%(reclaimed)s 已被新任务取代=%(superseded)s"
        % refresh
    )
    print(f"[结果] 股票成功={len(codes) - len(failures)} 股票失败={len(failures)}")
    return 1 if failures or refresh["failed"] else 0


if __name__ == "__main__":
    sys.exit(main())
