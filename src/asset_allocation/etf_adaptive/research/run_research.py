"""Command-line entry point for the adaptive ETF research runner.

Usage::

    python -m asset_allocation.etf_adaptive.research.run_research \
        --as-of-date 2026-09-01 \
        --output-dir reports/2026-09-01
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass, field, replace
from datetime import date, timedelta
from decimal import Decimal
from pathlib import Path
from types import MappingProxyType
from typing import Any, Callable, Mapping, Protocol, Sequence

from ..backtest_provider import AdaptiveBacktestDataProvider
from ..config import AdaptiveConfig
from ..contracts import DualPriceBar, LayeredInstrument, SubLayer, SubLayerBudget, asset_layer_for
from ..layers import validate_sub_layer
from ..frozen_selection import _canonical_hash
from .portfolio import evaluate_sub_layer_portfolios
from .report import ResearchArtifact, write_research_report
from .selection import (
    CandidateMetrics,
    ProductMetrics,
    SubLayerSelectionEvidence,
    pareto_front,
    select_sub_layer_products,
)


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

    def load_research_evidence(
        self, as_of_date: date, stock_code: str,
    ) -> Mapping[str, object]: ...

    def load_selection_evidence(
        self, as_of_date: date, sub_layer: SubLayer, budget: SubLayerBudget,
    ) -> SubLayerSelectionEvidence: ...


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
        candidates: dict[SubLayer, list[tuple[LayeredInstrument, ProductMetrics, CandidateMetrics, tuple[float, ...]]]] = {}
        for instrument in provider.load_instruments(config.as_of_date):
            sub_layer = validate_sub_layer(instrument)
            budget = configured_budgets.get(sub_layer)
            if budget is None:
                audit_rows.append({"stock_code": instrument.stock_code, "accepted": False, "reason": "no_budget"})
                continue
            evidence_loader = getattr(provider, "load_research_evidence", None)
            if not callable(evidence_loader):
                audit_rows.append({
                    "stock_code": instrument.stock_code, "sub_layer": sub_layer.value,
                    "accepted": False, "reason": "missing_walk_forward_evidence",
                })
                continue
            try:
                product, candidate, returns = _explicit_evidence(
                    evidence_loader(config.as_of_date, instrument.stock_code), instrument, sub_layer,
                )
            except ValueError as exc:
                audit_rows.append({"stock_code": instrument.stock_code, "sub_layer": sub_layer.value,
                                   "accepted": False, "reason": str(exc)})
                continue
            candidates.setdefault(sub_layer, []).append((instrument, product, candidate, returns))
        for sub_layer, layer_candidates in candidates.items():
            budget = configured_budgets[sub_layer]
            selection_loader = getattr(provider, "load_selection_evidence", None)
            if not callable(selection_loader):
                audit_rows.extend(_selection_rejections(layer_candidates, "missing_selection_evidence"))
                continue
            evidence = selection_loader(config.as_of_date, sub_layer, SubLayerBudget(sub_layer, budget))
            if not isinstance(evidence, SubLayerSelectionEvidence) or evidence.budget != SubLayerBudget(sub_layer, budget):
                audit_rows.extend(_selection_rejections(layer_candidates, "invalid_selection_evidence"))
                continue
            pareto = pareto_front(candidate for _, _, candidate, _ in layer_candidates)
            pareto_ids = frozenset(candidate.candidate_id for candidate in pareto)
            products = tuple(product for _, product, _, _ in layer_candidates)
            returns = {product.product_id: series for _, product, _, series in layer_candidates}
            evidence = replace(evidence, pareto_product_ids=pareto_ids)
            selected = select_sub_layer_products(products, evidence)
            if not selected:
                audit_rows.extend(_selection_rejections(layer_candidates, "selection_gate"))
                continue
            try:
                portfolio = evaluate_sub_layer_portfolios(selected, returns, evidence)
            except ValueError:
                audit_rows.extend(_selection_rejections(layer_candidates, "portfolio_gate"))
                continue
            selected_ids = {product.product_id for product in selected}
            for instrument, product, _, _ in layer_candidates:
                audit_rows.append({
                    "stock_code": instrument.stock_code, "sub_layer": sub_layer.value,
                    "accepted": product.product_id in selected_ids,
                    "reason": None if product.product_id in selected_ids else "selection_gate",
                })
            entry = {
                "budget": str(budget),
                "products": sorted(selected_ids),
                "audit": [row for row in audit_rows if row.get("sub_layer") == sub_layer.value],
                "oos": [_oos_artifact(candidate) for _, _, candidate, _ in layer_candidates],
                "pareto": sorted(pareto_ids),
                "portfolio": _portfolio_artifact(portfolio),
            }
            sub_layers[sub_layer.value] = entry
            weights = portfolio.capped_inverse_volatility.weights
            instruments = {instrument.stock_code: instrument for instrument, _, _, _ in layer_candidates}
            products_by_id = {product.product_id: product for _, product, _, _ in layer_candidates}
            for stock_code in sorted(selected_ids):
                instrument = instruments[stock_code]
                targets.append({
                    "stock_code": stock_code, "tracking_index_code": products_by_id[stock_code].tracking_index_code,
                    "layer": asset_layer_for(sub_layer).value, "sub_layer": sub_layer.value,
                    "sub_layer_budget": entry["budget"], "instrument_type": instrument.instrument_type.value,
                    "weight": _decimal_text(weights[stock_code]),
                })
        activation_date = config.as_of_date + timedelta(days=1)
        frozen_selection = {
            "selection_id": f"layered-{config.as_of_date.isoformat()}",
            "data_cutoff": config.as_of_date.isoformat(),
            "activation_date": activation_date.isoformat(),
            "review_date": (activation_date + timedelta(days=183)).isoformat(),
            "targets": targets,
            "sub_layer_budgets": {name: entry["budget"] for name, entry in sub_layers.items()},
        }
        selection_hash = _canonical_hash(frozen_selection)
        frozen_selection["config_hash"] = selection_hash
        for target in targets:
            target["config_hash"] = selection_hash
        return ResearchArtifact(
            attempted_config_count=len(audit_rows),
            failed_config_count=sum(1 for row in audit_rows if not row["accepted"]),
            data_cutoff=config.as_of_date.isoformat(),
            config_hash=selection_hash,
            artifacts={
                "universe_audit": {"as_of_date": config.as_of_date.isoformat(), "rows": audit_rows},
                "executive_report": (
                    f"# Adaptive layered equity research\n\nAs-of date: {config.as_of_date.isoformat()}\n"
                ),
            },
            frozen_selection=frozen_selection,
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


def _research_metrics(
    bars: Sequence[DualPriceBar], stock_code: str, as_of_date: date,
) -> tuple[tuple[float, ...], float, float, float] | None:
    """Build the minimum independent return evidence required by selection."""

    if len(bars) < 3 or bars[-1].stock_code != stock_code or bars[-1].trade_date != as_of_date:
        return None
    if any(bar.stock_code != stock_code for bar in bars):
        return None
    returns = tuple(
        current.raw_close / previous.raw_close - 1.0
        for previous, current in zip(bars, bars[1:])
    )
    if len(returns) < 2:
        return None
    nav = [bars[0].raw_close]
    nav.extend(bar.raw_close for bar in bars[1:])
    peak = nav[0]
    max_drawdown_abs = 0.0
    for value in nav:
        peak = max(peak, value)
        max_drawdown_abs = max(max_drawdown_abs, 1.0 - value / peak)
    return (
        returns,
        nav[-1] / nav[0] - 1.0,
        max_drawdown_abs,
        sum(value > 0.0 for value in returns) / len(returns),
    )


def _explicit_evidence(
    raw: object, instrument: LayeredInstrument, sub_layer: SubLayer,
) -> tuple[ProductMetrics, CandidateMetrics, tuple[float, ...]]:
    """Validate externally produced cost-adjusted walk-forward evidence."""

    if not isinstance(raw, Mapping):
        raise ValueError("missing_walk_forward_evidence")
    product, candidate, returns = raw.get("product"), raw.get("candidate"), raw.get("oos_returns")
    if not isinstance(product, ProductMetrics) or not isinstance(candidate, CandidateMetrics):
        raise ValueError("invalid_walk_forward_evidence")
    if product.product_id != instrument.stock_code or candidate.candidate_id != instrument.stock_code:
        raise ValueError("walk_forward_evidence_identity_mismatch")
    if product.sub_layer is not sub_layer or not isinstance(returns, tuple) or len(returns) < 2:
        raise ValueError("invalid_walk_forward_evidence")
    if any(not _finite_number(value) for value in returns):
        raise ValueError("invalid_walk_forward_evidence")
    if not all(_finite_number(value) for value in (
        product.history_confidence, product.average_amount, product.data_quality_score,
        product.cost_sensitivity, product.oos_evidence, candidate.annual_return,
        candidate.max_drawdown_abs, candidate.positive_window_share, candidate.cost_ratio,
    )):
        raise ValueError("invalid_walk_forward_evidence")
    return product, candidate, tuple(float(value) for value in returns)


def _finite_number(value: object) -> bool:
    return type(value) in (int, float) and math.isfinite(float(value))


def _selection_rejections(
    candidates: Sequence[tuple[LayeredInstrument, ProductMetrics, CandidateMetrics, tuple[float, ...]]],
    reason: str,
) -> list[dict[str, object]]:
    return [
        {"stock_code": instrument.stock_code, "sub_layer": product.sub_layer.value,
         "accepted": False, "reason": reason}
        for instrument, product, _, _ in candidates
    ]


def _oos_artifact(candidate: CandidateMetrics) -> dict[str, object]:
    return {
        "stock_code": candidate.candidate_id,
        "annual_return": candidate.annual_return,
        "max_drawdown_abs": candidate.max_drawdown_abs,
        "positive_window_share": candidate.positive_window_share,
    }


def _portfolio_artifact(portfolio: object) -> dict[str, object]:
    # The evaluation object deliberately stays internal; published artifacts are
    # simple, deterministic JSON values that downstream freeze checks can audit.
    return {
        "equal_weight": {
            "weights": portfolio.equal_weight.weights,
            "allocations": {key: str(value) for key, value in portfolio.equal_weight.allocations.items()},
        },
        "capped_inverse_volatility": {
            "weights": portfolio.capped_inverse_volatility.weights,
            "allocations": {key: str(value) for key, value in portfolio.capped_inverse_volatility.allocations.items()},
        },
    }


def _decimal_text(value: float) -> str:
    """Keep frozen weight text canonical for config-hash reproducibility."""

    return format(Decimal(str(value)).normalize(), "f")


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
