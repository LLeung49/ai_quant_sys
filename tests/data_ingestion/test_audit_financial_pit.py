from datetime import date, datetime

from data_ingestion.audit_financial_pit import (
    audit_rows,
    classify_row,
    quarantine_rows,
)


def test_classify_row_flags_invalid_code_and_zero_report_date() -> None:
    reasons = classify_row(
        {
            "stock_code": "TEST_deadbeef.SH",
            "report_date": "0000-00-00",
            "announcement_date": None,
        },
        as_of_date=date(2026, 10, 15),
    )

    assert reasons == ("invalid_stock_code", "invalid_report_date")


def test_classify_row_flags_dates_after_explicit_as_of_date() -> None:
    reasons = classify_row(
        {
            "stock_code": "600000.SH",
            "report_date": date(2026, 12, 31),
            "announcement_date": datetime(2026, 11, 1, 9, 30),
        },
        as_of_date=date(2026, 10, 15),
    )

    assert reasons == ("future_report_date", "future_announcement_date")


def test_classify_row_flags_present_but_entirely_empty_core_payload() -> None:
    reasons = classify_row(
        {
            "stock_code": "688795.SH",
            "report_date": date(2023, 9, 30),
            "announcement_date": date(2023, 9, 30),
            "revenue": None,
            "net_profit": None,
            "total_assets": None,
            "total_equity": None,
            "operating_cash_flow": None,
        },
        as_of_date=date(2026, 10, 16),
    )

    assert reasons == ("all_core_financials_null",)


def test_audit_rows_returns_only_rows_with_evidence() -> None:
    rows = [
        {
            "id": 1,
            "stock_code": "600000.SH",
            "report_date": date(2026, 9, 30),
            "announcement_date": None,
        },
        {
            "id": 2,
            "stock_code": "BAD",
            "report_date": date(2026, 9, 30),
            "announcement_date": None,
        },
    ]

    assert audit_rows(rows, as_of_date=date(2026, 10, 15)) == [
        {"id": 2, "stock_code": "BAD", "reasons": ["invalid_stock_code"]}
    ]


class _FakeCursor:
    def __init__(self, rows_by_id: dict[int, dict]) -> None:
        self.rows_by_id = rows_by_id
        self.commands: list[tuple[str, object]] = []
        self.rowcount = 0
        self._selected = None

    def execute(self, sql: str, params=None) -> None:
        self.commands.append((sql, params))
        normalized = " ".join(sql.split()).upper()
        if normalized.startswith("SELECT * FROM TRADE_STOCK_FINANCIAL_RAW_PIT"):
            self._selected = self.rows_by_id.get(params[0])
            self.rowcount = 1 if self._selected else 0
        elif normalized.startswith("DELETE FROM TRADE_STOCK_FINANCIAL_RAW_PIT"):
            self.rowcount = len(params)
        else:
            self.rowcount = 1

    def fetchone(self):
        return self._selected

    def close(self) -> None:
        pass


class _FakeConnection:
    def __init__(self, rows_by_id: dict[int, dict]) -> None:
        self.cursor_instance = _FakeCursor(rows_by_id)
        self.commits = 0
        self.rollbacks = 0

    def cursor(self, *args, **kwargs):
        return self.cursor_instance

    def begin(self) -> None:
        pass

    def commit(self) -> None:
        self.commits += 1

    def rollback(self) -> None:
        self.rollbacks += 1


def test_quarantine_rows_copies_payload_before_exact_id_delete() -> None:
    connection = _FakeConnection(
        {
            7: {
                "id": 7,
                "stock_code": "TEST_deadbeef.SH",
                "report_date": "0000-00-00",
            }
        }
    )

    moved = quarantine_rows(
        connection,
        [{"id": 7, "stock_code": "TEST_deadbeef.SH", "reasons": ["invalid_stock_code"]}],
        batch_id="financial-pit-audit-20261015",
    )

    assert moved == 1
    # One commit completes idempotent DDL setup; the second atomically commits
    # the copy-before-delete transaction.
    assert connection.commits == 2
    assert connection.rollbacks == 0
    commands = connection.cursor_instance.commands
    insert_index = next(i for i, (sql, _) in enumerate(commands) if "INSERT INTO" in sql.upper())
    delete_index = next(i for i, (sql, _) in enumerate(commands) if sql.lstrip().upper().startswith("DELETE"))
    assert insert_index < delete_index
    assert commands[delete_index][1] == (7,)
