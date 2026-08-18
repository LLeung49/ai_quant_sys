"""Return-regression fit of ETFs to an SW2 sector close series."""

from __future__ import annotations

import math
from collections.abc import Mapping
from dataclasses import dataclass

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

    sector = _recent_close(sector_close, window)
    sector_reason = _close_failure(sector)
    sector_returns = None if sector_reason else sector.pct_change().iloc[1:]
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
            failures.append(ReturnExposureFailure(code, "sector_nonfinite_close_data"))
            continue

        aligned = pd.concat(
            [etf.pct_change().rename("etf"), sector_returns.rename("sector")],
            axis=1,
            join="inner",
        ).dropna()
        sample_count = len(aligned)
        if sample_count < min_samples:
            failures.append(ReturnExposureFailure(code, "insufficient_common_returns"))
            continue

        x = aligned["sector"]
        y = aligned["etf"]
        variance = float(((x - x.mean()) ** 2).mean())
        if not math.isfinite(variance) or variance == 0.0:
            failures.append(ReturnExposureFailure(code, "zero_sector_return_variance"))
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
        ))

    results.sort(key=lambda item: (-item.sector_fit_score, -item.r_squared, item.etf_code))
    failures.sort(key=lambda item: (item.etf_code, item.failure_reason))
    return results, failures


def _recent_close(close: pd.Series, window: int) -> pd.Series:
    if not isinstance(close, pd.Series):
        return pd.Series(dtype=float)
    return pd.to_numeric(close.tail(window + 1), errors="coerce")


def _close_failure(close: pd.Series) -> str | None:
    if close.empty or close.isna().any() or not close.map(math.isfinite).all():
        return "nonfinite_close_data"
    return None
