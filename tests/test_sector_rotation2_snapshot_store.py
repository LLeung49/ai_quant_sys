from pathlib import Path

import pandas as pd
import pytest

from morning_conference.sector_rotation2 import snapshot_store


def test_migration_defines_approved_sector_rotation_tables():
    sql = Path("sql/20260804_create_sector_rotation_persistence_tables.sql").read_text(encoding="utf-8")

    assert "CREATE TABLE IF NOT EXISTS sector_rotation_run_log" in sql
    assert "CREATE TABLE IF NOT EXISTS sector_rotation_sector_daily_snapshot" in sql
    assert "CREATE TABLE IF NOT EXISTS sector_rotation_sector_forward_return" in sql
    assert "CREATE TABLE IF NOT EXISTS sector_rotation_backtest_metric" in sql
    assert "UNIQUE KEY uq_snapshot (as_of_date, sector_level, sector_name, model_version)" in sql


class FakeCursor:
    def __init__(self):
        self.calls = []
        self.rowcount = 0

    def execute(self, sql, params=()):
        self.calls.append((sql, params))
        self.rowcount = 1

    def executemany(self, sql, rows):
        self.calls.append((sql, list(rows)))
        self.rowcount = len(self.calls[-1][1])

    def close(self):
        pass


class FakeConnection:
    def __init__(self):
        self.cursor_instance = FakeCursor()
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


def test_persist_daily_snapshot_uses_one_parameterized_upsert_and_commits(monkeypatch):
    connection = FakeConnection()
    monkeypatch.setattr(snapshot_store, "get_connection", lambda: connection)
    frame = pd.DataFrame(
        [{"sector_name": "电子", "coverage_ratio": 1.0, "base_score": 0.2, "composite_score": 0.2}]
    )

    affected = snapshot_store.persist_daily_snapshot(
        frame, as_of_date="2026-01-05", sector_level=2, model_version="v1", run_id="run-1"
    )

    assert affected == 1
    assert connection.committed is True
    sql, rows = connection.cursor_instance.calls[0]
    assert "ON DUPLICATE KEY UPDATE" in sql
    assert "%s" in sql
    assert rows[0][0] == "2026-01-05"


def test_persist_daily_snapshot_rolls_back_when_upsert_fails(monkeypatch):
    connection = FakeConnection()
    monkeypatch.setattr(snapshot_store, "get_connection", lambda: connection)
    monkeypatch.setattr(connection.cursor_instance, "executemany", lambda *args: (_ for _ in ()).throw(RuntimeError("db down")))

    frame = pd.DataFrame([{"sector_name": "电子"}])

    try:
        snapshot_store.persist_daily_snapshot(frame, "2026-01-05", 2, "v1", "run-1")
    except RuntimeError:
        pass

    assert connection.rolled_back is True


def test_create_run_writes_running_audit_record(monkeypatch):
    connection = FakeConnection()
    monkeypatch.setattr(snapshot_store, "get_connection", lambda: connection)

    snapshot_store.create_run("run-1", "2026-01-05", 2, "v1", "hash", "2026-01-05")

    sql, params = connection.cursor_instance.calls[0]
    assert "sector_rotation_run_log" in sql
    assert params[0] == "run-1"
    assert params[6] == "running"
    assert connection.committed is True


def test_mark_run_failed_records_error_summary(monkeypatch):
    connection = FakeConnection()
    monkeypatch.setattr(snapshot_store, "get_connection", lambda: connection)

    snapshot_store.mark_run_failed("run-1", "source unavailable")

    sql, params = connection.cursor_instance.calls[0]
    assert "status = %s" in sql
    assert params == ("failed", "source unavailable", "run-1")
