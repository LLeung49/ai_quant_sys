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
ETF_CODE_PREFIXES = ("15", "16", "50", "51", "52", "53", "55", "56", "58")
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
        stock_fetcher: Callable | None = None,
        etf_fetcher: Callable | None = None,
        stock_fallback_fetcher: Callable | None = None,
        stock_secondary_fallback_fetcher: Callable | None = None,
        etf_fallback_fetcher: Callable | None = None,
        etf_dividend_fetcher: Callable | None = None,
        max_attempts: int = 3,
        request_timeout: float = 30.0,
        sleeper: Callable[[float], None] = time.sleep,
        jitter: Callable[[], float] = random.random,
    ) -> None:
        if max_attempts < 1:
            raise ValueError("max_attempts must be positive")
        if request_timeout <= 0:
            raise ValueError("request_timeout must be positive")
        custom_stock = stock_fetcher is not None
        custom_etf = etf_fetcher is not None
        self.stock_fetcher = stock_fetcher or ak.stock_zh_a_hist
        self.etf_fetcher = etf_fetcher or ak.fund_etf_hist_em
        self.stock_fallback_fetcher = (
            stock_fallback_fetcher
            if stock_fallback_fetcher is not None or custom_stock
            else ak.stock_zh_a_daily
        )
        self.stock_secondary_fallback_fetcher = (
            stock_secondary_fallback_fetcher
            if stock_secondary_fallback_fetcher is not None or custom_stock
            else ak.stock_zh_a_hist_tx
        )
        self.etf_fallback_fetcher = (
            etf_fallback_fetcher
            if etf_fallback_fetcher is not None or custom_etf
            else ak.fund_etf_hist_sina
        )
        self.etf_dividend_fetcher = (
            etf_dividend_fetcher
            if etf_dividend_fetcher is not None or custom_etf
            else ak.fund_etf_dividend_sina
        )
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

    def _normalize(
        self,
        stock_code: str,
        mode: str,
        frame,
        start_date: date,
        end_date: date,
        *,
        volume_divisor: int = 1,
    ) -> tuple[list[dict], list[dict]]:
        if frame is None or len(frame) == 0:
            raise ValueError("empty_response")
        columns = self._column_map(frame)
        rows: list[dict] = []
        quarantines: list[dict] = []
        for _, source in frame.iterrows():
            try:
                trade_date = _date_text(source[columns["trade_date"]])
                if not start_date.isoformat() <= trade_date <= end_date.isoformat():
                    continue
                row = {
                    "stock_code": stock_code,
                    "trade_date": trade_date,
                    "open_price": float(source[columns["open_price"]]),
                    "high_price": float(source[columns["high_price"]]),
                    "low_price": float(source[columns["low_price"]]),
                    "close_price": float(source[columns["close_price"]]),
                    # Both stock_zh_a_hist and fund_etf_hist_em report daily
                    # volume in lots and amount in yuan.
                    "volume": int(round(
                        float(source[columns["volume"]]) / volume_divisor
                    )),
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
        if not rows:
            raise ValueError("empty_response_in_requested_range")
        return rows, quarantines

    @staticmethod
    def _sina_symbol(stock_code: str) -> str:
        prefix = "sh" if stock_code.endswith(".SH") else "sz"
        return prefix + stock_code.split(".", 1)[0]

    def _adjust_sina_etf_frame(self, frame, dividends, mode: str, end_date: date):
        """Apply AKShare/Sina cumulative cash dividends to ETF OHLC rows."""

        if mode == "none":
            return frame
        if dividends is None:
            raise ValueError("ETF dividend response is unavailable")
        events: list[tuple[str, float]] = []
        if len(dividends):
            if len(dividends.columns) < 2:
                raise ValueError("ETF dividend schema drift")
            date_column = dividends.columns[0]
            value_column = dividends.columns[-1]
            for _, event in dividends.iterrows():
                event_date = _date_text(event[date_column])
                if event_date <= end_date.isoformat():
                    events.append((event_date, float(event[value_column])))
        events.sort()
        latest = events[-1][1] if events else 0.0
        adjusted = frame.copy(deep=True)
        columns = self._column_map(adjusted)
        for index, source in adjusted.iterrows():
            row_date = _date_text(source[columns["trade_date"]])
            cumulative = 0.0
            for event_date, value in events:
                if event_date > row_date:
                    break
                cumulative = value
            offset = cumulative if mode == "back" else cumulative - latest
            for field in ("open_price", "high_price", "low_price", "close_price"):
                column = columns[field]
                adjusted.at[index, column] = round(
                    float(source[column]) + offset, 6
                )
        return adjusted

    def fetch_batch(
        self, stock_code: str, start_date: date, end_date: date
    ) -> MarketBatch:
        if start_date > end_date:
            raise ValueError("start_date must not exceed end_date")
        etf = _is_etf(stock_code)
        fetcher = self.etf_fetcher if etf else self.stock_fetcher
        rows_by_mode: dict[str, list[dict]] = {}
        failures: dict[str, str] = {}
        quarantines: list[dict] = []
        interfaces: dict[str, str] = {}
        etf_dividends = None
        etf_dividends_loaded = False
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
                rows, mode_quarantines = self._normalize(
                    stock_code, mode, frame, start_date, end_date
                )
                interfaces[mode] = (
                    "fund_etf_hist_em" if etf else "stock_zh_a_hist"
                )
            except BaseException as exc:
                fallback = (
                    self.etf_fallback_fetcher if etf
                    else self.stock_fallback_fetcher
                )
                if fallback is None:
                    failures[mode] = f"{type(exc).__name__}: {exc}"
                    continue
                fallback_kwargs = {"symbol": self._sina_symbol(stock_code)}
                if not etf:
                    fallback_kwargs.update({
                        "start_date": start_date.strftime("%Y%m%d"),
                        "end_date": end_date.strftime("%Y%m%d"),
                        "adjust": adjust,
                    })
                try:
                    frame = self._fetch_with_retry(fallback, fallback_kwargs)
                    if etf and mode != "none":
                        if self.etf_dividend_fetcher is None:
                            raise ValueError("ETF dividend fallback is unavailable")
                        if not etf_dividends_loaded:
                            etf_dividends = self._fetch_with_retry(
                                self.etf_dividend_fetcher,
                                {"symbol": self._sina_symbol(stock_code)},
                            )
                            etf_dividends_loaded = True
                        frame = self._adjust_sina_etf_frame(
                            frame, etf_dividends, mode, end_date
                        )
                    rows, mode_quarantines = self._normalize(
                        stock_code,
                        mode,
                        frame,
                        start_date,
                        end_date,
                        volume_divisor=100,
                    )
                    interfaces[mode] = (
                        (
                            "fund_etf_hist_sina"
                            if mode == "none"
                            else "fund_etf_hist_sina+fund_etf_dividend_sina"
                        )
                        if etf else "stock_zh_a_daily"
                    )
                except BaseException as fallback_exc:
                    secondary = self.stock_secondary_fallback_fetcher if not etf else None
                    if secondary is None:
                        failures[mode] = (
                            f"primary={type(exc).__name__}: {exc}; "
                            f"fallback={type(fallback_exc).__name__}: {fallback_exc}"
                        )
                        continue
                    try:
                        frame = self._fetch_with_retry(secondary, {
                            "symbol": self._sina_symbol(stock_code),
                            "start_date": start_date.strftime("%Y%m%d"),
                            "end_date": end_date.strftime("%Y%m%d"),
                            "adjust": adjust,
                        })
                        rows, mode_quarantines = self._normalize(
                            stock_code,
                            mode,
                            frame,
                            start_date,
                            end_date,
                            volume_divisor=(
                                10000
                                if stock_code.split(".", 1)[0].startswith("689")
                                else 100
                            ),
                        )
                        interfaces[mode] = "stock_zh_a_hist_tx"
                    except BaseException as secondary_exc:
                        failures[mode] = (
                            f"primary={type(exc).__name__}: {exc}; "
                            f"fallback={type(fallback_exc).__name__}: {fallback_exc}; "
                            f"secondary={type(secondary_exc).__name__}: {secondary_exc}"
                        )
                        continue
            rows_by_mode[mode] = rows
            quarantines.extend(mode_quarantines)

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
                "interface": interfaces.get("none", "unavailable"),
                "interfaces": interfaces,
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
