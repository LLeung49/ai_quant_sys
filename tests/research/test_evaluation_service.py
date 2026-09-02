from datetime import date, datetime

import pandas as pd

import pytest

from morning_conference.sector_rotation2.research.availability import AvailabilityBasis
from morning_conference.sector_rotation2.research.contracts import CandidateSnapshot, ResearchContext, ReturnStatus
from morning_conference.sector_rotation2.research.evaluation.calendar import TradingCalendar
from morning_conference.sector_rotation2.research.evaluation.prices import InMemoryPriceBarProvider, PriceBar
from morning_conference.sector_rotation2.research.evaluation.service import backfill_forward_labels, run_signal_evaluation
from morning_conference.sector_rotation2.research.status import SnapshotMode


def test_run_signal_evaluation_keeps_event_mode_and_coverage_counts() -> None:
    frame = pd.DataFrame({
        "signal_event_id": ["a", "a", "b"], "gc_offset": [0, 1, 0],
        "signal_date": [date(2026, 1, 5), date(2026, 1, 6), date(2026, 1, 5)],
        "forward_return": [0.1, 0.2, None],
    })
    header, metrics = run_signal_evaluation(frame, signal_family="macd", sampling_mode="event")
    assert header["candidate_count"] == 2
    assert header["return_complete_count"] == 1
    assert any(metric["metric_name"] == "mean_return" for metric in metrics)


def test_delayed_snapshot_after_open_defers_label_to_following_trade_day() -> None:
    dates = tuple(date(2026, 1, day) for day in range(5, 10))
    snapshot = CandidateSnapshot(
        as_of_date=dates[0], entity_type="stock", entity_code="000001.SZ", sector_level=2, sector_name="test",
        strategy_type="short_term", candidate_status="candidate", candidate_score=1.0, model_version="v1",
        config_hash="c1", run_id="run", snapshot_mode=SnapshotMode.DELAYED_SHADOW, snapshot_id=42,
        data_available_at=datetime(2026, 1, 5, 18), run_at=datetime(2026, 1, 6, 10),
        execution_eligible_at=datetime(2026, 1, 6, 10), availability_basis=AvailabilityBasis.MARKET_CLOSE_1800,
    )
    provider = InMemoryPriceBarProvider({("stock", "000001.SZ"): {
        dates[0]: PriceBar(dates[0], close=10),
        dates[2]: PriceBar(dates[2], close=12, open=11, high=13, low=10),
    }}, open_entities={"stock"}, ohlc_entities={"stock"})

    labels = backfill_forward_labels(
        snapshots=[snapshot], calendar=TradingCalendar(dates), provider=provider,
        context=ResearchContext(dates[0], 2, "v1", "c1", "evaluation"), horizons={"short_term": (1,)},
    )

    assert labels[0].entry_date == dates[2]


def test_delayed_snapshot_missing_availability_metadata_is_rejected() -> None:
    snapshot = CandidateSnapshot(
        as_of_date=date(2026, 1, 5), entity_type="stock", entity_code="000001.SZ", sector_level=2, sector_name="test",
        strategy_type="short_term", candidate_status="candidate", candidate_score=1.0, model_version="v1",
        config_hash="c1", run_id="run", snapshot_mode=SnapshotMode.DELAYED_SHADOW,
    )
    provider = InMemoryPriceBarProvider({}, open_entities={"stock"}, ohlc_entities={"stock"})

    with pytest.raises(ValueError, match="availability metadata"):
        backfill_forward_labels(
            snapshots=[snapshot], calendar=TradingCalendar([date(2026, 1, 5), date(2026, 1, 6)]), provider=provider,
            context=ResearchContext(date(2026, 1, 5), 2, "v1", "c1", "evaluation"), horizons={"short_term": (1,)},
        )


def test_delayed_sector_missing_availability_metadata_is_rejected() -> None:
    snapshot = CandidateSnapshot(
        as_of_date=date(2026, 1, 5), entity_type="sector_l2", entity_code="S1", sector_level=2, sector_name="test",
        strategy_type="sector_opportunity", candidate_status="candidate", candidate_score=1.0, model_version="v1",
        config_hash="c1", run_id="run", snapshot_mode=SnapshotMode.DELAYED_SHADOW,
    )
    provider = InMemoryPriceBarProvider({}, open_entities=set(), ohlc_entities=set())

    with pytest.raises(ValueError, match="availability metadata"):
        backfill_forward_labels(
            snapshots=[snapshot], calendar=TradingCalendar([date(2026, 1, 5), date(2026, 1, 6)]), provider=provider,
            context=ResearchContext(date(2026, 1, 5), 2, "v1", "c1", "evaluation"), horizons={"sector_opportunity": (1,)},
        )


def test_delayed_sector_uses_explicit_unsupported_label() -> None:
    dates = tuple(date(2026, 1, day) for day in range(5, 8))
    snapshot = CandidateSnapshot(
        as_of_date=dates[0], entity_type="sector_l2", entity_code="S1", sector_level=2, sector_name="test",
        strategy_type="sector_opportunity", candidate_status="candidate", candidate_score=1.0, model_version="v1",
        config_hash="c1", run_id="run", snapshot_mode=SnapshotMode.DELAYED_SHADOW,
        data_available_at=datetime(2026, 1, 5, 18), run_at=datetime(2026, 1, 6, 8),
        execution_eligible_at=datetime(2026, 1, 6, 9, 30), availability_basis=AvailabilityBasis.MARKET_CLOSE_1800,
    )
    provider = InMemoryPriceBarProvider({("sector_l2", "S1"): {dates[0]: PriceBar(dates[0], close=10)}}, open_entities=set(), ohlc_entities=set())

    labels = backfill_forward_labels(
        snapshots=[snapshot], calendar=TradingCalendar(dates), provider=provider,
        context=ResearchContext(dates[0], 2, "v1", "c1", "evaluation"), horizons={"sector_opportunity": (1,)},
    )

    assert labels[0].return_status is ReturnStatus.UNSUPPORTED_PRICE_WINDOW
    assert labels[0].forward_return is None


def test_exhausted_delayed_calendar_emits_not_matured_and_continues_batch() -> None:
    """A leading-edge delayed snapshot must not abort labels for other snapshots."""
    first, last = date(2026, 1, 5), date(2026, 1, 6)
    delayed = CandidateSnapshot(
        as_of_date=last, entity_type="stock", entity_code="000001.SZ", sector_level=2, sector_name="test",
        strategy_type="short_term", candidate_status="candidate", candidate_score=1.0, model_version="v1",
        config_hash="c1", run_id="delayed", snapshot_mode=SnapshotMode.DELAYED_SHADOW, snapshot_id=42,
        data_available_at=datetime(2026, 1, 6, 18), run_at=datetime(2026, 1, 6, 20),
        execution_eligible_at=datetime(2026, 1, 7, 9, 30), availability_basis=AvailabilityBasis.MARKET_CLOSE_1800,
    )
    historical = CandidateSnapshot(
        as_of_date=first, entity_type="stock", entity_code="000002.SZ", sector_level=2, sector_name="test",
        strategy_type="short_term", candidate_status="candidate", candidate_score=1.0, model_version="v1",
        config_hash="c1", run_id="backfill", snapshot_mode=SnapshotMode.BACKFILL, snapshot_id=43,
    )
    provider = InMemoryPriceBarProvider({("stock", "000002.SZ"): {
        first: PriceBar(first, close=10),
        last: PriceBar(last, close=11, open=10, high=12, low=9),
    }}, open_entities={"stock"}, ohlc_entities={"stock"})

    labels = backfill_forward_labels(
        snapshots=[delayed, historical], calendar=TradingCalendar([first, last]), provider=provider,
        context=ResearchContext(last, 2, "v1", "c1", "evaluation"), horizons={"short_term": (1,)},
    )

    assert [label.return_status for label in labels] == [ReturnStatus.NOT_MATURED, ReturnStatus.COMPLETE]
    assert [label.source_snapshot_id for label in labels] == [42, 43]


def test_delayed_sector_keeps_one_label_identity_when_calendar_later_matures() -> None:
    """Calendar maturity may update status, but must not create a second unique-key identity."""
    signal_date, entry_date = date(2026, 1, 5), date(2026, 1, 6)
    snapshot = CandidateSnapshot(
        as_of_date=signal_date, entity_type="sector_l2", entity_code="S1", sector_level=2, sector_name="test",
        strategy_type="sector_opportunity", candidate_status="candidate", candidate_score=1.0,
        model_version="v1", config_hash="c1", run_id="delayed", snapshot_mode=SnapshotMode.DELAYED_SHADOW,
        snapshot_id=99, data_available_at=datetime(2026, 1, 5, 18), run_at=datetime(2026, 1, 6, 9),
        execution_eligible_at=datetime(2026, 1, 6, 9, 30), availability_basis=AvailabilityBasis.MARKET_CLOSE_1800,
    )
    provider = InMemoryPriceBarProvider({("sector_l2", "S1"): {
        signal_date: PriceBar(signal_date, close=10),
        entry_date: PriceBar(entry_date, close=11),
    }})
    context = ResearchContext(signal_date, 2, "evaluation_v1", "config-a", "evaluation")

    immature = backfill_forward_labels(
        snapshots=[snapshot], calendar=TradingCalendar([signal_date]), provider=provider,
        context=context, horizons={"sector_opportunity": (1,)},
    )[0]
    matured = backfill_forward_labels(
        snapshots=[snapshot], calendar=TradingCalendar([signal_date, entry_date]), provider=provider,
        context=context, horizons={"sector_opportunity": (1,)},
    )[0]

    assert immature.return_status is ReturnStatus.NOT_MATURED
    assert matured.return_status is ReturnStatus.UNSUPPORTED_PRICE_WINDOW
    assert immature.price_basis == matured.price_basis == "delayed_shadow_requires_tradable_open"
