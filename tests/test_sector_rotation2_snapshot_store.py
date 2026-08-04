from pathlib import Path


def test_migration_defines_approved_sector_rotation_tables():
    sql = Path("sql/20260804_create_sector_rotation_persistence_tables.sql").read_text(encoding="utf-8")

    assert "CREATE TABLE IF NOT EXISTS sector_rotation_run_log" in sql
    assert "CREATE TABLE IF NOT EXISTS sector_rotation_sector_daily_snapshot" in sql
    assert "CREATE TABLE IF NOT EXISTS sector_rotation_sector_forward_return" in sql
    assert "CREATE TABLE IF NOT EXISTS sector_rotation_backtest_metric" in sql
    assert "UNIQUE KEY uq_snapshot (as_of_date, sector_level, sector_name, model_version)" in sql
