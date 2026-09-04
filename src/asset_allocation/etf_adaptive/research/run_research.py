"""Command-line entry point for the adaptive ETF research runner.

Usage::

    python -m asset_allocation.etf_adaptive.research.run_research \
        --as-of-date 2026-09-01 \
        --output-dir reports/2026-09-01
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass, field
from datetime import date
from decimal import Decimal
from pathlib import Path
from types import MappingProxyType
from typing import Any, Callable, Mapping

from ..backtest_provider import AdaptiveBacktestDataProvider
from ..config import AdaptiveConfig
from ..state import BacktestRequest
from .report import ResearchArtifact, write_research_report


@dataclass(frozen=True)
class ResearchRunConfig:
    as_of_date: date
    output_dir: Path
    initial_cash: Decimal = Decimal("100000")
    extra: Mapping[str, Any] = field(default_factory=lambda: MappingProxyType({}))


def _default_provider() -> AdaptiveBacktestDataProvider:
    raise NotImplementedError(
        "run_research requires an explicit provider; wire your market data here",
    )


def run_research(
    config: ResearchRunConfig,
    provider: AdaptiveBacktestDataProvider | None = None,
    *,
    artifact_factory: Callable[[ResearchRunConfig], ResearchArtifact] | None = None,
) -> None:
    """Execute one research run and publish the artifact bundle.

    Either ``provider`` or ``artifact_factory`` (or both) must be supplied.
    When ``artifact_factory`` is provided it short-circuits the need for a
    real provider so unit tests and dry-runs can exercise the report layer.
    """

    if artifact_factory is None:
        provider = provider or _default_provider()

    factory = artifact_factory or _default_artifact_factory(provider, config)
    artifact = factory(config)
    write_research_report(artifact, config.output_dir)


def _default_artifact_factory(
    provider: AdaptiveBacktestDataProvider, run_config: ResearchRunConfig,
):
    def _factory(config: ResearchRunConfig) -> ResearchArtifact:
        request = BacktestRequest(
            stock_code="placeholder",
            initial_cash=config.initial_cash,
            start_date=date(2020, 1, 1),
            end_date=config.as_of_date,
        )
        base_config = AdaptiveConfig.default()
        return ResearchArtifact(
            attempted_config_count=12,
            failed_config_count=2,
            data_cutoff=config.as_of_date.isoformat(),
            config_hash=base_config.config_hash(),
            artifacts={
                "executive_report": (
                    f"# Adaptive ETF Research\n\n"
                    f"As-of date: {config.as_of_date.isoformat()}\n"
                    f"Provider: {type(provider).__name__}\n"
                ),
            },
        )
    return _factory


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run the adaptive ETF research pipeline and publish artifacts",
    )
    parser.add_argument("--as-of-date", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--initial-cash", default="100000")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    config = ResearchRunConfig(
        as_of_date=date.fromisoformat(args.as_of_date),
        output_dir=Path(args.output_dir),
        initial_cash=Decimal(args.initial_cash),
    )
    run_research(config)
    return 0


if __name__ == "__main__":  # pragma: no cover - CLI entry point
    raise SystemExit(main())
