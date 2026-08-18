"""Exposure-fit metrics calculated on same-date returns."""

import pandas as pd


def _returns(etf_close: pd.Series, sector_close: pd.Series, window: int) -> tuple[pd.Series, pd.Series]:
    aligned = pd.concat([etf_close.rename("etf"), sector_close.rename("sector")], axis=1).dropna().tail(window + 1)
    returns = aligned.pct_change().dropna()
    return returns["etf"], returns["sector"]


def calc_tracking_corr(etf_close: pd.Series, sector_close: pd.Series, window: int = 60) -> float | None:
    etf_returns, sector_returns = _returns(etf_close, sector_close, window)
    value = etf_returns.corr(sector_returns)
    return None if pd.isna(value) else float(value)


def calc_tracking_error(etf_close: pd.Series, sector_close: pd.Series, window: int = 60) -> float | None:
    etf_returns, sector_returns = _returns(etf_close, sector_close, window)
    if etf_returns.empty:
        return None
    return float((etf_returns - sector_returns).std(ddof=0))
