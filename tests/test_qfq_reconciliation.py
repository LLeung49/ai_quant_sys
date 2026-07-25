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
    monkeypatch.setattr(reconciliation, "execute_query", lambda sql, params=None: [
        price_row(close="10.000000", new_close="10.000003")
    ])
    monkeypatch.setattr(
        reconciliation,
        "execute_many",
        lambda sql, values: writes.append((sql, list(values))) or len(values),
    )

    first = reconciliation.reconcile_qfq_prices()
    second = reconciliation.reconcile_qfq_prices()

    assert first == second == {"compared": 1, "discrepancies": 1, "upserted": 1}
    assert len(writes) == 2
    assert all("ON DUPLICATE KEY UPDATE" in sql for sql, _ in writes)
    assert all(values[0][-1] == "qfq_ohlc_mismatch" for _, values in writes)


def test_reconcile_marks_previously_logged_matching_row_resolved(monkeypatch):
    reconciliation = load_reconciliation_module()
    writes = []
    monkeypatch.setattr(reconciliation, "execute_query", lambda sql, params=None: [price_row()])
    monkeypatch.setattr(
        reconciliation,
        "execute_many",
        lambda sql, values: writes.append((sql, list(values))) or len(values),
    )

    result = reconciliation.reconcile_qfq_prices()

    assert result == {"compared": 1, "discrepancies": 0, "upserted": 0}
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
