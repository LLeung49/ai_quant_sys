from dataclasses import dataclass
from datetime import date
from enum import Enum

from morning_conference.sector_rotation2.research.config_hash import build_config_hash


def test_config_hash_is_order_independent() -> None:
    assert build_config_hash({"a": 1, "b": 2}) == build_config_hash({"b": 2, "a": 1})


def test_result_affecting_change_changes_hash() -> None:
    assert build_config_hash({"threshold": 0.5}) != build_config_hash({"threshold": 0.6})


def test_config_hash_normalizes_dataclasses_enums_dates_and_tuples() -> None:
    class Mode(str, Enum):
        SHADOW = "shadow"

    @dataclass(frozen=True)
    class Config:
        as_of_date: date
        values: tuple[int, ...]
        mode: Mode

    assert build_config_hash(Config(date(2026, 8, 17), (1, 2), Mode.SHADOW)) == build_config_hash(
        {"as_of_date": "2026-08-17", "values": [1, 2], "mode": "shadow"}
    )
