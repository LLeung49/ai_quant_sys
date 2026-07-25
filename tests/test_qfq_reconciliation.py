from datetime import date
from decimal import Decimal
import importlib.util
from pathlib import Path
import sys


SRC_DIR = Path(__file__).parents[1] / "src"
INGESTION_DIR = SRC_DIR / "data_ingestion"
SCRIPT_PATH = INGESTION_DIR / "9-前复权对账与定向重刷.py"
sys.path.insert(0, str(SRC_DIR))


def load_reconciliation_module():
    sys.path.insert(0, str(INGESTION_DIR))
    try:
        spec = importlib.util.spec_from_file_location("qfq_reconciliation", SCRIPT_PATH)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    finally:
        sys.path.remove(str(INGESTION_DIR))


def price_row(*, close="10.000000", new_close=None):
    return {
        "stock_code": "600519.SH",
        "trade_date": date(2026, 7, 1),
        "old_open_price": "9.000000",
        "old_high_price": "11.000000",
        "old_low_price": "8.000000",
        "old_close_price": close,
        "new_open_price": "9.000000",
        "new_high_price": "11.000000",
        "new_low_price": "8.000000",
        "new_close_price": new_close if new_close is not None else close,
        "legacy_exists": 1,
        "projected_exists": 1,
    }


def test_price_tolerance_does_not_log_a_one_unit_last_place_difference():
    reconciliation = load_reconciliation_module()
    row = price_row(close="10.000000", new_close="10.000001")

    assert reconciliation.find_qfq_discrepancies([row]) == []
    assert reconciliation.PRICE_TOLERANCE == Decimal("0.000001")


def test_ohlc_discrepancy_preserves_legacy_and_independent_prices():
    reconciliation = load_reconciliation_module()
    row = price_row(close="10.000000", new_close="10.000003")

    assert reconciliation.find_qfq_discrepancies([row]) == [
        {
            "stock_code": "600519.SH",
            "trade_date": date(2026, 7, 1),
            "price_mode": "front",
            "old_open_price": Decimal("9.000000"),
            "old_high_price": Decimal("11.000000"),
            "old_low_price": Decimal("8.000000"),
            "old_close_price": Decimal("10.000000"),
            "new_open_price": Decimal("9.000000"),
            "new_high_price": Decimal("11.000000"),
            "new_low_price": Decimal("8.000000"),
            "new_close_price": Decimal("10.000003"),
            "diff_reason": "qfq_ohlc_mismatch",
        }
    ]


def test_reconcile_upserts_once_on_repeated_same_discrepancy(monkeypatch):
    reconciliation = load_reconciliation_module()
    writes = []

    def fake_query(sql, params=None):
        if sql == reconciliation.SELECT_DATE_BOUNDS_SQL:
            return [{"min_date": date(2026, 7, 1), "max_date": date(2026, 7, 1)}]
        if sql == reconciliation.SELECT_CODES_BATCH_SQL:
            return [{"stock_code": "600519.SH"}]
        if "UNION ALL" in sql:
            return [price_row(close="10.000000", new_close="10.000003")]
        return []

    monkeypatch.setattr(reconciliation, "execute_query", fake_query)
    monkeypatch.setattr(
        reconciliation,
        "execute_many",
        lambda sql, values: writes.append((sql, list(values))) or len(values),
    )

    first = reconciliation.reconcile_qfq_prices()
    second = reconciliation.reconcile_qfq_prices()

    assert first == second == {
        "compared": 1,
        "discrepancies": 1,
        "upserted": 1,
        "resolved": 0,
    }
    assert len(writes) == 2
    assert all("ON DUPLICATE KEY UPDATE" in sql for sql, _ in writes)
    assert all(values[0][-1] == "qfq_ohlc_mismatch" for _, values in writes)


def test_reconcile_marks_previously_logged_matching_row_resolved(monkeypatch):
    reconciliation = load_reconciliation_module()
    writes = []

    def fake_query(sql, params=None):
        if sql == reconciliation.SELECT_DATE_BOUNDS_SQL:
            return [{"min_date": date(2026, 7, 1), "max_date": date(2026, 7, 1)}]
        if sql == reconciliation.SELECT_CODES_BATCH_SQL:
            return [{"stock_code": "600519.SH"}]
        if "UNION ALL" in sql:
            return []
        return [price_row()]

    monkeypatch.setattr(reconciliation, "execute_query", fake_query)
    monkeypatch.setattr(
        reconciliation,
        "execute_many",
        lambda sql, values: writes.append((sql, list(values))) or len(values),
    )

    result = reconciliation.reconcile_qfq_prices()

    assert result == {
        "compared": 0,
        "discrepancies": 0,
        "upserted": 0,
        "resolved": 1,
    }
    assert writes == [
        (
            reconciliation.MARK_RECONCILE_LOG_RESOLVED_SQL,
            [("600519.SH", date(2026, 7, 1))],
        )
    ]


def test_confirmed_discrepancies_create_one_exact_legacy_date_range_task(monkeypatch):
    reconciliation = load_reconciliation_module()
    writes = []
    updates = []
    monkeypatch.setattr(reconciliation, "execute_query", lambda sql, params=None: [
        {
            "stock_code": "600519.SH",
            "refresh_from": date(2026, 7, 1),
            "refresh_to": date(2026, 7, 3),
        }
    ])
    monkeypatch.setattr(
        reconciliation,
        "execute_many",
        lambda sql, values: writes.append((sql, list(values))) or len(values),
    )
    monkeypatch.setattr(
        reconciliation,
        "execute_update",
        lambda sql, params=None: updates.append((sql, params)) or 1,
    )

    result = reconciliation.queue_confirmed_legacy_repairs()

    assert result == {"tasks": 1, "queued_logs": 1}
    assert writes[0][1] == [
        ("600519.SH", date(2026, 7, 1), date(2026, 7, 3), "qfq_ohlc_mismatch")
    ]
    assert updates[0][1] == ("600519.SH", date(2026, 7, 1), date(2026, 7, 3))
    assert "status = 'queued'" in updates[0][0]


def test_pending_repair_query_keeps_each_confirmed_date_exact():
    reconciliation = load_reconciliation_module()

    assert "trade_date AS refresh_from" in reconciliation.SELECT_PENDING_RANGES_SQL
    assert "trade_date AS refresh_to" in reconciliation.SELECT_PENDING_RANGES_SQL
    assert "MIN(trade_date)" not in reconciliation.SELECT_PENDING_RANGES_SQL
    assert "MAX(trade_date)" not in reconciliation.SELECT_PENDING_RANGES_SQL


def test_missing_legacy_row_is_detected_and_can_be_repaired_from_projection():
    reconciliation = load_reconciliation_module()
    row = price_row()
    row.update(
        {
            "legacy_exists": 0,
            "old_open_price": None,
            "old_high_price": None,
            "old_low_price": None,
            "old_close_price": None,
        }
    )

    discrepancy = reconciliation.find_qfq_discrepancies([row])[0]

    assert discrepancy["diff_reason"] == "legacy_qfq_missing"
    assert discrepancy["old_close_price"] is None
    assert discrepancy["new_close_price"] == Decimal("10.000000")


def test_missing_projected_row_is_detected_but_not_queued_for_legacy_repair():
    reconciliation = load_reconciliation_module()
    row = price_row()
    row.update(
        {
            "projected_exists": 0,
            "new_open_price": None,
            "new_high_price": None,
            "new_low_price": None,
            "new_close_price": None,
        }
    )

    discrepancy = reconciliation.find_qfq_discrepancies([row])[0]

    assert discrepancy["diff_reason"] == "projected_qfq_missing"
    assert discrepancy["new_close_price"] is None
    assert "diff_reason IN ('qfq_ohlc_mismatch', 'legacy_qfq_missing')" in (
        reconciliation.SELECT_PENDING_RANGES_SQL
    )


def test_legacy_repair_upserts_missing_rows_from_independent_qfq(monkeypatch):
    reconciliation = load_reconciliation_module()
    updates = []
    monkeypatch.setattr(
        reconciliation,
        "execute_query",
        lambda sql, params=None: [{"row_count": 1}],
    )
    monkeypatch.setattr(
        reconciliation,
        "execute_update",
        lambda sql, params=None: updates.append((sql, params)) or 1,
    )

    affected = reconciliation.refresh_legacy_qfq_range(
        "600519.SH",
        date(2026, 7, 1),
        date(2026, 7, 3),
    )

    assert affected == 1
    assert "INSERT INTO trade_stock_daily" in updates[0][0]
    assert "SELECT projected.stock_code, projected.trade_date" in updates[0][0]
    assert "INNER JOIN trade_price_reconcile_log" in updates[0][0]
    assert "log.status = 'queued'" in updates[0][0]
    assert "ON DUPLICATE KEY UPDATE" in updates[0][0]
    assert updates[0][1] == (
        "600519.SH",
        date(2026, 7, 1),
        date(2026, 7, 3),
    )


def test_legacy_repair_succeeds_when_source_exists_but_upsert_is_noop(monkeypatch):
    reconciliation = load_reconciliation_module()
    monkeypatch.setattr(
        reconciliation,
        "execute_query",
        lambda sql, params=None: [{"row_count": 2}],
    )
    monkeypatch.setattr(reconciliation, "execute_update", lambda sql, params=None: 0)

    assert reconciliation.refresh_legacy_qfq_range(
        "600519.SH",
        date(2026, 7, 1),
        date(2026, 7, 3),
    ) == 2


def test_queue_marks_only_repairable_reconcile_logs():
    reconciliation = load_reconciliation_module()

    assert "diff_reason IN ('qfq_ohlc_mismatch', 'legacy_qfq_missing')" in (
        reconciliation.MARK_LOG_RANGE_QUEUED_SQL
    )


def test_reconcile_queries_are_date_and_code_batched_and_resolve_only_open_logs():
    reconciliation = load_reconciliation_module()

    assert "trade_price_reconcile_log" in reconciliation.SELECT_UNRESOLVED_LOGS_SQL
    assert "status IN ('pending', 'queued')" in reconciliation.SELECT_UNRESOLVED_LOGS_SQL
    assert "{code_placeholders}" in reconciliation.SELECT_DISCREPANCIES_BATCH_SQL
    assert "trade_date BETWEEN %s AND %s" in reconciliation.SELECT_DISCREPANCIES_BATCH_SQL


def test_stale_running_legacy_task_is_reclaimed_before_retry(monkeypatch):
    reconciliation = load_reconciliation_module()
    task = {
        "id": 5,
        "stock_code": "600519.SH",
        "refresh_from": date(2026, 7, 1),
        "refresh_to": date(2026, 7, 3),
        "retry_count": 2,
    }
    updates = []

    def fake_query(sql, params=None):
        if sql == reconciliation.COUNT_QFQ_REPAIR_ROWS_SQL:
            return [{"row_count": 3}]
        return [task]

    monkeypatch.setattr(reconciliation, "execute_query", fake_query)
    monkeypatch.setattr(
        reconciliation,
        "complete_legacy_qfq_repair",
        lambda task, claim_token: 3,
    )
    monkeypatch.setattr(
        reconciliation,
        "execute_update",
        lambda sql, params=None: updates.append((sql, params)) or 1,
    )

    result = reconciliation.run_pending_legacy_repairs(lease_timeout_minutes=45)

    assert result["reclaimed"] == 1
    assert result["retried"] == 1
    assert result["done"] == 1
    assert result["failed"] == 0
    assert updates[0][1] == (45,)


def test_legacy_task_completion_is_guarded_by_claim_token():
    reconciliation = load_reconciliation_module()

    assert "WHEN status = 'running' THEN 'pending'" in (
        reconciliation.UPSERT_LEGACY_REPAIR_TASK_SQL
    )
    assert "claim_token = NULL" in reconciliation.UPSERT_LEGACY_REPAIR_TASK_SQL
    assert "claim_token = %s" in reconciliation.MARK_LEGACY_REPAIR_RUNNING_SQL
    assert "claim_token = %s" in reconciliation.MARK_LEGACY_REPAIR_DONE_SQL
    assert "claim_token = %s" in reconciliation.MARK_LEGACY_REPAIR_FAILED_SQL
    assert "claim_token = NULL" in reconciliation.RECLAIM_STALE_LEGACY_REPAIRS_SQL


def test_legacy_upsert_and_task_log_completion_share_one_transaction():
    reconciliation = load_reconciliation_module()

    class Cursor:
        def __init__(self):
            self.sql = []
            self.rowcount = 0

        def execute(self, sql, params=None):
            self.sql.append((sql, params))
            self.rowcount = 1

        def fetchone(self):
            return (2,)

        def close(self):
            pass

    class Connection:
        def __init__(self):
            self.cursor_instance = Cursor()
            self.committed = False
            self.rolled_back = False

        def cursor(self):
            return self.cursor_instance

        def commit(self):
            self.committed = True

        def rollback(self):
            self.rolled_back = True

        def close(self):
            pass

    connection = Connection()
    task = {
        "id": 5,
        "stock_code": "600519.SH",
        "refresh_from": date(2026, 7, 1),
        "refresh_to": date(2026, 7, 1),
    }

    result = reconciliation.complete_legacy_qfq_repair(
        task,
        "claim-a",
        connection_factory=lambda: connection,
    )

    assert result == 2
    assert connection.committed
    assert not connection.rolled_back
    sql = [item[0] for item in connection.cursor_instance.sql]
    assert sql == [
        reconciliation.COUNT_QFQ_REPAIR_ROWS_SQL,
        reconciliation.UPSERT_LEGACY_FROM_QFQ_SQL,
        reconciliation.MARK_LEGACY_REPAIR_DONE_SQL,
    ]


def test_cli_logs_resolution_retry_and_reclaim_counts(monkeypatch, capsys):
    reconciliation = load_reconciliation_module()
    monkeypatch.setattr(
        reconciliation,
        "reconcile_qfq_prices",
        lambda: {"compared": 3, "discrepancies": 1, "upserted": 1, "resolved": 2},
    )
    monkeypatch.setattr(
        reconciliation,
        "run_pending_legacy_repairs",
        lambda: {
            "done": 1,
            "failed": 0,
            "updated_rows": 5,
            "retried": 2,
            "reclaimed": 1,
            "superseded": 0,
        },
    )

    assert reconciliation.main(["--run-repairs"]) == 0
    output = capsys.readouterr().out
    assert "[对账] 比较=3 差异=1 写入=1 已解决=2" in output
    assert (
        "[重刷执行] 成功=1 失败=0 更新=5 重试=2 回收=1 "
        "已被新任务取代=0"
    ) in output
