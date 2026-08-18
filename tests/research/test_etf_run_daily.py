from datetime import date
from decimal import Decimal

import pytest

from morning_conference.sector_rotation2.research.config_hash import build_config_hash
from morning_conference.sector_rotation2.research.etf_core import run_daily
from morning_conference.sector_rotation2.research.status import SnapshotMode


def test_etf_runner_accepts_live_and_backfill_arguments() -> None:
    parser = run_daily.build_parser()
    live = parser.parse_args(["--as-of-date", "2026-08-18", "--level", "1"])
    backfill = parser.parse_args([
        "--backfill-start", "2026-08-10", "--backfill-end", "2026-08-18", "--level", "2",
    ])

    assert live.as_of_date == "2026-08-18"
    assert backfill.backfill_end == "2026-08-18"


def test_live_runner_rejects_historical_as_of_date() -> None:
    with pytest.raises(ValueError, match="BACKFILL"):
        run_daily.validate_mode_for_date(
            date(2026, 8, 17), SnapshotMode.LIVE_SHADOW, today=date(2026, 8, 18),
        )


def test_live_runner_rejects_future_as_of_date() -> None:
    with pytest.raises(ValueError, match="BACKFILL"):
        run_daily.validate_mode_for_date(
            date(2026, 8, 19), SnapshotMode.LIVE_SHADOW, today=date(2026, 8, 18),
        )


def test_runner_loads_one_deterministic_sector_snapshot_with_identity() -> None:
    assert hasattr(run_daily, "load_sector_rows")
    captured: dict[str, object] = {}

    def query(sql: str, params: tuple[object, ...]) -> list[dict[str, object]]:
        captured.update(sql=sql, params=params)
        return [{"sector_name": "半导体", "candidate_status": "ready", "model_version": "sector_opportunity_v1", "config_hash": "cfg", "snapshot_mode": "live_shadow"}]

    assert run_daily.load_sector_rows("2026-08-18", 2, SnapshotMode.LIVE_SHADOW, query) == [
        {"sector_name": "半导体", "candidate_status": "ready", "model_version": "sector_opportunity_v1", "config_hash": "cfg", "snapshot_mode": "live_shadow"},
    ]
    assert "ROW_NUMBER() OVER" in str(captured["sql"])
    assert "entity_type='sector'" in str(captured["sql"])


def test_runner_does_not_migrate_mapping_schema_on_every_execution(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(run_daily, "ensure_mapping_schema", lambda: (_ for _ in ()).throw(AssertionError("DDL")), raising=False)
    monkeypatch.setattr(run_daily, "MySQLSnapshotStore", lambda: type("Store", (), {"ensure_schema": lambda self: None})())
    monkeypatch.setattr(run_daily, "load_sector_rows", lambda *_: [])

    assert run_daily.run_one_date(date.today().isoformat(), 2) == 0


def test_runner_uses_loaded_execution_evidence_instead_of_defaults(monkeypatch: pytest.MonkeyPatch) -> None:
    today = date.today()
    mappings = [
        {"etf_code": "READY", "source_reference": "ref-ready"},
        {"etf_code": "EXTENDED", "source_reference": "ref-extended"},
        {"etf_code": "MISSING", "source_reference": "ref-missing"},
    ]
    evidence = {
        "READY": {"liquid": True, "extended": False, "avg_amount_20": 20_000_000.0},
        "EXTENDED": {"liquid": True, "extended": True, "avg_amount_20": 20_000_000.0},
        "MISSING": None,
    }
    snapshots = []
    monkeypatch.setattr(run_daily, "MySQLSnapshotStore", lambda: type("Store", (), {"ensure_schema": lambda self: None})())
    monkeypatch.setattr(run_daily, "load_sector_rows", lambda *_: [{
        "sector_name": "Bank", "candidate_status": "ready", "model_version": "sector_v1",
        "config_hash": "sector-cfg", "snapshot_mode": "live_shadow",
    }])
    monkeypatch.setattr(run_daily, "load_effective_return_etfs", lambda *_: mappings)
    monkeypatch.setattr(run_daily, "load_etf_macd_evidence", lambda *_: {"macd_triggered": True})
    monkeypatch.setattr(run_daily, "load_etf_execution_evidence", lambda code, _: evidence[code])
    monkeypatch.setattr(run_daily, "persist_etf_candidate", lambda _store, snapshot: snapshots.append(snapshot))

    assert run_daily.run_one_date(today.isoformat(), 2) == 3
    assert [snapshot.candidate_status for snapshot in snapshots] == ["ready", "extended", "blocked"]
    assert snapshots[0].feature_json["liquid"] is True
    assert snapshots[0].feature_json["extended"] is False
    assert "liquid" not in snapshots[2].feature_json
    assert "extended" not in snapshots[2].feature_json


def test_runner_uses_return_mappings_without_holdings_loader(monkeypatch: pytest.MonkeyPatch) -> None:
    today = date.today()
    mapping = {
        "etf_code": "LOW_CONFIDENCE",
        "mapping_type": "return_exposure_derived",
        "mapping_method": "sw2_return_regression_v1",
        "is_primary": 0,
        "effective_from": today,
        "effective_to": None,
        "source_as_of_date": today,
        "source_provider": "local_trade_daily",
        "mapping_version": "return_v1",
        "config_hash": "return-cfg",
        "rank_no": 2,
        "quality_status": "qualified",
        "failure_reason": None,
        "lookback_trading_days": 60,
        "window_start_date": date(2026, 5, 29),
        "window_end_date": today,
        "sample_count": 60,
        "corr": Decimal("0.80"),
        "beta": Decimal("1.10"),
        "r_squared": Decimal("0.64"),
        "residual_vol": Decimal("0.12"),
        "sector_fit_score": Decimal("0.90"),
        "confidence_status": "low_confidence",
        "price_source": "local_trade_daily",
        "price_as_of_date": today,
        "universe_source": "local_domestic_equity_etf",
    }
    snapshots = []
    return_loader_calls: list[tuple[object, ...]] = []
    monkeypatch.setattr(run_daily, "MySQLSnapshotStore", lambda: type("Store", (), {"ensure_schema": lambda self: None})())
    monkeypatch.setattr(run_daily, "load_sector_rows", lambda *_: [{
        "sector_name": "Bank", "candidate_status": "ready", "model_version": "sector_v1",
        "config_hash": "sector-cfg", "snapshot_mode": "live_shadow",
    }])
    def load_return_mappings(*args: object) -> list[dict[str, object]]:
        return_loader_calls.append(args)
        return [mapping]

    monkeypatch.setattr(run_daily, "load_effective_return_etfs", load_return_mappings)
    monkeypatch.setattr(
        run_daily,
        "load_effective_etfs",
        lambda *_: (_ for _ in ()).throw(AssertionError("holdings loader must not run")),
        raising=False,
    )
    monkeypatch.setattr(run_daily, "load_etf_macd_evidence", lambda *_: {"macd_triggered": True})
    monkeypatch.setattr(run_daily, "load_etf_execution_evidence", lambda *_: {"liquid": True, "extended": False})
    monkeypatch.setattr(run_daily, "persist_etf_candidate", lambda _store, snapshot: snapshots.append(snapshot))

    assert run_daily.run_one_date(today.isoformat(), 2) == 1
    assert snapshots[0].candidate_status == "blocked"
    assert "low_return_exposure_confidence" in snapshots[0].risk_flags_json
    assert return_loader_calls == [("Bank", 2, today)]
    expected_mapping = {
        "sector_level": 2,
        "sector_name": "Bank",
        "etf_code": "LOW_CONFIDENCE",
        "source_as_of_date": today.isoformat(),
        "source_provider": "local_trade_daily",
        "mapping_version": "return_v1",
        "config_hash": "return-cfg",
        "rank_no": 2,
        "mapping_type": "return_exposure_derived",
        "quality_status": "qualified",
        "mapping_method": "sw2_return_regression_v1",
        "window_start_date": "2026-05-29",
        "window_end_date": today.isoformat(),
        "lookback_trading_days": 60,
        "sample_count": 60,
        "corr": "0.80",
        "beta": "1.10",
        "r_squared": "0.64",
        "residual_vol": "0.12",
        "sector_fit_score": "0.90",
        "confidence_status": "low_confidence",
        "price_source": "local_trade_daily",
        "price_as_of_date": today.isoformat(),
        "universe_source": "local_domestic_equity_etf",
        "upstream_sector_snapshot": {
            "as_of_date": today.isoformat(),
            "entity_type": "sector",
            "entity_code": "Bank",
            "strategy_type": "sector_opportunity",
            "model_version": "sector_v1",
            "config_hash": "sector-cfg",
            "snapshot_mode": "live_shadow",
        },
    }
    assert snapshots[0].feature_json["mapping"] == expected_mapping
    assert snapshots[0].config_hash == build_config_hash(
        {"model_version": "etf_core_v1", "mapping": expected_mapping},
    )
