"""Rule status for SHADOW ETF candidates; never an order instruction."""


def select_candidate_status(
    *, sector_allowed: bool, liquid: bool | None, macd_triggered: bool, extended: bool | None,
) -> str:
    if liquid is None or extended is None:
        return "blocked"
    if not sector_allowed or not liquid:
        return "blocked"
    if not macd_triggered:
        return "wait_timing"
    if extended:
        return "extended"
    return "ready"
