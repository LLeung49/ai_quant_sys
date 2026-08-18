# SW2 ETF Actual-Exposure Mapping Design

**Goal:** Derive each SW2 sector's Top3 ETF mappings from actual ETF constituent weights without TuShare.

**Architecture:** MiniQMT supplies the operational SW2 universe, ETF basket/constituents and daily market data. AKShare supplies a refreshable SW2 index/component cross-check. The mapping service normalizes stock codes, joins ETF constituent weights to SW2 memberships, aggregates exposure by `(as_of_date, sector, ETF)`, and persists only the Top3 eligible ETFs as effective-dated mappings.

## Contracts

- `Exposure(SW2, ETF) = sum(weight for ETF constituent whose normalized code belongs to SW2)`.
- Mapping rows record `effective_from`, `source_as_of_date`, `source_provider`, `exposure_weight`, `coverage_ratio`, `mapping_version`, and `config_hash`.
- Deterministic ranking is `exposure_weight DESC, coverage_ratio DESC, etf_code ASC`; retain Top3.
- A row is usable only when both SW2 and ETF constituent dates are present and the ETF weight coverage meets the configured minimum.

## Data Quality

- Missing SW2 membership, ETF constituents, or inconsistent as-of dates blocks the affected mapping.
- Insufficient ETF weight coverage is persisted as an auditable quality failure, never converted into a READY candidate.
- Historical runs are `BACKFILL`; only same-day operational runs may produce `LIVE_SHADOW` candidates.

## Integration

`trade_sector_etf_map` becomes a derived output owned by the exposure service. The ETF candidate runner reads only effective-dated rows from this table. Existing MACD, liquidity, and tracking-fit calculations remain independent evidence and do not alter exposure.

## Testing

Tests cover code normalization, weighted overlap, Top3 tie ordering, missing/insufficient coverage blocks, effective-date lookup, and immutable candidate persistence.
