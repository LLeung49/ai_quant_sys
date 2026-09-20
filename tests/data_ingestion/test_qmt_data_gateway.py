import pytest

from data_ingestion.qmt_data_gateway import QMTBridgeError, QMTDataGateway


class _Response:
    def raise_for_status(self):
        return None

    def json(self):
        return {"error": "not cached"}


class _Session:
    def __init__(self):
        self.headers = {}
        self.calls = []

    def request(self, method, url, **kwargs):
        self.calls.append((method, url, kwargs))
        return _Response()


def test_from_env_and_error_envelope(monkeypatch):
    monkeypatch.setenv("QMT_BRIDGE_URL", "http://qmt/")
    monkeypatch.setenv("QMT_BRIDGE_TOKEN", "test-token")
    gateway = QMTDataGateway.from_env()
    session = gateway._session
    session.request = lambda method, url, **kwargs: _Response()
    assert gateway.base_url == "http://qmt"
    with pytest.raises(QMTBridgeError, match="not cached"):
        gateway._request("POST", "/api/xtdata/market_data_ex", {})
    assert session.headers["X-Token"] == "test-token"
