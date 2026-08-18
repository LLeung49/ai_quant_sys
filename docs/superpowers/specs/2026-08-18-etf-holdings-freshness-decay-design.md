# ETF Holdings Freshness-Decay Design

## Goal

Automate SW2-to-ETF exposure refreshes with periodically disclosed ETF holdings while making data age explicit.  Old holdings remain observable, but stale exposure can never produce an actionable ETF candidate.

## Source Hierarchy

1. **MiniQMT exact basket** is the preferred exposure source when the payload contains explicit constituent weights, a reported date, a weight unit, and an immutable source reference.
2. **AKShare disclosed holdings** are the normal exposure source.  Their periodic reporting date is preserved rather than relabeled as the refresh date.
3. **MiniQMT code-only baskets** are a universe/component cross-check only.  They cannot supply exposure weights.
4. MiniQMT remains the operational source for ETF universe, price, liquidity, and extension evidence.

The refresh chooses the complete usable basket with the smallest age.  It records every source used and any cross-check discrepancy in the mapping event metadata.

## Freshness and Candidate Policy

For a refresh date `D` and ETF holding disclosure date `H`:

- `age_days = max(0, (D - H).days)`.
- `freshness_confidence = 0.5 ** (age_days / 90)`.
- `fresh` when `age_days <= 90`.
- `aging` when `91 <= age_days <= 180`.
- `stale` when `age_days > 180`.

All three classes are persisted as exposure mappings when their weights, units, and provenance are valid.  `stale` mappings are visible and carry their computed exposure, but ETF candidates built from them are always `blocked` with a `stale_holdings` risk flag.  `fresh` and `aging` mappings can proceed to the existing liquidity, timing, and extension gates.

## Data Model

Qualified mapping rows retain their event date (`effective_from`) and add immutable holding provenance:

- `constituent_reported_date` (the provider’s holding disclosure date)
- `holdings_age_days`
- `freshness_status` (`fresh`, `aging`, `stale`)
- `freshness_confidence`
- `basket_source_priority` (`miniqmt_exact`, `akshare_disclosed`)
- optional cross-check status/detail for MiniQMT code-only comparison

`membership_as_of_date` remains the current refresh date because `trade_stock_status` is a current SW2 membership table.  The ETF holding date is intentionally allowed to precede it.  Mapping identity and candidate feature/config provenance include the reported date, freshness class, confidence, and source reference; they exclude mutable interval end dates.

## Refresh Flow

1. Load same-day SW2 members from `trade_stock_status`.
2. Load MiniQMT ETF universe and basket metadata.
3. Attempt a valid MiniQMT exact weighted basket.
4. If unavailable or older than a valid AKShare disclosed basket, automatically load AKShare holdings and choose the fresher complete source.
5. Calculate actual stock-weight overlap, rank Top3, and persist mappings with freshness metadata.
6. Persist quality failures only if no complete weighted basket is available.  A stale complete basket is not a quality failure.
7. Candidate runner reads mapping freshness and forces `blocked` for stale mappings before its normal execution-evidence gates.

## Safety Rules

- No equal-weight inference and no use of redemption quantities as portfolio weights.
- Provider reported date, weight unit, provider name, and source reference remain mandatory.
- No future holding disclosure date is accepted.
- Historical exposure refreshes are allowed only when SW2 membership can be supplied with a point-in-time membership provider; the current `trade_stock_status` provider remains live-date only.
- Refresh and candidate construction remain separate commands; neither invokes trading APIs.

## Acceptance Tests

- Fresher valid MiniQMT basket wins over AKShare; a valid fresher AKShare basket wins when MiniQMT is code-only or older.
- Freshness classification and confidence are deterministic at 0, 90, 91, 180, and 181 days.
- A periodic AKShare holding can create an `aging` or `stale` mapping without a same-day constituent date.
- `stale` mapping yields an ETF snapshot with `candidate_status='blocked'` and `stale_holdings` risk flag.
- Incomplete or unprovenanced baskets remain quality failures.
- Candidate hashes change when reported date, freshness class, confidence, or source reference changes.
