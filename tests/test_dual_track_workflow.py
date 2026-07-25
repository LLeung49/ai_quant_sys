"""End-to-end contracts for the independent market-data workflow.

Every external QMT and MySQL boundary is replaced with a deterministic fake.
The tests exercise the real normalization, storage routing, corporate-action
planning, retry lifecycle, reconciliation, and legacy repair queue logic.
"""

from datetime import date
from decimal import Decimal
import importlib.util
from pathlib import Path
import sys
import types


ROOT_DIR = Path(__file__).parents[1]
SRC_DIR = ROOT_DIR / "src"
INGESTION_DIR = SRC_DIR / "data_ingestion"
COLLECTOR_PATH = INGESTION_DIR / "8-原始行情与复权数据采集.py"
RECONCILIATION_PATH = INGESTION_DIR / "9-前复权对账与定向重刷.py"
sys.path.insert(0, str(SRC_DIR))

from data_ingestion import price_corporate_actions as actions  # noqa: E402
from data_ingestion import price_projection_store as projection_store  # noqa: E402


def _load_script(module_name, path, *, fake_xtdata=None):
    """Load a numbered script with controlled import-time dependencies."""
    replacements = {"price_projection_store": projection_store}
    if fake_xtdata is not None:
        fake_xtquant = types.ModuleType("xtquant")
        fake_xtquant.xtdata = fake_xtdata
        replacements["xtquant"] = fake_xtquant

    previous = {name: sys.modules.get(name) for name in replacements}
    sys.modules.update(replacements)
    sys.path.insert(0, str(INGESTION_DIR))
    try:
        spec = importlib.util.spec_from_file_location(module_name, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    finally:
        sys.path.remove(str(INGESTION_DIR))
        for name, prior in previous.items():
            if prior is None:
                sys.modules.pop(name, None)
            else:
                sys.modules[name] = prior


class OnePriceRow:
    def __len__(self):
        return 1

    def iterrows(self):
        yield "20260724", {
            "open": 10.0,
            "high": 11.0,
            "low": 9.0,
            "close": 10.5,
            "volume": 100,
            "amount": 1000.0,
            "preClose": 9.8,
            "suspendFlag": 0,
        }


class OneFactorRow:
    def __init__(self, cash):
        self.cash = cash

    def iterrows(self):
        yield date(2026, 7, 1), {
            "interest": self.cash,
            "stockBonus": 0,
            "stockGift": 0,
            "allotNum": 0,
            "allotPrice": None,
            "gugai": 0,
            "dr": Decimal("0.9900000000000000"),
        }


def _stored_event(cash):
    return {
        "stock_code": "000001.SZ",
        "ex_date": date(2026, 7, 1),
        "cash_dividend_per_share": cash,
        "stock_bonus_per_share": "0.00000000",
        "stock_gift_per_share": "0.00000000",
        "rights_issue_per_share": "0.00000000",
        "rights_issue_price": None,
        "share_reform_flag": 0,
        "qmt_dr_factor": "0.9900000000000000",
        "event_status": "effective",
        "data_source": "xtquant",
        "source_payload": {},
    }


def test_daily_collection_routes_qmt_none_front_back_to_independent_tables(monkeypatch):
    """A wrong dividend-mode/table mapping must fail this workflow test."""
    qmt_calls = []
    fake_xtdata = types.SimpleNamespace(
        download_history_data=lambda *args, **kwargs: None,
        get_market_data_ex=lambda **kwargs: qmt_calls.append(kwargs)
        or {"000001.SZ": OnePriceRow()},
    )
    collector = _load_script(
        "dual_track_collector_workflow",
        COLLECTOR_PATH,
        fake_xtdata=fake_xtdata,
    )
    database_writes = []
    monkeypatch.setattr(
        projection_store,
        "execute_many",
        lambda sql, values: database_writes.append((sql, list(values))) or len(values),
    )

    counts = collector.download_and_save_all_modes(
        "000001.SZ",
        "20260724",
        adjustment_asof=date(2026, 7, 24),
    )

    assert counts == {"none": 1, "front": 1, "back": 1}
    assert [call["dividend_type"] for call in qmt_calls] == ["none", "front", "back"]
    assert [
        next(
            table
            for table in (
                "trade_stock_daily_raw",
                "trade_stock_daily_qfq",
                "trade_stock_daily_bfq",
            )
            if f"INSERT INTO {table}" in sql
        )
        for sql, _ in database_writes
    ] == [
        "trade_stock_daily_raw",
        "trade_stock_daily_qfq",
        "trade_stock_daily_bfq",
    ]
    assert database_writes[0][1][0][-2:] == (9.8, 0)
    assert database_writes[1][1][0][-1] == date(2026, 7, 24)
    assert database_writes[2][1][0][-1] == date(2026, 7, 24)


def test_factor_snapshot_routes_new_and_corrected_events_to_exact_refresh_ranges():
    """New events must not rewrite bfq history; corrections must rewrite from ex-date."""
    data_start = date(2015, 1, 1)
    current = actions.normalize_qmt_factors("000001.SZ", OneFactorRow(0.12))

    new_plan = actions.plan_factor_snapshot(current, [], data_start)
    corrected_plan = actions.plan_factor_snapshot(
        current,
        [_stored_event("0.10000000")],
        data_start,
    )

    assert new_plan.refresh_tasks == [
        {
            "stock_code": "000001.SZ",
            "price_mode": "front",
            "refresh_from": data_start,
            "reason": "corporate_action_changed",
        }
    ]
    assert corrected_plan.refresh_tasks == [
        {
            "stock_code": "000001.SZ",
            "price_mode": "front",
            "refresh_from": data_start,
            "reason": "corporate_action_changed",
        },
        {
            "stock_code": "000001.SZ",
            "price_mode": "back",
            "refresh_from": date(2026, 7, 1),
            "reason": "corporate_action_changed",
        },
    ]


def test_failed_projection_refresh_is_durable_and_retried_on_the_next_run(monkeypatch):
    """Marking a failed refresh done, or excluding failed tasks, must fail."""
    task = {
        "id": 41,
        "stock_code": "000001.SZ",
        "price_mode": "front",
        "refresh_from": date(2015, 1, 1),
        "reason": "corporate_action_changed",
        "retry_count": 0,
    }
    task_status = {"value": "pending"}
    attempts = 0

    def fake_query(sql, params=None):
        if task_status["value"] in {"pending", "failed"}:
            return [task]
        return []

    def fake_update(sql, params=None):
        if sql == actions.RECLAIM_STALE_TASKS_SQL:
            return 0
        if "status = 'running'" in sql:
            task_status["value"] = "running"
        elif "status = 'failed'" in sql:
            task_status["value"] = "failed"
        elif "status = 'done'" in sql:
            task_status["value"] = "done"
        return 1

    def refresh_price(stock_code, price_mode, refresh_from):
        nonlocal attempts
        attempts += 1
        assert (stock_code, price_mode, refresh_from) == (
            "000001.SZ",
            "front",
            date(2015, 1, 1),
        )
        if attempts == 1:
            raise RuntimeError("QMT temporarily unavailable")
        return 1

    monkeypatch.setattr(actions, "execute_query", fake_query)
    monkeypatch.setattr(actions, "execute_update", fake_update)

    first_run = actions.run_due_refresh_tasks(refresh_price)
    second_run = actions.run_due_refresh_tasks(refresh_price)

    assert first_run == {"done": 0, "failed": 1, "retried": 0, "reclaimed": 0}
    assert second_run == {"done": 1, "failed": 0, "retried": 0, "reclaimed": 0}
    assert attempts == 2
    assert task_status["value"] == "done"


def test_qfq_discrepancy_is_logged_then_queued_for_confirmed_legacy_repair(monkeypatch):
    """A mismatched close must produce both an audit row and a repair task."""
    reconciliation = _load_script(
        "dual_track_reconciliation_workflow",
        RECONCILIATION_PATH,
    )
    overlap = {
        "stock_code": "000001.SZ",
        "trade_date": date(2026, 7, 24),
        "old_open_price": "10.000000",
        "old_high_price": "11.000000",
        "old_low_price": "9.000000",
        "old_close_price": "10.500000",
        "new_open_price": "10.000000",
        "new_high_price": "11.000000",
        "new_low_price": "9.000000",
        "new_close_price": "10.500010",
    }
    pending_range = {
        "stock_code": "000001.SZ",
        "refresh_from": date(2026, 7, 24),
        "refresh_to": date(2026, 7, 24),
    }
    batches = []
    updates = []

    def fake_query(sql, params=None):
        if sql == reconciliation.SELECT_DATE_BOUNDS_SQL:
            return [{"min_date": date(2026, 7, 24), "max_date": date(2026, 7, 24)}]
        if sql == reconciliation.SELECT_CODES_BATCH_SQL:
            return [{"stock_code": "000001.SZ"}]
        if "UNION ALL" in sql:
            return [overlap]
        if sql == reconciliation.SELECT_PENDING_RANGES_SQL:
            return [pending_range]
        return []

    monkeypatch.setattr(
        reconciliation,
        "execute_query",
        fake_query,
    )
    monkeypatch.setattr(
        reconciliation,
        "execute_many",
        lambda sql, values: batches.append((sql, list(values))) or len(values),
    )
    monkeypatch.setattr(
        reconciliation,
        "execute_update",
        lambda sql, params=None: updates.append((sql, params)) or 1,
    )

    reconcile_result = reconciliation.reconcile_qfq_prices()
    queue_result = reconciliation.queue_confirmed_legacy_repairs()

    assert reconcile_result == {
        "compared": 1,
        "discrepancies": 1,
        "upserted": 1,
        "resolved": 0,
    }
    assert queue_result == {"tasks": 1, "queued_logs": 1}
    reconcile_sql, reconcile_values = batches[0]
    repair_sql, repair_values = batches[1]
    assert "INSERT INTO trade_price_reconcile_log" in reconcile_sql
    assert reconcile_values[0][0:3] == (
        "000001.SZ",
        date(2026, 7, 24),
        "front",
    )
    assert reconcile_values[0][-1] == "qfq_ohlc_mismatch"
    assert "INSERT INTO trade_legacy_qfq_repair_task" in repair_sql
    assert repair_values == [
        (
            "000001.SZ",
            date(2026, 7, 24),
            date(2026, 7, 24),
            "qfq_ohlc_mismatch",
        )
    ]
    assert "status = 'queued'" in updates[0][0]
