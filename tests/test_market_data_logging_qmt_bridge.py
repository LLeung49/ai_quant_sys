from pathlib import Path


ROOT = Path(__file__).parents[1]
LEGACY_PATH = ROOT / "src/data_ingestion_qmt/1-行情数据采集_qmt_bridge.py"
CANONICAL_PATH = ROOT / "src/data_ingestion_qmt/8-原始行情与复权数据采集_qmt_bridge.py"


def test_legacy_qmt_market_writer_is_retired():
    assert not LEGACY_PATH.exists()


def test_canonical_qmt_market_collector_uses_the_qfq_table():
    source = CANONICAL_PATH.read_text(encoding="utf-8")
    assert "QMTDataGateway" in source
    assert "trade_stock_daily_qfq" in source


def test_canonical_qmt_market_collector_keeps_the_integrity_audit():
    source = CANONICAL_PATH.read_text(encoding="utf-8")
    assert "audit_and_repair_projection" in source
