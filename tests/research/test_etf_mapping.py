from datetime import date
from contextlib import contextmanager
import inspect

import pytest

from morning_conference.sector_rotation2.research.etf_core.exposure import ExposureResult, assess_sector_etfs
from morning_conference.sector_rotation2.research.etf_core import mapping
from morning_conference.sector_rotation2.research.etf_core.mapping import load_effective_etfs


def test_mapping_is_point_in_time_and_primary_sorted() -> None:
    target = date(2026, 8, 17)

    def query(_sql: str, _params: tuple[object, ...]) -> list[dict[str, object]]:
        return [
            {"etf_code": "512480.SH", "mapping_type": "exposure_derived", "quality_status": "qualified", "exposure_weight": 0.4, "coverage_ratio": 0.9, "rank_no": 2, "source_as_of_date": target, "membership_as_of_date": target, "constituent_as_of_date": target, "constituent_reported_date": target, "holdings_age_days": 0, "freshness_status": "fresh", "freshness_confidence": 1.0, "basket_source_priority": "miniqmt_exact", "source_provider": "provider_x", "source_reference": "provider:daily"},
            {"etf_code": "159995.SZ", "mapping_type": "exposure_derived", "quality_status": "qualified", "exposure_weight": 0.8, "coverage_ratio": 0.9, "rank_no": 1, "source_as_of_date": target, "membership_as_of_date": target, "constituent_as_of_date": target, "constituent_reported_date": target, "holdings_age_days": 0, "freshness_status": "fresh", "freshness_confidence": 1.0, "basket_source_priority": "miniqmt_exact", "source_provider": "provider_x", "source_reference": "provider:daily"},
        ]

    rows = load_effective_etfs("半导体", 1, target, query)
    assert [row["etf_code"] for row in rows] == ["159995.SZ", "512480.SH"]


def test_mapping_query_uses_effective_date_bounds() -> None:
    captured: dict[str, object] = {}

    def query(sql: str, params: tuple[object, ...]) -> list[dict[str, object]]:
        captured.update(sql=sql, params=params)
        return []

    load_effective_etfs("半导体", 1, date(2025, 12, 31), query)
    assert "effective_from <= %s" in str(captured["sql"])
    assert "effective_to IS NULL OR effective_to >= %s" in str(captured["sql"])
    assert captured["params"].count(date(2025, 12, 31)) == 5


def test_exposure_mapping_persists_only_quality_passing_top_three_with_audit_fields() -> None:
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

    assert hasattr(mapping, "persist_exposure_mapping")
    persisted = mapping.persist_exposure_mapping(
        sector_name="半导体",
        sector_level=2,
        as_of_date=date(2026, 8, 17),
        ranked=[
            ExposureResult("510001.SH", exposure_weight=0.80, coverage_ratio=1.00),
            ExposureResult("510002.SH", exposure_weight=0.60, coverage_ratio=0.90),
            ExposureResult("510003.SH", exposure_weight=0.40, coverage_ratio=0.79),
            ExposureResult("510004.SH", exposure_weight=0.20, coverage_ratio=0.95),
        ],
        source_as_of_date=date(2026, 8, 17),
        source_provider="provider_x",
        membership_as_of_date=date(2026, 8, 17),
        constituent_as_of_date=date(2026, 8, 17),
        constituent_reported_date=date(2026, 8, 17),
        basket_source_priority="miniqmt_exact",
        mapping_version="exposure_v1",
        config_hash="abc123",
        weight_unit="decimal",
        source_reference="xtdata.get_etf_info",
        min_coverage=0.80,
        transaction=transaction,
        ensure_schema=lambda: None,
    )

    assert persisted == 3
    sql, rows = commands[2]
    assert "source_as_of_date" in sql
    assert "membership_asof_mode" in sql
    assert [row[2] for row in rows] == ["510001.SH", "510002.SH", "510004.SH"]
    assert [row[12] for row in rows] == [1, 2, 3]
    assert all(row[15] == "current_mapping" for row in rows)
    assert all(row[16] == date(2026, 8, 17) and row[17] == date(2026, 8, 17) for row in rows)
    assert all(row[21] == "xtdata.get_etf_info" for row in rows)


def test_mapping_persists_and_loads_holdings_disclosure_freshness() -> None:
    for field in (
        "constituent_reported_date",
        "holdings_age_days",
        "freshness_status",
        "freshness_confidence",
        "basket_source_priority",
        "cross_check_status",
        "cross_check_detail",
    ):
        assert field in mapping.SECTOR_ETF_MAP_DDL

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

    refresh_date = date(2026, 8, 18)
    reported_date = date(2026, 5, 19)
    assert mapping.persist_exposure_mapping(
        sector_name="半导体",
        sector_level=2,
        as_of_date=refresh_date,
        ranked=[ExposureResult("510001.SH", exposure_weight=0.8, coverage_ratio=1.0)],
        source_as_of_date=refresh_date,
        source_provider="akshare",
        membership_as_of_date=refresh_date,
        constituent_as_of_date=refresh_date,
        constituent_reported_date=reported_date,
        basket_source_priority="akshare_disclosed",
        cross_check_status="mismatch",
        cross_check_detail="510300.SH: MiniQMT and AKShare constituent codes differ",
        mapping_version="exposure_v1",
        config_hash="cfg",
        weight_unit="decimal",
        source_reference="akshare:fund_portfolio_hold_em",
        transaction=transaction,
        ensure_schema=lambda: None,
    ) == 1

    insert_sql, inserted_rows = commands[2]
    row = inserted_rows[0]
    assert "constituent_reported_date" in insert_sql
    assert "holdings_age_days" in insert_sql
    assert "freshness_status" in insert_sql
    assert "freshness_confidence" in insert_sql
    assert "basket_source_priority" in insert_sql
    assert "cross_check_status" in insert_sql
    assert "cross_check_detail" in insert_sql
    assert row[22] == reported_date
    assert row[23] == 91
    assert row[24] == "aging"
    assert row[25] == pytest.approx(0.5 ** (91 / 90))
    assert row[26] == "akshare_disclosed"
    assert row[27] == "mismatch"
    assert row[28] == "510300.SH: MiniQMT and AKShare constituent codes differ"

    captured: dict[str, object] = {}

    def query(sql: str, params: tuple[object, ...]) -> list[dict[str, object]]:
        captured.update(sql=sql, params=params)
        return [{
            "etf_code": "510001.SH",
            "mapping_type": "exposure_derived",
            "quality_status": "qualified",
            "exposure_weight": 0.8,
            "coverage_ratio": 1.0,
            "rank_no": 1,
            "source_as_of_date": refresh_date,
            "membership_as_of_date": refresh_date,
            "constituent_as_of_date": refresh_date,
            "constituent_reported_date": reported_date,
            "holdings_age_days": 91,
            "freshness_status": "aging",
            "freshness_confidence": 0.5 ** (91 / 90),
            "basket_source_priority": "akshare_disclosed",
            "cross_check_status": "mismatch",
            "cross_check_detail": "510300.SH: MiniQMT and AKShare constituent codes differ",
            "source_provider": "akshare",
            "source_reference": "akshare:fund_portfolio_hold_em",
        }]

    rows = mapping.load_effective_etfs("半导体", 2, refresh_date, query)

    assert "constituent_reported_date" in captured["sql"]
    assert "holdings_age_days" in captured["sql"]
    assert "freshness_status" in captured["sql"]
    assert "freshness_confidence" in captured["sql"]
    assert "basket_source_priority" in captured["sql"]
    assert "cross_check_status" in captured["sql"]
    assert "cross_check_detail" in captured["sql"]
    assert rows[0]["constituent_reported_date"] == reported_date
    assert rows[0]["holdings_age_days"] == 91
    assert rows[0]["freshness_status"] == "aging"
    assert rows[0]["freshness_confidence"] == pytest.approx(0.5 ** (91 / 90))
    assert rows[0]["basket_source_priority"] == "akshare_disclosed"
    assert rows[0]["cross_check_status"] == "mismatch"
    assert rows[0]["cross_check_detail"] == "510300.SH: MiniQMT and AKShare constituent codes differ"


@pytest.mark.parametrize(
    ("constituent_reported_date", "basket_source_priority", "error"),
    [
        (None, "akshare_disclosed", "constituent_reported_date"),
        (date(2026, 8, 18), None, "basket_source_priority"),
        (date(2026, 8, 18), " ", "basket_source_priority"),
    ],
)
def test_qualified_mapping_requires_explicit_holdings_provenance(
    constituent_reported_date: date | None,
    basket_source_priority: str | None,
    error: str,
) -> None:
    with pytest.raises(ValueError, match=error):
        mapping.persist_exposure_mapping(
            sector_name="半导体",
            sector_level=2,
            as_of_date=date(2026, 8, 18),
            ranked=[ExposureResult("510001.SH", exposure_weight=0.8, coverage_ratio=1.0)],
            source_as_of_date=date(2026, 8, 18),
            source_provider="akshare",
            membership_as_of_date=date(2026, 8, 18),
            constituent_as_of_date=date(2026, 8, 18),
            constituent_reported_date=constituent_reported_date,
            basket_source_priority=basket_source_priority,
            mapping_version="exposure_v1",
            config_hash="cfg",
            weight_unit="decimal",
            source_reference="akshare:fund_portfolio_hold_em",
            transaction=lambda: pytest.fail("invalid mapping must not open a transaction"),
        )


def test_effective_loader_rejects_invalid_holdings_freshness_provenance() -> None:
    refresh_date = date(2026, 8, 18)
    reported_date = date(2026, 5, 19)
    confidence = 0.5 ** (91 / 90)
    base = {
        "mapping_type": "exposure_derived",
        "quality_status": "qualified",
        "exposure_weight": 0.8,
        "coverage_ratio": 1.0,
        "rank_no": 1,
        "source_as_of_date": refresh_date,
        "membership_as_of_date": refresh_date,
        "constituent_as_of_date": refresh_date,
        "constituent_reported_date": reported_date,
        "holdings_age_days": 91,
        "freshness_status": "aging",
        "freshness_confidence": confidence,
        "basket_source_priority": "akshare_disclosed",
        "source_provider": "akshare",
        "source_reference": "akshare:fund_portfolio_hold_em",
    }
    missing_reported_date = {**base, "etf_code": "510001.SH"}
    missing_reported_date.pop("constituent_reported_date")
    missing_age = {**base, "etf_code": "510008.SH"}
    missing_age.pop("holdings_age_days")
    missing_status = {**base, "etf_code": "510009.SH"}
    missing_status.pop("freshness_status")
    missing_confidence = {**base, "etf_code": "510010.SH"}
    missing_confidence.pop("freshness_confidence")
    missing_source_priority = {**base, "etf_code": "510011.SH"}
    missing_source_priority.pop("basket_source_priority")
    captured: dict[str, object] = {}

    def query(sql: str, params: tuple[object, ...]) -> list[dict[str, object]]:
        captured.update(sql=sql, params=params)
        return [
            missing_reported_date,
            {**base, "etf_code": "510002.SH", "holdings_age_days": 90},
            {**base, "etf_code": "510003.SH", "freshness_status": "fresh"},
            {**base, "etf_code": "510004.SH", "freshness_confidence": 1.0},
            {**base, "etf_code": "510005.SH", "basket_source_priority": " "},
            {**base, "etf_code": "510006.SH", "constituent_reported_date": date(2026, 8, 19)},
            {**base, "etf_code": "510007.SH"},
            missing_age,
            missing_status,
            missing_confidence,
            missing_source_priority,
        ]

    rows = mapping.load_effective_etfs("半导体", 2, refresh_date, query)

    assert "constituent_reported_date IS NOT NULL" in captured["sql"]
    assert "holdings_age_days IS NOT NULL" in captured["sql"]
    assert "freshness_status IS NOT NULL" in captured["sql"]
    assert "freshness_confidence IS NOT NULL" in captured["sql"]
    assert "basket_source_priority IS NOT NULL" in captured["sql"]
    assert [row["etf_code"] for row in rows] == ["510007.SH"]


def test_effective_loader_prefers_exposure_rank_then_legacy_primary_order() -> None:
    def query(_sql: str, _params: tuple[object, ...]) -> list[dict[str, object]]:
        return [
            {"etf_code": "510030.SH", "is_primary": 1, "rank_no": None},
            {"etf_code": "510020.SH", "is_primary": 0, "rank_no": 2},
            {"etf_code": "510010.SH", "is_primary": 0, "rank_no": 1},
            {"etf_code": "510040.SH", "is_primary": 0, "rank_no": None},
        ]

    rows = load_effective_etfs("半导体", 2, date(2026, 8, 17), query)

    assert rows == []


def test_sector_member_loader_reads_current_status_mapping_at_requested_level() -> None:
    captured: dict[str, object] = {}

    def query(sql: str, params: tuple[object, ...]) -> list[dict[str, object]]:
        captured.update(sql=sql, params=params)
        return [{"stock_code": "600000.SH"}, {"stock_code": "000001.SZ"}]

    assert hasattr(mapping, "load_sector_member_codes")
    assert mapping.load_sector_member_codes("半导体", 2, query) == ["600000.SH", "000001.SZ"]
    assert "trade_stock_status" in str(captured["sql"])
    assert "status.sector_2 = %s" in str(captured["sql"])
    assert captured["params"] == ("半导体",)
    assert "current_mapping" in mapping.load_sector_member_codes.__doc__


def test_mapping_ddl_contains_exposure_provenance_fields() -> None:
    for field in (
        "effective_from",
        "effective_to",
        "source_as_of_date",
        "source_provider",
        "exposure_weight",
        "coverage_ratio",
        "mapping_version",
        "config_hash",
        "rank_no",
        "weight_unit",
        "membership_asof_mode",
        "source_reference",
    ):
        assert field in mapping.SECTOR_ETF_MAP_DDL


def test_persist_uses_one_injected_transaction_and_rebuilds_effective_intervals() -> None:
    assert "transaction" in inspect.signature(mapping.persist_exposure_mapping).parameters

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

    assert mapping.persist_exposure_mapping(
        sector_name="半导体", sector_level=2, as_of_date=date(2026, 8, 17),
        ranked=[
            ExposureResult("510002.SH", exposure_weight=0.4, coverage_ratio=0.9),
            ExposureResult("510001.SH", exposure_weight=0.8, coverage_ratio=0.9),
        ],
        source_as_of_date=date(2026, 8, 17), source_provider="provider_x",
        membership_as_of_date=date(2026, 8, 17), constituent_as_of_date=date(2026, 8, 17),
        constituent_reported_date=date(2026, 8, 17), basket_source_priority="miniqmt_exact",
        mapping_version="exposure_v1", config_hash="abc123", weight_unit="decimal",
        source_reference="provider:daily",
        transaction=transaction, ensure_schema=lambda: None,
    ) == 2

    assert "FOR UPDATE" in commands[0][0]
    assert "DELETE FROM trade_sector_etf_map" in commands[1][0]
    assert "INSERT INTO trade_sector_etf_map" in commands[2][0]
    assert "effective_to" in commands[3][0]
    assert [row[2] for row in commands[2][1]] == ["510001.SH", "510002.SH"]
    assert [row[12] for row in commands[2][1]] == [1, 2]


def test_persist_records_auditable_failure_when_no_quality_mapping_is_available() -> None:
    assert "transaction" in inspect.signature(mapping.persist_exposure_mapping).parameters

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

    assert mapping.persist_exposure_mapping(
        sector_name="半导体", sector_level=2, as_of_date=date(2026, 8, 17),
        ranked=[ExposureResult("510001.SH", exposure_weight=0.0, coverage_ratio=0.7)],
        source_as_of_date=date(2026, 8, 17), source_provider="provider_x",
        membership_as_of_date=date(2026, 8, 17), constituent_as_of_date=date(2026, 8, 17),
        mapping_version="exposure_v1", config_hash="abc123", weight_unit="decimal",
        transaction=transaction, ensure_schema=lambda: None,
    ) == 1

    failure_row = commands[2][1][0]
    assert failure_row[2] == "510001.SH"
    assert failure_row[3] == "exposure_quality_failure"
    assert failure_row[9:11] == (0.0, 0.7)
    assert failure_row[18] == "failed"
    assert "no qualified" in failure_row[19]


def test_persist_rejects_mismatched_membership_and_constituent_dates() -> None:
    with pytest.raises(ValueError, match="must match"):
        mapping.persist_exposure_mapping(
            sector_name="半导体", sector_level=2, as_of_date=date(2026, 8, 17), ranked=[],
            source_as_of_date=None, source_provider="provider_x",
            membership_as_of_date=date(2026, 8, 17), constituent_as_of_date=date(2026, 8, 17),
            mapping_version="exposure_v1", config_hash="abc123", weight_unit="decimal",
        )


def test_persist_rejects_consistently_stale_provenance_dates() -> None:
    stale = date(2026, 8, 16)
    with pytest.raises(ValueError, match="must equal as_of_date"):
        mapping.persist_exposure_mapping(
            sector_name="半导体", sector_level=2, as_of_date=date(2026, 8, 17),
            ranked=[ExposureResult("510001.SH", exposure_weight=0.8, coverage_ratio=1.0)],
            source_as_of_date=stale, source_provider="provider_x",
            membership_as_of_date=stale, constituent_as_of_date=stale,
            mapping_version="exposure_v1", config_hash="abc123", weight_unit="decimal",
            source_reference="provider:stale",
            transaction=lambda: pytest.fail("stale input must fail before opening a transaction"),
        )


def test_persist_rejects_qualified_mapping_without_source_reference() -> None:
    with pytest.raises(ValueError, match="source_reference"):
        mapping.persist_exposure_mapping(
            sector_name="半导体", sector_level=2, as_of_date=date(2026, 8, 17),
            ranked=[ExposureResult("510001.SH", exposure_weight=0.8, coverage_ratio=1.0)],
            source_as_of_date=date(2026, 8, 17), source_provider="provider_x",
            membership_as_of_date=date(2026, 8, 17), constituent_as_of_date=date(2026, 8, 17),
            constituent_reported_date=date(2026, 8, 17), basket_source_priority="miniqmt_exact",
            mapping_version="exposure_v1", config_hash="abc123", weight_unit="decimal",
            transaction=lambda: pytest.fail("untraceable input must fail before opening a transaction"),
        )


def test_persist_rejects_qualified_mapping_with_blank_source_provider() -> None:
    with pytest.raises(ValueError, match="source_provider"):
        mapping.persist_exposure_mapping(
            sector_name="半导体", sector_level=2, as_of_date=date(2026, 8, 17),
            ranked=[ExposureResult("510001.SH", exposure_weight=0.8, coverage_ratio=1.0)],
            source_as_of_date=date(2026, 8, 17), source_provider=" ",
            membership_as_of_date=date(2026, 8, 17), constituent_as_of_date=date(2026, 8, 17),
            mapping_version="exposure_v1", config_hash="abc123", weight_unit="decimal",
            source_reference="provider:daily",
            transaction=lambda: pytest.fail("blank provider must fail before opening a transaction"),
        )


def test_effective_loader_never_runs_schema_ddl_and_returns_only_qualified_derived_top_three() -> None:
    calls: list[str] = []

    def query(sql: str, _params: tuple[object, ...]) -> list[dict[str, object]]:
        calls.append(sql)
        return [
            {"etf_code": "510004.SH", "mapping_type": "manual", "quality_status": "qualified", "exposure_weight": 0.9, "coverage_ratio": 1.0, "rank_no": 1},
            {"etf_code": "510003.SH", "mapping_type": "exposure_derived", "quality_status": "failed", "exposure_weight": 0.9, "coverage_ratio": 1.0, "rank_no": 1},
            {"etf_code": "510002.SH", "mapping_type": "exposure_derived", "quality_status": "qualified", "exposure_weight": 0.0, "coverage_ratio": 1.0, "rank_no": 2},
            {"etf_code": "510001.SH", "mapping_type": "exposure_derived", "quality_status": "qualified", "exposure_weight": 0.8, "coverage_ratio": 0.9, "rank_no": 1, "source_as_of_date": date(2026, 8, 17), "membership_as_of_date": date(2026, 8, 17), "constituent_as_of_date": date(2026, 8, 17), "constituent_reported_date": date(2026, 8, 17), "holdings_age_days": 0, "freshness_status": "fresh", "freshness_confidence": 1.0, "basket_source_priority": "miniqmt_exact", "source_provider": "provider_x", "source_reference": "provider:daily"},
        ]

    rows = mapping.load_effective_etfs("半导体", 2, date(2026, 8, 17), query)

    assert [row["etf_code"] for row in rows] == ["510001.SH"]
    assert len(calls) == 1
    assert "mapping_type='exposure_derived'" in calls[0]
    assert "quality_status='qualified'" in calls[0]


def test_effective_loader_rejects_stale_provenance_even_if_row_is_qualified() -> None:
    target = date(2026, 8, 17)
    captured: dict[str, object] = {}

    def query(sql: str, params: tuple[object, ...]) -> list[dict[str, object]]:
        captured.update(sql=sql, params=params)
        return [
            {"etf_code": "510001.SH", "mapping_type": "exposure_derived", "quality_status": "qualified", "exposure_weight": 0.8, "coverage_ratio": 1.0, "rank_no": 1, "source_as_of_date": date(2026, 8, 16), "membership_as_of_date": date(2026, 8, 16), "constituent_as_of_date": date(2026, 8, 16), "source_provider": "provider_x", "source_reference": "provider:stale"},
            {"etf_code": "510002.SH", "mapping_type": "exposure_derived", "quality_status": "qualified", "exposure_weight": 0.7, "coverage_ratio": 1.0, "rank_no": 2, "source_as_of_date": target, "membership_as_of_date": target, "constituent_as_of_date": target, "constituent_reported_date": target, "holdings_age_days": 0, "freshness_status": "fresh", "freshness_confidence": 1.0, "basket_source_priority": "miniqmt_exact", "source_provider": "provider_x", "source_reference": "provider:daily"},
        ]

    rows = mapping.load_effective_etfs("半导体", 2, target, query)

    assert [row["etf_code"] for row in rows] == ["510002.SH"]
    assert "source_as_of_date=%s" in str(captured["sql"])
    assert "membership_as_of_date=%s" in str(captured["sql"])
    assert "constituent_as_of_date=%s" in str(captured["sql"])


def test_effective_loader_rejects_qualified_row_with_blank_source_provider() -> None:
    target = date(2026, 8, 17)
    captured: dict[str, object] = {}

    def query(sql: str, params: tuple[object, ...]) -> list[dict[str, object]]:
        captured.update(sql=sql, params=params)
        base = {
            "mapping_type": "exposure_derived", "quality_status": "qualified",
            "exposure_weight": 0.8, "coverage_ratio": 1.0,
            "source_as_of_date": target, "membership_as_of_date": target,
            "constituent_as_of_date": target, "constituent_reported_date": target,
            "holdings_age_days": 0, "freshness_status": "fresh",
            "freshness_confidence": 1.0, "basket_source_priority": "miniqmt_exact",
            "source_reference": "provider:daily",
        }
        return [
            {**base, "etf_code": "510001.SH", "rank_no": 1, "source_provider": " "},
            {**base, "etf_code": "510002.SH", "rank_no": 2, "source_provider": "provider_x"},
        ]

    rows = mapping.load_effective_etfs("半导体", 2, target, query)

    assert [row["etf_code"] for row in rows] == ["510002.SH"]
    assert "source_provider IS NOT NULL" in str(captured["sql"])
    assert "TRIM(source_provider) <> ''" in str(captured["sql"])


def test_ensure_mapping_schema_adds_missing_columns_safely() -> None:
    updates: list[str] = []

    def query(sql: str, _params: tuple[object, ...]) -> list[dict[str, object]]:
        return [{"column_name": "id"}] if "information_schema.columns" in sql else [
            {"index_name": "uk_sector_etf_map", "column_name": "sector_level"},
            {"index_name": "uk_sector_etf_map", "column_name": "sector_name"},
            {"index_name": "uk_sector_etf_map", "column_name": "etf_code"},
            {"index_name": "uk_sector_etf_map", "column_name": "effective_from"},
        ]

    mapping.ensure_mapping_schema(
        query=query,
        execute_update=lambda sql, _params=(): updates.append(sql) or 1,
    )

    assert updates[0] == mapping.SECTOR_ETF_MAP_DDL
    assert any("ADD COLUMN quality_status" in sql for sql in updates)
    assert any("ADD COLUMN membership_as_of_date" in sql for sql in updates)


def test_ensure_mapping_schema_accepts_mysql_information_schema_uppercase_keys() -> None:
    updates: list[str] = []

    def query(sql: str, _params: tuple[object, ...]) -> list[dict[str, object]]:
        if "information_schema.columns" in sql:
            return [{"COLUMN_NAME": "id", "IS_NULLABLE": "NO"}]
        return [
            {"INDEX_NAME": "uk_sector_etf_map", "COLUMN_NAME": "sector_level"},
            {"INDEX_NAME": "uk_sector_etf_map", "COLUMN_NAME": "sector_name"},
            {"INDEX_NAME": "uk_sector_etf_map", "COLUMN_NAME": "etf_code"},
            {"INDEX_NAME": "uk_sector_etf_map", "COLUMN_NAME": "effective_from"},
        ]

    mapping.ensure_mapping_schema(
        query=query,
        execute_update=lambda sql, _params=(): updates.append(sql) or 1,
    )

    assert any("ADD COLUMN quality_status" in sql for sql in updates)
    assert any("DROP INDEX uk_sector_etf_map" in sql for sql in updates)


def test_schema_migration_keeps_manual_and_derived_same_day_as_distinct_rows() -> None:
    updates: list[str] = []

    def query(sql: str, _params: tuple[object, ...]) -> list[dict[str, object]]:
        if "information_schema.columns" in sql:
            return [{"column_name": name} for name in mapping._MIGRATION_COLUMNS]
        return [
            {"index_name": "uk_sector_etf_map", "column_name": "sector_level"},
            {"index_name": "uk_sector_etf_map", "column_name": "sector_name"},
            {"index_name": "uk_sector_etf_map", "column_name": "etf_code"},
            {"index_name": "uk_sector_etf_map", "column_name": "effective_from"},
        ]

    mapping.ensure_mapping_schema(query=query, execute_update=lambda sql, _params=(): updates.append(sql) or 1)

    assert "mapping_type" in mapping.SECTOR_ETF_MAP_DDL.split("uk_sector_etf_map", 1)[1]
    unique_migration = next(sql for sql in updates if "DROP INDEX uk_sector_etf_map" in sql)
    assert "ADD UNIQUE KEY uk_sector_etf_map" in unique_migration
    assert "mapping_type" in unique_migration


def test_schema_migration_makes_failure_provenance_nullable() -> None:
    updates: list[str] = []
    nullable_fields = {
        "source_as_of_date",
        "weight_unit",
        "membership_as_of_date",
        "constituent_as_of_date",
    }

    def query(sql: str, _params: tuple[object, ...]) -> list[dict[str, object]]:
        if "information_schema.columns" in sql:
            return [
                {
                    "column_name": name,
                    "is_nullable": "NO" if name in nullable_fields else "YES",
                }
                for name in mapping._MIGRATION_COLUMNS
            ]
        return [
            {"index_name": "uk_sector_etf_map", "column_name": name}
            for name in ("sector_level", "sector_name", "etf_code", "mapping_type", "effective_from")
        ]

    mapping.ensure_mapping_schema(
        query=query,
        execute_update=lambda sql, _params=(): updates.append(sql) or 1,
    )

    for field in nullable_fields:
        assert any(f"MODIFY COLUMN {field}" in sql and "NULL" in sql for sql in updates)


def test_real_exposure_assessment_persists_undercoverage_reason() -> None:
    commands: list[tuple[str, object]] = []

    class Transaction:
        def execute(self, sql: str, params: tuple[object, ...]) -> int:
            commands.append((sql, params)); return 1

        def execute_many(self, sql: str, rows: list[tuple[object, ...]]) -> int:
            commands.append((sql, rows)); return len(rows)

    @contextmanager
    def transaction():
        yield Transaction()

    assessment = assess_sector_etfs(
        {"600000"}, {"510300": [{"stock_code": "600000.SH", "weight": 0.7}]},
        min_coverage=0.9, weight_unit="decimal",
    )
    assert mapping.persist_exposure_assessment(
        sector_name="半导体", sector_level=2, as_of_date=date(2026, 8, 17), assessment=assessment,
        source_as_of_date=date(2026, 8, 17), source_provider="provider_x",
        membership_as_of_date=date(2026, 8, 17), constituent_as_of_date=date(2026, 8, 17),
        mapping_version="exposure_v1", config_hash="cfg", weight_unit="decimal",
        transaction=transaction, ensure_schema=lambda: None,
    ) == 1

    failure = commands[2][1][0]
    assert failure[2] == "510300"
    assert failure[10] == pytest.approx(0.7)
    assert "coverage_below_minimum" in failure[19]
