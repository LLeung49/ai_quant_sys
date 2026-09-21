from data_ingestion_qmt.qfq_integrity_audit import (
    IntegrityFinding,
    build_source_fingerprint,
    upsert_integrity_finding,
)


def test_fingerprint_is_stable_for_key_order_and_changes_for_price_change():
    first = build_source_fingerprint(
        {"open": 1, "close": 2}, {"open": 1}
    )
    reordered = build_source_fingerprint(
        {"close": 2, "open": 1}, {"open": 1}
    )
    changed = build_source_fingerprint(
        {"open": 1, "close": 3}, {"open": 1}
    )

    assert first == reordered
    assert first != changed


def test_upsert_preserves_first_seen(monkeypatch):
    captured = {}

    def capture_update(sql, params):
        captured["sql"] = sql
        captured["params"] = params
        return 1

    monkeypatch.setattr(
        "data_ingestion_qmt.qfq_integrity_audit.execute_update", capture_update
    )
    finding = IntegrityFinding(
        "300316.SZ",
        "2015-02-03",
        "qfq_ohlc_non_affine",
        "warning",
        "qmt_verified_exception",
        {"open": 26.46},
        {"open": 6.701783},
        "a" * 64,
        "qmt-v2",
        None,
        "QMT verified",
    )

    assert upsert_integrity_finding(finding) == 1
    assert "ON DUPLICATE KEY UPDATE" in captured["sql"]
    update_clause = captured["sql"].split("ON DUPLICATE KEY UPDATE", 1)[1]
    assert "first_detected_at" not in update_clause
