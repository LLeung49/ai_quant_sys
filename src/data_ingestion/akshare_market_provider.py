"""AKShare implementation of the canonical daily-market provider contract."""

from __future__ import annotations

from datetime import date, datetime, timezone
import queue
import random
import threading
import time
from typing import Callable

import akshare as ak

from .market_provider import MarketBatch
from .market_row_validation import validate_market_row, validate_projection_batch


MODE_ADJUST = {"none": "", "front": "qfq", "back": "hfq"}
ETF_CODE_PREFIXES = ("15", "16", "50", "51", "56", "58")
COLUMN_ALIASES = {
    "trade_date": ("日期", "date", "trade_date"),
    "open_price": ("开盘", "open", "open_price"),
    "high_price": ("最高", "high", "high_price"),
    "low_price": ("最低", "low", "low_price"),
    "close_price": ("收盘", "close", "close_price"),
    "volume": ("成交量", "volume"),
    "amount": ("成交额", "amount"),
    "turnover_rate": ("换手率", "turnover_rate"),
}
REQUIRED_COLUMNS = tuple(key for key in COLUMN_ALIASES if key != "turnover_rate")


def _is_etf(stock_code: str) -> bool:
    return stock_code.split(".", 1)[0].startswith(ETF_CODE_PREFIXES)


def _date_text(value: object) -> str:
    return str(value)[:10]


class AKShareMarketProvider:
    """Fetch raw/QFQ/HFQ as one validated, traceable batch."""

    def __init__(
        self,
        *,
        stock_fetcher: Callable = ak.stock_zh_a_hist,
        etf_fetcher: Callable = ak.fund_etf_hist_em,
        max_attempts: int = 3,
        request_timeout: float = 30.0,
        sleeper: Callable[[float], None] = time.sleep,
        jitter: Callable[[], float] = random.random,
    ) -> None:
        if max_attempts < 1:
            raise ValueError("max_attempts must be positive")
        if request_timeout <= 0:
            raise ValueError("request_timeout must be positive")
        self.stock_fetcher = stock_fetcher
        self.etf_fetcher = etf_fetcher
        self.max_attempts = max_attempts
        self.request_timeout = request_timeout
        self.sleeper = sleeper
        self.jitter = jitter

    def _invoke(self, fetcher: Callable, kwargs: dict):
        results: queue.Queue = queue.Queue(maxsize=1)

        def run() -> None:
            try:
                results.put((True, fetcher(**kwargs)))
            except BaseException as exc:  # forwarded to the caller thread
                results.put((False, exc))

        worker = threading.Thread(target=run, daemon=True, name="akshare-market-fetch")
        worker.start()
        worker.join(self.request_timeout)
        if worker.is_alive():
            raise TimeoutError(f"AKShare call exceeded {self.request_timeout}s")
        ok, value = results.get_nowait()
        if not ok:
            raise value
        return value

    def _fetch_with_retry(self, fetcher: Callable, kwargs: dict):
        last_error: BaseException | None = None
        for attempt in range(1, self.max_attempts + 1):
            try:
                return self._invoke(fetcher, kwargs)
            except BaseException as exc:
                last_error = exc
                if attempt < self.max_attempts:
                    self.sleeper(min(8.0, 0.5 * (2 ** (attempt - 1))) + self.jitter())
        assert last_error is not None
        raise RuntimeError(
            f"retry_exhausted after {self.max_attempts} attempts: "
            f"{type(last_error).__name__}: {last_error}"
        ) from last_error

    @staticmethod
    def _column_map(frame) -> dict[str, str]:
        available = set(frame.columns)
        resolved = {}
        for canonical, aliases in COLUMN_ALIASES.items():
            source = next((name for name in aliases if name in available), None)
            if source is not None:
                resolved[canonical] = source
        missing = sorted(set(REQUIRED_COLUMNS) - set(resolved))
        if missing:
            raise ValueError(f"schema_drift missing columns: {missing}")
        return resolved

    def _normalize(self, stock_code: str, mode: str, frame) -> tuple[list[dict], list[dict]]:
        if frame is None or len(frame) == 0:
            raise ValueError("empty_response")
        columns = self._column_map(frame)
        rows: list[dict] = []
        quarantines: list[dict] = []
        for _, source in frame.iterrows():
            try:
                row = {
                    "stock_code": stock_code,
                    "trade_date": _date_text(source[columns["trade_date"]]),
                    "open_price": float(source[columns["open_price"]]),
                    "high_price": float(source[columns["high_price"]]),
                    "low_price": float(source[columns["low_price"]]),
                    "close_price": float(source[columns["close_price"]]),
                    # Both stock_zh_a_hist and fund_etf_hist_em report daily
                    # volume in lots and amount in yuan.
                    "volume": int(float(source[columns["volume"]])),
                    "amount": float(source[columns["amount"]]),
                    "turnover_rate": (
                        float(source[columns["turnover_rate"]])
                        if "turnover_rate" in columns
                        else None
                    ),
                }
            except (TypeError, ValueError, OverflowError) as exc:
                raise ValueError(f"schema_drift invalid numeric value: {exc}") from exc
            if mode == "none":
                row.update({
                    "pre_close": None,
                    "suspend_flag": None,
                    "data_source": "akshare",
                })
            validation = validate_market_row(
                row, allow_negative_price=(mode == "front")
            )
            if not validation.is_valid:
                codes = sorted({issue.code for issue in validation.issues})
                raise ValueError(
                    f"invalid_market_row {row['trade_date']}: {','.join(codes)}"
                )
            if validation.quarantined:
                quarantines.append({
                    "stock_code": stock_code,
                    "trade_date": row["trade_date"],
                    "mode": mode,
                    "issues": [issue.code for issue in validation.issues],
                })
            rows.append(row)
        return rows, quarantines

    def fetch_batch(
        self, stock_code: str, start_date: date, end_date: date
    ) -> MarketBatch:
        if start_date > end_date:
            raise ValueError("start_date must not exceed end_date")
        etf = _is_etf(stock_code)
        fetcher = self.etf_fetcher if etf else self.stock_fetcher
        interface = "fund_etf_hist_em" if etf else "stock_zh_a_hist"
        rows_by_mode: dict[str, list[dict]] = {}
        failures: dict[str, str] = {}
        quarantines: list[dict] = []
        for mode, adjust in MODE_ADJUST.items():
            kwargs = {
                "symbol": stock_code.split(".", 1)[0],
                "period": "daily",
                "start_date": start_date.strftime("%Y%m%d"),
                "end_date": end_date.strftime("%Y%m%d"),
                "adjust": adjust,
            }
            try:
                frame = self._fetch_with_retry(fetcher, kwargs)
                rows, mode_quarantines = self._normalize(stock_code, mode, frame)
                rows_by_mode[mode] = rows
                quarantines.extend(mode_quarantines)
            except BaseException as exc:
                failures[mode] = f"{type(exc).__name__}: {exc}"

        if len(rows_by_mode) == len(MODE_ADJUST):
            batch_validation = validate_projection_batch(rows_by_mode)
            if not batch_validation.is_valid:
                failures["batch"] = "; ".join(
                    f"{issue.code}:{issue.stock_code}:{issue.trade_date}"
                    for issue in batch_validation.issues
                    if issue.severity == "error"
                )

        return MarketBatch(
            stock_code=stock_code,
            start_date=start_date,
            end_date=end_date,
            rows_by_mode=rows_by_mode,
            provenance={
                "provider": "akshare",
                "interface": interface,
                "volume_unit": "lot",
                "amount_unit": "yuan",
                "fetched_at": datetime.now(timezone.utc).isoformat(),
                "parameters": {
                    "start_date": start_date.isoformat(),
                    "end_date": end_date.isoformat(),
                    "adjustments": MODE_ADJUST.copy(),
                },
            },
            failures=failures,
            quarantines=tuple(quarantines),
        )
