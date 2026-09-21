from pathlib import Path


PATH = Path(__file__).parents[1] / "src/data_ingestion_qmt/2-财务数据采集_qmt_bridge.py"


def test_finance_copy_exists_without_direct_xtquant_import():
    assert PATH.exists()
    source = PATH.read_text(encoding="utf-8")
    assert "from xtquant import xtdata" not in source
    assert "QMTDataGateway" in source
