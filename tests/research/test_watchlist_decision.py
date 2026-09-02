from datetime import date

from morning_conference.sector_rotation2.research.watchlist import service as watchlist
from morning_conference.sector_rotation2.research.human_decision import service as decision


def _source():
    return [{"id": 7, "entity_type": "stock", "entity_code": "600000", "strategy_type": "stock_trend", "as_of_date": date(2026, 8, 20), "model_version": "v2", "config_hash": "hash", "snapshot_mode": "live_shadow"}]


def test_watchlist_add_references_snapshot_and_upserts(monkeypatch):
    calls = []
    monkeypatch.setattr(watchlist, "_snapshot", lambda _: _source()[0])
    monkeypatch.setattr(watchlist, "ensure_schema", lambda: None)
    monkeypatch.setattr(watchlist, "execute_update", lambda sql, params=(): calls.append((sql, params)))
    monkeypatch.setattr(watchlist, "get", lambda **_: {"snapshot_id": 7, "watch_status": "watch"})
    result = watchlist.add(user_id="u", snapshot_id=7)
    assert result["snapshot_id"] == 7
    assert "ON DUPLICATE KEY UPDATE" in calls[0][0]


def test_decision_log_is_append_only(monkeypatch):
    calls = []
    monkeypatch.setattr(decision, "execute_query", lambda sql, params=(): _source() if "FROM research_candidate_snapshot" in sql else [{"id": 9, "decision": "WATCH"}])
    monkeypatch.setattr(decision, "ensure_schema", lambda: None)
    monkeypatch.setattr(decision, "execute_update", lambda sql, params=(): calls.append(sql))
    result = decision.append(user_id="u", snapshot_id=7, decision="WATCH")
    assert result["decision"] == "WATCH"
    assert sum("INSERT INTO research_human_decision" in call for call in calls) == 1
