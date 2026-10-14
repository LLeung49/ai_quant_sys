from datetime import date

import pytest

from data_ingestion.market_provider import MarketBatch
from data_ingestion.market_rebuild_store import RebuildStore


def valid_rows(code="600519.SH"):
    base = {
        "stock_code": code,
        "trade_date": "2026-09-18",
        "open_price": 10.0,
        "high_price": 11.0,
        "low_price": 9.0,
        "close_price": 10.5,
        "volume": 100,
        "amount": 100000.0,
    }
    return {mode: [dict(base)] for mode in ("none", "front", "back")}


def complete_batch():
    return MarketBatch(
        "600519.SH",
        date(2026, 9, 18),
        date(2026, 9, 18),
        rows_by_mode=valid_rows(),
        provenance={"provider": "qmt_bridge", "fetched_at": "2026-10-14T00:00:00Z"},
    )


class Cursor:
    def __init__(self, owner, fail_on_insert=None):
        self.owner = owner
        self.fail_on_insert = fail_on_insert

    def execute(self, sql, params=()):
        self.owner.calls.append(("execute", sql, params))

    def executemany(self, sql, values):
        self.owner.calls.append(("executemany", sql, list(values)))
        if self.fail_on_insert and self.fail_on_insert in sql:
            raise RuntimeError("simulated insert failure")
        return len(values)

    def close(self):
        pass


class Connection:
    def __init__(self, fail_on_insert=None):
        self.calls = []
        self.commits = 0
        self.rollbacks = 0
        self.fail_on_insert = fail_on_insert

    def cursor(self):
        return Cursor(self, self.fail_on_insert)

    def commit(self):
        self.commits += 1

    def rollback(self):
        self.rollbacks += 1

    def close(self):
        pass


def test_store_uses_only_rebuild_targets_and_commits_complete_triple():
    connection = Connection()
    result = RebuildStore(lambda: connection, batch_id="batch-1").persist_validated_batch(
        complete_batch()
    )

    insert_sql = [sql for kind, sql, _ in connection.calls if kind == "executemany"]
    projection_sql = [sql for sql in insert_sql if "trade_stock_daily_" in sql]
    assert len(projection_sql) == 3
    assert all("_rebuild" in sql.split("INSERT INTO", 1)[1].split("(", 1)[0] for sql in projection_sql)
    assert connection.commits == 1
    assert connection.rollbacks == 0
    assert result.rows_written == 3


def test_incomplete_triple_cannot_open_a_database_connection():
    batch = complete_batch()
    batch.rows_by_mode.pop("front")
    batch.failures["front"] = "missing"
    opened = []

    with pytest.raises(ValueError, match="incomplete"):
        RebuildStore(lambda: opened.append(True), batch_id="batch-1").persist_validated_batch(batch)

    assert opened == []


def test_failed_projection_rolls_back_without_completed_checkpoint():
    connection = Connection(fail_on_insert="trade_stock_daily_qfq_rebuild")

    with pytest.raises(RuntimeError, match="simulated"):
        RebuildStore(lambda: connection, batch_id="batch-1").persist_validated_batch(
            complete_batch()
        )

    assert connection.commits == 0
    assert connection.rollbacks == 1
    completed = [
        sql for _, sql, _ in connection.calls
        if "status = 'complete'" in sql.lower()
    ]
    assert completed == []


def test_repeat_persist_is_an_idempotent_upsert():
    connection = Connection()
    store = RebuildStore(lambda: connection, batch_id="batch-1")

    store.persist_validated_batch(complete_batch())
    store.persist_validated_batch(complete_batch())

    projection_sql = [
        sql for kind, sql, _ in connection.calls
        if kind == "executemany" and "trade_stock_daily_" in sql
    ]
    assert projection_sql
    assert all("ON DUPLICATE KEY UPDATE" in sql for sql in projection_sql)
    assert connection.commits == 2


def test_multiple_codes_use_one_transaction_and_three_projection_inserts():
    connection = Connection()
    second = complete_batch()
    second.stock_code = "000001.SZ"
    second.rows_by_mode = valid_rows("000001.SZ")

    results = RebuildStore(
        lambda: connection, batch_id="batch-1"
    ).persist_validated_batches([complete_batch(), second])

    projection_calls = [
        (sql, values) for kind, sql, values in connection.calls
        if kind == "executemany" and "trade_stock_daily_" in sql
    ]
    assert len(projection_calls) == 3
    assert all(len(values) == 2 for _, values in projection_calls)
    assert connection.commits == 1
    assert [result.stock_code for result in results] == ["600519.SH", "000001.SZ"]
