import pytest

from data_ingestion.qmt_data_gateway import QMTBridgeError, QMTDataGateway


class _Response:
    def __init__(self, payload):
        self.payload = payload

    def raise_for_status(self):
        return None

    def json(self):
        return self.payload


class _Session:
    def __init__(self):
        self.headers = {}
        self.calls = []

    def request(self, method, url, **kwargs):
        self.calls.append((method, url, kwargs))
        return _Response({})


def test_from_env_and_error_envelope(monkeypatch):
    monkeypatch.setenv("QMT_BRIDGE_URL", "http://qmt/")
    monkeypatch.setenv("QMT_BRIDGE_TOKEN", "test-token")
    gateway = QMTDataGateway.from_env()
    session = gateway._session
    session.request = lambda method, url, **kwargs: _Response({"error": "not cached"})
    assert gateway.base_url == "http://qmt"
    with pytest.raises(QMTBridgeError, match="not cached"):
        gateway._request("POST", "/api/xtdata/market_data_ex", {})
    assert session.headers["X-Token"] == "test-token"


def test_from_env_reads_project_dotenv_when_process_env_is_unset(monkeypatch, tmp_path):
    env_file = tmp_path / ".env"
    env_file.write_text(
        "QMT_BRIDGE_URL=http://qmt-from-dotenv:16666\n"
        "QMT_BRIDGE_TOKEN=dotenv-token\n"
        "QMT_BRIDGE_CONNECT_TIMEOUT=4\n"
        "QMT_BRIDGE_READ_TIMEOUT=90\n",
        encoding="utf-8",
    )
    monkeypatch.setenv("AI_QUANT_ENV_FILE", str(env_file))
    for name in (
        "QMT_BRIDGE_URL",
        "QMT_BRIDGE_TOKEN",
        "QMT_BRIDGE_CONNECT_TIMEOUT",
        "QMT_BRIDGE_READ_TIMEOUT",
    ):
        monkeypatch.delenv(name, raising=False)

    gateway = QMTDataGateway.from_env()

    assert gateway.base_url == "http://qmt-from-dotenv:16666"
    assert gateway._session.headers["X-Token"] == "dotenv-token"
    assert gateway.timeout == (4.0, 90.0)


def test_market_data_restores_dataframe_index(monkeypatch):
    gateway = QMTDataGateway(base_url="http://qmt", token="test")
    gateway._session.request = lambda method, url, **kwargs: _Response({
        "data": {"600519.SH": [{"time": "20250102", "open": 1.0, "close": 2.0}]}
    })
    frame = gateway.get_market_data_ex(
        ["open", "close"], ["600519.SH"], "1d", "20250101", dividend_type="front"
    )["600519.SH"]
    assert frame.index[0] == "20250102"
    assert frame.iloc[0]["close"] == 2.0


def test_history_download_is_a_context_compatibility_noop():
    gateway = QMTDataGateway(base_url="http://qmt", token="test")
    gateway._session.request = lambda *args, **kwargs: pytest.fail("unexpected HTTP request")
    result = gateway.download_history_data(["600519.SH", "000001.SZ"], "1d", "20250101")
    assert result.downloaded == ("600519.SH", "000001.SZ")


@pytest.mark.parametrize("dividend_type", ["none", "front", "back"])
def test_market_data_preserves_requested_dividend_mode(monkeypatch, dividend_type):
    gateway = QMTDataGateway(base_url="http://qmt", token="test")
    calls = []

    def request(method, url, **kwargs):
        calls.append(kwargs["json"])
        return _Response({"data": {"600519.SH": [{"time": "20250102", "close": 2.0}]}})

    gateway._session.request = request
    gateway.get_market_data_ex(["close"], ["600519.SH"], "1d", dividend_type=dividend_type)
    assert calls[0]["dividend_type"] == dividend_type


def test_market_data_empty_and_missing_fields_remain_observable():
    gateway = QMTDataGateway(base_url="http://qmt", token="test")
    responses = iter([
        {"data": {"600519.SH": []}},
        {"data": {"600519.SH": [{"time": "20250102", "close": 2.0}]}},
    ])
    gateway._session.request = lambda method, url, **kwargs: _Response(next(responses))
    empty = gateway.get_market_data_ex(["close", "volume"], ["600519.SH"], "1d")
    present = gateway.get_market_data_ex(["close", "volume"], ["600519.SH"], "1d")
    assert empty["600519.SH"].empty
    assert "volume" not in present["600519.SH"].columns


def test_financial_data_restores_nested_dataframes():
    gateway = QMTDataGateway(base_url="http://qmt", token="test")
    gateway._session.request = lambda method, url, **kwargs: _Response({
        "data": {"600519.SH": {"Balance": [{"m_timetag": 20241231, "total_asset": 1.0}]}}
    })
    result = gateway.get_financial_data(
        ["total_asset"], ["600519.SH"], "20200101", "20250101", "report_time"
    )
    assert isinstance(result["600519.SH"]["Balance"], __import__("pandas").DataFrame)


def test_reference_envelopes_are_unwrapped():
    gateway = QMTDataGateway(base_url="http://qmt", token="test")
    calls = []
    responses_by_path = {
        "stock_list_in_sector": {"stocks": ["600519.SH"]},
        "sector_list": {"sectors": ["SW1食品饮料"]},
        "instrument_detail": {"data": {"600519.SH": {"OpenDate": "20010827"}}},
        "divid_factors": {"factors": {"1735689600000": [1, 0, 0, 0, 0, 0, 1.2]}},
    }
    def request(method, url, **kwargs):
        calls.append((method, url, kwargs["json"]))
        return _Response(next(value for key, value in responses_by_path.items() if key in url))

    gateway._session.request = request
    assert gateway.get_stock_list_in_sector("沪深A股") == ["600519.SH"]
    assert calls[0] == (
        "POST",
        "http://qmt/api/data/stock_list_in_sector",
        {"sectorname": "沪深A股"},
    )
    assert gateway.get_sector_list() == ["SW1食品饮料"]
    assert gateway.get_instrument_detail(["600519.SH"])["600519.SH"]["OpenDate"] == "20010827"
    assert gateway.get_divid_factors("600519.SH").iloc[0]["factor"] == 1.2


def test_financial_download_raises_for_partial_batch():
    gateway = QMTDataGateway(base_url="http://qmt", token="test")
    gateway._session.request = lambda method, url, **kwargs: _Response({
        "status": "success",
        "downloaded": ["600519.SH"],
        "failed": [{"stock": "000001.SZ", "error": "missing"}],
    })
    with pytest.raises(QMTBridgeError, match="000001.SZ"):
        gateway.download_financial_data(["600519.SH", "000001.SZ"], ["Balance"])


def test_sector_and_etf_refresh_contracts():
    gateway = QMTDataGateway(base_url="http://qmt", token="test")
    calls = []

    def request(method, url, **kwargs):
        calls.append(url)
        if url.endswith("/etf_info"):
            return _Response({"data": {"510300.SH": {"成份股信息": []}}})
        return _Response({"status": "success"})

    gateway._session.request = request
    gateway.download_sector_data()
    gateway.download_etf_info()
    assert "510300.SH" in gateway.get_etf_info()
    assert calls == [
        "http://qmt/api/xtdata/download_sector_data",
        "http://qmt/api/xtdata/download_etf_info",
        "http://qmt/api/xtdata/etf_info",
    ]


def test_refresh_endpoints_share_a_success_status_contract():
    gateway = QMTDataGateway(base_url="http://qmt", token="test")
    gateway._session.request = lambda method, url, **kwargs: _Response({"status": "failed"})

    with pytest.raises(QMTBridgeError, match="refresh failed"):
        gateway.download_sector_data()

    with pytest.raises(QMTBridgeError, match="refresh failed"):
        gateway.download_etf_info()


def test_divid_factors_forwards_requested_window():
    gateway = QMTDataGateway(base_url="http://qmt", token="test")
    calls = []

    def request(method, url, **kwargs):
        calls.append(kwargs["json"])
        return _Response({"factors": []})

    gateway._session.request = request
    gateway.get_divid_factors("600519.SH", "20250101", "20250131")
    assert calls == [{"stockcode": "600519.SH"}]


def test_context_data_endpoints_restore_xtdata_compatible_shapes():
    gateway = QMTDataGateway(base_url="http://qmt", token="test")
    calls = []

    def request(method, url, **kwargs):
        calls.append((method, url, kwargs["json"]))
        if url.endswith("/market_data_ex"):
            return _Response({"data": {"600519.SH": {"close": {"20250102": 2.0}}}})
        if url.endswith("/instrument_detail"):
            return _Response({"data": {"600519.SH": {"FloatVolume": 123}}})
        if url.endswith("/divid_factors"):
            return _Response({"stockcode": "600519.SH", "factors": {"1735689600000": [1, 0, 0, 0, 0, 0, 1.2]}})
        if url.endswith("/last_volume"):
            return _Response({"stockcode": "600519.SH", "last_volume": 456})
        raise AssertionError(url)

    gateway._session.request = request

    market = gateway.get_market_data_ex(["close"], ["600519.SH"], "1d", "20250101")
    assert market["600519.SH"].loc["20250102", "close"] == 2.0
    assert gateway.get_instrument_detail("600519.SH")["FloatVolume"] == 123
    assert gateway.get_last_volume("600519.SH") == 456
    assert gateway.get_divid_factors("600519.SH").iloc[0]["factor"] == 1.2
    assert calls[0] == (
        "POST", "http://qmt/api/data/market_data_ex",
        {"stock_code": "600519.SH", "fields": "close", "period": "1d",
         "start_time": "20250101", "end_time": "", "count": -1,
         "dividend_type": "none"},
    )


def test_context_market_data_does_not_require_xtdata_download():
    gateway = QMTDataGateway(base_url="http://qmt", token="test")
    gateway._session.request = lambda *args, **kwargs: pytest.fail("unexpected HTTP request")

    result = gateway.download_history_data("600519.SH", "1d", "20250101")

    assert result.downloaded == ("600519.SH",)
    assert result.failed == ()
