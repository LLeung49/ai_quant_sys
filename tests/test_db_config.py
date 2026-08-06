"""数据库配置文件发现规则的回归测试。"""

from __future__ import annotations

from data_ingestion import db_config


def test_resolve_env_path_prefers_explicit_environment_file(monkeypatch, tmp_path) -> None:
    """显式指定配置文件时，应优先使用该文件。

    输入：pytest 提供的临时目录和环境变量替换器。
    输出：断言返回的配置文件路径与 ``AI_QUANT_ENV_FILE`` 一致。
    """
    expected = tmp_path / "database.env"
    expected.write_text("WUCAI_SQL_HOST=example.test\n", encoding="utf-8")
    monkeypatch.setenv("AI_QUANT_ENV_FILE", str(expected))

    assert db_config.resolve_env_path() == expected
