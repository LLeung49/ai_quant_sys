"""Return-regression fit of ETFs to an SW2 sector close series."""

from __future__ import annotations

import math
from collections.abc import Mapping
from dataclasses import dataclass
from datetime import date, datetime

import pandas as pd


@dataclass(frozen=True)
class ReturnExposureResult:
    etf_code: str
    corr: float
    beta: float
    r_squared: float
    residual_vol: float
    sector_fit_score: float
    sample_count: int
    confidence_status: str
    window_start_date: date | None = None
    window_end_date: date | None = None
    price_as_of_date: date | None = None


@dataclass(frozen=True)
class ReturnExposureFailure:
    etf_code: str
    failure_reason: str


def assess_return_exposure(
    etf_closes: Mapping[str, pd.Series],
    sector_close: pd.Series,
    window: int = 60,
    min_samples: int = 50,
) -> tuple[list[ReturnExposureResult], list[ReturnExposureFailure]]:
    """Calculate auditable ETF/sector return fits, retaining rejected ETFs."""

    if window < 1 or min_samples < 1:
        raise ValueError("window and min_samples must be positive")
    effective_min_samples = max(50, min_samples)

    sector = _recent_close(sector_close, window)
    sector_reason = _close_failure(sector)
    results: list[ReturnExposureResult] = []
    failures: list[ReturnExposureFailure] = []

    for raw_code, raw_close in etf_closes.items():
        code = str(raw_code)
        etf = _recent_close(raw_close, window)
        reason = _close_failure(etf)
        if reason:
            failures.append(ReturnExposureFailure(code, reason))
            continue
        if sector_reason:
            failures.append(ReturnExposureFailure(code, sector_reason))
            continue
        if sector.index[-1] not in etf.index:
            failures.append(ReturnExposureFailure(code, "stale_price_data"))
            continue

        aligned_closes = pd.concat(
            [etf.rename("etf"), sector.rename("sector")],
            axis=1,
            join="outer",
            sort=False,
        ).reindex(sector.index)
        common = aligned_closes.notna().all(axis=1)
        trailing_start = len(common) - 1
        while trailing_start >= 0 and bool(common.iloc[trailing_start]):
            trailing_start -= 1
        consecutive_closes = aligned_closes.iloc[trailing_start + 1:]
        aligned = consecutive_closes.pct_change(fill_method=None).iloc[1:].dropna()
        if any(_return_failure(aligned[column]) for column in ("etf", "sector")):
            failures.append(ReturnExposureFailure(code, "nonfinite_return_data"))
            continue

        sample_count = len(aligned)
        if sample_count < effective_min_samples:
            reason = (
                "insufficient_consecutive_common_returns"
                if int(common.sum()) >= effective_min_samples + 1
                else "insufficient_common_returns"
            )
            failures.append(ReturnExposureFailure(code, reason))
            continue

        x = aligned["sector"]
        y = aligned["etf"]
        variance = float(((x - x.mean()) ** 2).mean())
        if not math.isfinite(variance) or variance == 0.0:
            failures.append(ReturnExposureFailure(code, "zero_sector_return_variance"))
            continue
        etf_variance = float(((y - y.mean()) ** 2).mean())
        if not math.isfinite(etf_variance) or etf_variance == 0.0:
            failures.append(ReturnExposureFailure(code, "zero_etf_return_variance"))
            continue
        covariance = float(((x - x.mean()) * (y - y.mean())).mean())
        beta = covariance / variance
        corr = float(x.corr(y))
        if not all(math.isfinite(value) for value in (beta, corr)):
            failures.append(ReturnExposureFailure(code, "nonfinite_regression_output"))
            continue
        r_squared = corr**2
        alpha = float(y.mean() - beta * x.mean())
        residual = y - (alpha + beta * x)
        residual_vol = float(residual.std(ddof=0) * math.sqrt(252.0))
        if not math.isfinite(residual_vol):
            failures.append(ReturnExposureFailure(code, "nonfinite_regression_output"))
            continue
        score = max(beta, 0.0) * max(corr, 0.0) * r_squared / (1.0 + residual_vol)
        results.append(ReturnExposureResult(
            etf_code=code,
            corr=corr,
            beta=beta,
            r_squared=r_squared,
            residual_vol=residual_vol,
            sector_fit_score=score,
            sample_count=sample_count,
            confidence_status=(
                "qualified" if beta > 0 and corr > 0 and r_squared >= 0.25
                else "low_confidence"
            ),
            window_start_date=_index_date(consecutive_closes.index[0]),
            window_end_date=_index_date(consecutive_closes.index[-1]),
            price_as_of_date=_index_date(consecutive_closes.index[-1]),
        ))

    results.sort(key=lambda item: (-item.sector_fit_score, -item.r_squared, item.etf_code))
    failures.sort(key=lambda item: (item.etf_code, item.failure_reason))
    return results, failures


def _recent_close(close: pd.Series, window: int) -> pd.Series:
    if not isinstance(close, pd.Series):
        return pd.Series(dtype=float)
    return pd.to_numeric(close.sort_index().tail(window + 1), errors="coerce")


def _close_failure(close: pd.Series) -> str | None:
    if close.empty or close.isna().any() or not close.map(math.isfinite).all():
        return "nonfinite_close_data"
    return None


def _return_failure(returns: pd.Series) -> bool:
    return bool(returns.isna().any() or not returns.map(math.isfinite).all())


def _index_date(value: object) -> date | None:
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    if isinstance(value, pd.Timestamp):
        return value.date()
    return None
