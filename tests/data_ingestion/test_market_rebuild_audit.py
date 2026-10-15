from datetime import date
from pathlib import Path

from data_ingestion.market_provider import MarketBatch
from data_ingestion.market_rebuild_audit import (
    assess_rebuild_metrics,
    build_stratified_sample,
    compare_source_batches,
)


def catalog():
    return [
        {"stock_code": "000001.SZ", "security_type": "stock", "listing_era": "old", "has_action": False, "abnormal": False},
        {"stock_code": "000002.SZ", "security_type": "stock", "listing_era": "old", "has_action": True, "abnormal": False},
        {"stock_code": "301001.SZ", "security_type": "stock", "listing_era": "new", "has_action": False, "abnormal": False},
        {"stock_code": "600519.SH", "security_type": "stock", "listing_era": "old", "has_action": True, "abnormal": True},
        {"stock_code": "510300.SH", "security_type": "etf", "listing_era": "old", "has_action": False, "abnormal": False},
        {"stock_code": "159915.SZ", "security_type": "etf", "listing_era": "old", "has_action": True, "abnormal": False},
    ]


def test_stratified_sample_is_deterministic_and_covers_each_stratum():
    first = build_stratified_sample(catalog(), seed=20261014, target_size=6)
    second = build_stratified_sample(catalog(), seed=20261014, target_size=6)

    assert first == second
    assert set(first) == {row["stock_code"] for row in catalog()}


def batch(provider, close=10.0, volume=100):
    base = {
        "stock_code": "600519.SH", "trade_date": "2026-09-18",
        "open_price": close, "high_price": close, "low_price": close,
        "close_price": close, "volume": volume, "amount": 100000.0,
    }
    return MarketBatch(
        "600519.SH", date(2026, 9, 18), date(2026, 9, 18),
        rows_by_mode={mode: [dict(base)] for mode in ("none", "front", "back")},
        provenance={"provider": provider},
    )


def test_qmt_akshare_difference_is_visible_but_advisory():
    comparison = compare_source_batches(batch("qmt_bridge", close=10.0), batch("akshare", close=10.8))

    assert comparison.compared_rows == 3
    assert comparison.outside_tolerance == 3
    assert comparison.hard_failures == ()
    assert comparison.warnings


def test_structural_rebuild_errors_block_cutover_even_when_source_check_is_relaxed():
    report = assess_rebuild_metrics({
        "incomplete_batches": 0,
        "duplicate_rows": 0,
        "zero_price_rows": 1,
        "non_finite_rows": 0,
        "invalid_ohlc_rows": 0,
        "mode_date_mismatches": 0,
        "mode_volume_amount_mismatches": 0,
    }, comparisons=[])

    assert not report.can_cutover
    assert "zero_price_rows=1" in report.hard_failures


def test_clean_rebuild_can_cut_over_with_akshare_tolerance_warnings():
    comparison = compare_source_batches(batch("qmt_bridge", close=10.0), batch("akshare", close=10.8))
    report = assess_rebuild_metrics({
        "incomplete_batches": 0,
        "duplicate_rows": 0,
        "zero_price_rows": 0,
        "non_finite_rows": 0,
        "invalid_ohlc_rows": 0,
        "mode_date_mismatches": 0,
        "mode_volume_amount_mismatches": 0,
    }, comparisons=[comparison])

    assert report.can_cutover
    assert report.warnings


def test_cutover_sql_is_guarded_reversible_and_never_truncates():
    sql = (Path(__file__).parents[2] / "sql" / "20261014_market_rebuild_cutover.sql").read_text(encoding="utf-8")

    assert "SIGNAL SQLSTATE '45000'" in sql
    assert "open_price=0" in sql
    assert "invalid price or foreign batch rows found in rebuild tables" in sql
    assert "RENAME TABLE" in sql
    assert "rollback_20261014" in sql
    assert "TRUNCATE" not in sql.upper()
    assert "trade_market_rebuild_expected_code" in sql
    assert "pilot-%" in sql
    assert "qmt-cache-validation%" in sql
    assert "expected universe differs from canonical universe" in sql
    assert "rollback table name already exists" in sql
    assert "rejected table name already exists" in sql
    assert "metadata row counts differ from staging" in sql
    assert "adjusted table contains rows absent from raw" in sql
    assert "rebuild_batch_id IS NULL" in sql


def test_universe_or_foreign_batch_mismatch_blocks_cutover():
    report = assess_rebuild_metrics({
        "missing_expected_codes": 1,
        "unexpected_completed_codes": 0,
        "canonical_universe_mismatches": 0,
        "staging_code_mismatches": 0,
        "foreign_batch_rows": 0,
    }, comparisons=[])

    assert not report.can_cutover
    assert "missing_expected_codes=1" in report.hard_failures


def test_proof_backed_integrity_metrics_block_cutover():
    report = assess_rebuild_metrics({
        "duplicate_rows": 1,
        "non_finite_rows": 1,
        "batch_row_count_mismatches": 1,
        "extra_adjusted_rows": 1,
        "rollback_table_collisions": 1,
    }, comparisons=[])

    assert not report.can_cutover
    assert set(report.hard_failures) == {
        "duplicate_rows=1",
        "non_finite_rows=1",
        "batch_row_count_mismatches=1",
        "extra_adjusted_rows=1",
        "rollback_table_collisions=1",
    }


def test_audit_source_has_no_hardcoded_zero_integrity_metrics():
    source = (Path(__file__).parents[2] / "src" / "data_ingestion" / "market_rebuild_audit.py").read_text(encoding="utf-8")

    assert '"duplicate_rows": 0' not in source
    assert '"non_finite_rows": 0' not in source
