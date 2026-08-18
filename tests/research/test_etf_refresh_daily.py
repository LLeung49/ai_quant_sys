from datetime import date
from pathlib import Path

import pytest

from morning_conference.sector_rotation2.research.etf_core import refresh_daily
from morning_conference.sector_rotation2.research.etf_core.providers import (
    ETFBasketInput,
    LocalSWMembershipProvider,
    SWMembershipInput,
    refresh_sector_etf_mapping,
)


TARGET = date(2026, 8, 18)
FIXTURES = Path(__file__).parent / "fixtures"


def test_refresh_cli_help_is_dedicated_from_candidate_runner() -> None:
    parser = refresh_daily.build_parser()
    args = parser.parse_args([
        "--as-of-date", "2026-08-18",
        "--level", "2",
        "--config-hash", "cfg",
    ])

    assert args.as_of_date == "2026-08-18"
    assert args.provider == "auto"


def test_refresh_cli_main_explicitly_invokes_mapping_refresh_runner() -> None:
    captured: dict[str, object] = {}

    def run_refresh_fn(**kwargs) -> int:
        captured.update(kwargs)
        return 7

    assert refresh_daily.main([
        "--as-of-date", "2026-08-18",
        "--level", "2",
        "--min-coverage", "0.85",
        "--mapping-version", "exposure_v2",
        "--config-hash", "cfg",
        "--basket-json", "audited-baskets.json",
    ], run_refresh_fn=run_refresh_fn) == 0

    assert captured.pop("progress") is print
    assert captured == {
        "target_date": TARGET,
        "sector_level": 2,
        "provider_name": "auto",
        "min_coverage": 0.85,
        "mapping_version": "exposure_v2",
        "config_hash": "cfg",
        "basket_json_path": Path("audited-baskets.json"),
    }


def test_audited_basket_json_produces_a_qualified_mapping() -> None:
    basket_path = FIXTURES / "audited-etf-baskets.json"

    class MembershipProvider:
        def load(self, sector_name: str, sector_level: int, target_date: date) -> SWMembershipInput:
            return SWMembershipInput(
                sector_name=sector_name,
                sector_level=sector_level,
                member_codes=("600000",),
                as_of_date=target_date,
            )

    persisted: list[dict[str, object]] = []

    def refresh_with_capture(**kwargs):
        return refresh_sector_etf_mapping(
            **kwargs,
            persist=lambda **values: persisted.append(values) or len(values["assessment"].eligible),
        )

    count = refresh_daily.run_refresh(
        target_date=TARGET,
        sector_level=2,
        provider_name="miniqmt",
        min_coverage=0.8,
        mapping_version="exposure_v1",
        config_hash="cfg",
        basket_json_path=basket_path,
        query=lambda *_: [{"sector_name": "Bank"}],
        membership_provider=MembershipProvider(),
        ensure_schema=lambda: None,
        refresh=refresh_with_capture,
    )

    assert count == 1
    assert persisted[0]["source_provider"] == "custodian_file"
    assert persisted[0]["source_reference"] == "sha256:immutable-report"
    assert persisted[0]["basket_source_priority"] == "audited_json_override"
    assert persisted[0]["cross_check_status"] == "not_run"
    assert persisted[0]["assessment"].eligible[0].etf_code == "512480.SH"


def test_auto_refresh_selects_periodic_akshare_aging_mapping_and_reports_summary(
    capsys: pytest.CaptureFixture[str],
) -> None:
    class Provider:
        def __init__(self, basket: ETFBasketInput) -> None:
            self.basket = basket
            self.calls = 0

        def load(self, target_date: date) -> ETFBasketInput:
            self.calls += 1
            assert target_date == TARGET
            return self.basket

    miniqmt = Provider(ETFBasketInput(
        baskets={"510300": ({"stock_code": "600000", "weight": 85.0},)},
        as_of_date=date(2026, 6, 30),
        weight_unit="percent",
        source_provider="miniqmt",
        source_reference="miniqmt:2026Q1",
        basket_source_priority="miniqmt_exact",
        constituent_codes={"510300": ("600000",)},
    ))
    akshare = Provider(ETFBasketInput(
        baskets={"510300": ({"stock_code": "600000", "weight": 100.0},)},
        as_of_date=date(2026, 5, 19),
        weight_unit="percent",
        source_provider="akshare",
        source_reference="akshare:fund_portfolio_hold_em:2026Q1",
        basket_source_priority="akshare_disclosed",
    ))
    persisted: list[dict[str, object]] = []

    class MembershipProvider:
        def load(self, sector_name: str, sector_level: int, target_date: date) -> SWMembershipInput:
            return SWMembershipInput(
                sector_name=sector_name,
                sector_level=sector_level,
                member_codes=("600000",),
                as_of_date=target_date,
            )

    def refresh_with_capture(**kwargs):
        return refresh_sector_etf_mapping(
            **kwargs,
            persist=lambda **values: persisted.append(values) or 1,
        )

    count = refresh_daily.run_refresh(
        target_date=TARGET,
        sector_level=2,
        provider_name="auto",
        min_coverage=0.9,
        mapping_version="exposure_v1",
        config_hash="cfg",
        query=lambda *_: [{"sector_name": "Bank"}],
        membership_provider=MembershipProvider(),
        miniqmt_provider=miniqmt,
        akshare_provider=akshare,
        ensure_schema=lambda: None,
        refresh=refresh_with_capture,
    )

    assert count == 1
    assert miniqmt.calls == 1
    assert akshare.calls == 1
    assert persisted[0]["source_provider"] == "akshare"
    assert persisted[0]["constituent_reported_date"] == date(2026, 5, 19)
    assert persisted[0]["basket_source_priority"] == "akshare_disclosed"
    assert persisted[0]["cross_check_status"] == "matched"
    assert capsys.readouterr().out == (
        "2026-08-18: refreshed 1 mapping rows across 1 sectors; "
        "chosen_source=akshare; fresh=0 aging=1 stale=0 quality_failure=0\n"
    )


def test_audited_basket_json_rejects_missing_immutable_provenance() -> None:
    with pytest.raises(ValueError, match="source_reference"):
        refresh_daily.AuditedJSONBasketProvider(
            FIXTURES / "invalid-etf-baskets-missing-reference.json",
        ).load(TARGET)


def test_refresh_summary_counts_persisted_quality_failures(
    capsys: pytest.CaptureFixture[str],
) -> None:
    class MembershipProvider:
        def load(self, sector_name: str, sector_level: int, target_date: date) -> SWMembershipInput:
            return SWMembershipInput(
                sector_name=sector_name,
                sector_level=sector_level,
                member_codes=("600000",),
                as_of_date=target_date,
            )

    class BasketProvider:
        def load(self, target_date: date) -> ETFBasketInput:
            assert target_date == TARGET
            return ETFBasketInput.unavailable(
                source_provider="miniqmt",
                issue=refresh_daily.ProviderQualityIssue("missing_weight", "fixture"),
            )

    count = refresh_daily.run_refresh(
        target_date=TARGET,
        sector_level=2,
        provider_name="miniqmt",
        min_coverage=0.8,
        mapping_version="exposure_v1",
        config_hash="cfg",
        query=lambda *_: [{"sector_name": "Bank"}],
        membership_provider=MembershipProvider(),
        basket_provider=BasketProvider(),
        ensure_schema=lambda: None,
        refresh=lambda **kwargs: refresh_sector_etf_mapping(
            **kwargs,
            persist=lambda **_values: 1,
        ),
    )

    assert count == 1
    assert capsys.readouterr().out == (
        "2026-08-18: refreshed 1 mapping rows across 1 sectors; "
        "chosen_source=miniqmt; fresh=0 aging=0 stale=0 quality_failure=1\n"
    )


def test_run_refresh_enumerates_local_sectors_and_refreshes_each_with_one_basket_load() -> None:
    query_calls: list[tuple[str, tuple[object, ...]]] = []

    def query(sql: str, params: tuple[object, ...]):
        query_calls.append((sql, params))
        return [{"sector_name": "银行"}, {"sector_name": "电子"}]

    class BasketProvider:
        calls = 0

        def load(self, target_date: date) -> ETFBasketInput:
            self.calls += 1
            return ETFBasketInput.unavailable(
                source_provider="miniqmt",
                issue=refresh_daily.ProviderQualityIssue("missing_weight", "fixture"),
            )

    basket_provider = BasketProvider()
    membership_provider = LocalSWMembershipProvider(
        query=lambda *_: [], current_date=lambda: TARGET,
    )
    refreshed: list[dict[str, object]] = []

    count = refresh_daily.run_refresh(
        target_date=TARGET,
        sector_level=2,
        provider_name="miniqmt",
        min_coverage=0.8,
        mapping_version="exposure_v1",
        config_hash="cfg",
        query=query,
        membership_provider=membership_provider,
        basket_provider=basket_provider,
        ensure_schema=lambda: None,
        refresh=lambda **kwargs: refreshed.append(kwargs) or type("R", (), {"persisted_rows": 1})(),
    )

    assert count == 2
    assert [call["sector_name"] for call in refreshed] == ["银行", "电子"]
    assert basket_provider.calls == 1
    assert all(call["membership_provider"] is membership_provider for call in refreshed)
    assert all(call["basket_provider"](TARGET).quality_issue.code == "missing_weight" for call in refreshed)
    assert "SELECT DISTINCT status.sector_2 AS sector_name" in query_calls[0][0]


def test_run_refresh_reports_provider_and_sector_progress() -> None:
    progress: list[str] = []

    class MembershipProvider:
        def load(self, sector_name: str, sector_level: int, target_date: date) -> SWMembershipInput:
            return SWMembershipInput(
                sector_name=sector_name,
                sector_level=sector_level,
                member_codes=("600000",),
                as_of_date=target_date,
            )

    basket = ETFBasketInput(
        baskets={"510300": ({"stock_code": "600000", "weight": 100.0},)},
        as_of_date=TARGET,
        weight_unit="percent",
        source_provider="miniqmt",
        source_reference="miniqmt:fixture",
        basket_source_priority="miniqmt_exact",
    )

    class BasketProvider:
        def load(self, target_date: date) -> ETFBasketInput:
            assert target_date == TARGET
            return basket

    refresh_daily.run_refresh(
        target_date=TARGET,
        sector_level=2,
        provider_name="miniqmt",
        min_coverage=0.8,
        mapping_version="exposure_v1",
        config_hash="cfg",
        query=lambda *_: [{"sector_name": "Bank"}],
        membership_provider=MembershipProvider(),
        basket_provider=BasketProvider(),
        ensure_schema=lambda: None,
        refresh=lambda **_kwargs: type("R", (), {"persisted_rows": 1})(),
        progress=progress.append,
    )

    assert progress == [
        "[refresh] mapping schema ready",
        "[refresh] loaded 1 SW2 sectors",
        "[refresh] loading MiniQMT ETF baskets",
        "[refresh] MiniQMT: available; eligible_etfs=1/1; undercovered=0; reported_date=2026-08-18",
        "[refresh] selected MiniQMT ETF baskets; etfs=1; reported_date=2026-08-18",
        "[refresh] sector 1/1: Bank",
        "[refresh] sector 1/1: persisted 1 rows",
    ]
