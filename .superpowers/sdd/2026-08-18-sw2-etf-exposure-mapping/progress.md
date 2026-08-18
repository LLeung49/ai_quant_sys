# SDD ledger — SW2 ETF actual-exposure mapping

| Task | Status | Evidence |
| --- | --- | --- |
| Constituent normalization | Complete | `752b786` |
| Exposure ranking | Complete | `c40a034` |
| Derived mapping persistence | Complete | `7432756` |
| Provider ingestion | Complete | `59eccf6` |

Ruling: ETF basket units are mandatory (`decimal` or `percent`); automatic inference is forbidden.

Ruling: schema migration is an explicit controlled deployment step, not a reader or daily-runner side effect.

Ruling: qualified mappings require exact provenance, explicit unit, and nonblank source provider/reference at every trust boundary.
