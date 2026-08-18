"""Refresh SW2 ETF mappings from local daily return regressions only."""

from __future__ import annotations

import argparse
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from datetime import date

import pandas as pd

from .mapping import ensure_mapping_schema, persist_return_exposure_mapping
from .return_data import ReturnMappingInput, load_return_mapping_input
from .return_exposure import (
    ReturnExposureFailure,
    ReturnExposureResult,
    assess_return_exposure,
)


RETURN_MAPPING_VERSION = "sw2_return_regression_v1"
RETURN_UNIVERSE_SOURCE = "local_domestic_equity_etf"


@dataclass(frozen=True)
class ReturnRefreshSummary:
    sectors: int
    etf_universe: int
    qualified: int
    low_confidence: int
    quality_failures: int
    persisted_rows: int


Loader = Callable[[date, int, int], ReturnMappingInput]
Assessor = Callable[
    [Mapping[str, pd.Series], pd.Series, int, int],
    tuple[list[ReturnExposureResult], list[ReturnExposureFailure]],
]
Persist = Callable[..., int]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Refresh effective-dated SW2 ETF mappings from local daily returns",
    )
    parser.add_argument("--as-of-date", required=True)
    parser.add_argument("--level", type=int, choices=(2,), required=True)
    parser.add_argument("--config-hash", required=True)
    parser.add_argument("--window", type=int, default=60)
    parser.add_argument("--min-samples", type=int, default=50)
    return parser


def run_refresh(
    *,
    target_date: date,
    sector_level: int,
    config_hash: str,
    window: int = 60,
    min_samples: int = 50,
    load_input: Loader = load_return_mapping_input,
    assessor: Assessor = assess_return_exposure,
    persist: Persist = persist_return_exposure_mapping,
    ensure_schema: Callable[[], None] = ensure_mapping_schema,
) -> ReturnRefreshSummary:
    """Run the injected local loader/model/persistence pipeline for every SW2."""

    if sector_level != 2:
        raise ValueError("return mapping refresh requires sector_level=2")
    if window < 1 or min_samples < 1:
        raise ValueError("window and min_samples must be positive")

    ensure_schema()
    loaded = load_input(target_date, sector_level, window)
    qualified_count = 0
    low_confidence_count = 0
    quality_failure_count = 0
    persisted_count = 0

    for sector_name in sorted(loaded.sector_closes):
        sector_close = loaded.sector_closes[sector_name]
        ranked, _failures = assessor(loaded.etf_closes, sector_close, window, min_samples)
        selected = sorted(
            (item for item in ranked if item.sample_count >= 50),
            key=lambda item: (-item.sector_fit_score, -item.r_squared, item.etf_code),
        )[:3]
        if selected:
            qualified_count += sum(item.confidence_status == "qualified" for item in selected)
            low_confidence_count += sum(item.confidence_status == "low_confidence" for item in selected)
        else:
            quality_failure_count += 1

        window_start, window_end = _window_bounds(sector_close, target_date, window)
        persisted_count += persist(
            sector_name,
            sector_level,
            target_date,
            selected,
            window_start_date=window_start,
            window_end_date=window_end,
            lookback_trading_days=window,
            price_as_of_date=window_end,
            price_source=loaded.price_source,
            universe_source=RETURN_UNIVERSE_SOURCE,
            mapping_version=RETURN_MAPPING_VERSION,
            config_hash=config_hash,
        )

    return ReturnRefreshSummary(
        sectors=len(loaded.sector_closes),
        etf_universe=len(loaded.universe_codes),
        qualified=qualified_count,
        low_confidence=low_confidence_count,
        quality_failures=quality_failure_count,
        persisted_rows=persisted_count,
    )


def main(
    argv: list[str] | None = None,
    *,
    load_input: Loader = load_return_mapping_input,
    assessor: Assessor = assess_return_exposure,
    persist: Persist = persist_return_exposure_mapping,
    ensure_schema: Callable[[], None] = ensure_mapping_schema,
) -> int:
    args = build_parser().parse_args(argv)
    summary = run_refresh(
        target_date=date.fromisoformat(args.as_of_date),
        sector_level=args.level,
        config_hash=args.config_hash,
        window=args.window,
        min_samples=args.min_samples,
        load_input=load_input,
        assessor=assessor,
        persist=persist,
        ensure_schema=ensure_schema,
    )
    print(
        f"{args.as_of_date}: sectors={summary.sectors} "
        f"etf_universe={summary.etf_universe} qualified={summary.qualified} "
        f"low_confidence={summary.low_confidence} "
        f"quality_failures={summary.quality_failures} "
        f"persisted_rows={summary.persisted_rows}",
    )
    return 0


def _window_bounds(series: pd.Series, target_date: date, window: int) -> tuple[date, date]:
    index = pd.to_datetime(series.tail(window + 1).index, errors="coerce")
    valid = [value.date() for value in index if not pd.isna(value)]
    if not valid:
        return target_date, target_date
    return min(valid), max(valid)


if __name__ == "__main__":
    raise SystemExit(main())
