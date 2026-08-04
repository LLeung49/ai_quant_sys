"""QMT 权益事件快照与复权投影的持久化刷新任务。

原始价格和权益事件是可审计事实；前/后复权价格则是可随供应商修订重建的投影。
本模块只负责“识别权益变化并登记任务”，不直接下载行情。任务仅在价格刷新函数成功
写入非零行数后才标记完成，因此进程中断或 QMT 短暂失败不会丢失重刷请求。
"""

from dataclasses import dataclass
from datetime import date, datetime, timezone
from decimal import Decimal, InvalidOperation
import json
from typing import Callable, Iterable, Literal
from uuid import uuid4

try:
    from .db_config import execute_query, execute_update, get_connection
    from .price_refresh_tasks import (
        INSERT_REFRESH_TASK_SQL,
        MARK_TASK_DONE_SQL,
        MARK_TASK_FAILED_SQL,
        MARK_TASK_RUNNING_SQL,
        RECLAIM_STALE_TASKS_SQL,
        SELECT_PENDING_TASKS_SQL,
        merge_refresh_tasks,
    )
except ImportError:  # Direct script execution from src/data_ingestion.
    from db_config import execute_query, execute_update, get_connection
    from price_refresh_tasks import (
        INSERT_REFRESH_TASK_SQL,
        MARK_TASK_DONE_SQL,
        MARK_TASK_FAILED_SQL,
        MARK_TASK_RUNNING_SQL,
        RECLAIM_STALE_TASKS_SQL,
        SELECT_PENDING_TASKS_SQL,
        merge_refresh_tasks,
    )


DATA_SOURCE = "xtquant"  # 同一股票、除权日可保留不同供应商来源的事件快照。
TASK_REASON = "corporate_action_changed"  # 供任务表审计、聚合和排障使用。

ACTION_VALUE_FIELDS = (
    "cash_dividend_per_share",
    "stock_bonus_per_share",
    "stock_gift_per_share",
    "rights_issue_per_share",
    "rights_issue_price",
    "share_reform_flag",
    "qmt_dr_factor",
)

SELECT_ACTION_SNAPSHOT_SQL = """
-- 只比较本次完整回看窗口；窗口外历史事件不因每日快照被误判为撤回。（先查询数据库中同一股票、同一数据源、同一最近 10 天窗口内已经保存的权益事件））
SELECT stock_code, ex_date, cash_dividend_per_share,
       stock_bonus_per_share, stock_gift_per_share,
       rights_issue_per_share, rights_issue_price, share_reform_flag,
       qmt_dr_factor, event_status, data_source, source_payload
FROM trade_corporate_action
WHERE stock_code = %s AND data_source = %s
  AND ex_date BETWEEN %s AND %s
ORDER BY ex_date
"""

UPSERT_ACTION_SQL = """
-- 相同主键重复出现时更新供应商事实，并重新置为有效，保证日任务可幂等执行。
INSERT INTO trade_corporate_action
    (stock_code, ex_date, cash_dividend_per_share, stock_bonus_per_share,
     stock_gift_per_share, rights_issue_per_share, rights_issue_price,
     share_reform_flag, qmt_dr_factor, event_status, data_source, source_payload)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, 'effective', %s, %s)
ON DUPLICATE KEY UPDATE
    cash_dividend_per_share = VALUES(cash_dividend_per_share),
    stock_bonus_per_share = VALUES(stock_bonus_per_share),
    stock_gift_per_share = VALUES(stock_gift_per_share),
    rights_issue_per_share = VALUES(rights_issue_per_share),
    rights_issue_price = VALUES(rights_issue_price),
    share_reform_flag = VALUES(share_reform_flag),
    qmt_dr_factor = VALUES(qmt_dr_factor),
    event_status = 'effective',
    source_payload = VALUES(source_payload),
    last_seen_at = CURRENT_TIMESTAMP
"""

CANCEL_ACTION_SQL = """
-- 仅撤销本窗口内原先有效、但本次供应商已不再返回的事件，保留历史审计记录。
UPDATE trade_corporate_action
SET event_status = 'cancelled', last_seen_at = CURRENT_TIMESTAMP
WHERE stock_code = %s AND ex_date = %s AND data_source = %s
  AND event_status = 'effective'
"""


@dataclass(frozen=True)
class ActionChange:
    """一次快照比较发现的事件变化，供日志和刷新范围规划使用。"""
    kind: Literal["new", "corrected", "cancelled"]
    stock_code: str
    ex_date: date


@dataclass
class SnapshotPlan:
    """一次快照的可审计写入计划：先写事实，再以同一事务写派生刷新任务。"""
    changes: list[ActionChange]
    events_to_upsert: list[dict]
    events_to_cancel: list[tuple[str, date, str]]
    refresh_tasks: list[dict]


def _is_null(value) -> bool:
    if value is None:
        return True
    try:
        return bool(value != value)
    except (TypeError, ValueError):
        return False


def _decimal_text(value, places: int) -> str | None:
    """以固定小数位规范化数值，消除 float/Decimal 表示差异造成的伪修订。"""
    if _is_null(value):
        return None
    try:
        decimal_value = Decimal(str(value))
    except (InvalidOperation, ValueError) as exc:
        raise ValueError(f"Invalid QMT factor value: {value!r}") from exc
    quantum = Decimal(1).scaleb(-places)
    return format(decimal_value.quantize(quantum), f".{places}f")


def _json_value(value):
    if _is_null(value):
        return None
    if isinstance(value, Decimal):
        return str(value)
    if hasattr(value, "item"):
        value = value.item()
    return value


def _event_date(value) -> date:
    """兼容 QMT 可能返回的日期、时间戳和字符串，统一转为权益事件除权日。"""
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    if isinstance(value, (int, float)):
        digits = str(int(value))
        if len(digits) == 8:
            return datetime.strptime(digits, "%Y%m%d").date()
        seconds = float(value) / 1000 if float(value) > 10_000_000_000 else float(value)
        return datetime.fromtimestamp(seconds, tz=timezone.utc).date()
    text = str(value)
    if len(text) >= 10 and text[4] == "-":
        return date.fromisoformat(text[:10])
    digits = "".join(character for character in text if character.isdigit())
    if len(digits) >= 8:
        return datetime.strptime(digits[:8], "%Y%m%d").date()
    raise ValueError(f"Unexpected QMT ex-date value: {value!r}")


def normalize_qmt_factors(stock_code: str, factor_frame) -> list[dict]:
    """将 QMT ``get_divid_factors`` 转为稳定的数据库权益事实。

    原始 QMT 字段同时保存在 ``source_payload``，便于以后核对字段语义或供应商修订；
    用固定精度的文本保存可比较数值，避免二进制浮点误差反复触发重刷。
    """
    events = []
    if factor_frame is None:
        return events
    for index_value, row in factor_frame.iterrows():
        values = {
            name: row.get(name) if hasattr(row, "get") else row[name]
            for name in (
                "interest", "stockBonus", "stockGift", "allotNum",
                "allotPrice", "gugai", "dr",
            )
        }
        ex_date = _event_date(index_value)
        share_reform = _json_value(values["gugai"])
        share_reform = int(share_reform) if share_reform is not None else 0
        payload = {name: _json_value(value) for name, value in values.items()}
        payload["gugai"] = share_reform
        events.append(
            {
                "stock_code": stock_code,
                "ex_date": ex_date.isoformat(),
                "cash_dividend_per_share": _decimal_text(values["interest"], 8) or "0.00000000",
                "stock_bonus_per_share": _decimal_text(values["stockBonus"], 8) or "0.00000000",
                "stock_gift_per_share": _decimal_text(values["stockGift"], 8) or "0.00000000",
                "rights_issue_per_share": _decimal_text(values["allotNum"], 8) or "0.00000000",
                "rights_issue_price": _decimal_text(values["allotPrice"], 8),
                "share_reform_flag": share_reform,
                "qmt_dr_factor": _decimal_text(values["dr"], 16),
                "event_status": "effective",
                "data_source": DATA_SOURCE,
                "source_payload": payload,
            }
        )
    return sorted(events, key=lambda item: item["ex_date"])


def _key(event: dict) -> tuple[str, date, str]:
    return (
        event["stock_code"],
        _event_date(event["ex_date"]),
        event.get("data_source") or DATA_SOURCE,
    )


def _comparison_value(field: str, value):
    if field in {
        "cash_dividend_per_share", "stock_bonus_per_share",
        "stock_gift_per_share", "rights_issue_per_share", "rights_issue_price",
    }:
        return _decimal_text(value, 8)
    if field == "qmt_dr_factor":
        return _decimal_text(value, 16)
    if field == "share_reform_flag":
        return int(value or 0)
    return value


def _same_action(current: dict, stored: dict) -> bool:
    """只比较影响复权的字段；来源载荷格式变化本身不应触发昂贵的历史重刷。"""
    return (
        stored.get("event_status", "effective") == "effective"
        and all(
            _comparison_value(field, current.get(field))
            == _comparison_value(field, stored.get(field))
            for field in ACTION_VALUE_FIELDS
        )
    )


def _refresh_requests(
    stock_code: str,
    ex_date: date,
    data_start: date,
    include_back: bool,
) -> list[dict]:
    """按复权方向生成最小且正确的刷新范围。

    前复权的历史价格会受新事件影响，始终从 ``data_start`` 重刷。正常新增事件不会
    改变后复权历史；只有供应商修订或撤回历史事件时，才从该除权日重刷后复权。
    """
    requests = [
        {
            "stock_code": stock_code,
            "price_mode": "front",
            "refresh_from": data_start,
            "reason": TASK_REASON,
        }
    ]
    if include_back:
        requests.append(
            {
                "stock_code": stock_code,
                "price_mode": "back",
                "refresh_from": ex_date,
                "reason": TASK_REASON,
            }
        )
    return requests


def plan_factor_snapshot(
    current_events: Iterable[dict],
    stored_events: Iterable[dict],
    data_start: date,
) -> SnapshotPlan:
    """比较一个完整来源窗口，规划事实写入、撤回和派生价格重刷。

    “窗口完整”是撤回判断的前提：若接口只返回部分日期，不能把缺失项当成已撤回。
    ``merge_refresh_tasks`` 会把同股票、同模式的多项请求折叠为最早起点，减少重复历史下载。
    """
    current = list(current_events)
    stored = list(stored_events)
    current_by_key = {_key(item): item for item in current}
    stored_by_key = {_key(item): item for item in stored}
    changes = []
    cancellations = []
    tasks = []

    for action_key, item in current_by_key.items():
        old = stored_by_key.get(action_key)
        if old is None:
            kind = "new"
        elif _same_action(item, old):
            continue
        else:
            kind = "corrected"
        stock_code, ex_date, _ = action_key
        changes.append(ActionChange(kind, stock_code, ex_date))
        tasks.extend(
            _refresh_requests(
                stock_code,
                ex_date,
                data_start,
                include_back=(kind == "corrected"),
            )
        )

    for action_key, item in stored_by_key.items():
        if action_key in current_by_key or item.get("event_status") == "cancelled":
            continue
        stock_code, ex_date, source = action_key
        changes.append(ActionChange("cancelled", stock_code, ex_date))
        cancellations.append((stock_code, ex_date, source))
        tasks.extend(_refresh_requests(stock_code, ex_date, data_start, include_back=True))

    changes.sort(key=lambda item: (item.ex_date, item.stock_code, item.kind))
    return SnapshotPlan(
        changes=changes,
        events_to_upsert=current,
        events_to_cancel=cancellations,
        refresh_tasks=merge_refresh_tasks(tasks),
    )


def _event_values(event: dict) -> tuple:
    return (
        event["stock_code"],
        _event_date(event["ex_date"]),
        event["cash_dividend_per_share"],
        event["stock_bonus_per_share"],
        event["stock_gift_per_share"],
        event["rights_issue_per_share"],
        event.get("rights_issue_price"),
        event["share_reform_flag"],
        event.get("qmt_dr_factor"),
        event.get("data_source") or DATA_SOURCE,
        json.dumps(event.get("source_payload"), ensure_ascii=False, sort_keys=True),
    )


def _task_values(task: dict) -> tuple:
    return (
        task["stock_code"],
        task["price_mode"],
        task["refresh_from"],
        task["reason"],
    )


def _apply_snapshot_plan(cursor, plan: SnapshotPlan) -> None:
    """在调用方事务中按“事件事实 → 撤回标记 → 刷新任务”顺序写入计划。"""
    if plan.events_to_upsert:
        cursor.executemany(UPSERT_ACTION_SQL, [_event_values(item) for item in plan.events_to_upsert])
    if plan.events_to_cancel:
        cursor.executemany(CANCEL_ACTION_SQL, plan.events_to_cancel)
    if plan.refresh_tasks:
        cursor.executemany(INSERT_REFRESH_TASK_SQL, [_task_values(item) for item in plan.refresh_tasks])


def persist_snapshot_plan(
    plan: SnapshotPlan,
    connection_factory: Callable = get_connection,
) -> None:
    """原子写入权益快照与刷新任务，防止事实已变更而任务遗漏。"""
    connection = connection_factory()
    cursor = connection.cursor()
    try:
        _apply_snapshot_plan(cursor, plan)
        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        cursor.close()
        connection.close()


def sync_qmt_factor_snapshot(
    stock_code: str,
    factor_frame,
    snapshot_start: date,
    snapshot_end: date,
    data_start: date,
) -> SnapshotPlan:
    """读取同窗口旧快照、生成差异计划并落库；返回值可用于调用方日志统计。"""
    # 先查询数据库中同一股票、同一数据源、同一最近 10 天窗口内已经保存的权益事件
    existing = execute_query(
        SELECT_ACTION_SNAPSHOT_SQL,
        (stock_code, DATA_SOURCE, snapshot_start, snapshot_end),
    )
    # 对比新旧，得出“哪些事实要更新、哪些投影要重刷”，factor_frame是最新查到的权益事件
    plan = plan_factor_snapshot(
        normalize_qmt_factors(stock_code, factor_frame),
        existing,
        data_start,
    )
    persist_snapshot_plan(plan)
    return plan


def run_due_refresh_tasks(
    refresh_price: Callable[[str, str, date], object],
    lease_timeout_minutes: int = 60,
) -> dict[str, int]:
    """执行待处理/失败的投影刷新任务，并把失败保留给后续运行重试。

    先回收超过租约的 ``running`` 任务，处理崩溃遗留状态。随后为每项任务写入唯一
    ``claim_token``；完成/失败更新都带该令牌，避免两个进程中较晚结束的旧执行覆盖
    新执行的状态。
    """
    reclaimed = execute_update(RECLAIM_STALE_TASKS_SQL, (lease_timeout_minutes,))
    result = {
        "done": 0,
        "failed": 0,
        "retried": 0,
        "reclaimed": reclaimed,
        "superseded": 0,
    }
    for task in execute_query(SELECT_PENDING_TASKS_SQL):
        if task.get("retry_count", 0):
            result["retried"] += 1
        # 条件更新确保只有一个并发执行者能从 pending/failed 认领此任务。
        claim_token = str(uuid4())
        claimed = execute_update(MARK_TASK_RUNNING_SQL, (claim_token, task["id"]))
        if not claimed:
            continue
        try:
            refresh_result = refresh_price(
                task["stock_code"],
                task["price_mode"],
                task["refresh_from"],
            )
            if refresh_result is None or refresh_result is False:
                raise RuntimeError("price refresh returned no result")
            if isinstance(refresh_result, (int, float)) and refresh_result <= 0:
                raise RuntimeError("price refresh wrote zero rows")
        except Exception as exc:
            message = f"{type(exc).__name__}: {exc}"[:1000]
            if execute_update(
                MARK_TASK_FAILED_SQL,
                (message, claim_token, task["id"]),
            ):
                result["failed"] += 1
            else:
                result["superseded"] += 1
        else:
            if execute_update(MARK_TASK_DONE_SQL, (claim_token, task["id"])):
                result["done"] += 1
            else:
                result["superseded"] += 1
    return result
