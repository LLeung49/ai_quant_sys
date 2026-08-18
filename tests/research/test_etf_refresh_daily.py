from datetime import date

from morning_conference.sector_rotation2.research.etf_core import refresh_daily
from morning_conference.sector_rotation2.research.etf_core.providers import (
    ETFBasketInput,
    LocalSWMembershipProvider,
)


TARGET = date(2026, 8, 18)


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
    ], run_refresh_fn=run_refresh_fn) == 0

    assert captured == {
        "target_date": TARGET,
        "sector_level": 2,
        "provider_name": "miniqmt",
        "min_coverage": 0.85,
        "mapping_version": "exposure_v2",
        "config_hash": "cfg",
    }


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
