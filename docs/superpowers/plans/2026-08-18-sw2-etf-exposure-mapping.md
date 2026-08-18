# SW2 ETF Actual-Exposure Mapping Implementation Plan — Completed

**Goal:** Generate effective-dated SW2 Top3 ETF mappings from actual ETF constituent weights.

## Completed work

- [x] Normalize constituent codes and aggregate duplicate weights.
- [x] Rank ETFs deterministically by exposure descending, coverage descending, then ETF code; retain Top3.
- [x] Persist quality-auditable, effective-dated derived mappings; the ETF runner reads only derived mappings.
- [x] Add local SW2 membership, MiniQMT exact-basket, and strict AKShare disclosure adapters.

## Constraints retained

- TuShare is not used.
- Missing membership, constituents, alignment, units, provenance, or coverage becomes an auditable quality failure.
- Snapshot candidates remain SHADOW, MANUAL_ONLY, and immutable.

**Completion evidence:** commits `752b786`, `c40a034`, `7432756`, and `59eccf6`; provider contracts and ETF Core suite passed before the freshness follow-on.
