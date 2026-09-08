from datetime import date
from decimal import Decimal

import pytest

from asset_allocation.etf_adaptive.research.baselines import BaselineKind
from asset_allocation.etf_adaptive.research.bluechip_basket import BlueChipBasket, BlueChipConstituent
from asset_allocation.etf_adaptive.research.bluechip_execution import (
    aggregate_bluechip_paths,
    run_bluechip_basket_walk_forward,
)
from asset_allocation.etf_adaptive.research.execution_evidence import (
    StitchedNavPoint,
    TargetEvidence,
)


def test_aggregate_bluechip_paths_uses_disclosed_member_weights() -> None:
    basket = BlueChipBasket("H30269.CSI", date(2024, 1, 2), (BlueChipConstituent("600900.SH", .6, "a" * 64), BlueChipConstituent("601088.SH", .4, "b" * 64)))
    paths = {
        "600900.SH": (StitchedNavPoint("wf_000", date(2024,1,2),1.0), StitchedNavPoint("wf_000", date(2024,1,3),1.2)),
        "601088.SH": (StitchedNavPoint("wf_000", date(2024,1,2),1.0), StitchedNavPoint("wf_000", date(2024,1,3),0.9)),
    }
    result = aggregate_bluechip_paths(basket, paths)
    assert result.nav == (1.0, 1.08)
    assert result.member_contribution == {
        "600900.SH": pytest.approx(0.12),
        "601088.SH": pytest.approx(-0.04),
    }


def test_run_bluechip_basket_walk_forward_executes_every_pit_member_without_substitution() -> None:
    basket = BlueChipBasket(
        "H30269.CSI",
        date(2024, 1, 2),
        (
            BlueChipConstituent("600900.SH", 0.6, "a" * 64),
            BlueChipConstituent("601088.SH", 0.4, "b" * 64),
        ),
    )
    calls: list[str] = []

    def runner(entry: object, _provider: object, _config: object) -> TargetEvidence:
        calls.append(entry.primary_code)  # type: ignore[union-attr]
        end_nav = 1.2 if entry.primary_code == "600900.SH" else 0.9  # type: ignore[union-attr]
        paths = {
            kind: (
                StitchedNavPoint("wf_000", date(2024, 1, 2), 1.0),
                StitchedNavPoint("wf_000", date(2024, 1, 3), end_nav),
            )
            for kind in BaselineKind
        }
        return TargetEvidence(entry, Decimal("100000"), {}, paths)  # type: ignore[arg-type]

    result = run_bluechip_basket_walk_forward(
        basket,
        provider=object(),
        config=object(),
        target_runner=runner,
    )

    assert calls == ["600900.SH", "601088.SH"]
    assert set(result.member_evidence) == {"600900.SH", "601088.SH"}
    assert result.paths[BaselineKind.FULL_ADAPTIVE].nav[-1] == pytest.approx(1.08)


def test_aggregate_bluechip_paths_rejects_missing_or_misaligned_members() -> None:
    basket = BlueChipBasket(
        "H30269.CSI",
        date(2024, 1, 2),
        (
            BlueChipConstituent("600900.SH", 0.6, "a" * 64),
            BlueChipConstituent("601088.SH", 0.4, "b" * 64),
        ),
    )
    first = (StitchedNavPoint("wf_000", date(2024, 1, 2), 1.0),)
    with pytest.raises(ValueError, match="exactly cover"):
        aggregate_bluechip_paths(basket, {"600900.SH": first})
    with pytest.raises(ValueError, match="aligned"):
        aggregate_bluechip_paths(
            basket,
            {
                "600900.SH": first,
                "601088.SH": (StitchedNavPoint("wf_000", date(2024, 1, 3), 1.0),),
            },
        )
