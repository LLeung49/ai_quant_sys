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

    def fetchall(self):
        return list(self.owner.fetchall_result)

    def close(self):
        pass


class Connection:
    def __init__(self, fail_on_insert=None, fetchall_result=()):
        self.calls = []
        self.commits = 0
        self.rollbacks = 0
        self.fail_on_insert = fail_on_insert
        self.fetchall_result = fetchall_result

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
    projection_sql = [
        sql for sql in insert_sql if "INSERT INTO trade_stock_daily_" in sql
    ]
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
        if kind == "executemany" and "INSERT INTO trade_stock_daily_" in sql
    ]
    assert projection_sql
    assert all("ON DUPLICATE KEY UPDATE" in sql for sql in projection_sql)
    assert connection.commits == 2


def test_retry_refreshes_batch_range_and_replaces_stale_gap_evidence():
    connection = Connection()

    RebuildStore(lambda: connection, batch_id="batch-1").persist_validated_batch(
        complete_batch()
    )

    assert "start_date=VALUES(start_date)" in __import__(
        "data_ingestion.market_rebuild_store", fromlist=["START_BATCH_SQL"]
    ).START_BATCH_SQL
    gap_deletes = [
        (sql, values) for kind, sql, values in connection.calls
        if kind == "executemany" and "DELETE FROM trade_market_rebuild_gap" in sql
    ]
    assert gap_deletes == [(
        "DELETE FROM trade_market_rebuild_gap WHERE batch_id=%s AND stock_code=%s",
        [("batch-1", "600519.SH")],
    )]


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
        if kind == "executemany" and "INSERT INTO trade_stock_daily_" in sql
    ]
    assert len(projection_calls) == 3
    assert all(len(values) == 2 for _, values in projection_calls)
    assert connection.commits == 1
    assert [result.stock_code for result in results] == ["600519.SH", "000001.SZ"]


def test_replacement_deletes_old_projection_rows_inside_same_transaction():
    connection = Connection()

    RebuildStore(lambda: connection, batch_id="batch-1").persist_validated_batch(
        complete_batch()
    )

    deletes = [
        (sql, values) for kind, sql, values in connection.calls
        if kind == "executemany" and sql.startswith("DELETE FROM trade_stock_daily_")
    ]
    assert len(deletes) == 3
    assert all(values == [("batch-1", "600519.SH")] for _, values in deletes)
    assert all("_rebuild" in sql for sql, _ in deletes)


def test_prepare_universe_persists_sorted_manifest_and_hash():
    connection = Connection()
    digest = RebuildStore(
        lambda: connection, batch_id="market-full-1"
    ).prepare_universe(["600519.SH", "000001.SZ", "600519.SH"])

    inserts = [
        values for kind, sql, values in connection.calls
        if kind == "executemany" and "trade_market_rebuild_expected_code" in sql
    ]
    assert len(inserts) == 1
    assert [row[1] for row in inserts[0]] == ["000001.SZ", "600519.SH"]
    assert all(row[2] == digest for row in inserts[0])
    assert connection.commits == 1


def test_prepare_universe_rejects_changed_manifest_on_resume():
    connection = Connection(fetchall_result=[("000001.SZ", "old-hash")])

    with pytest.raises(ValueError, match="universe manifest differs"):
        RebuildStore(
            lambda: connection, batch_id="market-full-1"
        ).prepare_universe(["000001.SZ", "600519.SH"])

    assert connection.commits == 0


def test_record_exclusions_persists_reason_and_json_evidence():
    connection = Connection()
    store = RebuildStore(lambda: connection, batch_id="market-full-1")

    store.record_exclusions({
        "158036.SZ": {
            "reason": "invalid_legacy_zero_only_code",
            "evidence": {"qmt_instrument_detail": "absent", "zero_rows": 486},
        }
    })

    inserts = [
        values for kind, sql, values in connection.calls
        if kind == "executemany" and "trade_market_rebuild_excluded_code" in sql
    ]
    assert len(inserts) == 1
    assert inserts[0][0][0:3] == (
        "market-full-1", "158036.SZ", "invalid_legacy_zero_only_code"
    )
    assert '"zero_rows": 486' in inserts[0][0][3]
    assert connection.commits == 1


def test_excluded_codes_are_read_for_resume():
    connection = Connection(fetchall_result=[("158036.SZ",), ("159047.SZ",)])

    codes = RebuildStore(
        lambda: connection, batch_id="market-full-1"
    ).excluded_codes()

    assert codes == {"158036.SZ", "159047.SZ"}


def test_replace_with_exclusion_removes_all_staging_evidence_atomically():
    connection = Connection()
    store = RebuildStore(lambda: connection, batch_id="market-full-1")

    store.replace_with_exclusion(
        "158058.SZ",
        reason="listed_after_rebuild_end",
        evidence={"open_date": "2026-10-14", "rebuild_end_date": "2026-10-13"},
    )

    executed = [(sql, params) for kind, sql, params in connection.calls if kind == "execute"]
    projection_deletes = [
        (sql, params) for sql, params in executed
        if sql.startswith("DELETE FROM trade_stock_daily_")
    ]
    assert len(projection_deletes) == 3
    assert all(params == ("market-full-1", "158058.SZ") for _, params in projection_deletes)
    assert any("DELETE FROM trade_market_rebuild_gap" in sql for sql, _ in executed)
    assert any("trade_market_rebuild_excluded_code" in sql for sql, _ in executed)
    assert any("status='failed'" in sql for sql, _ in executed)
    assert connection.commits == 1
    assert connection.rollbacks == 0
