"""Execute and aggregate independently-held PIT blue-chip constituent paths."""
from __future__ import annotations
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass, field
from decimal import Decimal

from ..backtest_provider import AdaptiveBacktestDataProvider
from ..contracts import SubLayer
from .baselines import BaselineKind
from .benchmark_contracts import WhitelistEntry
from .bluechip_basket import BlueChipBasket
from .execution_evidence import (
    StitchedNavPoint,
    ExecutionCostTurnover,
    TargetEvidence,
    TargetWalkForwardConfig,
    run_target_walk_forward,
)

@dataclass(frozen=True)
class BlueChipPath:
    points: tuple[StitchedNavPoint, ...]
    member_contribution: Mapping[str, float]

    @property
    def nav(self) -> tuple[float, ...]:
        return tuple(point.nav_total for point in self.points)


@dataclass(frozen=True)
class BlueChipBasketEvidence:
    """Cost-net evidence for a simultaneously-held historical constituent basket."""

    basket: BlueChipBasket
    member_evidence: Mapping[str, TargetEvidence]
    paths: Mapping[BaselineKind, BlueChipPath]
    initial_cash: Decimal | None = None
    execution_evidence: Mapping[BaselineKind, ExecutionCostTurnover] = field(default_factory=dict)

    @property
    def stitched_paths(self) -> Mapping[BaselineKind, tuple[StitchedNavPoint, ...]]:
        return {kind: path.points for kind, path in self.paths.items()}


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
    execution_evidence = _aggregate_execution_evidence(basket, member_evidence)
    return BlueChipBasketEvidence(
        basket,
        member_evidence,
        paths,
        next(iter(member_evidence.values())).initial_cash,
        execution_evidence,
    )


def _aggregate_execution_evidence(
    basket: BlueChipBasket,
    member_evidence: Mapping[str, TargetEvidence],
) -> Mapping[BaselineKind, ExecutionCostTurnover]:
    """Weight only execution evidence recorded for every PIT constituent."""

    expected = frozenset({BaselineKind.FULL_ADAPTIVE, BaselineKind.BUY_AND_HOLD})
    if any(frozenset(evidence.execution_evidence) != expected for evidence in member_evidence.values()):
        return {}
    return {
        kind: ExecutionCostTurnover(
            total_cost=sum(
                member.weight * member_evidence[member.stock_code]
                .execution_evidence[kind].total_cost
                for member in basket.members
            ),
            turnover=sum(
                member.weight * member_evidence[member.stock_code]
                .execution_evidence[kind].turnover
                for member in basket.members
            ),
        )
        for kind in expected
    }


def aggregate_bluechip_paths(basket: BlueChipBasket, paths: Mapping[str, Sequence[StitchedNavPoint]]) -> BlueChipPath:
    """Date-align all PIT members and aggregate their disclosed weights."""
    expected={member.stock_code for member in basket.members}
    if set(paths)!=expected: raise ValueError("paths must exactly cover basket members")
    reference=None
    for code in expected:
        boundaries=tuple((point.window_id, point.nav_date) for point in paths[code])
        if not boundaries: raise ValueError("member path must not be empty")
        if reference is None: reference=boundaries
        elif boundaries!=reference: raise ValueError("member window boundaries must be aligned")
    nav=tuple(sum(member.weight*paths[member.stock_code][index].nav_total for member in basket.members) for index in range(len(reference)))
    contribution={member.stock_code: member.weight*(paths[member.stock_code][-1].nav_total-1.0) for member in basket.members}
    return BlueChipPath(
        tuple(
            StitchedNavPoint(
                paths[next(iter(expected))][index].window_id,
                paths[next(iter(expected))][index].nav_date,
                nav[index],
            )
            for index in range(len(reference))
        ),
        contribution,
    )

__all__ = [
    "BlueChipBasketEvidence",
    "BlueChipPath",
    "aggregate_bluechip_paths",
    "run_bluechip_basket_walk_forward",
]
