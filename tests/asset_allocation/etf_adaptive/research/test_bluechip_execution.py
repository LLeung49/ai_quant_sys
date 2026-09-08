from datetime import date
from decimal import Decimal

from asset_allocation.etf_adaptive.research.bluechip_basket import BlueChipBasket, BlueChipConstituent
from asset_allocation.etf_adaptive.research.bluechip_execution import aggregate_bluechip_paths
from asset_allocation.etf_adaptive.research.execution_evidence import StitchedNavPoint


def test_aggregate_bluechip_paths_uses_disclosed_member_weights() -> None:
    basket = BlueChipBasket("H30269.CSI", date(2024, 1, 2), (BlueChipConstituent("600900.SH", .6, "a" * 64), BlueChipConstituent("601088.SH", .4, "b" * 64)))
    paths = {
        "600900.SH": (StitchedNavPoint("wf_000", date(2024,1,2),1.0), StitchedNavPoint("wf_000", date(2024,1,3),1.2)),
        "601088.SH": (StitchedNavPoint("wf_000", date(2024,1,2),1.0), StitchedNavPoint("wf_000", date(2024,1,3),0.9)),
    }
    result = aggregate_bluechip_paths(basket, paths)
    assert result.nav == (1.0, 1.08)
    assert result.member_contribution == {"600900.SH": 0.12, "601088.SH": -0.04}
