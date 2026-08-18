from dataclasses import FrozenInstanceError
from datetime import date
from contextlib import contextmanager
from functools import partial

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
)


TARGET = date(2026, 8, 18)


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
        source_reference="xtdata.get_etf_info",
    )


def test_explicit_provider_provenance_is_immutable_and_auditable() -> None:
    provenance = ProviderProvenance(
        provider_reported_date=TARGET,
        weight_unit="percent",
        source_reference="akshare:fund_portfolio_hold_em:2026Q3",
    )

    with pytest.raises(FrozenInstanceError):
        provenance.source_reference = "changed"


def test_miniqmt_never_manufactures_weight_from_redemption_component_codes() -> None:
    class Client:
        def download_etf_info(self) -> None:
            pass

        def get_etf_info(self):
            return {
                "510300.SH": {
                    "source_as_of_date": "2026-08-18",
                    "weight_unit": "percent",
                    "成份股信息": [{"成份股代码": "600000.SH"}],
                }
            }

    result = MiniQMTETFProvider(client=Client()).load(TARGET)

    assert not result.available
    assert result.baskets == {}
    assert result.quality_issue is not None
    assert result.quality_issue.code == "missing_constituent_weight"


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
        (
            {"source_as_of_date": "2026-08-17", "weight_unit": "percent", "成份股信息": [{"成份股代码": "600000", "权重": 100}]},
            "source_date_mismatch",
        ),
    ],
)
def test_miniqmt_requires_source_date_unit_and_exact_target_date(record, reason) -> None:
    class Client:
        def download_etf_info(self) -> None:
            pass

        def get_etf_info(self):
            return {"510300.SH": record}

    result = MiniQMTETFProvider(client=Client()).load(TARGET)

    assert not result.available
    assert result.quality_issue is not None
    assert result.quality_issue.code == reason


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


@pytest.mark.parametrize(
    ("source_date", "unit", "reason"),
    [
        (None, "percent", "missing_source_date"),
        (date(2026, 8, 17), "percent", "source_date_mismatch"),
        (TARGET, None, "missing_weight_unit"),
        (TARGET, "inferred", "invalid_weight_unit"),
    ],
)
def test_akshare_blocks_undated_stale_or_unit_inferred_holdings(source_date, unit, reason) -> None:
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
