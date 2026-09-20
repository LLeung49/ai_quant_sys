"""HTTP adapter for the QMT client-side data bridge.

The gateway deliberately exposes xtdata-shaped methods so collectors can be
copied with minimal business-logic changes while the transport remains
replaceable in tests.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import pandas as pd
import requests
from dotenv import dotenv_values


class QMTBridgeError(RuntimeError):
    """Raised when the bridge cannot satisfy a data request."""


@dataclass(frozen=True)
class DownloadResult:
    downloaded: tuple[str, ...]
    failed: tuple[dict[str, Any], ...]


def _chunks(values: list[str], size: int):
    for offset in range(0, len(values), size):
        yield values[offset : offset + size]


def resolve_env_path() -> Path:
    """Resolve .env with the same rules used by data_ingestion.db_config."""
    configured_path = os.environ.get("AI_QUANT_ENV_FILE")
    if configured_path:
        return Path(configured_path).expanduser()

    module_path = Path(__file__).resolve()
    for directory in module_path.parents:
        candidate = directory / ".env"
        if candidate.is_file():
            return candidate

    return Path(__file__).parent.parent.parent / ".env"


def _bridge_env(name: str, values: dict[str, str | None], default: str) -> str:
    if name in os.environ:
        return os.environ[name]
    return values.get(name) or default


class QMTDataGateway:
    def __init__(
        self,
        *,
        base_url: str = "http://127.0.0.1:15588",
        token: str = "",
        timeout: tuple[float, float] = (3.0, 60.0),
        session: requests.Session | None = None,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self._session = session or requests.Session()
        self._session.headers.update(
            {
                "X-Token": token,
                "Content-Type": "application/json; charset=utf-8",
            }
        )

    @classmethod
    def from_env(cls) -> "QMTDataGateway":
        values = dotenv_values(resolve_env_path())
        return cls(
            base_url=_bridge_env(
                "QMT_BRIDGE_URL", values, "http://127.0.0.1:15588"
            ),
            token=_bridge_env("QMT_BRIDGE_TOKEN", values, ""),
            timeout=(
                float(_bridge_env("QMT_BRIDGE_CONNECT_TIMEOUT", values, "3")),
                float(_bridge_env("QMT_BRIDGE_READ_TIMEOUT", values, "60")),
            ),
        )

    def connect(self) -> None:
        """Compatibility no-op; HTTP requests establish the bridge connection."""
        return None

    def _request(
        self, method: str, path: str, payload: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        try:
            response = self._session.request(
                method,
                self.base_url + path,
                json=payload,
                timeout=self.timeout,
            )
            response.raise_for_status()
            body = response.json()
        except (requests.RequestException, ValueError) as exc:
            raise QMTBridgeError(f"{method} {path}: {exc}") from exc
        if not isinstance(body, dict):
            raise QMTBridgeError(f"{method} {path}: invalid response envelope")
        if body.get("error"):
            raise QMTBridgeError(f"{method} {path}: {body['error']}")
        return body

    @staticmethod
    def _frame(records: Any) -> pd.DataFrame:
        if records is None:
            return pd.DataFrame()
        if isinstance(records, dict):
            records = list(records.values())
        frame = pd.DataFrame.from_records(records)
        if "time" in frame.columns:
            raw_times = frame.pop("time").astype(str)
            parsed = pd.to_datetime(raw_times, errors="raise")
            frame.index = parsed.dt.strftime("%Y%m%d")
        return frame

    def download_history_data(
        self,
        stock_code: str | list[str],
        period: str = "1d",
        start_time: str = "",
        end_time: str = "",
    ) -> DownloadResult:
        stocks = [stock_code] if isinstance(stock_code, str) else list(stock_code)
        downloaded: list[str] = []
        failed: list[dict[str, Any]] = []
        for batch in _chunks(stocks, 20):
            body = self._request(
                "POST",
                "/api/xtdata/download_history_data",
                {
                    "stock_list": ",".join(batch),
                    "period": period,
                    "start_time": start_time,
                    "end_time": end_time,
                },
            )
            downloaded.extend(str(code) for code in body.get("downloaded", []))
            failed.extend(body.get("failed", []) or [])
        if failed:
            codes = ", ".join(str(item.get("stock", "?")) for item in failed)
            raise QMTBridgeError(f"history download failed: {codes}")
        return DownloadResult(tuple(downloaded), tuple(failed))

    def get_market_data_ex(
        self,
        field_list: list[str],
        stock_list: list[str],
        period: str,
        start_time: str = "",
        end_time: str = "",
        count: int = -1,
        dividend_type: str = "none",
        fill_data: bool = True,
    ) -> dict[str, pd.DataFrame]:
        result: dict[str, pd.DataFrame] = {}
        for batch in _chunks(list(stock_list), 50):
            body = self._request(
                "POST",
                "/api/xtdata/market_data_ex",
                {
                    "field_list": ",".join(field_list),
                    "stock_list": ",".join(batch),
                    "period": period,
                    "start_time": start_time,
                    "end_time": end_time,
                    "count": count,
                    "dividend_type": dividend_type,
                    "fill_data": str(fill_data).lower(),
                },
            )
            for code, records in (body.get("data") or {}).items():
                result[code] = self._frame(records)
        return result

    def download_financial_data(
        self, stock_list: list[str], table_list: list[str]
    ) -> DownloadResult:
        downloaded: list[str] = []
        failed: list[dict[str, Any]] = []
        for batch in _chunks(list(stock_list), 20):
            body = self._request(
                "POST",
                "/api/xtdata/download_financial_data",
                {"stock_list": ",".join(batch), "table_list": ",".join(table_list)},
            )
            downloaded.extend(str(code) for code in body.get("downloaded", batch))
            failed.extend(body.get("failed", []) or [])
        if failed:
            codes = ", ".join(str(item.get("stock", "?")) for item in failed)
            raise QMTBridgeError(f"financial download failed: {codes}")
        return DownloadResult(tuple(downloaded), tuple(failed))

    def get_financial_data(
        self,
        fields: list[str] | None = None,
        stocks: list[str] | None = None,
        start_time: str = "",
        end_time: str = "",
        report_type: str = "report_time",
        **kwargs: Any,
    ) -> dict[str, dict[str, pd.DataFrame]]:
        fields = list(fields or kwargs.pop("table_list", []))
        stocks = list(stocks or kwargs.pop("stock_list", []))
        result: dict[str, dict[str, pd.DataFrame]] = {}
        for batch in _chunks(list(stocks), 50):
            body = self._request(
                "POST",
                "/api/xtdata/financial_data",
                {
                    "stock_list": ",".join(batch),
                    "table_list": ",".join(fields),
                    "start_time": start_time,
                    "end_time": end_time,
                    "report_type": report_type,
                },
            )
            for code, tables in (body.get("data") or {}).items():
                result[code] = {
                    name: self._frame(records)
                    for name, records in (tables or {}).items()
                }
        return result

    def download_financial_data2(
        self,
        stock_list: list[str],
        table_list: list[str],
        start_time: str = "",
        end_time: str = "",
        callback=None,
    ) -> DownloadResult:
        result = self.download_financial_data(stock_list, table_list)
        if callback is not None:
            callback(result)
        return result

    def get_stock_list_in_sector(self, sector_name: str) -> list[str]:
        body = self._request(
            "POST", "/api/xtdata/stock_list_in_sector", {"sector_name": sector_name}
        )
        return [str(code) for code in body.get("stocks", [])]

    def download_sector_data(self) -> None:
        self._refresh("/api/xtdata/download_sector_data")

    def download_etf_info(self) -> None:
        self._refresh("/api/xtdata/download_etf_info")

    def _refresh(self, path: str) -> None:
        body = self._request("POST", path, {})
        if body.get("status") != "success":
            raise QMTBridgeError(f"{path}: refresh failed")

    def get_etf_info(self) -> dict[str, Any]:
        body = self._request("POST", "/api/xtdata/etf_info", {})
        data = body.get("data")
        if not isinstance(data, dict):
            raise QMTBridgeError("/api/xtdata/etf_info: expected mapping")
        return data

    def get_sector_list(self) -> list[str]:
        body = self._request("GET", "/api/xtdata/sector_list")
        return [str(name) for name in body.get("sectors", [])]

    def get_instrument_detail(
        self, stock_list: str | list[str], iscomplete: bool = False
    ) -> dict[str, dict[str, Any]] | dict[str, Any]:
        scalar = isinstance(stock_list, str)
        stocks = [stock_list] if scalar else list(stock_list)
        result: dict[str, dict[str, Any]] = {}
        for batch in _chunks(stocks, 200):
            body = self._request(
                "POST",
                "/api/xtdata/instrument_detail",
                {"stock_list": ",".join(batch), "iscomplete": iscomplete},
            )
            for code, detail in (body.get("data") or {}).items():
                if isinstance(detail, dict) and detail.get("error"):
                    raise QMTBridgeError(f"instrument detail failed: {code}: {detail['error']}")
                if detail is not None:
                    result[code] = detail
        return result.get(stock_list, {}) if scalar else result

    def get_divid_factors(
        self, stock_code: str, start_time: str = "", end_time: str = ""
    ) -> pd.DataFrame:
        body = self._request(
            "POST",
            "/api/xtdata/divid_factors",
            {
                "stock_code": stock_code,
                "start_time": start_time,
                "end_time": end_time,
            },
        )
        return self._frame(body.get("factors", []))
