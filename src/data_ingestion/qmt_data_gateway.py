"""HTTP adapter for the QMT client-side data bridge.

The gateway deliberately exposes xtdata-shaped methods so collectors can be
copied with minimal business-logic changes while the transport remains
replaceable in tests.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Any

import pandas as pd
import requests


class QMTBridgeError(RuntimeError):
    """Raised when the bridge cannot satisfy a data request."""


@dataclass(frozen=True)
class DownloadResult:
    downloaded: tuple[str, ...]
    failed: tuple[dict[str, Any], ...]


def _chunks(values: list[str], size: int):
    for offset in range(0, len(values), size):
        yield values[offset : offset + size]


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
        return cls(
            base_url=os.getenv("QMT_BRIDGE_URL", "http://127.0.0.1:15588"),
            token=os.getenv("QMT_BRIDGE_TOKEN", ""),
            timeout=(
                float(os.getenv("QMT_BRIDGE_CONNECT_TIMEOUT", "3")),
                float(os.getenv("QMT_BRIDGE_READ_TIMEOUT", "60")),
            ),
        )

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
            frame.index = pd.to_datetime(frame.pop("time").astype(str), errors="raise")
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
