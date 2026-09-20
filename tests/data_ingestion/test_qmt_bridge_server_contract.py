import json
from pathlib import Path
import tokenize


ROOT = Path(__file__).parents[2]
SERVER_COPY = ROOT / "docs/user_demand/qmt_switch/CY_QMT_API_qmt_bridge.py"
SERVER_GBK_COPY = ROOT / "docs/user_demand/qmt_switch/CY_QMT_API_qmt_bridge_gbk.py"
ETF_FIXTURE = ROOT / "tests/fixtures/qmt_bridge/etf_info.json"


def _server_source(path: Path) -> str:
    with tokenize.open(path) as source:
        return source.read()


def test_server_copy_declares_missing_xtdata_routes():
    source = _server_source(SERVER_COPY)
    assert "跟陈博士学AI" in source
    for route in (
        "/api/xtdata/download_sector_data",
        "/api/xtdata/download_etf_info",
        "/api/xtdata/etf_info",
    ):
        assert route in source


def test_recorded_etf_response_is_mapping():
    payload = json.loads(ETF_FIXTURE.read_text(encoding="utf-8"))
    assert isinstance(payload["data"], dict)


def test_gbk_deployment_copy_preserves_chinese_source_text():
    source = _server_source(SERVER_GBK_COPY)
    assert source.startswith("# -*- coding: gbk -*-")
    assert "跟陈博士学AI" in source
    assert "/api/xtdata/download_sector_data" in source


def test_refresh_handlers_follow_existing_safe_call_convention():
    source = _server_source(SERVER_COPY)
    assert "safe_call(xtdata.download_sector_data)" in source
    assert "safe_call(xtdata.download_etf_info)" in source
    assert "safe_call(xtdata.get_etf_info)" in source
