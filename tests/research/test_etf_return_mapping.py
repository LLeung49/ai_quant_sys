from __future__ import annotations

import builtins
from contextlib import contextmanager
from datetime import date

import pandas as pd

from morning_conference.sector_rotation2.research.etf_core import mapping
from morning_conference.sector_rotation2.research.etf_core.mapping import (
    load_effective_return_etfs,
    persist_return_exposure_mapping,
)
from morning_conference.sector_rotation2.research.etf_core.refresh_return_mapping import main
from morning_conference.sector_rotation2.research.etf_core.return_data import ReturnMappingInput
from morning_conference.sector_rotation2.research.etf_core.return_exposure import (
    ReturnExposureFailure,
    ReturnExposureResult,
)


AS_OF_DATE = date(2026, 8, 19)
WINDOW_START = date(2026, 5, 27)


def _result(
    code: str,
    score: float,
    r_squared: float,
    confidence: str = "qualified",
) -> ReturnExposureResult:
    return ReturnExposureResult(
        etf_code=code,
        corr=0.8,
        beta=1.1,
        r_squared=r_squared,
        residual_vol=0.12,
        sector_fit_score=score,
        sample_count=60,
        confidence_status=confidence,
    )


def _recording_transaction(commands: list[tuple[str, object]]):
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

    return transaction


def _inserted_records(command: tuple[str, object]) -> list[dict[str, object]]:
    sql, raw_rows = command
    column_block = sql.split("(", 1)[1].split(") VALUES", 1)[0]
    columns = [column.strip() for column in column_block.split(",")]
    return [dict(zip(columns, row, strict=True)) for row in raw_rows]


def test_return_mapping_schema_safely_adds_nullable_audit_columns() -> None:
    fields = (
        "mapping_method",
        "lookback_trading_days",
        "window_start_date",
        "window_end_date",
        "sample_count",
        "corr",
        "beta",
        "r_squared",
        "residual_vol",
        "sector_fit_score",
        "confidence_status",
        "price_source",
        "price_as_of_date",
        "universe_source",
    )
    assert all(field in mapping.SECTOR_ETF_MAP_DDL for field in fields)

    updates: list[str] = []

    def query(sql: str, _params: tuple[object, ...]) -> list[dict[str, object]]:
        if "information_schema.columns" in sql:
            return [{"column_name": "id", "is_nullable": "NO"}]
        return [
            {"index_name": "uk_sector_etf_map", "column_name": column}
            for column in ("sector_level", "sector_name", "etf_code", "mapping_type", "effective_from")
        ]

    mapping.ensure_mapping_schema(
        query=query,
        execute_update=lambda sql, _params=(): updates.append(sql) or 1,
    )

    for field in fields:
        migration = next(sql for sql in updates if f"ADD COLUMN {field} " in sql)
        assert " NULL" in migration


def test_return_mapping_persists_sorted_top3_statistics_and_replaces_only_return_events() -> None:
    commands: list[tuple[str, object]] = []
    ranked = [
        _result("510004", 0.4, 0.8),
        _result("510002", 0.9, 0.7, "low_confidence"),
        _result("510003", 0.9, 0.8),
        _result("510001", 0.9, 0.8),
    ]

    count = persist_return_exposure_mapping(
        "Semiconductors",
        2,
        AS_OF_DATE,
        ranked,
        window_start_date=WINDOW_START,
        window_end_date=AS_OF_DATE,
        lookback_trading_days=60,
        price_as_of_date=AS_OF_DATE,
        price_source="local_trade_daily",
        universe_source="local_domestic_equity_etf",
        mapping_version="return_v1",
        config_hash="cfg",
        transaction=_recording_transaction(commands),
        ensure_schema=lambda: None,
    )

    assert count == 3
    records = _inserted_records(commands[2])
    assert [record["etf_code"] for record in records] == ["510001", "510003", "510002"]
    assert [record["rank_no"] for record in records] == [1, 2, 3]
    assert all(record["mapping_type"] == "return_exposure_derived" for record in records)
    assert all(record["mapping_method"] == "sw2_return_regression_v1" for record in records)
    assert all(record["quality_status"] == "qualified" for record in records)
    assert records[2]["confidence_status"] == "low_confidence"
    assert records[0]["window_start_date"] == WINDOW_START
    assert records[0]["window_end_date"] == AS_OF_DATE
    assert records[0]["lookback_trading_days"] == 60
    assert records[0]["sample_count"] == 60
    assert records[0]["sector_fit_score"] == 0.9
    assert records[0]["price_source"] == "local_trade_daily"
    assert records[0]["price_as_of_date"] == AS_OF_DATE
    assert records[0]["universe_source"] == "local_domestic_equity_etf"

    lock_sql, delete_sql, rebuild_sql = commands[0][0], commands[1][0], commands[3][0]
    for sql in (lock_sql, delete_sql, rebuild_sql):
        assert "mapping_type='return_exposure_derived'" in sql.replace(" ", "")
        assert "mapping_type IN" not in sql
        assert "exposure_quality_failure" not in sql


def test_return_mapping_records_one_auditable_quality_failure() -> None:
    commands: list[tuple[str, object]] = []

    count = persist_return_exposure_mapping(
        "Semiconductors",
        2,
        AS_OF_DATE,
        [],
        window_start_date=WINDOW_START,
        window_end_date=AS_OF_DATE,
        lookback_trading_days=60,
        price_as_of_date=AS_OF_DATE,
        price_source="local_trade_daily",
        universe_source="local_domestic_equity_etf",
        mapping_version="return_v1",
        config_hash="cfg",
        transaction=_recording_transaction(commands),
        ensure_schema=lambda: None,
    )

    assert count == 1
    record = _inserted_records(commands[2])[0]
    assert record["mapping_type"] == "return_mapping_quality_failure"
    assert record["quality_status"] == "failed"
    assert record["failure_reason"] == "no_return_exposure_with_sufficient_observations"
    assert record["mapping_method"] == "sw2_return_regression_v1"
    assert record["price_as_of_date"] == AS_OF_DATE
    assert "ON DUPLICATE KEY UPDATE" in commands[2][0]


def test_effective_return_loader_keeps_low_confidence_and_reads_full_provenance() -> None:
    captured: dict[str, object] = {}
    base = {
        "mapping_type": "return_exposure_derived",
        "quality_status": "qualified",
        "mapping_method": "sw2_return_regression_v1",
        "lookback_trading_days": 60,
        "window_start_date": WINDOW_START,
        "window_end_date": AS_OF_DATE,
        "sample_count": 60,
        "corr": 0.8,
        "beta": 1.1,
        "r_squared": 0.64,
        "residual_vol": 0.12,
        "price_source": "local_trade_daily",
        "price_as_of_date": AS_OF_DATE,
        "universe_source": "local_domestic_equity_etf",
    }

    def query(sql: str, params: tuple[object, ...]) -> list[dict[str, object]]:
        captured.update(sql=sql, params=params)
        return [
            {**base, "etf_code": "510002", "rank_no": 2, "sector_fit_score": 0.6, "confidence_status": "low_confidence"},
            {**base, "etf_code": "510001", "rank_no": 1, "sector_fit_score": 0.9, "confidence_status": "qualified"},
            {**base, "etf_code": "510099", "mapping_type": "exposure_derived", "rank_no": 1, "sector_fit_score": 1.0, "confidence_status": "qualified"},
        ]

    rows = load_effective_return_etfs("Semiconductors", 2, AS_OF_DATE, query)

    assert [row["etf_code"] for row in rows] == ["510001", "510002"]
    assert rows[1]["confidence_status"] == "low_confidence"
    assert rows[1]["corr"] == 0.8
    assert rows[1]["beta"] == 1.1
    assert rows[1]["r_squared"] == 0.64
    assert rows[1]["residual_vol"] == 0.12
    assert rows[1]["window_start_date"] == WINDOW_START
    sql = str(captured["sql"])
    assert "mapping_type='return_exposure_derived'" in sql
    assert "constituent_reported_date" not in sql
    assert "freshness_status" not in sql


def test_return_refresh_cli_uses_injected_local_pipeline_without_external_imports(
    monkeypatch,
    capsys,
) -> None:
    index = pd.date_range("2026-05-27", periods=61, freq="B")
    loaded = ReturnMappingInput(
        as_of_date=AS_OF_DATE,
        sector_closes={"Sector A": pd.Series(range(61), index=index), "Sector B": pd.Series(range(61), index=index)},
        etf_closes={"510001": pd.Series(range(61), index=index), "510002": pd.Series(range(61), index=index)},
        universe_codes=("510001", "510002"),
    )
    loader_calls: list[tuple[date, int, int]] = []
    persisted: list[dict[str, object]] = []

    def loader(target_date: date, sector_level: int, window: int):
        loader_calls.append((target_date, sector_level, window))
        return loaded

    assessments = iter([
        ([_result("510001", 0.8, 0.7), _result("510002", 0.5, 0.2, "low_confidence")], []),
        ([], [ReturnExposureFailure("510001", "insufficient_common_returns")]),
    ])

    def assessor(_etfs, _sector, window: int, min_samples: int):
        assert (window, min_samples) == (60, 50)
        return next(assessments)

    def persist(*args, **kwargs):
        persisted.append({"args": args, **kwargs})
        return min(3, len(args[3])) if args[3] else 1

    real_import = builtins.__import__

    def guarded_import(name, *args, **kwargs):
        if any(token in name.lower() for token in ("akshare", "miniqmt", "xtquant", "providers")):
            raise AssertionError(f"external provider import attempted: {name}")
        return real_import(name, *args, **kwargs)

    monkeypatch.setattr(builtins, "__import__", guarded_import)

    assert main(
        ["--as-of-date", "2026-08-19", "--level", "2", "--config-hash", "cfg"],
        load_input=loader,
        assessor=assessor,
        persist=persist,
        ensure_schema=lambda: None,
    ) == 0

    assert loader_calls == [(AS_OF_DATE, 2, 60)]
    assert [call["args"][0] for call in persisted] == ["Sector A", "Sector B"]
    assert persisted[0]["price_source"] == "local_trade_daily"
    assert persisted[0]["universe_source"] == "local_domestic_equity_etf"
    assert persisted[1]["args"][3] == []
    output = capsys.readouterr().out
    assert "sectors=2" in output
    assert "etf_universe=2" in output
    assert "qualified=1" in output
    assert "low_confidence=1" in output
    assert "quality_failures=1" in output
