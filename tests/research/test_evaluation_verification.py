from morning_conference.sector_rotation2.research.evaluation import verify_backfill, verify_evaluation


def test_backfill_verification_reports_mode_isolation_and_delayed_metadata(monkeypatch) -> None:
    def fake_query(sql: str, *_args):
        if "data_available_at IS NULL" in sql and "GROUP BY snapshot_mode" in sql:
            return [{"snapshot_mode": "backfill", "n": 12}, {"snapshot_mode": "delayed_shadow", "n": 0}]
        if "snapshot_mode='delayed_shadow'" in sql:
            return [{"n": 0}]
        if "GROUP BY snapshot_mode, return_status, label_type" in sql:
            return []
        if "COUNT(DISTINCT source_snapshot_id)" in sql:
            return []
        return [{"n": 0}]

    monkeypatch.setattr(verify_backfill, "execute_query", fake_query)

    result = verify_backfill.verify()

    assert result["availability_null_counts"] == {"backfill": 12, "delayed_shadow": 0}
    assert result["mode_mismatch_count"] == 0
    assert result["delayed_missing_metadata_count"] == 0


def test_evaluation_verification_reports_delayed_metadata_and_mode_isolation(monkeypatch) -> None:
    def fake_query(sql: str, *_args):
        if "snapshot_mode='delayed_shadow'" in sql:
            return [{"n": 0}]
        if "f.snapshot_mode<>s.snapshot_mode" in sql:
            return [{"n": 0}]
        if "trade_sector_daily" in sql:
            return [{"n": 756, "min_date": "2024-01-01", "max_date": "2026-08-20"}]
        if "SUM(return_complete_count)" in sql:
            return [{"complete_returns": 0, "candidates": 0}]
        return [{"n": 0}]

    monkeypatch.setattr(verify_evaluation, "execute_query", fake_query)

    result = verify_evaluation.verify()

    assert result["evaluation_mode_mismatch_count"] == 0
    assert result["delayed_missing_metadata_count"] == 0
