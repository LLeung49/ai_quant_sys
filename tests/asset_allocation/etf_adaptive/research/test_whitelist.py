"""Read-only effective-dated whitelist resolution."""

from __future__ import annotations

from datetime import date

import pytest

from asset_allocation.etf_adaptive.contracts import SubLayer
from asset_allocation.etf_adaptive.research.whitelist import WhitelistRepository


def _row(**overrides: object) -> dict[str, object]:
    row: dict[str, object] = {
        "exposure_id": "csi_dividend_low_vol",
        "sub_layer": SubLayer.DEFENSIVE_DIVIDEND_ETF.value,
        "primary_code": "515450.SH",
        "backup_code": "515080.SH",
        "effective_from": date(2020, 1, 1),
        "effective_to": None,
        "source_hash": "a" * 64,
        "valuation_multiplier": 1.0,
    }
    row.update(overrides)
    return row


def test_load_resolves_the_active_entry_for_the_requested_date() -> None:
    observed_params: list[tuple[object, ...]] = []

    def query(_: str, params: tuple[object, ...]) -> tuple[dict[str, object], ...]:
        observed_params.append(params)
        return (_row(),)

    entries = WhitelistRepository(query).load(date(2024, 6, 30))

    assert observed_params == [(date(2024, 6, 30), date(2024, 6, 30))]
    assert len(entries) == 1
    assert entries[0].exposure_id == "csi_dividend_low_vol"
    assert entries[0].primary_code == "515450.SH"


def test_load_rejects_duplicate_active_exposure() -> None:
    repository = WhitelistRepository(
        lambda _sql, _params: (
            _row(),
            _row(primary_code="563020.SH", backup_code="515450.SH"),
        )
    )

    with pytest.raises(ValueError, match="duplicate active exposure"):
        repository.load(date(2024, 6, 30))


def test_load_rejects_a_row_without_a_source_hash() -> None:
    repository = WhitelistRepository(
        lambda _sql, _params: (_row(source_hash=None),)
    )

    with pytest.raises(ValueError, match="source_hash"):
        repository.load(date(2024, 6, 30))


def test_load_rejects_a_row_without_a_backup() -> None:
    repository = WhitelistRepository(
        lambda _sql, _params: (_row(backup_code=None),)
    )

    with pytest.raises(ValueError, match="backup_code"):
        repository.load(date(2024, 6, 30))


def test_load_rejects_when_no_approved_mapping_is_active() -> None:
    repository = WhitelistRepository(lambda _sql, _params: ())

    with pytest.raises(ValueError, match="no active whitelist entries"):
        repository.load(date(2024, 6, 30))
