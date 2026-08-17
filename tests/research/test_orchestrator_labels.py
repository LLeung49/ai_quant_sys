from morning_conference.sector_rotation2.research.orchestrator.labels import (
    classify_short_term_direction,
    parse_short_term_labels,
)


def test_volume_only_is_neutral() -> None:
    assert classify_short_term_direction({"volume_spike"}) == "neutral"


def test_positive_and_negative_is_mixed() -> None:
    assert classify_short_term_direction({"pulse_up", "pulse_down"}) == "mixed"


def test_empty_labels_is_none() -> None:
    assert classify_short_term_direction(set()) == "none"


def test_csv_labels_are_normalized_to_a_set() -> None:
    assert parse_short_term_labels(" pulse_up, volume_spike, pulse_up ") == {"pulse_up", "volume_spike"}
