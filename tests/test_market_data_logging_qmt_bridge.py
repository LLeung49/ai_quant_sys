import importlib.util
from pathlib import Path

import pytest


PATH = Path(__file__).parents[1] / "src/data_ingestion/1-行情数据采集_qmt_bridge.py"


def test_market_copy_exists_without_direct_xtquant_import():
    assert PATH.exists()
    source = PATH.read_text(encoding="utf-8")
    assert "from xtquant import xtdata" not in source
    assert "QMTDataGateway" in source


def test_market_bridge_serializes_http_requests():
    source = PATH.read_text(encoding="utf-8")
    assert "NUM_WORKERS = 1" in source


def test_market_bridge_rejects_an_empty_combined_stock_pool():
    spec = importlib.util.spec_from_file_location("market_bridge", PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    class EmptyGateway:
        def get_stock_list_in_sector(self, sector_name):
            return []

    with pytest.raises(RuntimeError, match="股票列表为空"):
        module._load_sector_stock_codes(EmptyGateway(), ["沪深A股", "沪深ETF"])
