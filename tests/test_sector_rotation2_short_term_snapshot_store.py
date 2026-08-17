"""”短期异动快照表事务持久化的单元测试。
"""
from __future__ import annotations

from datetime import datetime

import pytest

from morning_conference.sector_rotation2.short_term import snapshot_store


class FakeCursor:
    def __init__(self):
        self.calls = []
        self.rowcount = 0
    def execute(self, sql, params=()):
        self.calls.append((sql, params))
        self.rowcount = 1
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

def _patch_connection(monkeypatch, connection):
    monkeypatch.setattr(snapshot_store, "get_connection", lambda: connection)

def test_create_short_term_run_inserts_running_audit_row(monkeypatch):
    connection = FakeConnection()
    _patch_connection(monkeypatch, connection)
    snapshot_store.create_short_term_run(
        run_id="run-1",
        as_of_date="2026-08-14",
        sector_level=2,
        model_version="v2_short_term",
        config_hash="hash",
        source_max_trade_date="2026-08-14",
    )
    sql, params = connection.cursor_instance.calls[0]
    assert "sector_rotation_run_log" in sql
    assert params[0] == "run-1"
    assert params[6] == "running"
    assert connection.committed is True

def test_mark_short_term_run_succeeded_writes_eligible_and_skipped_counts(monkeypatch):
    connection = FakeConnection()
    _patch_connection(monkeypatch, connection)
    snapshot_store.mark_short_term_run_succeeded("run-1", 30, 0)
    sql, params = connection.cursor_instance.calls[0]
    # 不能出现现在代码中的列名。
    assert "snapshot_rows" not in sql
    assert "error_message" not in sql
    # 表中应该出现的列名。
    assert "eligible_sector_count" in sql
    assert "skipped_sector_count" in sql
    assert "finished_at = %s" in sql
    assert "model_version LIKE %s" in sql
    assert params[1] == 30  # eligible_sector_count
    assert params[2] == 0   # skipped_sector_count
    assert params[3] == "run-1"
    assert params[4] == "v2_%"
    assert isinstance(params[0], datetime)
    assert connection.committed is True

def test_mark_short_term_run_failed_uses_error_summary_column(monkeypatch):
    connection = FakeConnection()
    _patch_connection(monkeypatch, connection)
    snapshot_store.mark_short_term_run_failed("run-1", "boom")
    sql, params = connection.cursor_instance.calls[0]
    # 表里的实际列名为日志表中的错误摘要列。
    assert "error_summary = %s" in sql
    assert "error_message" not in sql
    assert params[1] == "boom"
    assert params[2] == "run-1"
    assert params[3] == "v2_%"
    assert connection.committed is True
