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
    assert args.provider == "miniqmt"


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

    assert captured == {
        "target_date": TARGET,
        "sector_level": 2,
        "provider_name": "miniqmt",
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
    assert persisted[0]["assessment"].eligible[0].etf_code == "512480.SH"


def test_audited_basket_json_rejects_missing_immutable_provenance() -> None:
    with pytest.raises(ValueError, match="source_reference"):
        refresh_daily.AuditedJSONBasketProvider(
            FIXTURES / "invalid-etf-baskets-missing-reference.json",
        ).load(TARGET)


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
