"""Execute and aggregate independently-held PIT blue-chip constituent paths."""
from __future__ import annotations
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass

from ..backtest_provider import AdaptiveBacktestDataProvider
from ..contracts import SubLayer
from .baselines import BaselineKind
from .benchmark_contracts import WhitelistEntry
from .bluechip_basket import BlueChipBasket
from .execution_evidence import (
    StitchedNavPoint,
    TargetEvidence,
    TargetWalkForwardConfig,
    run_target_walk_forward,
)

@dataclass(frozen=True)
class BlueChipPath:
    nav: tuple[float, ...]
    member_contribution: Mapping[str, float]


@dataclass(frozen=True)
class BlueChipBasketEvidence:
    """Cost-net evidence for a simultaneously-held historical constituent basket."""

    basket: BlueChipBasket
    member_evidence: Mapping[str, TargetEvidence]
    paths: Mapping[BaselineKind, BlueChipPath]


def _member_entry(basket: BlueChipBasket, stock_code: str, source_hash: str) -> WhitelistEntry:
    """Adapt one constituent to the existing single-instrument execution contract.

    The placeholder backup is deliberately never persisted or selected: basket
    membership comes only from the disclosed PIT constituent record.
    """

    return WhitelistEntry(
        exposure_id=f"bluechip:{basket.index_code}:{stock_code}",
        sub_layer=SubLayer.DEFENSIVE_BLUE_CHIP,
        primary_code=stock_code,
        backup_code=f"{stock_code}:not-a-substitute",
        effective_from=basket.as_of_date,
        effective_to=basket.as_of_date,
        source_hash=source_hash,
        valuation_multiplier=1.0,
    )


def run_bluechip_basket_walk_forward(
    basket: BlueChipBasket,
    provider: AdaptiveBacktestDataProvider,
    config: TargetWalkForwardConfig,
    *,
    target_runner: Callable[
        [WhitelistEntry, AdaptiveBacktestDataProvider, TargetWalkForwardConfig],
        TargetEvidence,
    ] = run_target_walk_forward,
) -> BlueChipBasketEvidence:
    """Execute every disclosed member independently, then weight-align every baseline.

    No member can replace another: missing coverage or date misalignment is
    rejected by the underlying runner and :func:`aggregate_bluechip_paths`.
    """

    if not isinstance(basket, BlueChipBasket):
        raise ValueError("basket must be a BlueChipBasket")
    if not callable(target_runner):
        raise ValueError("target_runner must be callable")
    member_evidence = {
        member.stock_code: target_runner(
            _member_entry(basket, member.stock_code, member.source_hash),
            provider,
            config,
        )
        for member in basket.members
    }
    expected_baselines = frozenset(BaselineKind)
    if any(
        frozenset(evidence.stitched_paths) != expected_baselines
        for evidence in member_evidence.values()
    ):
        raise ValueError("every member must provide every baseline path")
    paths = {
        kind: aggregate_bluechip_paths(
            basket,
            {
                code: evidence.stitched_paths[kind]
                for code, evidence in member_evidence.items()
            },
        )
        for kind in BaselineKind
    }
    return BlueChipBasketEvidence(basket, member_evidence, paths)


def aggregate_bluechip_paths(basket: BlueChipBasket, paths: Mapping[str, Sequence[StitchedNavPoint]]) -> BlueChipPath:
    """Date-align all PIT members and aggregate their disclosed weights."""
    expected={member.stock_code for member in basket.members}
    if set(paths)!=expected: raise ValueError("paths must exactly cover basket members")
    reference=None
    for code in expected:
        dates=tuple(point.nav_date for point in paths[code])
        if not dates: raise ValueError("member path must not be empty")
        if reference is None: reference=dates
        elif dates!=reference: raise ValueError("member paths must be aligned")
    nav=tuple(sum(member.weight*paths[member.stock_code][index].nav_total for member in basket.members) for index in range(len(reference)))
    contribution={member.stock_code: member.weight*(paths[member.stock_code][-1].nav_total-1.0) for member in basket.members}
    return BlueChipPath(nav, contribution)

__all__ = [
    "BlueChipBasketEvidence",
    "BlueChipPath",
    "aggregate_bluechip_paths",
    "run_bluechip_basket_walk_forward",
]
