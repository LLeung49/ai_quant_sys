from datetime import date
from types import SimpleNamespace

import pytest

from data_ingestion.financial_recovery import rebuild_repair_history as rebuild
from morning_conference.sector_rotation2.research.status import SnapshotMode


class Cursor:
    def __init__(self, fail_insert=False):
        self.statements = []
        self.rowcount = 4
        self.fail_insert = fail_insert

    def execute(self, sql, params=()):
        self.statements.append(sql)

    def executemany(self, sql, values):
        self.statements.append(sql)
        if self.fail_insert:
            raise RuntimeError("insert failed")

    def fetchone(self):
        return (1,)

    def close(self):
        pass


class Connection:
    def __init__(self, fail_insert=False):
        self.mock_cursor = Cursor(fail_insert)
        self.commits = 0
        self.rollbacks = 0

    def cursor(self):
        return self.mock_cursor

    def commit(self):
        self.commits += 1

    def rollback(self):
        self.rollbacks += 1

    def close(self):
        pass


def snapshot():
    return SimpleNamespace(
        as_of_date=date(2024, 1, 2), entity_code="000001.SZ",
        strategy_type="stock_repair", snapshot_mode=SnapshotMode.BACKFILL,
        sector_level=2,
        run_id="recovery-test",
    )


def test_replace_removes_linked_labels_in_same_transaction(monkeypatch):
    connection = Connection()
    monkeypatch.setattr(rebuild, "_insert_values", lambda _: ("new",))

    assert rebuild.replace_backfill_day(
        "2024-01-02", [snapshot()], connection_factory=lambda: connection,
    ) == 4

    statements = connection.mock_cursor.statements
    assert "sector_rotation_research_forward_label" in statements[0]
    assert "DELETE FROM research_candidate_snapshot" in statements[1]
    assert connection.commits == 1
    assert connection.rollbacks == 0


def test_replace_rolls_back_labels_and_snapshots_on_insert_failure(monkeypatch):
    connection = Connection(fail_insert=True)
    monkeypatch.setattr(rebuild, "_insert_values", lambda _: ("new",))

    with pytest.raises(RuntimeError, match="insert failed"):
        rebuild.replace_backfill_day(
            "2024-01-02", [snapshot()], connection_factory=lambda: connection,
        )

    assert connection.commits == 0
    assert connection.rollbacks == 1


def test_parallel_scoring_keeps_commit_order_and_unique_run_ids(monkeypatch):
    monkeypatch.setattr(rebuild, "ProcessPoolExecutor", rebuild.ThreadPoolExecutor)
    monkeypatch.setattr(rebuild, "score_day", lambda day, **kwargs: (day, kwargs["run_id"]))
    days = ["2024-01-02", "2024-01-03", "2024-01-04"]
    results = list(rebuild.scored_dates(days, workers=1, date_workers=2))
    assert [day for day, _, _ in results] == days
    assert len({run_id for _, run_id, _ in results}) == len(days)
    assert all(future.result() == (day, run_id) for day, run_id, future in results)


def test_replacement_refuses_unarchived_snapshot_ids(monkeypatch):
    connection = Connection()
    connection.mock_cursor.fetchone = lambda: (101, 9, "2026-10-18 12:00:00")
    with pytest.raises(ValueError, match="outside verified archives"):
        rebuild.replace_backfill_day(
            "2024-01-02", [snapshot()], connection_factory=lambda: connection,
            archive_limits={"snapshot_max_id": 100, "forward_labels": {
                "max_id": 10, "max_updated": "2026-10-19 00:00:00",
            }},
        )
    assert connection.commits == 0
    assert connection.rollbacks == 1
    assert not any("DELETE" in sql for sql in connection.mock_cursor.statements)


def test_completion_marker_is_written_before_commit(monkeypatch):
    connection = Connection()
    answers = iter([(100, 9, "2026-10-18 12:00:00"), (1,)])
    connection.mock_cursor.fetchone = lambda: next(answers)
    monkeypatch.setattr(rebuild, "_insert_values", lambda _: ("new",))
    rebuild.replace_backfill_day(
        "2024-01-02", [snapshot()], connection_factory=lambda: connection,
        archive_limits={"snapshot_max_id": 100, "forward_labels": {
            "max_id": 10, "max_updated": "2026-10-19 00:00:00",
        }},
    )
    assert "INSERT INTO financial_repair_recovery_day" in connection.mock_cursor.statements[-1]
    assert connection.commits == 1
