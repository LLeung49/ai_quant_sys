# ETF Holdings Freshness-Decay Implementation Plan — Completed

**Goal:** Automatically derive SW2 ETF exposure from MiniQMT exact baskets or AKShare periodic holdings, retain stale mappings, and block stale ETF candidates.

## Completed work

- [x] Model and persist disclosure date, age, freshness class, decay confidence, and source priority.
- [x] Automate MiniQMT/AKShare retrieval; require explicit MiniQMT provenance and use code-only data only for cross-checking.
- [x] Select only sources whose every ETF basket meets `min_coverage`; then prefer newer disclosure dates and MiniQMT exact baskets on equal dates.
- [x] Persist complete stale mappings but force resulting ETF candidates to `blocked` with `stale_holdings`.
- [x] Add automatic refresh summaries for chosen source and `fresh` / `aging` / `stale` / `quality_failure` counts.

## Constraints retained

- `freshness_confidence = 0.5 ** (age_days / 90)`; fresh `<=90`, aging `91..180`, stale `>180`.
- `trade_stock_status` remains current-day membership only; historical refresh requires PIT membership.
- No equal-weight inference, trading API, or order action.

**Completion evidence:** commits `bb09233`, `6099f54`, `90ab7d4`, `bdf52b0`, and `63ec6bb`; 121 ETF Core tests passed on 2026-08-18.
