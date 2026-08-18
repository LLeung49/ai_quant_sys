# SDD ledger — ETF holdings freshness decay

| Task | Status | Evidence |
| --- | --- | --- |
| Holdings freshness persistence | Complete | `bb09233` |
| Automatic source selection | Complete | `6099f54`, hardened by `63ec6bb` |
| Stale candidate gate | Complete | `90ab7d4` |
| Automated refresh acceptance | Complete | `bdf52b0` |

Ruling: `constituent_as_of_date` is the mapping refresh date; `constituent_reported_date` is the disclosed holdings date.

Ruling: automatic selection first requires each ETF basket to meet refresh `min_coverage`, then favors the newest disclosure; complete MiniQMT exact data wins equal-date ties over AKShare.

Final verification: 121 ETF Core tests passed on 2026-08-18. Final review approved fallback, coverage-first selection, and cross-source checks.
