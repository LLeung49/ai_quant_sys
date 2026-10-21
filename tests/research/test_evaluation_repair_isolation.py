from datetime import date

from morning_conference.sector_rotation2.research.evaluation import run_backfill, run_evaluation
from morning_conference.sector_rotation2.research.status import SnapshotMode


def test_label_backfill_excludes_rejected_repair_snapshots(monkeypatch):
    seen = []
    monkeypatch.setattr(run_backfill, "execute_query", lambda sql, params: seen.append(sql) or [])
    run_backfill.run(
        snapshot_mode=SnapshotMode.LIVE_SHADOW,
        start_date=date(2026, 8, 20), end_date=date(2026, 9, 18), sector_level=2,
    )
    assert "validation_status='rejected'" in seen[0]
    assert "stock_repair" in seen[0]


def test_label_backfill_can_scope_to_one_strategy(monkeypatch):
    seen = []
    monkeypatch.setattr(run_backfill, "execute_query", lambda sql, params: seen.append((sql, params)) or [])
    run_backfill.run(
        snapshot_mode=SnapshotMode.BACKFILL,
        start_date=date(2024, 1, 2), end_date=date(2024, 1, 31), sector_level=2,
        strategy_type="stock_repair",
    )
    assert "strategy_type=%s" in seen[0][0]
    assert "stock_repair" in seen[0][1]


def test_aggregation_excludes_rejected_repair_snapshots(monkeypatch):
    seen = []
    monkeypatch.setattr(run_evaluation, "execute_query", lambda sql, params: seen.append(sql) or [])
    run_evaluation.run(
        snapshot_mode="live_shadow",
        start_date=date(2026, 8, 20), end_date=date(2026, 9, 18),
    )
    assert "validation_status='rejected'" in seen[0]
    assert "stock_repair" in seen[0]


def test_aggregation_can_scope_to_one_strategy(monkeypatch):
    seen = []
    monkeypatch.setattr(run_evaluation, "execute_query", lambda sql, params: seen.append((sql, params)) or [])
    run_evaluation.run(
        snapshot_mode="backfill", start_date=date(2024, 1, 2), end_date=date(2024, 1, 31),
        strategy_type="stock_repair",
    )
    assert "strategy_type=%s" in seen[0][0]
    assert "stock_repair" in seen[0][1]
