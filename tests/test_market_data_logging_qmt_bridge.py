from pathlib import Path


PATH = Path(__file__).parents[1] / "src/data_ingestion/1-行情数据采集_qmt_bridge.py"


def test_market_copy_exists_without_direct_xtquant_import():
    assert PATH.exists()
    source = PATH.read_text(encoding="utf-8")
    assert "from xtquant import xtdata" not in source
    assert "QMTDataGateway" in source


def test_market_bridge_serializes_http_requests():
    source = PATH.read_text(encoding="utf-8")
    assert "NUM_WORKERS = 1" in source
