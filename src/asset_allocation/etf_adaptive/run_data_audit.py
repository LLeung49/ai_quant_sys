"""Read-only audit entry point for the adaptive ETF research universe."""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
from datetime import date
from enum import Enum
import json
from pathlib import Path
from typing import Protocol

from data_ingestion.db_config import execute_query
from morning_conference.sector_rotation2.research.evaluation.prices import (
    load_authoritative_market_calendar,
)

from .contracts import DataQualityError, DataQualityIssue, DualPriceBar, ETFMetadata
from .market_data import AdaptiveMarketDataProvider
from .universe import evaluate_eligibility


_NON_MATERIAL_QUALITY_REASONS = frozenset({"unverified_pre_close"})
_ADJUSTMENT_VERSION_QUALITY_REASONS = frozenset(
    {
        "stale_adjustment_asof",
        "adjustment_provenance_unavailable",
        "invalid_adjustment_asof",
        "adjustment_asof_mismatch",
        "future_adjustment_asof",
        "future_latest_action_date",
    }
)


class AuditProvider(Protocol):
    last_quality_issues: tuple[DataQualityIssue, ...]

    def load_metadata(self, as_of_date: date) -> tuple[ETFMetadata, ...]: ...

    def load_bars(
        self, stock_code: str, start_date: date, end_date: date
    ) -> tuple[DualPriceBar, ...]: ...


@dataclass(frozen=True)
class DateCoverage:
    first_trade_date: str | None
    last_trade_date: str | None
    session_count: int


@dataclass(frozen=True)
class AuditReport:
    as_of_date: str
    universe_count: int
    eligible_count: int
    rejected_count: int
    eligible_by_exposure_group: dict[str, int]
    rejected_by_reason: dict[str, int]
    examples_by_reason: dict[str, tuple[str, ...]]
    date_coverage: dict[str, DateCoverage]
    data_quality_error_count: int
    data_quality_by_reason: dict[str, int]
    raw_qfq_mismatch_count: int
    stale_adjustment_version_count: int


def audit_universe(
    as_of_date: date,
    provider: AuditProvider,
    output_path: Path | None = None,
) -> AuditReport:
    """Audit point-in-time ETF eligibility and optionally write a local report."""

    eligible_count = 0
    rejected_count = 0
    eligible_by_exposure_group: dict[str, int] = {}
    rejected_by_reason: dict[str, int] = {}
    examples_by_reason: dict[str, set[str]] = {}
    date_coverage: dict[str, DateCoverage] = {}
    data_quality_by_reason: dict[str, int] = {}

    def record_quality_issue(reason: str, stock_code: str) -> None:
        data_quality_by_reason[reason] = data_quality_by_reason.get(reason, 0) + 1
        examples_by_reason.setdefault(reason, set()).add(stock_code)

    def record_quality_issues(issues: tuple[DataQualityIssue, ...]) -> int:
        material_issue_count = 0
        for issue in issues:
            reason = issue.code.value if isinstance(issue.code, Enum) else issue.code
            if reason in _NON_MATERIAL_QUALITY_REASONS:
                continue
            record_quality_issue(reason, issue.stock_code)
            material_issue_count += 1
        return material_issue_count

    def record_quality_error(exc: DataQualityError) -> None:
        issues = exc.issues or provider.last_quality_issues
        if issues and record_quality_issues(issues):
            return
        reason = "unclassified_data_quality_error"
        record_quality_issue(reason, "<unknown>")

    try:
        metadata_rows = sorted(
            provider.load_metadata(as_of_date), key=lambda item: item.stock_code
        )
    except DataQualityError as exc:
        metadata_rows = []
        record_quality_error(exc)

    for metadata in metadata_rows:
        try:
            bars = provider.load_bars(
                metadata.stock_code, metadata.listing_date, as_of_date
            )
        except DataQualityError as exc:
            rejected_count += 1
            rejected_by_reason["data_quality_error"] = (
                rejected_by_reason.get("data_quality_error", 0) + 1
            )
            examples_by_reason.setdefault("data_quality_error", set()).add(
                metadata.stock_code
            )
            date_coverage[metadata.stock_code] = DateCoverage(None, None, 0)
            record_quality_error(exc)
            continue
        record_quality_issues(provider.last_quality_issues)
        point_in_time_bars = tuple(
            bar for bar in bars if bar.trade_date <= as_of_date
        )
        future_bars = tuple(bar for bar in bars if bar.trade_date > as_of_date)
        trade_dates = sorted(bar.trade_date for bar in point_in_time_bars)
        date_coverage[metadata.stock_code] = DateCoverage(
            first_trade_date=trade_dates[0].isoformat() if trade_dates else None,
            last_trade_date=trade_dates[-1].isoformat() if trade_dates else None,
            session_count=len(set(trade_dates)),
        )
        eligibility = evaluate_eligibility(metadata, point_in_time_bars, as_of_date)
        if future_bars:
            reason = "bar_date_after_as_of_date"
            rejected_count += 1
            rejected_by_reason[reason] = rejected_by_reason.get(reason, 0) + 1
            examples_by_reason.setdefault(reason, set()).add(metadata.stock_code)
            for _ in future_bars:
                record_quality_issue(reason, metadata.stock_code)
        elif eligibility.eligible:
            eligible_count += 1
            exposure_group = eligibility.exposure_group
            if exposure_group is not None:
                eligible_by_exposure_group[exposure_group] = (
                    eligible_by_exposure_group.get(exposure_group, 0) + 1
                )
        else:
            rejected_count += 1
        for reason in eligibility.rejection_reasons:
            rejected_by_reason[reason] = rejected_by_reason.get(reason, 0) + 1
            examples_by_reason.setdefault(reason, set()).add(metadata.stock_code)

    report = AuditReport(
        as_of_date=as_of_date.isoformat(),
        universe_count=len(metadata_rows),
        eligible_count=eligible_count,
        rejected_count=rejected_count,
        eligible_by_exposure_group=dict(sorted(eligible_by_exposure_group.items())),
        rejected_by_reason=dict(sorted(rejected_by_reason.items())),
        examples_by_reason={
            reason: tuple(sorted(codes)[:10])
            for reason, codes in sorted(examples_by_reason.items())
        },
        date_coverage=dict(sorted(date_coverage.items())),
        data_quality_error_count=sum(data_quality_by_reason.values()),
        data_quality_by_reason=dict(sorted(data_quality_by_reason.items())),
        raw_qfq_mismatch_count=data_quality_by_reason.get(
            "raw_qfq_date_mismatch", 0
        ),
        stale_adjustment_version_count=sum(
            data_quality_by_reason.get(reason, 0)
            for reason in _ADJUSTMENT_VERSION_QUALITY_REASONS
        ),
    )
    if output_path is not None:
        output_path.write_text(
            json.dumps(asdict(report), ensure_ascii=False, sort_keys=True),
            encoding="utf-8",
        )
    return report


def default_provider() -> AdaptiveMarketDataProvider:
    """Build the production provider over the repository's read-only query adapter."""

    return AdaptiveMarketDataProvider(
        query=execute_query,
        calendar_loader=lambda start_date, end_date: load_authoritative_market_calendar(
            start_date, end_date, execute_query
        ),
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Audit adaptive ETF universe and market-data quality"
    )
    parser.add_argument("--as-of-date", required=True)
    parser.add_argument("--output-json", required=True)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    report = audit_universe(
        date.fromisoformat(args.as_of_date),
        default_provider(),
        Path(args.output_json),
    )
    print(json.dumps(asdict(report), ensure_ascii=False, sort_keys=True))
    return 0 if report.data_quality_error_count == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
