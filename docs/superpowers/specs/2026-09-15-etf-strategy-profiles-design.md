# ETF Strategy Profiles Design

## Goal

Make ETF research profile-driven so that any future industry ETF can use a declared, versioned strategy profile without copying strategy logic. The three profiles are mutually exclusive: `grid_core`, `grid_plus_optional_trend`, and `core_hold_rebalance`.

## Scope and non-goals

This change changes research selection, validation, provenance, and reporting. It does not authorize a live order, relax the existing OOS, cost, drawdown/CVaR, shadow-run, or human-review gates, or alter the ETF universe automatically.

## Architecture

`StrategyProfileSpec` is a new immutable research declaration. It owns a profile id, version, the executable strategy or benchmark specification, parameter-selection policy, and required evidence. `ExperimentSpec` records the profile declaration and its hash, so reports for industry ETFs remain comparable and reproducible.

```text
Validation target -> declared profile -> profile-specific training selection
                                      -> one executable configuration
                                      -> integrated OOS + attribution
                                      -> fail-closed publication/activation gates
```

Profiles are assigned explicitly in the experiment manifest. A future industry ETF must name a profile; it receives no implicit profile and no automatic trade authority.

## Profiles

### `grid_core` v1

- Executes the existing `GRID_ONLY_POLICY` through a versioned `StrategySpec`.
- Screens and freezes only GRID axes; TREND configuration is not selected or scored.
- Runs GRID-only OOS against buy-and-hold and fixed-half rebalancing benchmarks.
- Primary pass evidence is the integrated GRID-only OOS series: stable windows, return/risk, drawdown, CVaR, cost, reproducibility, and execution evidence.
- Intended initial research assignment: dividend, low-volatility dividend, CSI 300, and range-bound industry ETF candidates.

### `grid_plus_optional_trend` v1

- Executes the existing `FULL_ADAPTIVE_POLICY` through a versioned `StrategySpec`.
- Screens and freezes GRID axes. TREND uses the profile's immutable conservative `TrendConfig`; it is never silently optimized when its standalone ratios are unavailable.
- Primary pass evidence is the integrated FULL_ADAPTIVE OOS series, not a standalone TREND Sharpe/Sortino threshold.
- Every OOS window must record attribution and mode observations. Missing trend attribution is a fail-closed research blocker. Low trend participation is diagnostic evidence, not an automatic rejection.
- The report records trend active-session count, contribution, incremental execution cost, and contribution to drawdown/CVaR. Activation still requires a human review of these fields after the ordinary OOS gate and shadow run; this profile alone cannot activate trading.
- Intended initial research assignment: ChiNext, STAR 50, Hang Seng Technology, Hang Seng Internet, and regime-sensitive industry ETF candidates.

### `core_hold_rebalance` v1

- Executes the existing deterministic buy-and-hold and fixed-half rebalancing specifications; it does not invoke the adaptive engine or parameter sweep.
- Compares the two declared long-term core implementations using the same market data, costs, OOS boundaries, provenance, and report format.
- No adaptive parameter-selection or mode-attribution claim is made.
- Intended initial research assignment: Nasdaq 100, S&P 500, and future industry ETFs whose adaptive profile fails and whose long-horizon holding thesis is being evaluated.

## Selection and validation rules

1. A profile produces exactly one executable configuration or benchmark declaration per walk-forward window. It is invalid to merge GRID parameters from one profile with TREND parameters from another.
2. `grid_core` does not create, score, or require a TREND candidate.
3. `grid_plus_optional_trend` may use a low-activity TREND module, but must publish complete integrated OOS and attribution evidence. Undefined standalone ratios are reported as diagnostics only.
4. `core_hold_rebalance` has no parameter surface. It is evaluated as a deterministic reference strategy, not promoted through adaptive selection.
5. All profiles remain fail-closed: a missing config, benchmark provenance, OOS window, cost record, attribution required by the profile, execution evidence, shadow evidence, or human approval yields `do_not_trade`.

## Reporting and provenance

Every summary and run manifest records `profile_id`, `profile_version`, `profile_hash`, selected config or benchmark declaration, and the exact profile evidence policy. Candidate-score CSVs are emitted only for profiles with a parameter surface.

For `grid_plus_optional_trend`, reports additionally expose per-window and stitched TREND diagnostics: active sessions, contribution, execution cost, and drawdown/CVaR contribution. These fields must be present, not inferred from missing values.

## Error handling

- Unknown, undeclared, or incompatible profile assignment raises an error before market data is read.
- A profile that cannot produce its one executable declaration returns a research failure with a profile-specific blocker, never a fallback configuration.
- An industry ETF with insufficient history stays `data_rejected`; profile assignment does not change history requirements.
- Existing legacy `FULL_ADAPTIVE`, `GRID_ONLY`, `TREND_ONLY`, B&H, and fixed-half baselines remain supported for historical reports and regression tests.

## Testing and acceptance

- Unit tests verify immutable profile hashes, valid/invalid profile assignments, and that profile selection cannot read OOS data.
- Engine tests prove `grid_core` emits no TREND order reasons and `core_hold_rebalance` emits no adaptive orders.
- Validation tests prove undefined standalone TREND ratios do not reject an otherwise complete optional-trend integrated result, while missing attribution does reject it.
- Report tests verify profile provenance and required optional-trend diagnostics.
- The full ETF suite must pass before any regenerated research report is accepted.

## Rollout

- [x] Ship profile abstractions and tests with no change to current live/shadow selection. The research CLI now requires an explicit `--profile` for every named experiment; a new experiment name must also provide a `--stock-code` from the fixed validation manifest. The historical fixed-universe route remains explicitly `legacy_unprofiled`, research-only, and fail-closed.
- [ ] Run profile-specific research reports for the fixed ETF universe, storing results in a new report directory.
- [ ] Review report evidence and separately approve any future shadow-run candidate. No profile auto-authorizes real trading.
