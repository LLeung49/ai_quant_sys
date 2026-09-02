"""Tests for trend service + run_daily orchestration."""

import json
from datetime import date, timedelta
from typing import Any

import pytest

from morning_conference.sector_rotation2.research.snapshot import InMemorySnapshotStore, SnapshotConflictError
from morning_conference.sector_rotation2.research.status import ResearchStatus, SnapshotMode
from morning_conference.sector_rotation2.research.stock_alpha import run_trend_daily
from morning_conference.sector_rotation2.research.stock_alpha.common import load_stock_universe
from morning_conference.sector_rotation2.research.stock_alpha.config import TrendAlphaConfig
from morning_conference.sector_rotation2.research.stock_alpha.run_trend_daily import (
    build_parser,
    run_one_date,
    validate_mode_for_date,
)
from morning_conference.sector_rotation2.research.stock_alpha.service import (
    build_trend_candidate,
    load_trend_follow_sectors,
    persist_trend_candidates,
    score_features_frame,
)


class _StubMySQLSnapshotStore:
    def __init__(self) -> None:
        self._inner = InMemorySnapshotStore()

    def ensure_schema(self) -> None:
        return None

    def get(self, identity):
        return self._inner.get(identity)

    def insert(self, snapshot) -> None:
        self._inner.insert(snapshot)


_AS_OF = date(2026, 8, 17)
_HISTORY_DAYS = 60


def _history_days() -> list[date]:
    days = [_AS_OF - timedelta(days=_HISTORY_DAYS - 1 - i) for i in range(_HISTORY_DAYS)]
    return list(reversed(days))


def _status_rows() -> list[dict[str, Any]]:
    return [
        {"stock_code": "600000", "listing_date": date(2024, 1, 2), "is_suspended": False,
         "is_tradable": True, "sector_1": "Bank", "sector_2": "State Bank"},
        {"stock_code": "000001", "listing_date": date(2024, 1, 2), "is_suspended": False,
         "is_tradable": True, "sector_1": "Bank", "sector_2": "Joint Bank"},
        {"stock_code": "601318", "listing_date": date(2020, 1, 2), "is_suspended": False,
         "is_tradable": True, "sector_1": "Insurance", "sector_2": "Insurance"},
        {"stock_code": "300750", "listing_date": date(2018, 6, 1), "is_suspended": True,
         "is_tradable": True, "sector_1": "Tech", "sector_2": "EV Battery"},
    ]


def _price_history_rows() -> list[dict[str, Any]]:
    return [
        {"stock_code": "600000", "valid_price_days": 250},
        {"stock_code": "000001", "valid_price_days": 250},
        {"stock_code": "601318", "valid_price_days": 250},
        {"stock_code": "300750", "valid_price_days": 1800},
    ]


def _stock_close_rows() -> list[dict[str, Any]]:
    days = _history_days()
    rows = []
    for code, base in [("600000", 10), ("000001", 20), ("601318", 30)]:
        for i, d in enumerate(days):
            # The SQL aliases ``close_price AS close``; the stub mirrors that.
            rows.append({"stock_code": code, "trade_date": d, "close": base + i * 0.5,
                         "volume": 1000, "amount": 1000})
    return rows


def _sector_close_rows() -> list[dict[str, Any]]:
    days = _history_days()
    return [
        {"sector_name": "Bank", "trade_date": d, "close": 1000 + i * 5} for i, d in enumerate(days)
    ] + [
        {"sector_name": "Insurance", "trade_date": d, "close": 2000 + i * 3} for i, d in enumerate(days)
    ]


def _stub_query(sql: str, params: tuple) -> list[dict[str, Any]]:
    normalized = " ".join(sql.split())
    if "FROM research_candidate_snapshot" in normalized and "canonical_rank=1" in normalized:
        snapshot_mode_value = params[2]
        return [
            {"sector_name": "Bank", "candidate_status": "trend_reinforced", "model_version": "sector_opportunity_v1",
             "config_hash": "abc", "snapshot_mode": snapshot_mode_value,
             "feature_json": json.dumps({"playbook": "trend_follow", "lifecycle_state": "trending"})},
            {"sector_name": "Insurance", "candidate_status": "trend_reinforced", "model_version": "sector_opportunity_v1",
             "config_hash": "abc", "snapshot_mode": snapshot_mode_value,
             "feature_json": json.dumps({"playbook": "trend_follow", "lifecycle_state": "trending"})},
            {"sector_name": "Repair", "candidate_status": "recovery_confirming", "model_version": "sector_opportunity_v1",
             "config_hash": "abc", "snapshot_mode": snapshot_mode_value,
             "feature_json": json.dumps({"playbook": "repair_probe", "lifecycle_state": "emerging"})},
        ]
    if "AS sector_name" in normalized and "FROM trade_stock_status" in normalized:
        return [{"stock_code": code, "sector_name": name} for code, name in
                [("600000", "Bank"), ("000001", "Bank"), ("601318", "Insurance"), ("300750", "Tech")]]
    if "FROM trade_stock_status" in normalized and "GROUP BY" not in normalized:
        return _status_rows()
    if "FROM trade_stock_daily_qfq" in normalized and "GROUP BY" in normalized:
        return _price_history_rows()
    if "FROM trade_stock_daily_qfq" in normalized:
        return _stock_close_rows()
    if "FROM trade_sector_daily" in normalized:
        return _sector_close_rows()
    return []


def test_load_trend_follow_sectors_filters_by_playbook() -> None:
    sectors = load_trend_follow_sectors("2026-08-17", 1, SnapshotMode.LIVE_SHADOW, _stub_query)
    names = {s["sector_name"] for s in sectors}
    assert names == {"Bank", "Insurance"}


def test_load_stock_universe_filters_by_sector_and_eligibility() -> None:
    cfg = TrendAlphaConfig()
    universe = load_stock_universe(
        as_of_date=_AS_OF,
        sector_names={"Bank"},
        sector_level=1,
        config=cfg,
        query=_stub_query,
    )
    codes = {row.stock_code for row in universe}
    assert codes == {"600000", "000001"}


def _build_context():
    from morning_conference.sector_rotation2.research.stock_alpha.service import SectorTrendContext
    return SectorTrendContext(
        as_of_date=_AS_OF,
        sector_level=1,
        sector_name="Bank",
        model_version="sector_opportunity_v1",
        config_hash="abc",
        snapshot_mode=SnapshotMode.LIVE_SHADOW,
    )


def _base_row() -> dict[str, Any]:
    return {
        "stock_code": "600000", "candidate_score": 0.0, "risk_penalty": 0.0,
        "alpha_strength": 0.0, "breakout20": False, "breakout60": False,
        "strong_pullback": False, "limit_up_streak": None, "hot_leader_source": "unavailable",
        "mapping_quality": "current_mapping", "eligibility_unknown": [],
        "rr_5": None, "rr_10": None, "rr_20": None, "alpha_persistence": None,
        "trend_quality": None, "er": None, "adx": None, "ma_stack": False,
        "trend_structure": None, "liquidity": None, "amount_20d_median": None,
        "distance_ma20": None, "volatility_20d": None, "hot_leader_bonus": 0.0,
        "rank_in_sector": None,
    }


def test_build_trend_candidate_is_shadow_and_manual_only() -> None:
    cfg = TrendAlphaConfig()
    ctx = _build_context()
    row = {**_base_row(), "candidate_score": 0.30, "alpha_strength": 0.20, "risk_penalty": 0.05,
           "breakout20": True, "ma_stack": True, "amount_20d_median": 1e6}
    snapshot = build_trend_candidate(row=row, sector_context=ctx, config=cfg, run_id="run-1")
    assert snapshot.entity_type == "stock"
    assert snapshot.strategy_type == "stock_trend"
    assert snapshot.research_status is ResearchStatus.SHADOW
    assert snapshot.snapshot_mode is SnapshotMode.LIVE_SHADOW
    assert snapshot.feature_json["sector_playbook"] == "trend_follow"
    assert snapshot.feature_json["upstream_sector_snapshot"]["entity_code"] == "Bank"


def test_persist_trend_candidates_rejects_unsupported_mode() -> None:
    cfg = TrendAlphaConfig()
    ctx = _build_context()
    snapshot = build_trend_candidate(row=_base_row(), sector_context=ctx, config=cfg, run_id="run-1")
    object.__setattr__(snapshot, "snapshot_mode", SnapshotMode.REPLAY)
    with pytest.raises(ValueError, match="LIVE_SHADOW or BACKFILL"):
        persist_trend_candidates(InMemorySnapshotStore(), [snapshot])


def test_persist_trend_candidates_idempotent_on_live_shadow() -> None:
    cfg = TrendAlphaConfig()
    ctx = _build_context()
    snapshot = build_trend_candidate(row=_base_row(), sector_context=ctx, config=cfg, run_id="run-1")
    store = InMemorySnapshotStore()
    persist_trend_candidates(store, [snapshot])
    persist_trend_candidates(store, [snapshot])


def test_persist_trend_candidates_conflict_on_changed_payload() -> None:
    cfg = TrendAlphaConfig()
    ctx = _build_context()
    snapshot = build_trend_candidate(row=_base_row(), sector_context=ctx, config=cfg, run_id="run-1")
    store = InMemorySnapshotStore()
    persist_trend_candidates(store, [snapshot])
    changed_snapshot = build_trend_candidate(
        row={**_base_row(), "candidate_score": 0.10},
        sector_context=ctx, config=cfg, run_id="run-2",
    )
    with pytest.raises(SnapshotConflictError):
        persist_trend_candidates(store, [changed_snapshot])


def test_run_one_date_persists_only_trend_follow_sectors(monkeypatch: pytest.MonkeyPatch) -> None:
    captured: dict[str, Any] = {}
    monkeypatch.setattr(run_trend_daily, "MySQLSnapshotStore", _StubMySQLSnapshotStore)
    monkeypatch.setattr(run_trend_daily, "create_run", lambda *args: captured.update(create=args))
    monkeypatch.setattr(run_trend_daily, "mark_run_succeeded", lambda *args: captured.update(succeeded=args))
    monkeypatch.setattr(run_trend_daily, "mark_run_failed", lambda *args: captured.update(failed=args))
    count = run_one_date("2026-08-17", 1, SnapshotMode.LIVE_SHADOW, today=_AS_OF, query=_stub_query)
    assert count > 0
    assert captured["succeeded"][1] == count


def test_run_one_date_rejects_live_mode_for_historical_date() -> None:
    with pytest.raises(ValueError, match="non-today --as-of-date requires BACKFILL"):
        run_one_date("2026-08-10", 1, SnapshotMode.LIVE_SHADOW)


def test_validate_mode_for_date_accepts_backfill_anywhere() -> None:
    validate_mode_for_date(date(2020, 1, 1), SnapshotMode.BACKFILL, today=_AS_OF)


def test_build_parser_accepts_backfill_window() -> None:
    parser = build_parser()
    args = parser.parse_args(["--backfill-start", "2026-08-10", "--backfill-end", "2026-08-17", "--level", "2"])
    assert args.backfill_start == "2026-08-10"
    assert args.backfill_end == "2026-08-17"


def test_build_parser_retains_force_replace_flag() -> None:
    parser = build_parser()
    args = parser.parse_args(["--as-of-date", "2026-08-17", "--level", "2", "--force-replace"])
    assert args.force_replace is True
    assert args.level == 2


def test_force_replace_trend_deletes_only_requested_snapshot_mode() -> None:
    calls: list[tuple[str, tuple[object, ...]]] = []

    def query(sql: str, params: tuple[object, ...]) -> list[dict[str, int]]:
        calls.append((sql, params))
        return [{"c": 2}]

    def update(sql: str, params: tuple[object, ...]) -> None:
        calls.append((sql, params))

    deleted = run_trend_daily._delete_existing_trend_snapshots(
        "2026-08-17", 2, SnapshotMode.DELAYED_SHADOW, query=query, update=update,
    )

    assert deleted == 2
    assert all("snapshot_mode=%s" in sql for sql, _ in calls)
    assert all(params == ("2026-08-17", 2, "delayed_shadow") for _, params in calls)


def test_build_parser_rejects_missing_date_window() -> None:
    parser = build_parser()
    with pytest.raises(SystemExit):
        parser.parse_args(["--level", "2"])


def _sample_feature_frame():
    import pandas as pd
    return pd.DataFrame({
        "as_of_date": [_AS_OF] * 4,
        "sector_name": ["Bank", "Bank", "Bank", "Tech"],
        "sector_level": [1] * 4,
        "stock_code": ["600000", "000001", "601318", "300750"],
        "rr_5": [0.02, -0.01, 0.03, -0.02],
        "rr_10": [0.04, -0.02, 0.05, -0.03],
        "rr_20": [0.06, -0.04, 0.07, -0.05],
        "er": [0.6, 0.4, 0.7, 0.3],
        "adx": [None, None, None, None],
        "ma_stack": [True, False, True, False],
        "breakout20": [True, False, True, False],
        "breakout60": [False, False, True, False],
        "strong_pullback": [False, True, False, False],
        "distance_ma20": [0.10, 0.05, 0.30, 0.50],
        "volatility_20d": [0.20, 0.15, 0.25, 0.40],
        "amount_20d_median": [2e6, 1e6, 3e6, 5e5],
        "limit_up_streak": [None, None, None, None],
        "hot_leader_source": ["unavailable"] * 4,
        "mapping_quality": ["current_mapping"] * 4,
        "eligibility_unknown": [[], [], [], []],
    })


def test_score_features_frame_returns_expected_columns() -> None:
    cfg = TrendAlphaConfig()
    frame = score_features_frame(_sample_feature_frame(), config=cfg)
    assert "candidate_score" in frame.columns
    assert "rank_in_sector" in frame.columns
    assert "risk_penalty" in frame.columns


def test_score_features_frame_handles_empty_frame() -> None:
    import pandas as pd
    cfg = TrendAlphaConfig()
    frame = score_features_frame(pd.DataFrame(), config=cfg)
    assert "candidate_score" in frame.columns
    assert "rank_in_sector" in frame.columns
    assert len(frame) == 0
