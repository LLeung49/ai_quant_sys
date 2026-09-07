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
from typing import Any, Callable, Mapping, Protocol, Sequence

from ..backtest_provider import AdaptiveBacktestDataProvider
from ..config import AdaptiveConfig
from ..contracts import DualPriceBar, LayeredInstrument, SubLayer, asset_layer_for
from ..layers import validate_sub_layer
from .report import ResearchArtifact, write_research_report


@dataclass(frozen=True)
class ResearchRunConfig:
    as_of_date: date
    output_dir: Path
    initial_cash: Decimal = Decimal("100000")
    extra: Mapping[str, Any] = field(default_factory=lambda: MappingProxyType({}))


class _LayeredResearchProvider(Protocol):
    def load_instruments(self, as_of_date: date) -> Sequence[LayeredInstrument]: ...

    def load_bars(
        self, stock_code: str, start_date: date, end_date: date,
    ) -> Sequence[DualPriceBar]: ...


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

    if artifact_factory is None and provider is None:
        raise NotImplementedError("run_research requires a layered market-data provider")

    factory = artifact_factory or _default_artifact_factory(provider, config)
    artifact = factory(config)
    write_research_report(artifact, config.output_dir)


def _default_artifact_factory(provider: _LayeredResearchProvider, run_config: ResearchRunConfig):
    def _factory(config: ResearchRunConfig) -> ResearchArtifact:
        base_config = AdaptiveConfig.default()
        configured_budgets = _sub_layer_budgets(config.extra)
        sub_layers: dict[str, dict[str, object]] = {}
        targets: list[dict[str, str]] = []
        audit_rows: list[dict[str, object]] = []
        for instrument in provider.load_instruments(config.as_of_date):
            sub_layer = validate_sub_layer(instrument)
            budget = configured_budgets.get(sub_layer)
            if budget is None:
                audit_rows.append({"stock_code": instrument.stock_code, "accepted": False, "reason": "no_budget"})
                continue
            bars = tuple(provider.load_bars(instrument.stock_code, date(2020, 1, 1), config.as_of_date))
            oos_return = _oos_return(bars, instrument.stock_code, config.as_of_date)
            accepted = oos_return is not None and oos_return > 0
            audit_rows.append({
                "stock_code": instrument.stock_code, "sub_layer": sub_layer.value,
                "accepted": accepted, "oos_return": oos_return,
            })
            if not accepted:
                continue
            entry = sub_layers.setdefault(sub_layer.value, {
                "budget": str(budget), "products": [], "audit": [], "oos": [], "pareto": [], "portfolio": {},
            })
            entry["products"].append(instrument.stock_code)
            entry["audit"].append(audit_rows[-1])
            entry["oos"].append({"stock_code": instrument.stock_code, "return": oos_return})
        for sub_layer_name, entry in sub_layers.items():
            products = sorted(entry["products"])
            weight = Decimal("1") / Decimal(len(products))
            entry["pareto"] = products
            entry["portfolio"] = {"weights": {code: str(weight) for code in products}}
            sub_layer = SubLayer(sub_layer_name)
            for stock_code in products:
                instrument = next(item for item in provider.load_instruments(config.as_of_date) if item.stock_code == stock_code)
                targets.append({
                    "stock_code": stock_code, "tracking_index_code": stock_code,
                    "layer": asset_layer_for(sub_layer).value, "sub_layer": sub_layer.value,
                    "sub_layer_budget": entry["budget"], "instrument_type": instrument.instrument_type.value,
                    "weight": str(weight), "config_hash": base_config.config_hash(),
                })
        return ResearchArtifact(
            attempted_config_count=len(audit_rows),
            failed_config_count=sum(1 for row in audit_rows if not row["accepted"]),
            data_cutoff=config.as_of_date.isoformat(),
            config_hash=base_config.config_hash(),
            artifacts={
                "universe_audit": {"as_of_date": config.as_of_date.isoformat(), "rows": audit_rows},
                "executive_report": (
                    f"# Adaptive layered equity research\n\nAs-of date: {config.as_of_date.isoformat()}\n"
                ),
            },
            frozen_selection={
                "selection_id": f"layered-{config.as_of_date.isoformat()}",
                "config_hash": base_config.config_hash(), "targets": targets,
                "sub_layer_budgets": {name: entry["budget"] for name, entry in sub_layers.items()},
            },
            sub_layers=sub_layers,
        )
    return _factory


def _sub_layer_budgets(extra: Mapping[str, Any]) -> dict[SubLayer, Decimal]:
    raw = extra.get("sub_layer_budgets", {})
    if not isinstance(raw, Mapping):
        raise ValueError("extra.sub_layer_budgets must be a mapping")
    budgets: dict[SubLayer, Decimal] = {}
    for name, amount in raw.items():
        value = Decimal(str(amount))
        if not value.is_finite() or value <= 0:
            raise ValueError("sub-layer budgets must be positive finite decimals")
        budgets[SubLayer(str(name))] = value
    return budgets


def _oos_return(bars: Sequence[DualPriceBar], stock_code: str, as_of_date: date) -> float | None:
    if len(bars) < 2 or bars[-1].stock_code != stock_code or bars[-1].trade_date != as_of_date:
        return None
    start, end = bars[0].raw_close, bars[-1].raw_close
    return None if start <= 0 else float(end / start - 1)


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
