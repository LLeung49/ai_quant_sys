from dataclasses import FrozenInstanceError
from datetime import date
from contextlib import contextmanager
from functools import partial
import builtins

import pytest

from morning_conference.sector_rotation2.research.etf_core.exposure import ExposureAssessment
from morning_conference.sector_rotation2.research.etf_core.mapping import persist_exposure_assessment
from morning_conference.sector_rotation2.research.etf_core.providers import (
    AKShareETFProvider,
    ETFBasketInput,
    LocalSWMembershipProvider,
    MiniQMTETFProvider,
    ProviderProvenance,
    ProviderQualityIssue,
    SWMembershipInput,
    refresh_sector_etf_mapping,
    select_freshest_basket,
)


TARGET = date(2026, 8, 18)


def _basket(
    *,
    provider: str,
    reported_date: date,
    stock_code: str = "600000.SH",
    weight: float = 100.0,
) -> ETFBasketInput:
    return ETFBasketInput(
        baskets={"510300.SH": ({"stock_code": stock_code, "weight": weight},)},
        as_of_date=reported_date,
        weight_unit="percent",
        source_provider=provider,
        source_reference=f"{provider}:{reported_date.isoformat()}",
        basket_source_priority=(
            "miniqmt_exact" if provider == "miniqmt" else "akshare_disclosed"
        ),
    )


def test_newer_complete_miniqmt_basket_wins_over_akshare() -> None:
    result = select_freshest_basket(
        _basket(provider="miniqmt", reported_date=date(2026, 6, 30)),
        _basket(provider="akshare", reported_date=date(2026, 3, 31)),
        TARGET,
    )

    assert result.source_provider == "miniqmt"
    assert result.basket_source_priority == "miniqmt_exact"


def test_newer_akshare_disclosure_wins_over_older_complete_miniqmt() -> None:
    result = select_freshest_basket(
        _basket(provider="miniqmt", reported_date=date(2026, 3, 31)),
        _basket(provider="akshare", reported_date=date(2026, 6, 30)),
        TARGET,
    )

    assert result.source_provider == "akshare"
    assert result.as_of_date == date(2026, 6, 30)


def test_miniqmt_exact_wins_when_complete_sources_have_the_same_reported_date() -> None:
    reported_date = date(2026, 6, 30)

    result = select_freshest_basket(
        _basket(provider="miniqmt", reported_date=reported_date),
        _basket(provider="akshare", reported_date=reported_date),
        TARGET,
    )

    assert result.source_provider == "miniqmt"
    assert result.basket_source_priority == "miniqmt_exact"


def test_newer_partial_source_cannot_displace_older_complete_source() -> None:
    result = select_freshest_basket(
        _basket(
            provider="miniqmt",
            reported_date=date(2026, 6, 30),
            weight=79.0,
        ),
        _basket(provider="akshare", reported_date=date(2026, 3, 31)),
        TARGET,
        min_coverage=0.8,
    )

    assert result.source_provider == "akshare"
    assert result.as_of_date == date(2026, 3, 31)


def test_source_with_any_undercovered_etf_basket_is_not_complete() -> None:
    partial_miniqmt = ETFBasketInput(
        baskets={
            "510300.SH": ({"stock_code": "600000", "weight": 100.0},),
            "510500.SH": ({"stock_code": "000001", "weight": 79.0},),
        },
        as_of_date=date(2026, 6, 30),
        weight_unit="percent",
        source_provider="miniqmt",
        source_reference="miniqmt:2026Q2",
        basket_source_priority="miniqmt_exact",
    )
    complete_akshare = _basket(
        provider="akshare",
        reported_date=date(2026, 3, 31),
    )

    result = select_freshest_basket(
        partial_miniqmt,
        complete_akshare,
        TARGET,
        min_coverage=0.8,
    )

    assert result.source_provider == "akshare"


def test_cross_check_compares_miniqmt_with_akshare_when_miniqmt_is_selected() -> None:
    result = select_freshest_basket(
        _basket(
            provider="miniqmt",
            reported_date=date(2026, 6, 30),
            stock_code="600000",
        ),
        _basket(
            provider="akshare",
            reported_date=date(2026, 3, 31),
            stock_code="000001",
        ),
        TARGET,
    )

    assert result.source_provider == "miniqmt"
    assert result.cross_check_status == "mismatch"
    assert "constituent_mismatch=1" in (result.cross_check_detail or "")


def test_code_only_miniqmt_is_cross_check_not_weight_source() -> None:
    miniqmt_codes = ETFBasketInput.unavailable(
        source_provider="miniqmt",
        issue=ProviderQualityIssue("missing_constituent_weight", "codes only"),
        etf_codes=("510300.SH",),
        constituent_codes={"510300.SH": ("600000.SH", "000001.SZ")},
    )
    akshare = _basket(
        provider="akshare", reported_date=date(2026, 6, 30), stock_code="600000"
    )

    result = select_freshest_basket(miniqmt_codes, akshare, TARGET)

    assert result.source_provider == "akshare"
    assert result.baskets == akshare.baskets
    assert result.cross_check_status == "mismatch"
    assert "510300" in (result.cross_check_detail or "")


def test_cross_check_compares_miniqmt_and_akshare_universes_symmetrically() -> None:
    miniqmt_codes = ETFBasketInput.unavailable(
        source_provider="miniqmt",
        issue=ProviderQualityIssue("missing_constituent_weight", "codes only"),
        etf_codes=("510300", "510500"),
        constituent_codes={
            "510300": ("600000",),
            "510500": ("000001",),
        },
    )
    akshare = ETFBasketInput(
        baskets={
            "510300": ({"stock_code": "600000", "weight": 50.0},),
            "159995": ({"stock_code": "002371", "weight": 50.0},),
        },
        as_of_date=date(2026, 6, 30),
        weight_unit="percent",
        source_provider="akshare",
        source_reference="akshare:2026Q2",
        basket_source_priority="akshare_disclosed",
    )

    result = select_freshest_basket(miniqmt_codes, akshare, TARGET)

    assert result.cross_check_status == "mismatch"
    assert "miniqmt_only=1" in (result.cross_check_detail or "")
    assert "akshare_only=1" in (result.cross_check_detail or "")
    assert "constituent_mismatch=0" in (result.cross_check_detail or "")
    assert "miniqmt_only:510500" in (result.cross_check_detail or "")
    assert "akshare_only:159995" in (result.cross_check_detail or "")


def test_cross_check_detail_is_bounded_and_deterministic_for_large_mismatch() -> None:
    mini_codes = {
        f"{510000 + index:06d}": ("600000",)
        for index in range(200)
    }
    akshare_baskets = {
        f"{159000 + index:06d}": ({"stock_code": "000001", "weight": 0.5},)
        for index in range(200)
    }
    miniqmt = ETFBasketInput.unavailable(
        source_provider="miniqmt",
        issue=ProviderQualityIssue("missing_constituent_weight", "codes only"),
        etf_codes=tuple(mini_codes),
        constituent_codes=mini_codes,
    )
    akshare = ETFBasketInput(
        baskets=akshare_baskets,
        as_of_date=date(2026, 6, 30),
        weight_unit="percent",
        source_provider="akshare",
        source_reference="akshare:2026Q2",
        basket_source_priority="akshare_disclosed",
    )

    first = select_freshest_basket(miniqmt, akshare, TARGET)
    second = select_freshest_basket(miniqmt, akshare, TARGET)

    assert first.cross_check_detail == second.cross_check_detail
    assert first.cross_check_detail is not None
    assert len(first.cross_check_detail) < 1024
    assert "miniqmt_only=200" in first.cross_check_detail
    assert "akshare_only=200" in first.cross_check_detail
    assert "sha256=" in first.cross_check_detail
    assert "sample=" in first.cross_check_detail


def test_local_sw_provider_reads_trade_stock_status_current_mapping() -> None:
    captured: dict[str, object] = {}

    def query(sql: str, params: tuple[object, ...]):
        captured.update(sql=sql, params=params)
        return [{"stock_code": "600000.SH"}, {"stock_code": "000001.SZ"}]

    result = LocalSWMembershipProvider(query=query, current_date=lambda: TARGET).load(
        sector_name="银行", sector_level=2, target_date=TARGET,
    )

    assert result == SWMembershipInput(
        sector_name="银行",
        sector_level=2,
        member_codes=("600000.SH", "000001.SZ"),
        as_of_date=TARGET,
        asof_mode="current_mapping",
        source_provider="trade_stock_status",
    )
    assert "FROM trade_stock_status" in str(captured["sql"])
    assert "sector_2 = %s" in str(captured["sql"])
    assert captured["params"] == ("银行",)


def test_local_sw_provider_rejects_historical_target_for_current_mapping() -> None:
    result = LocalSWMembershipProvider(
        query=lambda *_: pytest.fail("historical current mapping must not be queried"),
        current_date=lambda: TARGET,
    ).load("银行", 2, date(2026, 8, 17))

    assert not result.available
    assert result.quality_issue == ProviderQualityIssue(
        code="membership_date_mismatch",
        detail="trade_stock_status current_mapping is dated 2026-08-18, target is 2026-08-17",
    )


def test_miniqmt_import_error_becomes_unavailable_and_auto_falls_back_to_akshare(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    real_import = builtins.__import__

    def fail_xtquant_import(name, *args, **kwargs):
        if name == "xtquant":
            raise ModuleNotFoundError("No module named 'xtquant'")
        return real_import(name, *args, **kwargs)

    monkeypatch.setattr(builtins, "__import__", fail_xtquant_import)

    miniqmt = MiniQMTETFProvider().load(TARGET)
    result = select_freshest_basket(
        miniqmt,
        _basket(provider="akshare", reported_date=date(2026, 6, 30)),
        TARGET,
    )

    assert miniqmt.quality_issue is not None
    assert miniqmt.quality_issue.code == "provider_error"
    assert result.source_provider == "akshare"


def test_miniqmt_provider_call_error_becomes_unavailable_and_auto_falls_back() -> None:
    class Client:
        def download_etf_info(self) -> None:
            raise RuntimeError("MiniQMT terminal is offline")

    miniqmt = MiniQMTETFProvider(client=Client()).load(TARGET)
    result = select_freshest_basket(
        miniqmt,
        _basket(provider="akshare", reported_date=date(2026, 6, 30)),
        TARGET,
    )

    assert miniqmt.quality_issue == ProviderQualityIssue(
        "provider_error",
        "MiniQMT terminal is offline",
    )
    assert result.source_provider == "akshare"


def test_miniqmt_extracts_complete_weighted_baskets_after_downloading_redemption_list() -> None:
    class Client:
        downloaded = False

        def download_etf_info(self) -> None:
            self.downloaded = True

        def get_etf_info(self):
            assert self.downloaded
            return {
                "510300.SH": {
                    "source_as_of_date": "2026-08-18",
                    "weight_unit": "percent",
                    "source_reference": "miniqmt:weighted-basket:2026-08-18",
                    "成份股信息": [
                        {"成份股代码": "600000.SH", "权重": 60.0},
                        {"成份股代码": "000001.SZ", "权重": 40.0},
                    ],
                }
            }

    result = MiniQMTETFProvider(client=Client()).load(TARGET)

    assert result == ETFBasketInput(
        baskets={
            "510300.SH": (
                {"stock_code": "600000.SH", "weight": 60.0},
                {"stock_code": "000001.SZ", "weight": 40.0},
            )
        },
        as_of_date=TARGET,
        weight_unit="percent",
        source_provider="miniqmt",
        source_reference="miniqmt:weighted-basket:2026-08-18",
        basket_source_priority="miniqmt_exact",
        etf_codes=("510300.SH",),
        constituent_codes={"510300.SH": ("600000.SH", "000001.SZ")},
    )


def test_explicit_provider_provenance_is_immutable_and_auditable() -> None:
    provenance = ProviderProvenance(
        provider_reported_date=TARGET,
        weight_unit="percent",
        source_reference="akshare:fund_portfolio_hold_em:2026Q3",
    )

    with pytest.raises(FrozenInstanceError):
        provenance.source_reference = "changed"


def test_miniqmt_exact_basket_requires_explicit_source_reference() -> None:
    class Client:
        def download_etf_info(self) -> None:
            pass

        def get_etf_info(self):
            return {
                "510300.SH": {
                    "source_as_of_date": "2026-08-18",
                    "weight_unit": "percent",
                    "成份股信息": [{"成份股代码": "600000", "权重": 100}],
                }
            }

    result = MiniQMTETFProvider(client=Client()).load(TARGET)

    assert not result.available
    assert result.quality_issue is not None
    assert result.quality_issue.code == "missing_source_reference"


def test_miniqmt_never_manufactures_weight_from_redemption_component_codes() -> None:
    class Client:
        def download_etf_info(self) -> None:
            pass

        def get_etf_info(self):
            return {
                "510300.SH": {
                    "source_as_of_date": "2026-08-18",
                    "weight_unit": "percent",
                    "source_reference": "miniqmt:code-only:2026-08-18",
                    "成份股信息": [{"成份股代码": "600000.SH"}],
                }
            }

    result = MiniQMTETFProvider(client=Client()).load(TARGET)

    assert not result.available
    assert result.baskets == {}
    assert result.quality_issue is not None
    assert result.quality_issue.code == "missing_constituent_weight"


def test_miniqmt_retains_code_only_components_even_without_weight_provenance() -> None:
    class Client:
        def download_etf_info(self) -> None:
            pass

        def get_etf_info(self):
            return {
                "510300.SH": {
                    "成份股信息": [
                        {"成份股代码": "600000.SH"},
                        {"成份股代码": "000001.SZ"},
                    ],
                }
            }

    result = MiniQMTETFProvider(client=Client()).load(TARGET)

    assert not result.available
    assert result.baskets == {}
    assert result.etf_codes == ("510300.SH",)
    assert result.constituent_codes == {
        "510300.SH": ("600000.SH", "000001.SZ"),
    }


@pytest.mark.parametrize(
    ("record", "reason"),
    [
        (
            {"weight_unit": "percent", "成份股信息": [{"成份股代码": "600000", "权重": 100}]},
            "missing_source_date",
        ),
        (
            {"source_as_of_date": "2026-08-18", "成份股信息": [{"成份股代码": "600000", "权重": 100}]},
            "missing_weight_unit",
        ),
    ],
)
def test_miniqmt_requires_source_date_and_unit(record, reason) -> None:
    class Client:
        def download_etf_info(self) -> None:
            pass

        def get_etf_info(self):
            return {"510300.SH": record}

    result = MiniQMTETFProvider(client=Client()).load(TARGET)

    assert not result.available
    assert result.quality_issue is not None
    assert result.quality_issue.code == reason


def test_miniqmt_accepts_an_older_explicit_report_date() -> None:
    class Client:
        def download_etf_info(self) -> None:
            pass

        def get_etf_info(self):
            return {
                "510300.SH": {
                    "source_as_of_date": "2026-08-17",
                    "weight_unit": "percent",
                    "source_reference": "miniqmt:weighted-basket:2026-08-17",
                    "成份股信息": [{"成份股代码": "600000", "权重": 100}],
                }
            }

    result = MiniQMTETFProvider(client=Client()).load(TARGET)

    assert result.available
    assert result.as_of_date == date(2026, 8, 17)


def test_akshare_parses_injected_dataframe_only_with_auditable_provenance() -> None:
    class Frame:
        def to_dict(self, orient: str):
            assert orient == "records"
            return [
                {"基金代码": "510300.SH", "股票代码": "600000.SH", "持仓占比": 55.0},
                {"基金代码": "510300.SH", "股票代码": "000001.SZ", "持仓占比": 45.0},
            ]

    result = AKShareETFProvider(
        dataframe=Frame(),
        provenance=ProviderProvenance(
            provider_reported_date=TARGET,
            weight_unit="percent",
            source_reference="akshare:fund_portfolio_hold_em:2026Q3",
        ),
    ).load(TARGET)

    assert result.available
    assert result.as_of_date == TARGET
    assert result.weight_unit == "percent"
    assert result.source_reference == "akshare:fund_portfolio_hold_em:2026Q3"
    assert result.baskets["510300.SH"][0] == {"stock_code": "600000.SH", "weight": 55.0}


def test_akshare_lazily_loads_etf_universe_and_preserves_latest_disclosed_quarter() -> None:
    class Client:
        universe_calls = 0
        holding_calls: list[tuple[str, str]] = []

        def fund_etf_spot_em(self):
            self.universe_calls += 1
            return [{"代码": "510300"}, {"代码": "159995"}]

        def fund_portfolio_hold_em(self, *, symbol: str, date: str):
            self.holding_calls.append((symbol, date))
            return [
                {"股票代码": "600000", "占净值比例": 45.0, "季度": "2026年2季度股票投资明细"},
                {"股票代码": "000001", "占净值比例": 40.0, "季度": "2026年2季度股票投资明细"},
                {"股票代码": "600519", "占净值比例": 35.0, "季度": "2026年1季度股票投资明细"},
            ]

    client = Client()
    provider = AKShareETFProvider(client=client)
    assert client.universe_calls == 0

    result = provider.load(TARGET)

    assert client.universe_calls == 1
    assert client.holding_calls == [("510300", "2026"), ("159995", "2026")]
    assert result.available
    assert result.as_of_date == date(2026, 6, 30)
    assert result.basket_source_priority == "akshare_disclosed"
    assert result.source_reference == "akshare:fund_portfolio_hold_em:2026Q2"
    assert result.baskets["510300"] == (
        {"stock_code": "600000", "weight": 45.0},
        {"stock_code": "000001", "weight": 40.0},
    )


@pytest.mark.parametrize(
    ("source_date", "unit", "reason"),
    [
        (None, "percent", "missing_source_date"),
        (date(2026, 8, 19), "percent", "future_source_date"),
        (TARGET, None, "missing_weight_unit"),
        (TARGET, "inferred", "invalid_weight_unit"),
    ],
)
def test_akshare_blocks_undated_future_or_unit_inferred_holdings(source_date, unit, reason) -> None:
    result = AKShareETFProvider(
        dataframe=[{"etf_code": "510300", "stock_code": "600000", "weight": 100}],
        provenance=None if source_date is None and unit == "percent" else ProviderProvenance(
            provider_reported_date=source_date,
            weight_unit=unit,
            source_reference="akshare:test-fixture",
        ),
    ).load(TARGET)

    assert not result.available
    assert result.quality_issue is not None
    assert result.quality_issue.code == reason


def test_akshare_missing_metadata_is_a_structured_result_not_constructor_error() -> None:
    result = AKShareETFProvider(dataframe=[]).load(TARGET)

    assert not result.available
    assert result.quality_issue is not None
    assert result.quality_issue.code == "missing_source_date"


@pytest.mark.parametrize("provider", [AKShareETFProvider, MiniQMTETFProvider])
def test_adapters_reject_raw_caller_date_and_unit_overrides(provider) -> None:
    with pytest.raises(TypeError):
        provider(declared_source_date=TARGET, weight_unit="percent")


def test_explicit_provenance_requires_a_source_reference() -> None:
    result = AKShareETFProvider(
        dataframe=[{"etf_code": "510300", "stock_code": "600000", "weight": 100}],
        provenance=ProviderProvenance(TARGET, "percent", None),
    ).load(TARGET)

    assert not result.available
    assert result.quality_issue is not None
    assert result.quality_issue.code == "missing_source_reference"


@pytest.mark.parametrize(
    ("changed_field", "changed_value", "reason"),
    [
        ("source_as_of_date", "2026-08-17", "inconsistent_provider_reported_date"),
        ("weight_unit", "decimal", "inconsistent_weight_unit"),
        ("source_reference", "akshare:second", "inconsistent_source_reference"),
    ],
)
def test_akshare_rejects_mixed_row_provenance_and_preserves_first_reference(
    changed_field,
    changed_value,
    reason,
) -> None:
    first = {
        "etf_code": "510300", "stock_code": "600000", "weight": 60,
        "source_as_of_date": "2026-08-18", "weight_unit": "percent",
        "source_reference": "akshare:first",
    }
    second = {
        "etf_code": "510300", "stock_code": "000001", "weight": 40,
        "source_as_of_date": "2026-08-18", "weight_unit": "percent",
        "source_reference": "akshare:first",
    }
    second[changed_field] = changed_value

    result = AKShareETFProvider(dataframe=[first, second]).load(TARGET)

    assert not result.available
    assert result.quality_issue is not None
    assert result.quality_issue.code == reason
    assert result.source_reference == "akshare:first"


def test_akshare_preserves_known_source_reference_on_component_parse_failure() -> None:
    result = AKShareETFProvider(
        dataframe=[{"etf_code": "510300", "stock_code": "600000"}],
        provenance=ProviderProvenance(TARGET, "percent", "akshare:audited"),
    ).load(TARGET)

    assert not result.available
    assert result.quality_issue is not None
    assert result.quality_issue.code == "missing_constituent_weight"
    assert result.source_reference == "akshare:audited"


@pytest.mark.parametrize("bad_weight", [-1, float("nan"), float("inf")])
def test_miniqmt_rejects_non_finite_or_negative_component_weights(bad_weight) -> None:
    class Client:
        def download_etf_info(self) -> None:
            pass

        def get_etf_info(self):
            return {
                "510300.SH": {
                    "source_as_of_date": "2026-08-18",
                    "weight_unit": "decimal",
                    "source_reference": "miniqmt:weighted-basket:2026-08-18",
                    "成份股信息": [{"成份股代码": "600000", "权重": bad_weight}],
                }
            }

    result = MiniQMTETFProvider(client=Client()).load(TARGET)

    assert not result.available
    assert result.quality_issue is not None
    assert result.quality_issue.code == "invalid_constituent_weight"


def test_refresh_assesses_complete_inputs_and_persists_assessment() -> None:
    membership = SWMembershipInput(
        sector_name="银行", sector_level=2, member_codes=("600000",),
        as_of_date=TARGET, asof_mode="current_mapping", source_provider="trade_stock_status",
    )
    baskets = ETFBasketInput(
        baskets={"510300.SH": ({"stock_code": "600000", "weight": 1.0},)},
        as_of_date=TARGET, weight_unit="decimal", source_provider="miniqmt",
        source_reference="xtdata.get_etf_info",
        basket_source_priority="miniqmt_exact",
        cross_check_status="matched",
        cross_check_detail="1 MiniQMT basket matched the selected weighted source",
    )
    captured: dict[str, object] = {}

    result = refresh_sector_etf_mapping(
        sector_name="银行", sector_level=2, target_date=TARGET,
        membership_provider=lambda *_: membership,
        basket_provider=lambda *_: baskets,
        min_coverage=0.8, mapping_version="exposure_v1", config_hash="cfg",
        persist=lambda **kwargs: captured.update(kwargs) or 1,
    )

    assert result.persisted_rows == 1
    assert result.quality_issue is None
    assessment = captured["assessment"]
    assert isinstance(assessment, ExposureAssessment)
    assert [item.etf_code for item in assessment.eligible] == ["510300.SH"]
    assert captured["membership_as_of_date"] == TARGET
    assert captured["constituent_as_of_date"] == TARGET
    assert captured["source_reference"] == "xtdata.get_etf_info"
    assert captured["constituent_reported_date"] == TARGET
    assert captured["basket_source_priority"] == "miniqmt_exact"
    assert captured["cross_check_status"] == "matched"
    assert captured["cross_check_detail"] == "1 MiniQMT basket matched the selected weighted source"


def test_refresh_persists_stale_complete_basket_as_a_qualified_mapping() -> None:
    reported_date = date(2026, 2, 17)
    membership = SWMembershipInput(
        sector_name="閾惰", sector_level=2, member_codes=("600000",),
        as_of_date=TARGET, asof_mode="current_mapping", source_provider="trade_stock_status",
    )
    baskets = ETFBasketInput(
        baskets={"510300.SH": ({"stock_code": "600000", "weight": 1.0},)},
        as_of_date=reported_date, weight_unit="decimal", source_provider="akshare",
        source_reference="akshare:fund_portfolio_hold_em:2026Q1",
        basket_source_priority="akshare_disclosed",
    )
    commands: list[tuple[str, object]] = []

    class Transaction:
        def execute(self, sql: str, params: tuple[object, ...]) -> int:
            commands.append((sql, params))
            return 1

        def execute_many(self, sql: str, rows: list[tuple[object, ...]]) -> int:
            commands.append((sql, rows))
            return len(rows)

    @contextmanager
    def transaction():
        yield Transaction()

    result = refresh_sector_etf_mapping(
        sector_name="閾惰", sector_level=2, target_date=TARGET,
        membership_provider=lambda *_: membership,
        basket_provider=lambda *_: baskets,
        min_coverage=0.8, mapping_version="exposure_v1", config_hash="cfg",
        persist=partial(
            persist_exposure_assessment,
            transaction=transaction,
            ensure_schema=lambda: None,
        ),
    )

    assert result.quality_issue is None
    assert [item.etf_code for item in result.assessment.eligible] == ["510300.SH"]
    row = commands[2][1][0]
    assert row[18] == "qualified"
    assert row[22] == reported_date
    assert row[23] == (TARGET - reported_date).days
    assert row[24] == "stale"
    assert row[26] == "akshare_disclosed"


def test_refresh_persists_quality_failure_only_when_provider_is_unavailable() -> None:
    issue = ProviderQualityIssue("missing_constituent_weight", "510300.SH has no recognized weight")
    membership = SWMembershipInput(
        sector_name="银行", sector_level=2, member_codes=("600000",),
        as_of_date=TARGET, asof_mode="current_mapping", source_provider="trade_stock_status",
    )
    unavailable = ETFBasketInput.unavailable(source_provider="miniqmt", issue=issue)
    captured: dict[str, object] = {}

    result = refresh_sector_etf_mapping(
        sector_name="银行", sector_level=2, target_date=TARGET,
        membership_provider=lambda *_: membership,
        basket_provider=lambda *_: unavailable,
        min_coverage=0.8, mapping_version="exposure_v1", config_hash="cfg",
        persist=lambda **kwargs: captured.update(kwargs) or 1,
    )

    assert result.persisted_rows == 1
    assert result.quality_issue == issue
    assert captured["assessment"] == ExposureAssessment(eligible=[], rejected=[])
    assert captured["quality_failure_reason"] == "missing_constituent_weight: 510300.SH has no recognized weight"
    assert captured["source_as_of_date"] is None
    assert captured["weight_unit"] is None


def test_refresh_never_persists_a_future_reported_date() -> None:
    issue = ProviderQualityIssue("future_source_date", "reported after target")
    membership = SWMembershipInput(
        sector_name="Bank",
        sector_level=2,
        member_codes=("600000",),
        as_of_date=TARGET,
    )
    unavailable = ETFBasketInput.unavailable(
        source_provider="akshare",
        issue=issue,
        as_of_date=date(2026, 8, 19),
        weight_unit="percent",
        source_reference="akshare:future",
    )
    captured: dict[str, object] = {}

    result = refresh_sector_etf_mapping(
        sector_name="Bank",
        sector_level=2,
        target_date=TARGET,
        membership_provider=lambda *_: membership,
        basket_provider=lambda *_: unavailable,
        min_coverage=0.8,
        mapping_version="exposure_v1",
        config_hash="cfg",
        persist=lambda **kwargs: captured.update(kwargs) or 1,
    )

    assert result.quality_issue == issue
    assert captured["constituent_reported_date"] is None


def test_custom_basket_without_source_reference_never_becomes_qualified() -> None:
    membership = SWMembershipInput(
        sector_name="银行", sector_level=2, member_codes=("600000",),
        as_of_date=TARGET, asof_mode="current_mapping", source_provider="trade_stock_status",
    )
    untraceable = ETFBasketInput(
        baskets={"510300.SH": ({"stock_code": "600000", "weight": 1.0},)},
        as_of_date=TARGET,
        weight_unit="decimal",
        source_provider="custom",
        source_reference=None,
    )
    captured: dict[str, object] = {}

    assert not untraceable.available
    result = refresh_sector_etf_mapping(
        sector_name="银行", sector_level=2, target_date=TARGET,
        membership_provider=lambda *_: membership,
        basket_provider=lambda *_: untraceable,
        min_coverage=0.8, mapping_version="exposure_v1", config_hash="cfg",
        persist=lambda **kwargs: captured.update(kwargs) or 1,
    )

    assert result.quality_issue is not None
    assert result.quality_issue.code == "missing_source_reference"
    assert captured["assessment"] == ExposureAssessment(eligible=[], rejected=[])
    assert captured["quality_failure_reason"].startswith("missing_source_reference:")


@pytest.mark.parametrize("source_provider", [" ", None])
def test_basket_availability_requires_nonempty_source_provider(source_provider) -> None:
    basket = ETFBasketInput(
        baskets={"510300.SH": ({"stock_code": "600000", "weight": 1.0},)},
        as_of_date=TARGET,
        weight_unit="decimal",
        source_provider=source_provider,
        source_reference="provider:daily",
    )

    assert not basket.available


def test_refresh_real_persistence_keeps_missing_provider_metadata_null_on_failure() -> None:
    commands: list[tuple[str, object]] = []

    class Transaction:
        def execute(self, sql: str, params: tuple[object, ...]) -> int:
            commands.append((sql, params))
            return 1

        def execute_many(self, sql: str, rows: list[tuple[object, ...]]) -> int:
            commands.append((sql, rows))
            return len(rows)

    @contextmanager
    def transaction():
        yield Transaction()

    missing = ETFBasketInput.unavailable(
        source_provider="miniqmt",
        issue=ProviderQualityIssue("missing_source_date", "provider did not declare a date"),
    )
    membership = SWMembershipInput(
        sector_name="银行", sector_level=2, member_codes=("600000",),
        as_of_date=TARGET, asof_mode="current_mapping", source_provider="trade_stock_status",
    )

    result = refresh_sector_etf_mapping(
        sector_name="银行", sector_level=2, target_date=TARGET,
        membership_provider=lambda *_: membership,
        basket_provider=lambda *_: missing,
        min_coverage=0.8, mapping_version="exposure_v1", config_hash="cfg",
        persist=partial(
            persist_exposure_assessment,
            transaction=transaction,
            ensure_schema=lambda: None,
        ),
    )

    assert result.persisted_rows == 1
    failure_row = commands[2][1][0]
    assert failure_row[3] == "exposure_quality_failure"
    assert failure_row[7] is None
    assert failure_row[14] is None
    assert failure_row[17] is None
    assert failure_row[18] == "failed"
    assert failure_row[19] == "missing_source_date: provider did not declare a date"
