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

import argparse
import math
import sys
import threading
import time
from datetime import date, timedelta

try:
    from .qmt_data_gateway import QMTDataGateway
except ImportError:
    from qmt_data_gateway import QMTDataGateway

qmt_gateway = QMTDataGateway.from_env()


def set_gateway_for_test(gateway):
    global qmt_gateway
    qmt_gateway = gateway

from akshare_market_fallback import fetch_valid_rows
from db_config import execute_query
from market_volume_contract import normalize_to_lot
from price_corporate_actions import run_due_refresh_tasks, sync_qmt_factor_snapshot
from price_projection_store import (
    get_existing_latest_dates,
    write_daily_rows,
    write_daily_rows_batch,
)
try:
    from data_ingestion_qmt.price_projection_integrity import (
        audit_raw_qfq_projection,
        classify_projection_issues,
        find_raw_qfq_issues,
        load_raw_qfq_rows,
    )
    from data_ingestion_qmt.qfq_integrity_audit import (
        IntegrityFinding,
        build_source_fingerprint,
        upsert_integrity_finding,
    )
except ImportError:  # Direct execution from src/data_ingestion_qmt.
    from price_projection_integrity import (
        audit_raw_qfq_projection,
        classify_projection_issues,
        find_raw_qfq_issues,
        load_raw_qfq_rows,
    )
    from qfq_integrity_audit import (
        IntegrityFinding,
        build_source_fingerprint,
        upsert_integrity_finding,
    )


DATA_START = "20150101"
DATA_START_DATE = date(2015, 1, 1)
A_SHARE_SECTOR = "沪深A股"
ETF_SECTOR = "沪深ETF"
SECTORS = (A_SHARE_SECTOR, ETF_SECTOR)
DIVIDEND_TYPES = ("none", "front", "back")  # QMT 原始、前复权、后复权三种投影。
# 每日重复读取最近窗口：即使权益公告在之后被修订/撤回，也能被快照比较发现。
ACTION_LOOKBACK_DAYS = 10
# QMT 一次返回过多 DataFrame 会占用大量内存；按固定批次限制峰值并便于失败重试。
MARKET_BATCH_SIZE = 5
# 单只代码 download_history_data 的最长等待时间；超时则跳过下载、继续读已有本地缓存。
# qmt_gateway 对部分新上市代码的请求可能无限挂起，需要此保护。
DOWNLOAD_TIMEOUT_SECONDS = 45
MARKET_FIELDS = (
    "open", "high", "low", "close", "volume", "amount", "preClose", "suspendFlag",
)
REQUIRED_MARKET_FIELDS = ("open", "high", "low", "close", "volume", "amount")


def _progress(message: str) -> None:
    """Print collector progress immediately, including when stdout is redirected."""
    print(message, flush=True)

# 获取股票最近的权益日
SELECT_ADJUSTMENT_ASOF_SQL = """
-- 投影中已纳入的最新有效除权日，仅作数据血缘标记，不参与价格计算。
SELECT MAX(ex_date) AS adjustment_asof
FROM trade_corporate_action
WHERE stock_code = %s
  AND data_source = 'qmt_context'
  AND event_status = 'effective'
"""

SELECT_ADJUSTMENTS_ASOF_SQL = """
SELECT stock_code, MAX(ex_date) AS adjustment_asof
FROM trade_corporate_action
WHERE stock_code IN ({placeholders})
  AND data_source = 'qmt_context'
  AND event_status = 'effective'
GROUP BY stock_code
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


def _load_turnover_rates(
    gateway, stock_codes: list[str], start_date: str, end_date: str,
) -> dict[str, dict[str, float]]:
    """Read QMT historical turnover without blocking price persistence.

    Missing values stay ``NULL`` in QFQ/BFQ.  They must not be reconstructed
    from current float shares, which would distort historical factor inputs.
    """
    if not stock_codes:
        return {}
    try:
        return gateway.get_turnover_rate(stock_codes, start_date, end_date)
    except Exception as exc:
        _progress(
            f"[换手率缺失] QMT 查询失败 codes={len(stock_codes)} "
            f"start={start_date} end={end_date} error={type(exc).__name__}: {exc}"
        )
        return {}


def _apply_turnover_rates(
    rows: list[dict], rates_by_stock: dict[str, dict[str, float]],
) -> None:
    """Apply QMT fractional rates using the table's percentage convention."""
    for row in rows:
        compact_date = str(row["trade_date"]).replace("-", "")
        rate = rates_by_stock.get(str(row["stock_code"]), {}).get(compact_date)
        try:
            row["turnover_rate"] = (
                round(float(rate) * 100, 4) if math.isfinite(float(rate)) else None
            )
        except (TypeError, ValueError, OverflowError):
            row["turnover_rate"] = None


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


def _is_invalid_market_value(value) -> bool:
    """判断 QMT 核心行情值是否无法安全写入 MySQL 数值列。"""
    try:
        return not math.isfinite(float(value))
    except (TypeError, ValueError, OverflowError):
        return True


def _split_qmt_rows(stock_code: str, dataframe, dividend_type: str) -> tuple[list[dict], set[str]]:
    """把 QMT 行转为固定库表字段，保留原始行情特有的昨收和停牌标记。

    三个模式共享 OHLCV/成交额字段；只有 ``none`` 是交易事实，因而额外保存
    ``preClose`` 和 ``suspendFlag``。复权表的换手率在批量下载完成后由
    ``ContextInfo.get_turnover_rate`` 合并；QMT 未返回时才保留 ``None``。
    """
    rows = []
    dirty_dates = set()
    for index_value, row in dataframe.iterrows():
        trade_date = _as_trade_date(index_value)
        invalid_field = next(
            (
                field_name
                for field_name in REQUIRED_MARKET_FIELDS
                if _is_invalid_market_value(row[field_name])
            ),
            None,
        )
        if invalid_field is not None:
            _progress(
                "[行情无效值] "
                f"stock={stock_code} trade_date={trade_date} mode={dividend_type} "
                f"field={invalid_field} value={row[invalid_field]!r}; skipped row"
            )
            dirty_dates.add(trade_date)
            continue
        item = {
            "stock_code": stock_code,
            "trade_date": trade_date,
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
            item["data_source"] = "qmt_context"
        else:
            item["turnover_rate"] = None
        rows.append(item)
    return rows, dirty_dates


def _rows_from_dataframe(stock_code: str, dataframe, dividend_type: str) -> list[dict]:
    """Compatibility wrapper for callers that only need valid QMT rows."""
    return _split_qmt_rows(stock_code, dataframe, dividend_type)[0]


def _rows_from_fallback(stock_code: str, rows_by_date: dict[str, dict], dividend_type: str) -> list[dict]:
    rows = []
    for trade_date, values in rows_by_date.items():
        if any(_is_invalid_market_value(values.get(field)) for field in REQUIRED_MARKET_FIELDS):
            continue
        try:
            volume = normalize_to_lot(
                values["amount"], values["close"], values["volume"]
            )
        except ValueError:
            continue
        item = {
            "stock_code": stock_code,
            "trade_date": trade_date,
            "open_price": float(values["open"]),
            "high_price": float(values["high"]),
            "low_price": float(values["low"]),
            "close_price": float(values["close"]),
            "volume": volume,
            "amount": float(values["amount"]),
        }
        if dividend_type == "none":
            item["pre_close"] = None
            item["suspend_flag"] = None
            item["data_source"] = "akshare"
        else:
            item["turnover_rate"] = None
        rows.append(item)
    return rows


def _classify_fallback_failures(
    failures: dict[str, str], asof: str | None = None,
) -> tuple[dict[str, str], dict[str, str]]:
    """Separate today's not-yet-published rows from actual fallback failures."""
    today_text = asof or date.today().isoformat()
    pending = {
        trade_date: reason
        for trade_date, reason in failures.items()
        if trade_date == today_text
    }
    failed = {
        trade_date: reason
        for trade_date, reason in failures.items()
        if trade_date != today_text
    }
    return pending, failed


def _rows_with_fallback(stock_code: str, dataframe, dividend_type: str) -> tuple[list[dict], dict[str, str]]:
    rows, dirty_dates = _split_qmt_rows(stock_code, dataframe, dividend_type)
    if not dirty_dates:
        return rows, {}
    fallback_rows, failures = fetch_valid_rows(stock_code, dividend_type, dirty_dates)
    rows.extend(_rows_from_fallback(stock_code, fallback_rows, dividend_type))
    if failures:
        pending, failed = _classify_fallback_failures(failures)
        if pending:
            _progress(
                f"[行情待补] stock={stock_code} mode={dividend_type} "
                f"dates={sorted(pending)} reasons={pending}"
            )
        if failed:
            _progress(
                f"[行情回退失败] stock={stock_code} mode={dividend_type} "
                f"dates={sorted(failed)} reasons={failed}"
            )
    return rows, failures


def _fetch_mode_rows(
    stock_code: str,
    dividend_type: str,
    start_date: str,
)-> list[dict]:
    """下载并幂等写入一个价格模式，返回实际写入的行数。

    ``start_date`` 由三张表中最早的游标决定，保证它们日期对齐。供应商返回空表、
    或转换后没有有效行，都抛出异常：调用者会保留该股票失败记录，后续运行可重试。
    ``adjustment_asof`` 只随前/后复权行写入，表示该投影使用的权益事件版本。
    """
    if dividend_type not in DIVIDEND_TYPES:
        raise ValueError(f"Unsupported dividend type: {dividend_type}")
    qmt_gateway.download_history_data(stock_code, "1d", start_time=start_date)
    data = qmt_gateway.get_market_data_ex(
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
    rows, fallback_failures = _rows_with_fallback(stock_code, dataframe, dividend_type)
    if not rows:
        raise RuntimeError(
            f"QMT returned no valid {MODE_LABELS[dividend_type]} rows for {stock_code}"
        )
    _, hard_failures = _classify_fallback_failures(fallback_failures)
    if hard_failures:
        raise RuntimeError(
            f"AkShare could not repair {MODE_LABELS[dividend_type]} rows for {stock_code}: "
            f"{sorted(hard_failures)}"
        )
    return rows


def download_and_save_mode(
    stock_code: str,
    dividend_type: str,
    start_date: str,
    adjustment_asof: date | None,
) -> int:
    """Fetch and persist one mode for the existing single-mode refresh path."""
    rows = _fetch_mode_rows(stock_code, dividend_type, start_date)
    write_daily_rows(dividend_type, rows, adjustment_asof)
    return len(rows)


def download_and_save_all_modes(
    stock_code: str, start_date: str, adjustment_asof: date | None = None,
) -> dict[str, int]:
    """按固定顺序拉取原始、前复权、后复权；三者从同一起点重新对齐。"""
    rows_by_mode = {
        dividend_type: _fetch_mode_rows(stock_code, dividend_type, start_date)
        for dividend_type in DIVIDEND_TYPES
    }
    issues = find_raw_qfq_issues(rows_by_mode["none"], rows_by_mode["front"])
    hard_candidate_issues = [
        issue for issue in issues if issue.reason != "qfq_ohlc_affine_mismatch"
    ]
    if hard_candidate_issues:
        sample = ", ".join(
            f"{issue.trade_date}:{issue.reason}" for issue in hard_candidate_issues[:3]
        )
        raise RuntimeError(
            f"raw/qfq candidate integrity failed for {stock_code}: {sample}"
        )
    counts = {}
    for dividend_type, rows in rows_by_mode.items():
        write_daily_rows(dividend_type, rows, adjustment_asof)
        counts[dividend_type] = len(rows)
    return counts


def _fetch_qmt_audit_rows(
    stock_code: str, dividend_type: str, trade_dates: set[str],
) -> list[dict]:
    """Read current QMT evidence for only the non-affine dates under audit."""
    if not trade_dates:
        return []
    compact_dates = sorted(trade_date.replace("-", "") for trade_date in trade_dates)
    data = qmt_gateway.get_market_data_ex(
        field_list=list(MARKET_FIELDS),
        stock_list=[stock_code],
        period="1d",
        start_time=compact_dates[0],
        end_time=compact_dates[-1],
        dividend_type=dividend_type,
    )
    dataframe = data.get(stock_code) if data else None
    if dataframe is None or len(dataframe) == 0:
        raise RuntimeError(
            f"empty QMT {MODE_LABELS[dividend_type]} evidence for {stock_code}"
        )
    rows, _ = _split_qmt_rows(stock_code, dataframe, dividend_type)
    return [row for row in rows if row["trade_date"] in trade_dates]


def _record_integrity_finding(
    stock_code: str, trade_date: str, check_code: str, severity: str,
    status: str, raw_row: dict | None, qfq_row: dict | None,
    last_error: str | None = None, note: str | None = None,
) -> None:
    upsert_integrity_finding(IntegrityFinding(
        stock_code=stock_code,
        trade_date=trade_date,
        check_code=check_code,
        severity=severity,
        status=status,
        raw_ohlc=raw_row,
        qfq_ohlc=qfq_row,
        source_fingerprint=build_source_fingerprint(raw_row, qfq_row),
        validator_version="qmt-v2",
        last_error=last_error,
        note=note,
    ))


def _verify_audit_issues(stock_code: str, issues):
    """Classify only QMT non-affine rows; source query failures stay hard."""
    stored_raw, stored_qfq = load_raw_qfq_rows(stock_code)
    affected_dates = {
        issue.trade_date for issue in issues
        if issue.reason == "qfq_ohlc_affine_mismatch"
    }
    if not affected_dates:
        return classify_projection_issues(
            issues, stored_raw, stored_qfq, [], []
        ), stored_raw, stored_qfq
    qmt_raw = _fetch_qmt_audit_rows(stock_code, "none", affected_dates)
    qmt_qfq = _fetch_qmt_audit_rows(stock_code, "front", affected_dates)
    return (
        classify_projection_issues(issues, stored_raw, stored_qfq, qmt_raw, qmt_qfq),
        stored_raw,
        stored_qfq,
    )


def audit_and_repair_projection(
    stock_code: str, adjustment_asof: date | None,
) -> dict[str, int]:
    """Rebuild one independently projected instrument only after an audit fails.

    The repair always starts at the managed history boundary.  A candidate is
    validated in memory by :func:`download_and_save_all_modes` before it can
    overwrite any of the independent raw/QFQ/BFQ projections, and the stored
    result is immediately re-audited.
    """
    try:
        issues = audit_raw_qfq_projection(stock_code)
        if not issues:
            return {"detected": 0, "repaired": 0, "failed": 0}
        decision, stored_raw, stored_qfq = _verify_audit_issues(stock_code, issues)
        raw_by_date = {str(row["trade_date"]): row for row in stored_raw}
        qfq_by_date = {str(row["trade_date"]): row for row in stored_qfq}
        for exception in decision.verified_exceptions:
            _record_integrity_finding(
                stock_code, exception.trade_date, exception.check_code,
                "warning", exception.status,
                raw_by_date.get(exception.trade_date), qfq_by_date.get(exception.trade_date),
                note="QMT raw/front response matches stored non-affine pair",
            )
        if not decision.hard_issues:
            _progress(
                f"[raw/qfq integrity] stock={stock_code} "
                f"action=qmt_verified_exception count={len(decision.verified_exceptions)}"
            )
            return {"detected": len(issues), "repaired": 0, "failed": 0}
        issues = decision.hard_issues
        for issue in issues:
            _record_integrity_finding(
                stock_code, issue.trade_date, issue.reason, "error", "repair_pending",
                raw_by_date.get(issue.trade_date), qfq_by_date.get(issue.trade_date),
                note="QMT source differs from storage or hard integrity check failed",
            )
        sample = ", ".join(
            f"{issue.trade_date}:{issue.reason}" for issue in issues[:3]
        )
        _progress(
            f"[raw/qfq integrity] stock={stock_code} issues={len(issues)} "
            f"sample={sample}; action=full_rebuild"
        )
        download_and_save_all_modes(stock_code, DATA_START, adjustment_asof)
        remaining = audit_raw_qfq_projection(stock_code)
        post_decision, post_raw, post_qfq = _verify_audit_issues(stock_code, remaining)
        if post_decision.hard_issues:
            raise RuntimeError(
                f"post-repair audit still has {len(post_decision.hard_issues)} hard issue(s)"
            )
        for exception in post_decision.verified_exceptions:
            _record_integrity_finding(
                stock_code, exception.trade_date, exception.check_code,
                "warning", exception.status,
                {str(row["trade_date"]): row for row in post_raw}.get(exception.trade_date),
                {str(row["trade_date"]): row for row in post_qfq}.get(exception.trade_date),
                note="QMT raw/front response matches stored non-affine pair after rebuild",
            )
    except Exception as exc:
        _progress(
            f"[raw/qfq integrity] stock={stock_code} action=repair_failed "
            f"error={type(exc).__name__}: {exc}"
        )
        return {"detected": int("issues" in locals()), "repaired": 0, "failed": 1}
    _progress(
        f"[raw/qfq integrity] stock={stock_code} action=repaired_verified"
    )
    return {"detected": 1, "repaired": 1, "failed": 0}


def _download_one_with_timeout(stock_code: str, start_date: str) -> bool:
    """在独立守护线程中下载单只代码历史缓存，超时后返回 False 并继续主流程。

    ``download_history_data`` 对部分新上市代码会无限阻塞（qmt_gateway 服务端不返回）；
    此函数把阻塞隔离在守护线程内，主线程最多等待 ``DOWNLOAD_TIMEOUT_SECONDS`` 秒。
    超时后线程继续在后台运行（daemon），不会阻止进程退出；下次运行可能已完成写盘。
    """
    done = threading.Event()
    exc_holder: list[BaseException | None] = [None]

    def _run() -> None:
        try:
            qmt_gateway.download_history_data(stock_code, "1d", start_date, "")
        except Exception as exc:
            exc_holder[0] = exc
        finally:
            done.set()

    t = threading.Thread(target=_run, daemon=True, name=f"dl-{stock_code}")
    t.start()
    completed = done.wait(timeout=DOWNLOAD_TIMEOUT_SECONDS)
    if not completed:
        _progress(
            f"[下载超时] {stock_code} start={start_date} "
            f"超过 {DOWNLOAD_TIMEOUT_SECONDS}s，跳过等待、继续读已有本地缓存"
        )
    elif exc_holder[0] is not None:
        _progress(
            f"[下载异常] {stock_code}: "
            f"{type(exc_holder[0]).__name__}: {exc_holder[0]}"
        )
    return completed


def _download_history_batch(stock_codes: list[str], start_date: str) -> set[str]:
    """逐只代码下载日线缓存，每只都有独立超时保护；返回超时代码集合。

    原先使用 ``download_history_data2`` 批量接口，但该接口对部分新上市代码会无限
    挂起（qmt_gateway 服务端对这些代码的请求永不返回）。改为逐只调用并隔离超时，单只代码
    挂起不会阻塞整批。下载只与原始日线缓存有关，不需要为三种 dividend_type 重复执行。
    返回超时代码集合，供上层对这些代码触发 AkShare 降级采集。
    """
    timed_out: set[str] = set()
    for stock_code in stock_codes:
        completed = _download_one_with_timeout(stock_code, start_date)
        if not completed:
            timed_out.add(stock_code)
    return timed_out


def _akshare_fallback_for_timeout(
    stock_code: str,
    start_date: str,
    adjustment_asof: date | None,
    counts: dict[str, int],
    failed_codes: set[str],
) -> None:
    """对 qmt_gateway 下载超时的代码，逐模式从 AkShare 拉取全量日线并写库。

    start_date 到今天的全部日期都是"目标日期"；AkShare 返回哪天就写哪天，
    不强制要求每天都在。写入成功（任意模式有行）则从失败集合移除该代码，
    三个模式全部失败才保留为失败。
    日志前缀 ``[QMT超时→AkShare降级]`` 便于日志聚合过滤。
    """
    today_str = date.today().isoformat()
    # 生成 start_date 到 today 的所有日期作为目标（AkShare 会忽略非交易日）
    start_dt = date(int(start_date[:4]), int(start_date[4:6]), int(start_date[6:8]))
    all_dates: set[str] = set()
    cur = start_dt
    while cur <= date.today():
        all_dates.add(cur.isoformat())
        cur += timedelta(days=1)

    candidates: dict[str, list[dict]] = {}
    for dividend_type in DIVIDEND_TYPES:
        try:
            fallback_rows, failures = fetch_valid_rows(stock_code, dividend_type, all_dates)
            rows = _rows_from_fallback(stock_code, fallback_rows, dividend_type)
            if not rows:
                reason_sample = list(failures.values())[:2] if failures else ["no rows returned"]
                _progress(
                    f"[QMT超时→AkShare降级] {stock_code} mode={dividend_type} "
                    f"AkShare 无数据：{reason_sample}"
                )
                continue
            candidates[dividend_type] = rows
            # 统计有多少日期真正被 AkShare 填入
            filled = len(fallback_rows)
            pending_today = today_str in failures
            hard_fail_count = sum(
                1 for d, r in failures.items() if d != today_str
            )
            _progress(
                f"[QMT超时→AkShare降级] {stock_code} mode={dividend_type} "
                f"已写入={len(rows)} 日期={filled} "
                f"今日待发布={int(pending_today)} 永久失败={hard_fail_count}"
            )
        except Exception as exc:
            _progress(
                f"[QMT超时→AkShare降级] {stock_code} mode={dividend_type} "
                f"异常 {type(exc).__name__}: {exc}"
            )
    any_written = False
    if len(candidates) == len(DIVIDEND_TYPES):
        issues = find_raw_qfq_issues(candidates["none"], candidates["front"])
        if issues:
            _progress(
                f"[raw/qfq integrity] stock={stock_code} action=reject_akshare_candidate "
                f"issues={len(issues)}"
            )
        else:
            for dividend_type, rows in candidates.items():
                write_daily_rows(dividend_type, rows, adjustment_asof)
                counts[dividend_type] = counts.get(dividend_type, 0) + len(rows)
            any_written = True
    if any_written:
        failed_codes.discard(stock_code)
    else:
        _progress(
            f"[QMT超时→AkShare降级] {stock_code} 三种模式均无数据，保留为失败"
        )


def download_and_save_batch(
    stock_codes: list[str],
    start_date: str,
    adjustment_asofs: dict[str, date | None],
) -> tuple[dict[str, int], list[str]]:
    """批量下载并写入多只同起点股票的 raw/qfq/bfq 日线。

    QMT 对每种 ``dividend_type`` 接受一组代码并返回 ``{代码: DataFrame}``。每种模式
    只查询一次、每批日线只下载一次，再把所有有效行一次写入目标表。某一股票缺少任一
    模式时，只将该股票加入失败列表，其他股票与其他模式仍可正常落库。
    QMT 下载超时的代码会自动降级到 AkShare 全量拉取；三种模式均无 AkShare 数据时
    才最终标记为失败。
    """
    if not stock_codes:
        return {mode: 0 for mode in DIVIDEND_TYPES}, []
    started_at = time.monotonic()
    _progress(
        f"[行情批次] start={start_date} codes={len(stock_codes)} "
        "阶段=开始下载历史缓存"
    )
    xtdata_timed_out = _download_history_batch(stock_codes, start_date)
    _progress(
        f"[行情批次] start={start_date} codes={len(stock_codes)} "
        f"阶段=历史缓存下载完成 elapsed={time.monotonic() - started_at:.1f}s"
        + (f" 超时={len(xtdata_timed_out)}" if xtdata_timed_out else "")
    )
    counts = {mode: 0 for mode in DIVIDEND_TYPES}
    failed_codes = set()
    candidates: dict[str, dict[str, list[dict]]] = {
        stock_code: {} for stock_code in stock_codes
    }
    for dividend_type in DIVIDEND_TYPES:
        mode_started_at = time.monotonic()
        mode_label = MODE_LABELS[dividend_type]
        _progress(
            f"[行情批次] start={start_date} codes={len(stock_codes)} "
            f"阶段=开始读取{mode_label} ({dividend_type})"
        )
        data = qmt_gateway.get_market_data_ex(
            field_list=list(MARKET_FIELDS),
            stock_list=stock_codes,
            period="1d",
            start_time=start_date,
            dividend_type=dividend_type,
        )
        rows = []
        for stock_code in stock_codes:
            if stock_code in xtdata_timed_out:
                # 超时代码不在此处处理，统一由后面的降级逻辑负责
                continue
            dataframe = data.get(stock_code) if data else None
            if dataframe is None or len(dataframe) == 0:
                failed_codes.add(stock_code)
                continue
            code_rows, fallback_failures = _rows_with_fallback(
                stock_code, dataframe, dividend_type
            )
            if not code_rows:
                failed_codes.add(stock_code)
                continue
            _, hard_failures = _classify_fallback_failures(fallback_failures)
            if hard_failures:
                failed_codes.add(stock_code)
            candidates[stock_code][dividend_type] = code_rows
            rows.extend(code_rows)
        missing = sum(
            1
            for code in stock_codes
            if code not in xtdata_timed_out
            and (data is None or data.get(code) is None or len(data.get(code)) == 0)
        )
        _progress(
            f"[行情批次] start={start_date} codes={len(stock_codes)} "
            f"阶段={mode_label}读取完成 rows={len(rows)} "
            f"missing={missing} "
            f"elapsed={time.monotonic() - mode_started_at:.1f}s"
        )
    safe_rows = {mode: [] for mode in DIVIDEND_TYPES}
    for stock_code in stock_codes:
        if stock_code in xtdata_timed_out or stock_code in failed_codes:
            continue
        candidate = candidates[stock_code]
        if any(mode not in candidate for mode in DIVIDEND_TYPES):
            failed_codes.add(stock_code)
            continue
        issues = find_raw_qfq_issues(candidate["none"], candidate["front"])
        if issues:
            failed_codes.add(stock_code)
            _progress(
                f"[raw/qfq integrity] stock={stock_code} action=reject_candidate "
                f"issues={len(issues)}"
            )
            continue
        for dividend_type in DIVIDEND_TYPES:
            safe_rows[dividend_type].extend(candidate[dividend_type])

    turnover_codes = sorted({row["stock_code"] for row in safe_rows["front"]})
    turnover_rates = _load_turnover_rates(
        qmt_gateway,
        turnover_codes,
        start_date,
        date.today().strftime("%Y%m%d"),
    )
    for dividend_type in ("front", "back"):
        _apply_turnover_rates(safe_rows[dividend_type], turnover_rates)
    for dividend_type, rows in safe_rows.items():
        if rows:
            write_daily_rows_batch(dividend_type, rows, adjustment_asofs)
            counts[dividend_type] = len(rows)

    # QMT 超时代码：逐只触发 AkShare 降级采集
    for stock_code in xtdata_timed_out:
        failed_codes.add(stock_code)  # 先标记失败，akshare 成功后会移除
        _akshare_fallback_for_timeout(
            stock_code,
            start_date,
            adjustment_asofs.get(stock_code),
            counts,
            failed_codes,
        )

    return counts, sorted(failed_codes)



def get_adjustment_asof(stock_code: str) -> date | None:
    """返回该股票已生效权益事件的最新除权日，作为复权行的可追溯版本标记。"""
    rows = execute_query(SELECT_ADJUSTMENT_ASOF_SQL, (stock_code,))
    return rows[0]["adjustment_asof"] if rows and rows[0]["adjustment_asof"] else None


def get_adjustment_asofs(stock_codes: list[str]) -> dict[str, date | None]:
    """一次查询所有代码的最新有效权益事件日期。"""
    result = {stock_code: None for stock_code in stock_codes}
    if not stock_codes:
        return result
    placeholders = ", ".join(["%s"] * len(stock_codes))
    rows = execute_query(
        SELECT_ADJUSTMENTS_ASOF_SQL.format(placeholders=placeholders),
        tuple(stock_codes),
    )
    for row in rows:
        result[row["stock_code"]] = row["adjustment_asof"] or None
    return result


def sync_stock_actions(stock_code: str, today: date):
    """保存最近完整权益窗口，并把需要重刷的前/后复权范围写入持久任务表。

    仅 A 股调用此方法；ETF 仍采集三种价格，但不假定其可从此 QMT 权益因子接口获得
    同一语义的公司行为。这里不直接重刷价格，任务会在本轮普通采集结束后统一执行。
    """
    snapshot_start = today - timedelta(days=ACTION_LOOKBACK_DAYS)
    factor_frame = qmt_gateway.get_divid_factors(
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
        for stock_code in qmt_gateway.get_stock_list_in_sector(sector) or []:
            if "." in str(stock_code) and stock_code not in seen:
                seen.add(stock_code)
                codes.append(stock_code)
            if sector == A_SHARE_SECTOR and "." in str(stock_code):
                a_share_codes.add(stock_code)
    return codes, a_share_codes


def get_all_codes() -> list[str]:
    return get_code_universe()[0]


_EPOCH_OPEN_DATE = {"0", "19700101"}  # qmt_gateway 对「上市日期未同步」的占位值。
_NEW_CODE_FALLBACK_YEARS = 2          # OpenDate 无效时的安全回退跨度（年）。


def _new_code_start(stock_code: str, today: date) -> str:
    """为从未入库的代码计算合理的下载起点。

    优先使用 qmt_gateway instrument detail 中的 ``OpenDate``（格式 ``YYYYMMDD``）；
    如果 OpenDate 是占位值（0 / 19700101）或晚于今天，则回退到今天往前
    ``_NEW_CODE_FALLBACK_YEARS`` 年，保证不会从 DATA_START(2015) 拉 11 年的数据。
    最终结果被 DATA_START 下限截断，确保不超出数据库已有最早边界。
    """
    detail = qmt_gateway.get_instrument_detail(stock_code) or {}
    open_date_str = str(detail.get("OpenDate", "0")).strip()
    if open_date_str not in _EPOCH_OPEN_DATE and len(open_date_str) == 8:
        try:
            open_date = date(
                int(open_date_str[:4]),
                int(open_date_str[4:6]),
                int(open_date_str[6:8]),
            )
            if DATA_START_DATE <= open_date <= today:
                _progress(
                    f"[新代码起点] {stock_code} OpenDate={open_date_str} "
                    "→ 使用上市日作为下载起点"
                )
                return open_date_str
        except ValueError:
            pass
    # OpenDate 无效：从近 N 年开始，避免从 2015 年起拉全量
    fallback = max(
        DATA_START_DATE,
        date(today.year - _NEW_CODE_FALLBACK_YEARS, today.month, today.day),
    )
    _progress(
        f"[新代码起点] {stock_code} OpenDate={open_date_str!r} 无效 "
        f"→ 回退至 {fallback.strftime('%Y%m%d')}"
    )
    return fallback.strftime("%Y%m%d")


def _earliest_start(
    latest_dates: dict[str, dict[str, str]],
    stock_code: str,
    today: date | None = None,
) -> str:
    """取三张投影表中最早游标；代码从未入库时用上市日（而非 DATA_START）作起点。

    对已有游标的代码，仍选三表中最早游标，保证 raw/qfq/bfq 日期对齐；
    存储层的 UPSERT 使重叠写入安全。
    对全新代码，调用 ``_new_code_start`` 避免从 2015 年发起不必要的全量下载。
    """
    starts = [latest_dates[mode].get(stock_code) for mode in DIVIDEND_TYPES]
    if any(value is None for value in starts):
        # A partially populated projection is an integrity incident, not a
        # newly listed instrument.  Rebuild it from the managed history floor
        # so raw/QFQ/BFQ regain the same coverage before incrementing again.
        if any(value is not None for value in starts):
            return DATA_START
        return _new_code_start(stock_code, today or date.today())
    return min(starts)


def _chunks(items: list[str], size: int):
    """以固定大小切分同起点代码，控制 QMT 返回 DataFrame 的内存峰值。"""
    for offset in range(0, len(items), size):
        yield items[offset:offset + size]


def main(skip_equity_snapshot: bool = False) -> int:
    """执行完整日任务：权益事实 → 三类价格投影 → 待执行的派生刷新。

    单只股票失败不会中断全市场采集；失败代码会汇总并导致非零退出码，供调度器告警。
    任务队列在所有普通增量写入后才执行，避免权益事件触发的历史重刷与本轮增量写入竞争。
    """
    qmt_gateway.connect()
    latest_dates = {mode: get_existing_latest_dates(mode) for mode in DIVIDEND_TYPES}
    total_rows = {mode: 0 for mode in DIVIDEND_TYPES}
    failures = []
    action_counts = {"new": 0, "corrected": 0, "cancelled": 0, "tasks": 0}
    codes, a_share_codes = get_code_universe()
    today = date.today()
    # 权益快照仍逐 A 股同步；普通日线随后按相同增量起点分组批量请求 QMT。
    codes_by_start: dict[str, list[str]] = {}
    adjustment_asofs = get_adjustment_asofs(codes)
    if skip_equity_snapshot:
        _progress("[权益快照] 已跳过（命令行参数 --skip-equity-snapshot）")
    for number, stock_code in enumerate(codes, start=1):
        try:
            if not skip_equity_snapshot and stock_code in a_share_codes:
                plan = sync_stock_actions(stock_code, today)
                for change in plan.changes:
                    action_counts[change.kind] += 1
                action_counts["tasks"] += len(plan.refresh_tasks)
            start_date = _earliest_start(latest_dates, stock_code, today)
            codes_by_start.setdefault(start_date, []).append(stock_code)
        except Exception as exc:
            failures.append(stock_code)
            print(f"[权益 {number}/{len(codes)}] {stock_code}: failed - {type(exc).__name__}: {exc}")
        if number == 1 or number % 100 == 0 or number == len(codes):
            _progress(
                f"[权益快照] {number}/{len(codes)} "
                f"成功={number - len(failures)} 失败={len(failures)}"
            )

    batch_number = 0
    batch_count = sum(
        (len(stock_codes) + MARKET_BATCH_SIZE - 1) // MARKET_BATCH_SIZE
        for stock_codes in codes_by_start.values()
    )
    for start_date in sorted(codes_by_start):
        for stock_batch in _chunks(codes_by_start[start_date], MARKET_BATCH_SIZE):
            batch_number += 1
            batch_adjustment_asofs = {
                stock_code: adjustment_asofs[stock_code]
                for stock_code in stock_batch
            }
            try:
                print(
                    f"[行情批次 {batch_number}/{batch_count}] start={start_date} "
                    f"codes={len(stock_batch)} 阶段=进入QMT请求",
                    flush=True,
                )
                counts, batch_failures = download_and_save_batch(
                    stock_batch,
                    start_date,
                    batch_adjustment_asofs,
                )
            except Exception as exc:
                failures.extend(stock_batch)
                _progress(
                    f"[行情批次 {batch_number}/{batch_count}] start={start_date} "
                    f"codes={len(stock_batch)}: failed - {type(exc).__name__}: {exc}"
                )
                continue
            for mode, count in counts.items():
                total_rows[mode] += count
            failures.extend(batch_failures)
            _progress(
                f"[行情批次 {batch_number}/{batch_count}] start={start_date} "
                f"codes={len(stock_batch)} raw={counts['none']} qfq={counts['front']} "
                f"bfq={counts['back']} failed={len(batch_failures)}"
            )
    # 任务执行器只认识“股票、模式、起点”；闭包负责把它适配为本文件的 QMT 下载函数。
    integrity_counts = {"detected": 0, "repaired": 0, "failed": 0}
    for stock_code in codes:
        result = audit_and_repair_projection(
            stock_code, adjustment_asofs.get(stock_code)
        )
        for key, value in result.items():
            integrity_counts[key] += value
        if result["failed"]:
            failures.append(stock_code)

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
        "[raw/qfq integrity] detected=%(detected)s repaired=%(repaired)s failed=%(failed)s"
        % integrity_counts
    )
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
    parser = argparse.ArgumentParser(description="采集原始行情与复权日线数据")
    parser.add_argument(
        "--skip-equity-snapshot",
        action="store_true",
        help="跳过权益快照同步，仅采集行情数据",
    )
    args = parser.parse_args()
    sys.exit(main(skip_equity_snapshot=args.skip_equity_snapshot))


