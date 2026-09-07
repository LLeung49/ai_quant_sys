# ETF Adaptive Production Completion Design

## Purpose

Complete the production boundaries left open by the ETF adaptive strategy
plans: an executable research pipeline, a freezeable research selection,
durable daily shadow execution, and durable readiness verification.  The
system continues to emit advice only; it never imports or exposes brokerage
order placement.

## Research pipeline

`run_research` will build a real read-only data provider, enumerate the
approved parameter families, run walk-forward backtests and baselines, select
products and portfolios, and create one `ResearchArtifact` from those results.
Its CLI will return a non-zero exit status for unavailable data, failed runs,
or artifact publication failure.  Dependency injection remains available only
for tests and controlled integrations.

## Research-to-freeze contract

The research manifest will contain a `frozen_selection` payload: selection
identity, canonical selection hash, selected targets, layer weights, research
cutoff, activation date, review date, and the strategy config payload/hash.
`FrozenSelection.from_research_manifest` will load this payload and validate
its canonical selection hash independently of the strategy config hash.  This
prevents a report from being activated if either its holdings or its parameter
identity was modified.

## Daily shadow operation

The daily CLI will construct the repository market-data provider and a MySQL
shadow store, load an already activated frozen selection, invoke
`run_shadow_date`, persist the run transactionally, then print canonical JSON.
The CLI will reject manual configuration injection: activation is a separate,
auditable operation.  The callable orchestration remains deterministic and
has no brokerage dependencies.

## Readiness verification

The verification CLI will use the MySQL shadow store, retrieve persisted runs
and health checks for the requested period, parse optional observed-fill JSON,
evaluate every readiness gate, print a structured JSON result, and exit zero
only if every gate passes.  It does not treat readiness as authorization to
place orders.

## Artifact publication

Artifacts are fully written and validated in a sibling staging directory.
Publishing uses a recoverable replacement sequence: retain the prior output
until the staging directory is complete, rename it to a sibling backup, rename
staging into the destination, then remove the backup.  If activation fails,
restore the backup.  Staging and backup cleanup supports nested directories.

## Verification

Tests will cover default-provider wiring through injectable factories, real
manifest-to-freeze loading, daily and readiness CLI service wiring, observed
fill parsing, atomic-replacement rollback, and the existing full adaptive ETF
suite.  No test requires a live database; adapters are substituted at the
boundary.
