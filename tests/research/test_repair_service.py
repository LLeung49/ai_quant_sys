"""Tests for the Repair service layer."""

import json
from datetime import date
from typing import Any

import pytest

from morning_conference.sector_rotation2.research.financial.service import (
    REPAIR_PLAYBOOKS,
    RepairSectorContext,
    build_repair_candidate,
    load_repair_sectors,
    persist_repair_candidates,
    score_repair_sector,
)
from morning_conference.sector_rotation2.research.snapshot import InMemorySnapshotStore, SnapshotConflictError
from morning_conference.sector_rotation2.research.status import ExecutionStatus, ResearchStatus, SnapshotMode
from morning_conference.sector_rotation2.research.stock_alpha.config import TrendAlphaConfig


def _raw_rows() -> list[dict[str, Any]]:
    """Build 4 quarterly raw rows for a single stock."""

    periods = [
        (date(2025, 9, 30), date(2025, 10, 25), date(2025, 10, 25), "h1"),
        (date(2025, 12, 31), date(2026, 1, 25), date(2026, 1, 25), "h2"),
        (date(2026, 3, 31), date(2026, 4, 25), date(2026, 4, 25), "h3"),
        (date(2026, 6, 30), date(2026, 7, 25), date(2026, 7, 25), "h4"),
    ]
    rows = []
    for report, announce, first_seen, h in periods:
        rows.append({
            "stock_code": "600000",
            "source_table": "miniqmt",
            "report_date": report,
            "period_type": "quarterly",
            "announcement_date": announce,
            "first_seen_at": first_seen,
            "source_hash": h,
            "is_restated": 0,
            "source_verified": 1,
            "data_source": "miniqmt",
            "revenue": 100.0,
            "net_profit": 10.0,
            "total_assets": 200.0,
            "total_equity": 80.0,
            "operating_cash_flow": 15.0,
        })
    return rows


def _capital_rows() -> list[dict[str, Any]]:
    return [{
        "stock_code": "600000",
        "report_date": date(2026, 6, 30),
        "announcement_date": date(2026, 7, 25),
        "total_shares": 1000.0,
        "circulating_shares": 950.0,
        "source_hash": "c1",
        "data_source": "miniqmt",
    }]


def _stub_query(sql: str, params: tuple) -> list[dict[str, Any]]:
    norm = " ".join(sql.split())
    if "FROM trade_stock_daily" in norm and "WHERE trade_date = %s" in norm:
        return [{"stock_code": "600000", "close": 10.0}]
    if "FROM trade_stock_financial_raw_pit" in norm:
        return _raw_rows()
    if "FROM trade_stock_capital_pit" in norm:
        return _capital_rows()
    if "FROM research_candidate_snapshot" in norm and "canonical_rank=1" in norm:
        return [{
            "sector_name": "Bank", "candidate_status": "trend_reinforced",
            "model_version": "sector_opportunity_v1", "config_hash": "abc",
            "snapshot_mode": params[2],
            "feature_json": json.dumps({"playbook": "repair_probe", "lifecycle_state": "emerging"}),
        }]
    return []


def test_repair_playbooks_constant() -> None:
    assert REPAIR_PLAYBOOKS == frozenset({"repair_probe", "early_repair"})


def test_load_repair_sectors_filters_by_playbook() -> None:
    sectors = load_repair_sectors("2026-08-17", 2, SnapshotMode.BACKFILL, _stub_query)
    names = {s["sector_name"] for s in sectors}
    assert names == {"Bank"}


def test_build_repair_candidate_is_shadow_and_manual_only() -> None:
    cfg = TrendAlphaConfig()
    ctx = RepairSectorContext(
        as_of_date=date(2026, 8, 17), sector_level=2, sector_name="Bank",
        model_version="sector_opportunity_v1", config_hash="abc",
        snapshot_mode=SnapshotMode.BACKFILL,
    )
    row = {
        "stock_code": "600000", "candidate_score": 0.30, "candidate_status": "repair_full",
        "valuation_rank": 0.5, "quality_score": 0.20, "technical_score": 0.0,
        "momentum_score": 0.25, "risk_penalty": 0.0,
        "attribution": {"valuation_rank": 0.5}, "qualitative_flags": [],
        "payout_subtype": "original",
    }
    snapshot = build_repair_candidate(row=row, sector_context=ctx, config=cfg, run_id="run-1")
    assert snapshot.entity_type == "stock"
    assert snapshot.strategy_type == "stock_repair"
    assert snapshot.research_status is ResearchStatus.SHADOW
    assert snapshot.execution_status is ExecutionStatus.MANUAL_ONLY
    assert snapshot.feature_json["sector_playbook"] == "repair_probe"


def test_persist_repair_candidates_rejects_unsupported_mode() -> None:
    cfg = TrendAlphaConfig()
    ctx = RepairSectorContext(
        as_of_date=date(2026, 8, 17), sector_level=2, sector_name="Bank",
        model_version="sector_opportunity_v1", config_hash="abc",
        snapshot_mode=SnapshotMode.BACKFILL,
    )
    row = {
        "stock_code": "600000", "candidate_score": 0.0, "candidate_status": "value_trap",
        "valuation_rank": None, "quality_score": None, "technical_score": 0.0,
        "momentum_score": None, "risk_penalty": 0.0,
        "attribution": {}, "qualitative_flags": [],
        "payout_subtype": "original",
    }
    snapshot = build_repair_candidate(row=row, sector_context=ctx, config=cfg, run_id="run-1")
    object.__setattr__(snapshot, "snapshot_mode", SnapshotMode.REPLAY)
    with pytest.raises(ValueError, match="LIVE_SHADOW or BACKFILL"):
        persist_repair_candidates(InMemorySnapshotStore(), [snapshot])


def test_persist_repair_candidates_idempotent_on_live_shadow() -> None:
    cfg = TrendAlphaConfig()
    ctx = RepairSectorContext(
        as_of_date=date(2026, 8, 17), sector_level=2, sector_name="Bank",
        model_version="sector_opportunity_v1", config_hash="abc",
        snapshot_mode=SnapshotMode.LIVE_SHADOW,
    )
    row = {
        "stock_code": "600000", "candidate_score": 0.0, "candidate_status": "value_trap",
        "valuation_rank": None, "quality_score": None, "technical_score": 0.0,
        "momentum_score": None, "risk_penalty": 0.0,
        "attribution": {}, "qualitative_flags": [],
        "payout_subtype": "original",
    }
    snapshot = build_repair_candidate(row=row, sector_context=ctx, config=cfg, run_id="run-1")
    store = InMemorySnapshotStore()
    persist_repair_candidates(store, [snapshot])
    persist_repair_candidates(store, [snapshot])


def test_persist_repair_candidates_conflict_on_changed_payload() -> None:
    cfg = TrendAlphaConfig()
    ctx = RepairSectorContext(
        as_of_date=date(2026, 8, 17), sector_level=2, sector_name="Bank",
        model_version="sector_opportunity_v1", config_hash="abc",
        snapshot_mode=SnapshotMode.BACKFILL,
    )
    row = {
        "stock_code": "600000", "candidate_score": 0.0, "candidate_status": "value_trap",
        "valuation_rank": None, "quality_score": None, "technical_score": 0.0,
        "momentum_score": None, "risk_penalty": 0.0,
        "attribution": {}, "qualitative_flags": [],
        "payout_subtype": "original",
    }
    snapshot = build_repair_candidate(row=row, sector_context=ctx, config=cfg, run_id="run-1")
    store = InMemorySnapshotStore()
    persist_repair_candidates(store, [snapshot])
    changed = build_repair_candidate(
        row={**row, "candidate_score": 0.10}, sector_context=ctx, config=cfg, run_id="run-2",
    )
    with pytest.raises(SnapshotConflictError):
        persist_repair_candidates(store, [changed])


def test_score_repair_sector_emits_snapshot_for_eligible_stock() -> None:
    cfg = TrendAlphaConfig()
    snapshots = score_repair_sector(
        {
            "sector_name": "Bank", "candidate_status": "trend_reinforced",
            "model_version": "sector_opportunity_v1", "config_hash": "abc",
            "snapshot_mode": "backfill",
        },
        as_of_date="2026-08-17", level=2, mode=SnapshotMode.BACKFILL,
        config=cfg, run_id="run-1", store=None, query=_stub_query,
    )
    assert len(snapshots) == 1
    assert snapshots[0].entity_code == "600000"
    assert snapshots[0].strategy_type == "stock_repair"


def test_run_repair_daily_parser_accepts_backfill_window() -> None:
    from morning_conference.sector_rotation2.research.stock_alpha.run_repair_daily import (
        build_parser,
    )
    parser = build_parser()
    args = parser.parse_args([
        "--as-of-date", "2026-08-17", "--level", "2",
        "--mode", "backfill", "--dry-run", "--allow-estimated-pit",
    ])
    assert args.as_of_date == "2026-08-17"
    assert args.level == 2
    assert args.mode == "backfill"
    assert args.dry_run is True
    assert args.allow_estimated_pit is True


def test_run_repair_daily_parser_rejects_missing_date_window() -> None:
    from morning_conference.sector_rotation2.research.stock_alpha.run_repair_daily import (
        build_parser,
    )
    parser = build_parser()
    with pytest.raises(SystemExit):
        parser.parse_args(["--level", "2"])


def test_run_repair_daily_rejects_live_mode_for_historical_date() -> None:
    from morning_conference.sector_rotation2.research.stock_alpha.run_repair_daily import (
        run_one_date,
    )
    with pytest.raises(ValueError, match="non-today"):
        run_one_date("2026-08-10", 2, SnapshotMode.LIVE_SHADOW)


def test_run_repair_daily_validate_mode_accepts_backfill_anywhere() -> None:
    from morning_conference.sector_rotation2.research.stock_alpha.run_repair_daily import (
        validate_mode_for_date,
    )
    validate_mode_for_date(date(2020, 1, 1), SnapshotMode.BACKFILL, today=date(2026, 8, 17))
