from datetime import date
from decimal import Decimal
from pathlib import Path
import sys


SRC_DIR = Path(__file__).parents[1] / "src"
sys.path.insert(0, str(SRC_DIR))

from data_ingestion import price_corporate_actions as actions  # noqa: E402


DATA_START = date(2015, 1, 1)


def event(
    *,
    cash: str = "0.12000000",
    ex_date: str = "2026-07-01",
    status: str = "effective",
):
    return {
        "stock_code": "000001.SZ",
        "ex_date": ex_date,
        "cash_dividend_per_share": cash,
        "stock_bonus_per_share": "0.10000000",
        "stock_gift_per_share": "0.20000000",
        "rights_issue_per_share": "0.00000000",
        "rights_issue_price": None,
        "share_reform_flag": 1,
        "qmt_dr_factor": "0.9876543210987654",
        "event_status": status,
        "data_source": "xtquant",
        "source_payload": {
            "interest": float(cash),
            "stockBonus": 0.1,
            "stockGift": 0.2,
            "allotNum": 0,
            "allotPrice": None,
            "gugai": 1,
            "dr": "0.9876543210987654",
        },
    }


class OneRowFactorFrame:
    def iterrows(self):
        yield date(2026, 7, 1), {
            "interest": 0.12,
            "stockBonus": 0.1,
            "stockGift": 0.2,
            "allotNum": 0,
            "allotPrice": None,
            "gugai": 1,
            "dr": Decimal("0.9876543210987654"),
        }


def test_normalize_qmt_factor_frame_preserves_exact_adjustment_fields():
    assert actions.normalize_qmt_factors("000001.SZ", OneRowFactorFrame()) == [event()]


def test_new_event_persists_snapshot_and_only_queues_full_qfq_refresh():
    plan = actions.plan_factor_snapshot([event()], [], DATA_START)

    assert [change.kind for change in plan.changes] == ["new"]
    assert plan.events_to_upsert == [event()]
    assert plan.events_to_cancel == []
    assert plan.refresh_tasks == [
        {
            "stock_code": "000001.SZ",
            "price_mode": "front",
            "refresh_from": DATA_START,
            "reason": "corporate_action_changed",
        }
    ]


def test_corrected_event_queues_full_qfq_and_bfq_from_ex_date():
    corrected = event(cash="0.12000000")
    stored = event(cash="0.10000000")

    plan = actions.plan_factor_snapshot([corrected], [stored], DATA_START)

    assert [change.kind for change in plan.changes] == ["corrected"]
    assert plan.events_to_upsert == [corrected]
    assert plan.refresh_tasks == [
        {
            "stock_code": "000001.SZ",
            "price_mode": "front",
            "refresh_from": DATA_START,
            "reason": "corporate_action_changed",
        },
        {
            "stock_code": "000001.SZ",
            "price_mode": "back",
            "refresh_from": date(2026, 7, 1),
            "reason": "corporate_action_changed",
        },
    ]


def test_missing_stored_event_is_persisted_as_cancelled_and_refreshes_both_projections():
    stored = event()

    plan = actions.plan_factor_snapshot([], [stored], DATA_START)

    assert [change.kind for change in plan.changes] == ["cancelled"]
    assert plan.events_to_upsert == []
    assert plan.events_to_cancel == [("000001.SZ", date(2026, 7, 1), "xtquant")]
    assert [task["price_mode"] for task in plan.refresh_tasks] == ["front", "back"]
    assert plan.refresh_tasks[0]["refresh_from"] == DATA_START
    assert plan.refresh_tasks[1]["refresh_from"] == date(2026, 7, 1)


def test_unchanged_event_updates_snapshot_without_queuing_refresh():
    current = event()
    stored = event()

    plan = actions.plan_factor_snapshot([current], [stored], DATA_START)

    assert plan.changes == []
    assert plan.events_to_upsert == [current]
    assert plan.events_to_cancel == []
    assert plan.refresh_tasks == []


def test_snapshot_plan_is_committed_with_event_cancellation_and_durable_tasks():
    class RecordingCursor:
        def __init__(self):
            self.batches = []

        def executemany(self, sql, values):
            self.batches.append((sql, list(values)))

        def close(self):
            pass

    class RecordingConnection:
        def __init__(self):
            self.recording_cursor = RecordingCursor()
            self.committed = False
            self.closed = False

        def cursor(self):
            return self.recording_cursor

        def commit(self):
            self.committed = True

        def rollback(self):
            raise AssertionError("valid snapshot must not roll back")

        def close(self):
            self.closed = True

    connection = RecordingConnection()
    plan = actions.plan_factor_snapshot([], [event()], DATA_START)

    actions.persist_snapshot_plan(plan, connection_factory=lambda: connection)

    assert connection.committed
    assert connection.closed
    sql_text = "\n".join(sql for sql, _ in connection.recording_cursor.batches)
    assert "event_status = 'cancelled'" in sql_text
    assert "INSERT INTO trade_price_refresh_task" in sql_text


def test_failed_refresh_remains_durable_and_is_retried_then_marked_done(monkeypatch):
    task = {
        "id": 7,
        "stock_code": "000001.SZ",
        "price_mode": "front",
        "refresh_from": date(2015, 1, 1),
        "reason": "corporate_action_changed",
        "retry_count": 0,
    }
    status = {"value": "pending"}
    attempts = []

    def fake_query(sql, params=None):
        assert "status IN ('pending', 'failed')" in sql
        return [task] if status["value"] in {"pending", "failed"} else []

    def fake_update(sql, params=None):
        if sql == actions.RECLAIM_STALE_TASKS_SQL:
            return 0
        if "status = 'running'" in sql:
            status["value"] = "running"
        elif "status = 'failed'" in sql:
            status["value"] = "failed"
        elif "status = 'done'" in sql:
            status["value"] = "done"
        return 1

    def refresh_price(stock_code, price_mode, refresh_from):
        attempts.append((stock_code, price_mode, refresh_from))
        if len(attempts) == 1:
            raise RuntimeError("QMT unavailable")
        return 1

    monkeypatch.setattr(actions, "execute_query", fake_query)
    monkeypatch.setattr(actions, "execute_update", fake_update)

    first = actions.run_due_refresh_tasks(refresh_price)
    second = actions.run_due_refresh_tasks(refresh_price)

    assert first == {"done": 0, "failed": 1, "retried": 0, "reclaimed": 0}
    assert second == {"done": 1, "failed": 0, "retried": 0, "reclaimed": 0}
    assert status["value"] == "done"
    assert attempts == [
        ("000001.SZ", "front", date(2015, 1, 1)),
        ("000001.SZ", "front", date(2015, 1, 1)),
    ]


def test_task_is_not_marked_done_when_refresh_reports_failure(monkeypatch):
    task = {
        "id": 9,
        "stock_code": "000001.SZ",
        "price_mode": "back",
        "refresh_from": date(2026, 7, 1),
        "reason": "corporate_action_changed",
        "retry_count": 2,
    }
    updates = []
    monkeypatch.setattr(actions, "execute_query", lambda sql, params=None: [task])
    monkeypatch.setattr(
        actions,
        "execute_update",
        lambda sql, params=None: (
            updates.append((sql, params))
            or (0 if sql == actions.RECLAIM_STALE_TASKS_SQL else 1)
        ),
    )

    result = actions.run_due_refresh_tasks(
        lambda *_: (_ for _ in ()).throw(ValueError("empty market response"))
    )

    assert result == {"done": 0, "failed": 1, "retried": 1, "reclaimed": 0}
    assert not any("status = 'done'" in sql for sql, _ in updates)
    assert any("status = 'failed'" in sql for sql, _ in updates)


def test_zero_row_projection_refresh_is_failed_not_done(monkeypatch):
    task = {
        "id": 10,
        "stock_code": "000001.SZ",
        "price_mode": "front",
        "refresh_from": DATA_START,
        "reason": "corporate_action_changed",
        "retry_count": 0,
    }
    updates = []
    monkeypatch.setattr(actions, "execute_query", lambda sql, params=None: [task])
    monkeypatch.setattr(
        actions,
        "execute_update",
        lambda sql, params=None: (
            updates.append((sql, params))
            or (0 if sql == actions.RECLAIM_STALE_TASKS_SQL else 1)
        ),
    )

    result = actions.run_due_refresh_tasks(lambda *_: 0)

    assert result["failed"] == 1
    assert result["done"] == 0
    assert any("status = 'failed'" in sql for sql, _ in updates)


def test_stale_running_projection_task_is_reclaimed_after_crash(monkeypatch):
    task = {
        "id": 11,
        "stock_code": "000001.SZ",
        "price_mode": "front",
        "refresh_from": DATA_START,
        "reason": "corporate_action_changed",
        "retry_count": 1,
    }
    updates = []
    monkeypatch.setattr(actions, "execute_query", lambda sql, params=None: [task])
    monkeypatch.setattr(
        actions,
        "execute_update",
        lambda sql, params=None: updates.append((sql, params)) or 1,
    )

    result = actions.run_due_refresh_tasks(lambda *_: 3, lease_timeout_minutes=30)

    assert result == {
        "done": 1,
        "failed": 0,
        "retried": 1,
        "reclaimed": 1,
    }
    assert "status = 'running'" in updates[0][0]
    assert "retry_count = retry_count + 1" in updates[0][0]
    assert updates[0][1] == (30,)
