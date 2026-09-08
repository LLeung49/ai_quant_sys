"""Aggregation of independently executed PIT blue-chip constituent paths."""
from __future__ import annotations
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from .bluechip_basket import BlueChipBasket
from .execution_evidence import StitchedNavPoint

@dataclass(frozen=True)
class BlueChipPath:
    nav: tuple[float, ...]
    member_contribution: Mapping[str, float]

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

__all__=["BlueChipPath","aggregate_bluechip_paths"]
