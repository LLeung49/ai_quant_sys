from datetime import date, datetime

from fastapi.testclient import TestClient

from morning_conference.sector_rotation2.api.app import create_app
from morning_conference.sector_rotation2.api import research_router


def _row(strategy: str, entity: str, status: str = "ready") -> dict:
    return {
        "id": 1, "as_of_date": date(2026, 8, 20), "entity_type": "stock",
        "entity_code": entity, "sector_level": 2, "sector_name": "半导体",
        "strategy_type": strategy, "candidate_status": status, "candidate_score": 0.5,
        "rank_in_sector": 1, "research_status": "shadow", "validation_status": "not_evaluated",
        "execution_status": "manual_only", "model_version": "v2", "config_hash": "hash",
        "snapshot_mode": "live_shadow", "feature_json": "{}", "reasons_json": "[]",
        "risk_flags_json": "[]", "created_at": date(2026, 8, 20),
    }


def test_today_summary_reads_current_snapshot_rows(monkeypatch):
    monkeypatch.setattr(research_router, "execute_query", lambda *_: [_row("stock_trend", "600000")])
    client = TestClient(create_app())
    response = client.get("/api/v1/sector-rotation/research/today-summary", params={"as_of_date": "2026-08-20"})
    assert response.status_code == 200
    assert response.json()["summary"]["trend_candidates"] == 1
    assert response.json()["research_status"] == "shadow"


def test_today_summary_counts_explicit_data_quality_blocks(monkeypatch):
    monkeypatch.setattr(
        research_router,
        "execute_query",
        lambda *_: [{
            **_row("stock_trend", "600000", status="data_quality_blocked"),
            "risk_flags_json": "[]",
        }],
    )
    response = TestClient(create_app()).get(
        "/api/v1/sector-rotation/research/today-summary",
        params={"as_of_date": "2026-08-20"},
    )

    assert response.status_code == 200
    assert response.json()["summary"]["data_quality_blocked"] == 1


def test_invalid_date_is_stable_error(monkeypatch):
    monkeypatch.setattr(research_router, "execute_query", lambda *_: [])
    response = TestClient(create_app()).get("/api/v1/sector-rotation/research/opportunities", params={"as_of_date": "bad"})
    assert response.status_code == 422
    assert response.json()["error"]["code"] == "INVALID_DATE"


def test_stock_endpoint_accepts_strategy_filter(monkeypatch):
    seen = {}
    def fake_query(sql, params):
        seen["params"] = params
        return [_row("stock_repair", "600000")]
    monkeypatch.setattr(research_router, "execute_query", fake_query)
    response = TestClient(create_app()).get("/api/v1/sector-rotation/research/stock-candidates", params={"as_of_date": "2026-08-20", "strategy_type": "stock_repair"})
    assert response.status_code == 200
    assert response.json()["candidates"][0]["strategy_type"] == "stock_repair"
    assert "stock_repair" in seen["params"]


def test_rejected_legacy_repair_snapshots_are_hidden_from_workbench(monkeypatch):
    seen = {}

    def fake_query(sql, params):
        seen["sql"] = " ".join(sql.split())
        return []

    monkeypatch.setattr(research_router, "execute_query", fake_query)
    response = TestClient(create_app()).get(
        "/api/v1/sector-rotation/research/stock-candidates",
        params={"as_of_date": "2025-01-15", "strategy_type": "stock_repair",
                "snapshot_mode": "backfill"},
    )
    assert response.status_code == 200
    assert "NOT (strategy_type='stock_repair' AND validation_status='rejected')" in seen["sql"]


def test_candidate_endpoint_returns_security_name_and_falls_back_to_code(monkeypatch):
    seen = {}

    def fake_query(sql, params):
        seen["sql"] = sql
        return [
            {**_row("etf_core", "510300.SH"), "entity_name": "沪深300ETF"},
            _row("etf_core", "510500.SH"),
        ]

    monkeypatch.setattr(research_router, "execute_query", fake_query)
    response = TestClient(create_app()).get(
        "/api/v1/sector-rotation/research/etf-candidates",
        params={"as_of_date": "2026-08-20"},
    )

    assert response.status_code == 200
    assert [row["entity_name"] for row in response.json()["candidates"]] == ["沪深300ETF", "510500.SH"]
    assert "LEFT JOIN trade_stock_status" in seen["sql"]


def test_unscored_etf_is_not_reported_as_data_quality_blocked(monkeypatch):
    def fake_query(_sql, _params):
        return [{
            **_row("etf_core", "510300.SH"),
            "candidate_score": None,
            "candidate_status": "ready",
            "risk_flags_json": "[]",
        }]

    monkeypatch.setattr(research_router, "execute_query", fake_query)
    response = TestClient(create_app()).get(
        "/api/v1/sector-rotation/research/etf-candidates",
        params={"as_of_date": "2026-08-20"},
    )

    assert response.status_code == 200
    assert response.json()["candidates"][0]["is_data_quality_blocked"] is False


def test_explicit_quality_block_is_projected(monkeypatch):
    monkeypatch.setattr(
        research_router,
        "execute_query",
        lambda *_: [{
            **_row("stock_trend", "600000", status="data_quality_blocked"),
            "risk_flags_json": '["data_quality_blocked"]',
        }],
    )
    response = TestClient(create_app()).get(
        "/api/v1/sector-rotation/research/stock-candidates",
        params={"as_of_date": "2026-08-20"},
    )

    assert response.status_code == 200
    assert response.json()["candidates"][0]["is_data_quality_blocked"] is True


def test_delayed_candidate_api_returns_operational_times_without_cross_mode_fallback(monkeypatch):
    calls: list[tuple[str, tuple]] = []

    def fake_query(sql, params):
        calls.append((sql, params))
        return [{
            **_row("stock_trend", "600000"),
            "snapshot_mode": "delayed_shadow",
            "data_available_at": datetime(2026, 8, 24, 18),
            "run_at": datetime(2026, 8, 25, 9, 10),
            "execution_eligible_at": datetime(2026, 8, 25, 9, 30),
            "daily_bar_entry_date": date(2026, 8, 25),
            "availability_basis": "market_close_1800",
        }]

    monkeypatch.setattr(research_router, "execute_query", fake_query)
    response = TestClient(create_app()).get(
        "/api/v1/sector-rotation/research/stock-candidates",
        params={"as_of_date": "2026-08-24", "snapshot_mode": "delayed_shadow"},
    )

    assert response.status_code == 200
    candidate = response.json()["candidates"][0]
    assert candidate["execution_eligible_at"] == "2026-08-25T09:30:00"
    assert candidate["data_available_at"] == "2026-08-24T18:00:00"
    assert candidate["run_at"] == "2026-08-25T09:10:00"
    assert candidate["daily_bar_entry_date"] == "2026-08-25"
    assert candidate["availability_basis"] == "market_close_1800"
    assert len(calls) == 1
    assert calls[0][1][2] == "delayed_shadow"
    assert "daily_bar_entry_date" in calls[0][0]
    assert "TIME(current_snapshot.run_at) < '09:30:00'" in calls[0][0]


def test_delayed_candidate_reports_missing_daily_projection_separately(monkeypatch):
    monkeypatch.setattr(
        research_router,
        "execute_query",
        lambda *_: [{
            **_row("etf_core", "510300.SH"),
            "snapshot_mode": "delayed_shadow",
            "data_available_at": datetime(2026, 8, 28, 18),
            "run_at": datetime(2026, 8, 30, 11, 30),
            "execution_eligible_at": datetime(2026, 8, 31, 9, 30),
            "daily_bar_entry_date": None,
            "availability_basis": "market_close_1800",
        }],
    )

    response = TestClient(create_app()).get(
        "/api/v1/sector-rotation/research/etf-candidates",
        params={"as_of_date": "2026-08-28", "snapshot_mode": "delayed_shadow"},
    )

    assert response.status_code == 200
    candidate = response.json()["candidates"][0]
    assert candidate["execution_eligible_at"] == "2026-08-31T09:30:00"
    assert candidate["daily_bar_entry_date"] is None
    assert candidate["daily_bar_entry_reason"] == "trading_calendar_unavailable"


def test_delayed_summary_remains_in_delayed_mode(monkeypatch):
    seen = {}

    def fake_query(_sql, params):
        seen["params"] = params
        return [{**_row("stock_trend", "600000"), "snapshot_mode": "delayed_shadow"}]

    monkeypatch.setattr(research_router, "execute_query", fake_query)
    response = TestClient(create_app()).get(
        "/api/v1/sector-rotation/research/today-summary",
        params={"as_of_date": "2026-08-24", "snapshot_mode": "delayed_shadow"},
    )

    assert response.status_code == 200
    assert response.json()["snapshot_mode"] == "delayed_shadow"
    assert seen["params"][2] == "delayed_shadow"


def test_latest_date_explicit_empty_mode_returns_null_without_cross_mode_fallback(monkeypatch):
    calls = []

    def fake_query(sql, params):
        calls.append((sql, params))
        return [{"as_of_date": None, "snapshot_mode": "delayed_shadow"}]

    monkeypatch.setattr(research_router, "execute_query", fake_query)
    response = TestClient(create_app()).get(
        "/api/v1/sector-rotation/research/latest-date",
        params={"level": 2, "snapshot_mode": "delayed_shadow"},
    )

    assert response.status_code == 200
    assert response.json() == {
        "as_of_date": None,
        "sector_level": 2,
        "snapshot_mode": "delayed_shadow",
    }
    assert len(calls) == 1


def test_watchlist_and_decision_routes_delegate_to_services(monkeypatch):
    monkeypatch.setattr(research_router.watchlist_service, "list_items", lambda **_: [{"snapshot_id": 7}])
    monkeypatch.setattr(research_router.watchlist_service, "add", lambda **payload: {"snapshot_id": payload["snapshot_id"]})
    monkeypatch.setattr(research_router.decision_service, "append", lambda **payload: {"decision": payload["decision"]})
    client = TestClient(create_app())
    assert client.get("/api/v1/sector-rotation/research/watchlist").json()["items"] == [{"snapshot_id": 7}]
    assert client.post("/api/v1/sector-rotation/research/watchlist", json={"snapshot_id": 7}).json()["snapshot_id"] == 7
    assert client.post("/api/v1/sector-rotation/research/decisions", json={"snapshot_id": 7, "decision": "ENTER"}).json()["decision"] == "ENTER"
