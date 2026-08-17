"""Normalize independent v2 labels into a direction without scoring them."""

from collections.abc import Iterable


POSITIVE_LABELS = frozenset({"pulse_up", "extreme_up", "limit_cluster", "short_rebound_candidate"})
NEGATIVE_LABELS = frozenset({"pulse_down", "extreme_down", "limit_panic", "short_breakdown_candidate"})
NEUTRAL_LABELS = frozenset({"volume_spike"})


def parse_short_term_labels(value: str | Iterable[str] | None) -> set[str]:
    if value is None:
        return set()
    if isinstance(value, str):
        return {label.strip() for label in value.split(",") if label.strip()}
    return {str(label).strip() for label in value if str(label).strip()}


def classify_short_term_direction(labels: str | Iterable[str] | None) -> str:
    normalized = parse_short_term_labels(labels)
    has_positive = bool(normalized & POSITIVE_LABELS)
    has_negative = bool(normalized & NEGATIVE_LABELS)
    if has_positive and has_negative:
        return "mixed"
    if has_positive:
        return "positive"
    if has_negative:
        return "negative"
    if normalized & NEUTRAL_LABELS:
        return "neutral"
    return "none"
