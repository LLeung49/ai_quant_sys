from __future__ import annotations

import builtins
import copy
import importlib
import sys
from contextlib import contextmanager
from datetime import date, timedelta

import pandas as pd

from morning_conference.sector_rotation2.research.etf_core import mapping
from morning_conference.sector_rotation2.research.etf_core.mapping import (
    load_effective_return_etfs,
    persist_return_exposure_mapping,
)
from morning_conference.sector_rotation2.research.etf_core.return_data import ReturnMappingInput
from morning_conference.sector_rotation2.research.etf_core.return_exposure import (
    ReturnExposureFailure,
    ReturnExposureResult,
)
from morning_conference.sector_rotation2.research.etf_core.service import build_etf_candidate


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


class StatefulMappingDatabase:
    """Exercise the real transaction wrapper against durable in-memory rows."""

    def __init__(self) -> None:
        self.rows: list[dict[str, object]] = []
        self.connections = 0
        self.commits = 0
        self.rollbacks = 0
        self.fail_insert = False
        self.sql: list[str] = []

    def connect(self):
        database = self
        pending = copy.deepcopy(self.rows)
        database.connections += 1

        class Cursor:
            rowcount = 0

            def execute(self, sql: str, params: tuple[object, ...]) -> None:
                database.sql.append(sql)
                compact = " ".join(sql.split())
                if compact.startswith("SELECT id"):
                    self.rowcount = 0
                    return
                if compact.startswith("DELETE"):
                    level, sector, event_date = params
                    event_type = (
                        "return_mapping_quality_failure"
                        if "return_mapping_quality_failure" in sql
                        else "return_exposure_derived"
                    )
                    before = len(pending)
                    pending[:] = [
                        row for row in pending
                        if not (
                            row["sector_level"] == level
                            and row["sector_name"] == sector
                            and row["effective_from"] == event_date
                            and row["mapping_type"] == event_type
                        )
                    ]
                    self.rowcount = before - len(pending)
                    return
                if compact.startswith("UPDATE trade_sector_etf_map"):
                    level, sector = params[0], params[1]
                    dated = sorted({
                        row["effective_from"]
                        for row in pending
                        if row["sector_level"] == level
                        and row["sector_name"] == sector
                        and row["mapping_type"] == "return_exposure_derived"
                    })
                    for row in pending:
                        if (
                            row["sector_level"] == level
                            and row["sector_name"] == sector
                            and row["mapping_type"] == "return_exposure_derived"
                        ):
                            later = [value for value in dated if value > row["effective_from"]]
                            row["effective_to"] = min(later) - timedelta(days=1) if later else None
                    self.rowcount = len(dated)
                    return
                raise AssertionError(f"unexpected SQL: {sql}")

            def executemany(self, sql: str, raw_rows: list[tuple[object, ...]]) -> None:
                database.sql.append(sql)
                if database.fail_insert:
                    raise RuntimeError("injected insert failure")
                columns = [
                    column.strip()
                    for column in sql.split("(", 1)[1].split(") VALUES", 1)[0].split(",")
                ]
                for raw_row in raw_rows:
                    record = dict(zip(columns, raw_row, strict=True))
                    key = tuple(
                        record[name]
                        for name in ("sector_level", "sector_name", "etf_code", "mapping_type", "effective_from")
                    )
                    pending[:] = [
                        row for row in pending
                        if tuple(
                            row[name]
                            for name in ("sector_level", "sector_name", "etf_code", "mapping_type", "effective_from")
                        ) != key
                    ]
                    pending.append(record)
                self.rowcount = len(raw_rows)

            def close(self) -> None:
                pass

        class Connection:
            def cursor(self):
                return Cursor()

            def commit(self) -> None:
                database.rows = copy.deepcopy(pending)
                database.commits += 1

            def rollback(self) -> None:
                database.rollbacks += 1

            def close(self) -> None:
                pass

        return Connection()

    def effective_query(self, _sql: str, params: tuple[object, ...]) -> list[dict[str, object]]:
        sector, level, upper, lower = params[:4]
        return [
            copy.deepcopy(row)
            for row in self.rows
            if row["sector_name"] == sector
            and row["sector_level"] == level
            and row["effective_from"] <= upper
            and (row["effective_to"] is None or row["effective_to"] >= lower)
        ]


def _persist_state(
    database: StatefulMappingDatabase,
    event_date: date,
    ranked: list[ReturnExposureResult],
    *,
    price_date: date | None = None,
) -> int:
    observed_date = price_date or event_date
    original_connection = mapping.get_connection
    mapping.get_connection = database.connect
    try:
        return persist_return_exposure_mapping(
            "Semiconductors",
            2,
            event_date,
            ranked,
            window_start_date=observed_date - timedelta(days=84),
            window_end_date=observed_date,
            lookback_trading_days=60,
            price_as_of_date=observed_date,
            price_source="local_trade_daily",
            universe_source="local_domestic_equity_etf",
            mapping_version="return_v1",
            config_hash="cfg",
            transaction=mapping.open_mapping_transaction,
        )
    finally:
        mapping.get_connection = original_connection


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
    insert_command = next(command for command in commands if command[0].lstrip().startswith("INSERT"))
    records = _inserted_records(insert_command)
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

    lock_sql = commands[0][0]
    assert "return_exposure_derived" in lock_sql
    assert "return_mapping_quality_failure" in lock_sql
    delete_sql = next(
        sql for sql, _ in commands
        if sql.lstrip().startswith("DELETE") and "return_exposure_derived" in sql
    )
    failure_delete_sql = next(
        sql for sql, _ in commands
        if sql.lstrip().startswith("DELETE") and "return_mapping_quality_failure" in sql
    )
    rebuild_sql = next(sql for sql, _ in commands if sql.lstrip().startswith("UPDATE"))
    for sql in (delete_sql, rebuild_sql):
        assert "mapping_type='return_exposure_derived'" in sql.replace(" ", "")
        assert "mapping_type IN" not in sql
        assert "exposure_quality_failure" not in sql
        assert "return_mapping_quality_failure" not in sql
    assert "mapping_type='return_mapping_quality_failure'" in failure_delete_sql.replace(" ", "")


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
    insert_command = next(command for command in commands if command[0].lstrip().startswith("INSERT"))
    record = _inserted_records(insert_command)[0]
    assert record["mapping_type"] == "return_mapping_quality_failure"
    assert record["quality_status"] == "failed"
    assert record["failure_reason"] == "no_return_exposure_with_sufficient_observations"
    assert record["mapping_method"] == "sw2_return_regression_v1"
    assert record["price_as_of_date"] == AS_OF_DATE
    assert "ON DUPLICATE KEY UPDATE" in insert_command[0]


def test_stateful_success_rerun_replaces_same_day_rows_on_one_connection() -> None:
    database = StatefulMappingDatabase()

    _persist_state(database, AS_OF_DATE, [_result("510001", 0.8, 0.7), _result("510002", 0.7, 0.6)])
    _persist_state(database, AS_OF_DATE, [_result("510003", 0.9, 0.8)])

    assert [(row["mapping_type"], row["etf_code"]) for row in database.rows] == [
        ("return_exposure_derived", "510003"),
    ]
    assert (database.connections, database.commits, database.rollbacks) == (2, 2, 0)


def test_stateful_failure_rerun_is_idempotent() -> None:
    database = StatefulMappingDatabase()

    _persist_state(database, AS_OF_DATE, [])
    _persist_state(database, AS_OF_DATE, [])

    assert len(database.rows) == 1
    assert database.rows[0]["mapping_type"] == "return_mapping_quality_failure"
    assert (database.connections, database.commits, database.rollbacks) == (2, 2, 0)


def test_stateful_failure_and_success_transitions_leave_one_event_kind() -> None:
    database = StatefulMappingDatabase()

    _persist_state(database, AS_OF_DATE, [])
    _persist_state(database, AS_OF_DATE, [_result("510001", 0.8, 0.7)])
    assert {row["mapping_type"] for row in database.rows} == {"return_exposure_derived"}

    _persist_state(database, AS_OF_DATE, [])
    assert {row["mapping_type"] for row in database.rows} == {"return_mapping_quality_failure"}
    assert len(database.rows) == 1


def test_stateful_out_of_order_events_rebuild_intervals_and_load_inside_interval() -> None:
    database = StatefulMappingDatabase()
    earlier = AS_OF_DATE - timedelta(days=4)

    _persist_state(database, AS_OF_DATE, [_result("510019", 0.9, 0.8)])
    _persist_state(database, earlier, [_result("510015", 0.8, 0.7)])

    rows_by_date = {row["effective_from"]: row for row in database.rows}
    assert rows_by_date[earlier]["effective_to"] == AS_OF_DATE - timedelta(days=1)
    assert rows_by_date[AS_OF_DATE]["effective_to"] is None
    effective = load_effective_return_etfs(
        "Semiconductors",
        2,
        earlier + timedelta(days=2),
        database.effective_query,
    )
    assert [row["etf_code"] for row in effective] == ["510015"]
    assert effective[0]["price_as_of_date"] == earlier


def test_stateful_insert_failure_rolls_back_all_mutations_on_the_single_connection() -> None:
    database = StatefulMappingDatabase()
    _persist_state(database, AS_OF_DATE, [_result("510001", 0.8, 0.7)])
    committed = copy.deepcopy(database.rows)
    database.fail_insert = True

    try:
        _persist_state(database, AS_OF_DATE, [_result("510002", 0.9, 0.8)])
    except RuntimeError as exc:
        assert str(exc) == "injected insert failure"
    else:
        raise AssertionError("insert failure must escape the transaction")

    assert database.rows == committed
    assert (database.connections, database.commits, database.rollbacks) == (2, 1, 1)


def test_weekend_event_accepts_last_trade_date_as_coherent_price_window_provenance() -> None:
    database = StatefulMappingDatabase()
    saturday = date(2026, 8, 22)
    friday = date(2026, 8, 21)

    _persist_state(database, saturday, [_result("510001", 0.8, 0.7)], price_date=friday)

    assert database.rows[0]["effective_from"] == saturday
    assert database.rows[0]["window_end_date"] == friday
    assert database.rows[0]["price_as_of_date"] == friday
    assert database.rows[0]["source_as_of_date"] == friday


def test_effective_return_loader_keeps_low_confidence_and_reads_full_provenance() -> None:
    captured: dict[str, object] = {}
    base = {
        "mapping_type": "return_exposure_derived",
        "quality_status": "qualified",
        "mapping_method": "sw2_return_regression_v1",
        "effective_from": AS_OF_DATE,
        "effective_to": None,
        "source_as_of_date": AS_OF_DATE,
        "source_provider": "local_trade_daily",
        "mapping_version": "return_v1",
        "config_hash": "cfg",
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


def test_effective_return_loader_rejects_row_with_incoherent_source_date() -> None:
    database = StatefulMappingDatabase()
    _persist_state(
        database,
        AS_OF_DATE,
        [_result("510001", 0.9, 0.8), _result("510002", 0.8, 0.7)],
    )
    database.rows[0]["source_as_of_date"] = AS_OF_DATE - timedelta(days=1)

    rows = load_effective_return_etfs(
        "Semiconductors",
        2,
        AS_OF_DATE,
        database.effective_query,
    )

    assert [row["etf_code"] for row in rows] == ["510002"]


def test_return_refresh_cli_uses_injected_local_pipeline_without_external_imports(
    monkeypatch,
    capsys,
) -> None:
    requested_date = date(2026, 8, 22)
    observed_date = date(2026, 8, 21)
    index = pd.bdate_range(end=observed_date, periods=61)
    loaded = ReturnMappingInput(
        as_of_date=requested_date,
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
    attempted_imports: list[str] = []

    def guarded_import(name, *args, **kwargs):
        attempted_imports.append(name)
        normalized = name.lower()
        if (
            any(token in normalized for token in ("akshare", "miniqmt", "xtquant"))
            or normalized == "providers"
            or normalized.endswith(".providers")
        ):
            raise AssertionError(f"external provider import attempted: {name}")
        return real_import(name, *args, **kwargs)

    monkeypatch.setattr(builtins, "__import__", guarded_import)
    module_name = "morning_conference.sector_rotation2.research.etf_core.refresh_return_mapping"
    sys.modules.pop(module_name, None)
    refresh_module = importlib.import_module(module_name)

    assert refresh_module.main(
        ["--as-of-date", "2026-08-22", "--level", "2", "--config-hash", "cfg"],
        load_input=loader,
        assessor=assessor,
        persist=persist,
        ensure_schema=lambda: None,
    ) == 0

    assert loader_calls == [(requested_date, 2, 60)]
    assert [call["args"][0] for call in persisted] == ["Sector A", "Sector B"]
    assert persisted[0]["price_source"] == "local_trade_daily"
    assert persisted[0]["window_end_date"] == observed_date
    assert persisted[0]["price_as_of_date"] == observed_date
    assert persisted[0]["universe_source"] == "local_domestic_equity_etf"
    assert persisted[1]["args"][3] == []
    output = capsys.readouterr().out
    assert "sectors=2" in output
    assert "etf_universe=2" in output
    assert "qualified=1" in output
    assert "low_confidence=1" in output
    assert "quality_failures=1" in output
    assert not any(
        any(token in name.lower() for token in ("akshare", "miniqmt", "xtquant"))
        or name.lower() == "providers"
        or name.lower().endswith(".providers")
        for name in attempted_imports
    )


def test_local_return_refresh_persists_both_confidence_events_and_blocks_low_confidence_candidate(
    monkeypatch,
    capsys,
) -> None:
    requested_date = date(2026, 8, 22)
    observed_date = date(2026, 8, 21)
    index = pd.bdate_range(end=observed_date, periods=61)
    loaded = ReturnMappingInput(
        as_of_date=requested_date,
        sector_closes={"Sector A": pd.Series(range(61), index=index)},
        etf_closes={"510001": pd.Series(range(61), index=index), "510002": pd.Series(range(61), index=index)},
        universe_codes=("510001", "510002"),
    )
    database = StatefulMappingDatabase()

    def loader(target_date: date, sector_level: int, window: int) -> ReturnMappingInput:
        assert (target_date, sector_level, window) == (requested_date, 2, 60)
        return loaded

    def assessor(_etfs, _sector, window: int, min_samples: int):
        assert (window, min_samples) == (60, 50)
        return [
            _result("510001", 0.9, 0.8),
            _result("510002", 0.8, 0.7, "low_confidence"),
        ], []

    real_import = builtins.__import__
    attempted_imports: list[str] = []

    def guarded_import(name, *args, **kwargs):
        attempted_imports.append(name)
        normalized = name.lower()
        if (
            any(token in normalized for token in ("akshare", "miniqmt", "xtquant"))
            or normalized == "providers"
            or normalized.endswith(".providers")
        ):
            raise AssertionError(f"external provider import attempted: {name}")
        return real_import(name, *args, **kwargs)

    monkeypatch.setattr(builtins, "__import__", guarded_import)
    module_name = "morning_conference.sector_rotation2.research.etf_core.refresh_return_mapping"
    sys.modules.pop(module_name, None)
    refresh_module = importlib.import_module(module_name)
    original_connection = mapping.get_connection
    mapping.get_connection = database.connect
    try:
        assert refresh_module.main(
            ["--as-of-date", "2026-08-22", "--level", "2", "--config-hash", "cfg"],
            load_input=loader,
            assessor=assessor,
            persist=persist_return_exposure_mapping,
            ensure_schema=lambda: None,
        ) == 0
    finally:
        mapping.get_connection = original_connection

    effective = load_effective_return_etfs(
        "Sector A",
        2,
        requested_date,
        database.effective_query,
    )
    assert [(row["etf_code"], row["confidence_status"]) for row in effective] == [
        ("510001", "qualified"),
        ("510002", "low_confidence"),
    ]
    assert {(row["mapping_type"], row["etf_code"]) for row in database.rows} == {
        ("return_exposure_derived", "510001"),
        ("return_exposure_derived", "510002"),
    }

    low_confidence = build_etf_candidate(
        as_of_date=requested_date,
        sector_level=2,
        sector_name="Sector A",
        etf_code="510002",
        sector_allowed=True,
        liquid=True,
        macd_evidence={"macd_triggered": True},
        extended=False,
        run_id="acceptance-run",
        mapping_metadata=effective[1],
    )
    assert low_confidence.candidate_status == "blocked"
    assert "low_return_exposure_confidence" in low_confidence.risk_flags_json
    assert "persisted_rows=2" in capsys.readouterr().out
    assert not any(
        any(token in name.lower() for token in ("akshare", "miniqmt", "xtquant"))
        or name.lower() == "providers"
        or name.lower().endswith(".providers")
        for name in attempted_imports
    )
