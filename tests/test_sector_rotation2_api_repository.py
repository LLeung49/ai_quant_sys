"""板块轮动可视化只读查询仓储的契约测试。"""

from __future__ import annotations

import pytest


def test_load_snapshot_only_reads_successful_run_and_keeps_null(monkeypatch: pytest.MonkeyPatch) -> None:
    """输入：快照查询条件；输出：仅成功运行的快照及原始空值。"""
    from morning_conference.sector_rotation2.api.repository import SectorRotationRepository

    captured: dict[str, object] = {}

    def fake_execute_query(sql: str, params: tuple[object, ...]) -> list[dict[str, object]]:
        captured["sql"] = sql
        captured["params"] = params
        return [{"sector_name": "半导体", "velocity_score": None, "score_eligible": 1}]

    monkeypatch.setattr("morning_conference.sector_rotation2.api.repository.execute_query", fake_execute_query)

    result = SectorRotationRepository().load_snapshot("2026-08-04", 2, "v1")

    assert result == [{"sector_name": "半导体", "velocity_score": None, "score_eligible": 1}]
    assert "status = %s" in str(captured["sql"])
    assert "_source_max_trade_date" in str(captured["sql"])
    assert "_eligible_sector_count" in str(captured["sql"])
    assert "succeeded" in captured["params"]
    assert captured["params"][-3:] == ("2026-08-04", 2, "v1")


def test_load_sector_history_accepts_five_sectors(monkeypatch: pytest.MonkeyPatch) -> None:
    """输入：五个行业；输出：使用五个参数化占位符执行有界历史查询。"""
    from morning_conference.sector_rotation2.api.repository import SectorRotationRepository

    captured: dict[str, object] = {}

    def fake_execute_query(sql: str, params: tuple[object, ...]) -> list[dict[str, object]]:
        captured["sql"], captured["params"] = sql, params
        return []

    monkeypatch.setattr("morning_conference.sector_rotation2.api.repository.execute_query", fake_execute_query)
    sectors = ["半导体", "通信设备", "软件开发", "证券", "贵金属"]

    assert SectorRotationRepository().load_sector_history(sectors, "2026-07-01", "2026-08-06", 2, "v1") == []
    assert str(captured["sql"]).count("%s") == 10
    assert captured["params"][-5:] == tuple(sectors)


def test_load_sector_history_rejects_more_than_five_sectors() -> None:
    """输入：六个行业；输出：明确的参数异常，防止无界历史查询。"""
    from morning_conference.sector_rotation2.api.repository import SectorRotationRepository

    with pytest.raises(ValueError, match="最多只能查询 5 个行业"):
        SectorRotationRepository().load_sector_history(
            ["半导体", "通信设备", "软件开发", "证券", "贵金属", "教育"], "2026-07-01", "2026-08-04", 2, "v1"
        )


def test_load_snapshot_rejects_unsupported_sector_level() -> None:
    """输入：不支持的行业层级；输出：参数异常，不发起数据库查询。"""
    from morning_conference.sector_rotation2.api.repository import SectorRotationRepository

    with pytest.raises(ValueError, match="行业层级只能为 1 或 2"):
        SectorRotationRepository().load_snapshot("2026-08-04", 3, "v1")


def test_load_sector_kline_is_parameterized_bounded_and_ascending(monkeypatch: pytest.MonkeyPatch) -> None:
    """参数：行业、层级与截止日；返回：参数化的 350 根升序 K 线查询结果。"""
    from morning_conference.sector_rotation2.api.repository import SectorRotationRepository

    captured: dict[str, object] = {}

    def fake_execute_query(sql: str, params: tuple[object, ...]) -> list[dict[str, object]]:
        captured["sql"], captured["params"] = sql, params
        return []

    monkeypatch.setattr("morning_conference.sector_rotation2.api.repository.execute_query", fake_execute_query)
    result = SectorRotationRepository().load_sector_kline("半导体' OR 1=1", 2, "2026-08-06")

    assert result == []
    assert "trade_date <= %s" in str(captured["sql"])
    assert "ORDER BY trade_date DESC" in str(captured["sql"])
    assert "LIMIT %s" in str(captured["sql"])
    assert str(captured["sql"]).rstrip().endswith("ORDER BY trade_date ASC")
    assert captured["params"] == ("半导体' OR 1=1", 2, "2026-08-06", 350)
    assert "OR 1=1" not in str(captured["sql"])


def test_load_sector_kline_rejects_unsupported_sector_level_before_query(monkeypatch: pytest.MonkeyPatch) -> None:
    """参数：三级行业；返回：执行 SQL 前抛出 ValueError 异常。"""
    from morning_conference.sector_rotation2.api.repository import SectorRotationRepository

    def fail_execute_query(sql: str, params: tuple[object, ...]) -> list[dict[str, object]]:
        raise AssertionError("非法层级不应执行 SQL")

    monkeypatch.setattr("morning_conference.sector_rotation2.api.repository.execute_query", fail_execute_query)

    with pytest.raises(ValueError, match="行业层级只能为 1 或 2"):
        SectorRotationRepository().load_sector_kline("半导体", 3, "2026-08-06")


def test_load_sector_wave_prices_uses_current_members_and_bounded_dates(monkeypatch: pytest.MonkeyPatch) -> None:
    from morning_conference.sector_rotation2.api.repository import SectorRotationRepository

    captured = {}

    def fake_query(sql, params):
        captured.update(sql=sql, params=params)
        return []

    monkeypatch.setattr("morning_conference.sector_rotation2.api.repository.execute_query", fake_query)
    assert SectorRotationRepository().load_sector_wave_prices("半导体", 2, ["2026-08-03", "2026-08-10"]) == []
    assert "status.sector_2 = %s" in captured["sql"]
    assert "trade_stock_daily_qfq" in captured["sql"]
    assert "daily.trade_date IN (%s, %s)" in captured["sql"]
    assert captured["params"] == ("半导体", "2026-08-03", "2026-08-10")
    many_dates = [f"2026-{index // 28 + 1:02d}-{index % 28 + 1:02d}" for index in range(13)]
    assert SectorRotationRepository().load_sector_wave_prices("半导体", 2, many_dates) == []
    with pytest.raises(ValueError):
        SectorRotationRepository().load_sector_wave_prices("半导体", 2, many_dates + many_dates)


def test_list_available_dates_returns_only_successful_run_dates(monkeypatch: pytest.MonkeyPatch) -> None:
    """输入：层级与版本；输出：去重、倒序的成功运行日期。"""
    from morning_conference.sector_rotation2.api.repository import SectorRotationRepository

    captured: dict[str, object] = {}

    def fake_execute_query(sql: str, params: tuple[object, ...]) -> list[dict[str, object]]:
        captured["sql"], captured["params"] = sql, params
        return [{"as_of_date": "2026-08-04"}]

    monkeypatch.setattr("morning_conference.sector_rotation2.api.repository.execute_query", fake_execute_query)
    assert SectorRotationRepository().list_available_dates(2, "v1") == ["2026-08-04"]
    assert "status = %s" in str(captured["sql"])
    assert captured["params"] == ("succeeded", 2, "v1")


def test_load_calendar_availability_keeps_upstream_trade_dates_separate_from_successful_snapshots(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Break caught: deriving calendar trade days from successful snapshots hides pending upstream trading days."""
    from morning_conference.sector_rotation2.api.repository import SectorRotationRepository

    captured: list[tuple[str, tuple[object, ...]]] = []

    def fake_execute_query(sql: str, params: tuple[object, ...]) -> list[dict[str, object]]:
        captured.append((sql, params))
        if "FROM trade_sector_daily" in sql:
            return [{"trade_date": "2026-08-10"}, {"trade_date": "2026-08-11"}]
        return [{"as_of_date": "2026-08-10"}]

    monkeypatch.setattr("morning_conference.sector_rotation2.api.repository.execute_query", fake_execute_query)

    trade_dates, snapshot_dates = SectorRotationRepository().load_calendar_availability(
        2, "v1", "2026-08-10", "2026-08-11"
    )

    assert trade_dates == ["2026-08-10", "2026-08-11"]
    assert snapshot_dates == ["2026-08-10"]
    assert len(captured) == 2
    trade_sql, trade_params = captured[0]
    snapshot_sql, snapshot_params = captured[1]
    assert "trade_date BETWEEN %s AND %s" in trade_sql
    assert trade_params == (2, "2026-08-10", "2026-08-11")
    assert "status = %s" in snapshot_sql
    assert "as_of_date BETWEEN %s AND %s" in snapshot_sql
    assert snapshot_params == ("succeeded", "2026-08-10", "2026-08-11", 2, "v1")


def test_load_replay_bounds_date_range_and_only_reads_successful_runs(monkeypatch: pytest.MonkeyPatch) -> None:
    """输入：日期范围；输出：参数化的全市场历史快照。"""
    from morning_conference.sector_rotation2.api.repository import SectorRotationRepository

    captured: dict[str, object] = {}

    def fake_execute_query(sql: str, params: tuple[object, ...]) -> list[dict[str, object]]:
        captured["sql"], captured["params"] = sql, params
        return []

    monkeypatch.setattr("morning_conference.sector_rotation2.api.repository.execute_query", fake_execute_query)
    assert SectorRotationRepository().load_replay("2026-07-01", "2026-08-04", 2, "v1") == []
    assert "status = %s" in str(captured["sql"])
    assert captured["params"] == ("succeeded", "2026-07-01", "2026-08-04", 2, "v1")
