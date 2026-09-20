import json
from pathlib import Path


ROOT = Path(__file__).parents[2]
SERVER_COPY = ROOT / "docs/user_demand/qmt_switch/CY_QMT_API_qmt_bridge.py"
ETF_FIXTURE = ROOT / "tests/fixtures/qmt_bridge/etf_info.json"


def test_server_copy_declares_missing_xtdata_routes():
    source = SERVER_COPY.read_text(encoding="utf-8")
    for route in (
        "/api/xtdata/download_sector_data",
        "/api/xtdata/download_etf_info",
        "/api/xtdata/etf_info",
    ):
        assert route in source


def test_recorded_etf_response_is_mapping():
    payload = json.loads(ETF_FIXTURE.read_text(encoding="utf-8"))
    assert isinstance(payload["data"], dict)


def test_refresh_handlers_follow_existing_safe_call_convention():
    source = SERVER_COPY.read_text(encoding="utf-8")
    assert "safe_call(xtdata.download_sector_data)" in source
    assert "safe_call(xtdata.download_etf_info)" in source
    assert "safe_call(xtdata.get_etf_info)" in source
