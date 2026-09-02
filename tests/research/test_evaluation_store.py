from datetime import date

import pytest

from morning_conference.sector_rotation2.research.contracts import (
    BenchmarkStatus, ForwardLabel, PathStatus, ResearchContext, ReturnStatus,
)
from morning_conference.sector_rotation2.research.evaluation.schema import FORWARD_LABEL_DDL
from morning_conference.sector_rotation2.research.evaluation.labels import (
    build_delayed_not_matured_label,
    build_delayed_unavailable_label,
)
from morning_conference.sector_rotation2.research.evaluation.store import persist_forward_labels
from morning_conference.sector_rotation2.research.status import SnapshotMode


class Cursor:
    rowcount = 1

    def __init__(self) -> None:
        self.executemany_calls: list[tuple[str, list[tuple[object, ...]]]] = []

    def executemany(self, sql: str, rows: list[tuple[object, ...]]) -> None:
        self.executemany_calls.append((sql, rows))

    def close(self) -> None: pass


class Connection:
    def __init__(self) -> None:
        self.cursor_instance = Cursor()
        self.committed = False
        self.rolled_back = False

    def cursor(self) -> Cursor: return self.cursor_instance
    def commit(self) -> None: self.committed = True
    def rollback(self) -> None: self.rolled_back = True


class UpsertCursor(Cursor):
    def __init__(self) -> None:
        super().__init__()
        self.rows: dict[tuple[object, ...], tuple[object, ...]] = {}

    def executemany(self, sql: str, rows: list[tuple[object, ...]]) -> None:
        super().executemany(sql, rows)
        for row in rows:
            unique_key = tuple(row[index] for index in (0, 1, 5, 6, 7, 8, 9, 26, 27))
            previous = self.rows.get(unique_key)
            if previous is None or not (previous[24] == 1 and row[24] == 0):
                self.rows[unique_key] = row


class UpsertConnection(Connection):
    def __init__(self) -> None:
        super().__init__()
        self.cursor_instance = UpsertCursor()


def label(**changes: object) -> ForwardLabel:
    values = dict(
        signal_date=date(2026, 1, 5), entity_type="stock", entity_code="000001.SZ", benchmark_type="none",
        benchmark_code="", horizon=5, label_type="tradable", entry_date=date(2026, 1, 6), exit_date=date(2026, 1, 10),
        price_basis="qfq", signal_close=10.0, entry_price=10.1, exit_price=11.0, entry_gap=0.01,
        forward_return=0.089, benchmark_return=None, excess_return=None, mae=-0.02, mfe=0.12,
        return_status=ReturnStatus.COMPLETE, path_status=PathStatus.COMPLETE,
        benchmark_status=BenchmarkStatus.NOT_REQUESTED, is_complete=True, excess_is_complete=False,
        source_snapshot_id=101, snapshot_mode=SnapshotMode.BACKFILL,
    )
    values.update(changes)
    return ForwardLabel(**values)


def context() -> ResearchContext:
    return ResearchContext(date(2026, 1, 5), 2, "evaluation_v1", "config-a", "run-a")


def test_forward_label_ddl_keys_by_snapshot_identity_and_mode() -> None:
    assert "source_snapshot_id BIGINT NOT NULL" in FORWARD_LABEL_DDL
    assert "snapshot_mode VARCHAR(16) NOT NULL" in FORWARD_LABEL_DDL
    assert "source_snapshot_id, snapshot_mode" in FORWARD_LABEL_DDL
    assert "label_model_version VARCHAR(64) NOT NULL" in FORWARD_LABEL_DDL
    assert "label_config_hash VARCHAR(64) NOT NULL" in FORWARD_LABEL_DDL
    assert "run_id VARCHAR(64) NOT NULL" in FORWARD_LABEL_DDL


def test_persisted_label_carries_provenance_and_non_null_benchmark_identity() -> None:
    connection = Connection()
    persist_forward_labels(connection, [label()], context())
    assert connection.committed is True
    _, rows = connection.cursor_instance.executemany_calls[0]
    row = rows[0]
    assert row[0:7] == (101, "backfill", date(2026, 1, 5), "stock", "000001.SZ", "none", "")
    assert row[-3:] == ("evaluation_v1", "config-a", "run-a")


def test_forward_label_requires_snapshot_identity() -> None:
    with pytest.raises(ValueError, match="source_snapshot_id"):
        persist_forward_labels(Connection(), [label(source_snapshot_id=None)], context())


def test_delayed_sector_not_matured_then_unsupported_updates_one_row_idempotently() -> None:
    immature = build_delayed_not_matured_label(
        signal_date=date(2026, 1, 5), entity_type="sector_l2", entity_code="S1", horizon=1,
        label_type="close_to_close", source_snapshot_id=99, snapshot_mode=SnapshotMode.DELAYED_SHADOW,
    )
    unsupported = build_delayed_unavailable_label(
        signal_date=date(2026, 1, 5), entity_type="sector_l2", entity_code="S1", horizon=1,
        source_snapshot_id=99, snapshot_mode=SnapshotMode.DELAYED_SHADOW,
    )
    connection = UpsertConnection()

    persist_forward_labels(connection, [immature], context())
    persist_forward_labels(connection, [unsupported], context())
    persist_forward_labels(connection, [unsupported], context())

    assert len(connection.cursor_instance.rows) == 1
    stored = next(iter(connection.cursor_instance.rows.values()))
    assert stored[9] == "delayed_shadow_requires_tradable_open"
    assert stored[21] == ReturnStatus.UNSUPPORTED_PRICE_WINDOW.value
