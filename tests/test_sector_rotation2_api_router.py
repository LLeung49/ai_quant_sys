"""板块轮动可视化 HTTP API 的契约测试。"""

from __future__ import annotations

from decimal import Decimal

import pytest
from fastapi.testclient import TestClient
from pymysql import MySQLError


def test_snapshot_returns_not_found_when_no_successful_snapshot(monkeypatch) -> None:
    """输入：不存在成功快照的日期；输出：404 和可读错误码。"""
    from morning_conference.sector_rotation2.api.app import create_app
    from morning_conference.sector_rotation2.api.repository import SectorRotationRepository

    monkeypatch.setattr(SectorRotationRepository, "load_snapshot", lambda *_: [])
    response = TestClient(create_app()).get(
        "/api/v1/sector-rotation/snapshot",
        params={"as_of_date": "2026-08-04", "level": 2, "model_version": "v1"},
    )

    assert response.status_code == 404
    assert response.headers["x-request-id"]
    assert response.json() == {
        "error": {
            "code": "SNAPSHOT_NOT_FOUND",
            "message": "未找到已成功运行的板块快照",
            "details": None,
            "request_id": response.headers["x-request-id"],
        }
    }


def test_snapshot_rejects_unsupported_sector_level() -> None:
    """输入：三级行业参数；输出：422，不应执行数据查询。"""
    from morning_conference.sector_rotation2.api.app import create_app

    response = TestClient(create_app()).get(
        "/api/v1/sector-rotation/snapshot",
        params={"as_of_date": "2026-08-04", "level": 3, "model_version": "v1"},
    )

    assert response.status_code == 422
    assert response.json()["error"]["code"] == "REQUEST_VALIDATION_ERROR"
    assert response.json()["error"]["request_id"] == response.headers["x-request-id"]


def test_available_dates_returns_successful_run_dates(monkeypatch) -> None:
    """输入：行业层级和模型版本；输出：前端可选的成功运行日期。"""
    from morning_conference.sector_rotation2.api.app import create_app
    from morning_conference.sector_rotation2.api.repository import SectorRotationRepository

    monkeypatch.setattr(SectorRotationRepository, "list_available_dates", lambda *_: ["2026-08-04", "2026-08-03"])
    response = TestClient(create_app()).get("/api/v1/sector-rotation/available-dates", params={"level": 2, "model_version": "v1"})

    assert response.status_code == 200
    assert response.json() == {
        "sector_level": 2,
        "model_version": "v1",
        "dates": ["2026-08-04", "2026-08-03"],
        "meta": {
            "run_status": "succeeded",
            "field_version": "v1",
            "source_max_trade_date": None,
            "eligible_sector_count": None,
            "skipped_sector_count": None,
            "market_regime": None,
            "regime_multiplier": None,
        },
    }


def test_snapshot_serializes_mysql_decimal_metrics_as_json_numbers(monkeypatch) -> None:
    """输入：含 MySQL Decimal 指标的快照行；输出：前端可直接运算的 JSON number。"""
    from morning_conference.sector_rotation2.api.app import create_app
    from morning_conference.sector_rotation2.api.repository import SectorRotationRepository

    monkeypatch.setattr(
        SectorRotationRepository,
        "load_snapshot",
        lambda *_: [{"sector_name": "教育", "composite_score": Decimal("0.73129092"), "velocity_score": Decimal("0.95")}],
    )
    response = TestClient(create_app()).get(
        "/api/v1/sector-rotation/snapshot",
        params={"as_of_date": "2026-08-04", "level": 2, "model_version": "v1"},
    )

    assert response.status_code == 200
    assert response.json()["sectors"][0]["composite_score"] == 0.73129092
    assert isinstance(response.json()["sectors"][0]["composite_score"], float)


def test_snapshot_returns_stable_run_metadata_without_leaking_internal_columns(monkeypatch) -> None:
    """输入：含运行审计字段的快照；输出：统一 meta，行业记录不暴露内部辅助字段。"""
    from morning_conference.sector_rotation2.api.app import create_app
    from morning_conference.sector_rotation2.api.repository import SectorRotationRepository

    monkeypatch.setattr(
        SectorRotationRepository,
        "load_snapshot",
        lambda *_: [{
            "sector_name": "半导体",
            "market_regime": "high_volatility",
            "regime_multiplier": Decimal("0.85"),
            "_source_max_trade_date": "2026-08-04",
            "_eligible_sector_count": 113,
            "_skipped_sector_count": 0,
        }],
    )
    response = TestClient(create_app()).get(
        "/api/v1/sector-rotation/snapshot",
        params={"as_of_date": "2026-08-04", "level": 2, "model_version": "v1"},
    )

    assert response.status_code == 200
    assert response.json()["meta"] == {
        "run_status": "succeeded",
        "field_version": "v1",
        "source_max_trade_date": "2026-08-04",
        "eligible_sector_count": 113,
        "skipped_sector_count": 0,
        "market_regime": "high_volatility",
        "regime_multiplier": 0.85,
    }
    assert all(not key.startswith("_") for key in response.json()["sectors"][0])


def test_sector_history_returns_standard_not_found_when_no_stored_points(monkeypatch) -> None:
    """输入：没有存储点的历史区间；输出：统一的 404 错误信封。"""
    from morning_conference.sector_rotation2.api.app import create_app
    from morning_conference.sector_rotation2.api.repository import SectorRotationRepository

    monkeypatch.setattr(SectorRotationRepository, "load_sector_history", lambda *_: [])
    response = TestClient(create_app()).get(
        "/api/v1/sector-rotation/sector-history",
        params=[("sector_name", "半导体"), ("start_date", "2026-07-01"), ("end_date", "2026-08-04")],
    )

    assert response.status_code == 404
    assert response.json()["error"]["code"] == "HISTORY_NOT_FOUND"


def test_sector_history_accepts_five_sector_names(monkeypatch) -> None:
    """输入：五个行业名称；输出：通过 HTTP 参数校验并一次传入仓储层。"""
    from morning_conference.sector_rotation2.api.app import create_app
    from morning_conference.sector_rotation2.api.repository import SectorRotationRepository

    captured: dict[str, object] = {}

    def fake_history(_self, sector_names, *_args):
        captured["sector_names"] = sector_names
        return [{"as_of_date": "2026-08-06", "sector_name": sector_names[0]}]

    monkeypatch.setattr(SectorRotationRepository, "load_sector_history", fake_history)
    sectors = ["半导体", "通信设备", "软件开发", "证券", "贵金属"]
    response = TestClient(create_app()).get(
        "/api/v1/sector-rotation/sector-history",
        params=[*(('sector_name', name) for name in sectors), ("start_date", "2026-07-01"), ("end_date", "2026-08-06")],
    )

    assert response.status_code == 200
    assert captured["sector_names"] == sectors


def test_sector_history_rejects_six_sector_names_before_repository(monkeypatch) -> None:
    """输入：六个行业名称；输出：422 且不访问仓储层。"""
    from morning_conference.sector_rotation2.api.app import create_app
    from morning_conference.sector_rotation2.api.repository import SectorRotationRepository

    monkeypatch.setattr(SectorRotationRepository, "load_sector_history", lambda *_: pytest.fail("六行业请求不应进入仓储层"))
    sectors = ["A", "B", "C", "D", "E", "F"]
    response = TestClient(create_app()).get(
        "/api/v1/sector-rotation/sector-history",
        params=[*(('sector_name', name) for name in sectors), ("start_date", "2026-07-01"), ("end_date", "2026-08-06")],
    )

    assert response.status_code == 422
    assert response.json()["error"]["code"] == "REQUEST_VALIDATION_ERROR"


@pytest.mark.parametrize("origin", ["http://localhost:5173", "http://127.0.0.1:5174"])
def test_api_allows_local_vite_origin_for_browser_requests(origin: str) -> None:
    """输入：本机任意 Vite 开发端口的 CORS 预检；输出：允许该源读取只读 API。"""
    from morning_conference.sector_rotation2.api.app import create_app

    response = TestClient(create_app()).options(
        "/api/v1/sector-rotation/snapshot",
        headers={"Origin": origin, "Access-Control-Request-Method": "GET"},
    )

    assert response.status_code == 200
    assert response.headers["access-control-allow-origin"] == origin


def test_database_failure_returns_stable_safe_error(monkeypatch) -> None:
    """输入：数据库连接异常；输出：503 稳定错误码，不向浏览器泄漏连接详情。"""
    from morning_conference.sector_rotation2.api.app import create_app
    from morning_conference.sector_rotation2.api.repository import SectorRotationRepository

    def fail_query(*_args) -> list[str]:
        raise MySQLError("password=secret; connection refused")

    monkeypatch.setattr(SectorRotationRepository, "list_available_dates", fail_query)
    response = TestClient(create_app(), raise_server_exceptions=False).get(
        "/api/v1/sector-rotation/available-dates",
        params={"level": 2, "model_version": "v1"},
    )

    assert response.status_code == 503
    assert response.json()["error"]["code"] == "DATABASE_UNAVAILABLE"
    assert "secret" not in response.text
    assert response.json()["error"]["request_id"] == response.headers["x-request-id"]


def test_replay_rejects_reversed_date_range_with_stable_error(monkeypatch) -> None:
    """输入：开始日晚于结束日；输出：422 稳定业务错误，且不访问仓储层。"""
    from morning_conference.sector_rotation2.api.app import create_app
    from morning_conference.sector_rotation2.api.repository import SectorRotationRepository

    monkeypatch.setattr(SectorRotationRepository, "load_replay", lambda *_: pytest.fail("非法区间不应执行查询"))
    response = TestClient(create_app()).get(
        "/api/v1/sector-rotation/replay",
        params={"start_date": "2026-08-05", "end_date": "2026-08-04", "level": 2, "model_version": "v1"},
    )

    assert response.status_code == 422
    assert response.json()["error"]["code"] == "INVALID_DATE_RANGE"


def test_unexpected_failure_still_returns_uniform_error_envelope(monkeypatch) -> None:
    """输入：未预料的服务端异常；输出：500 统一错误信封且不泄漏内部详情。"""
    from morning_conference.sector_rotation2.api.app import create_app
    from morning_conference.sector_rotation2.api.repository import SectorRotationRepository

    def fail_query(*_args) -> list[str]:
        raise RuntimeError("internal secret detail")

    monkeypatch.setattr(SectorRotationRepository, "list_available_dates", fail_query)
    response = TestClient(create_app(), raise_server_exceptions=False).get(
        "/api/v1/sector-rotation/available-dates",
        params={"level": 2, "model_version": "v1"},
    )

    assert response.status_code == 500
    assert response.json()["error"]["code"] == "INTERNAL_SERVER_ERROR"
    assert "secret" not in response.text
