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


def test_market_data_restores_dataframe_index(monkeypatch):
    gateway = QMTDataGateway(base_url="http://qmt", token="test")
    gateway._session.request = lambda method, url, **kwargs: _Response({
        "data": {"600519.SH": [{"time": "20250102", "open": 1.0, "close": 2.0}]}
    })
    frame = gateway.get_market_data_ex(
        ["open", "close"], ["600519.SH"], "1d", "20250101", dividend_type="front"
    )["600519.SH"]
    assert frame.index[0].strftime("%Y%m%d") == "20250102"
    assert frame.iloc[0]["close"] == 2.0


def test_history_download_raises_for_failed_code():
    gateway = QMTDataGateway(base_url="http://qmt", token="test")
    gateway._session.request = lambda method, url, **kwargs: _Response({
        "status": "success",
        "downloaded": ["600519.SH"],
        "failed": [{"stock": "000001.SZ", "error": "offline"}],
    })
    with pytest.raises(QMTBridgeError, match="000001.SZ"):
        gateway.download_history_data(["600519.SH", "000001.SZ"], "1d", "20250101")


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
