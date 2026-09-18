# ETF Diagnostic Research Mode Design

## Goal

Allow ETF research to produce useful, reproducible out-of-sample (OOS) evidence when a training window has no formal stable parameter plateau. The new mode is for diagnosis only: it must never create evidence for freezing, shadow running, order generation, or trading authorization.

## Problem

The current profile validation path treats a missing stable GRID plateau as a terminal failure. A candidate must beat or match buy-and-hold in at least 75% of four equal training subperiods and, for every tuned numeric axis, have passing immediate lower and upper neighbors. If one walk-forward window has no such interior plateau, the runner returns before producing later OOS, attribution, or comparative evidence.

That rule is appropriate for formal promotion, but it prevents research from answering whether the strategy mechanism has potential, which regimes fail, and whether instability comes from the parameter surface, stops, cooldowns, or the optional TREND module.

## Scope and non-goals

This change adds an explicit run-mode boundary to the ETF research runner and report contracts.

It does not:

- weaken formal-validation selection, OOS isolation, cost, drawdown, CVaR, shadow-run, or human-review gates;
- change the ETF universe, strategy profiles, execution model, price calendar requirements, or declared transaction costs;
- make any diagnostic result freeze-eligible, shadow-run eligible, or trading-authorized;
- repair or infer missing corporate actions or adjustment provenance.

## Run modes

### `formal_validation`

This is the current production-evidence route and remains the default for formal reports.

- Every selection family required by the profile must produce a stable plateau candidate.
- A missing plateau returns the existing failed result (`no_stable_grid_training_parameters` for the optional-trend profile) and does not create executable OOS strategy evidence.
- Only this mode can contribute to the existing formal research decision. It still requires all downstream evidence, shadow-run controls, and human review; passing this mode alone does not authorize trading.

### `research_diagnostic`

This is a research-only route. It shares the same data provider, calendar checks, indicators, transaction-cost model, execution semantics, rolling windows, benchmarks, and report calculations as formal validation.

For every walk-forward window:

1. Training uses only that window's training dates, exactly as in formal validation.
2. If a stable candidate exists, select it using the unchanged formal stable-candidate ranking and record `selection_status: stable`.
3. If no stable candidate exists, select the highest-ranked training candidate from the declared candidate set, using the existing deterministic ranking fields but without plateau membership as a prerequisite. Record `selection_status: diagnostic_unstable_selection` and the formal rejection reason.
4. Freeze that selected configuration for only the following OOS window. OOS data cannot alter the selected configuration, the candidate rank, or its instability label.
5. Run OOS and write the same strategy, benchmark, cost, exposure, daily NAV, trade, state, and attribution evidence as a completed formal window.

The fallback is not a hidden relaxation of formal selection. It is an explicit diagnostic selection rule whose output is permanently non-promotable.

## Authorization boundary

Every diagnostic result, report, manifest, and publication decision must carry all of the following immutable values:

```json
{
  "run_mode": "research_diagnostic",
  "research_only": true,
  "activation_eligible": false,
  "shadow_run_eligible": false,
  "trading_authorized": false
}
```

No CLI option, report edit, profile declaration, experiment identifier, or downstream publication helper may override these values. A diagnostic result must be rejected if passed to a freeze, shadow-run, or order-authorization interface. Formal and diagnostic artifacts must use different report output directories or an explicit mode path component, so an operator cannot mistake one for the other.

## Data-quality boundary

The following conditions remain fatal in both modes: missing or misaligned price bars, invalid trading calendar, invalid training/OOS boundary, future-data contamination, missing execution/cost model, invalid experiment/profile identity, or incomplete report provenance.

ETF adjustment provenance or corporate-action completeness may be reported as a non-fatal `limitations` item only when the existing provider can otherwise construct a valid, non-forward-looking dual-price series. The limitation must include the affected field/source and state that the result is research-only and not production-grade audit evidence. A diagnostic mode must not suppress a fatal data-quality error.

## Reporting contract

The report and JSON manifest must show, per window:

- `run_mode`, profile identity/hash, experiment identity/hash, and data cutoff;
- selected configuration/hash and training-only selection rank;
- `selection_status`, whether a formal plateau existed, and the precise formal rejection reason when it did not;
- candidate-score ledger, including stability membership and rejection reasons;
- strategy and declared benchmark OOS metrics, daily NAV, trades, costs, exposure, and mode observations;
- GRID, TREND, switching, protective-exit, cash/opportunity-cost, and execution-cost attribution where required by the profile;
- `limitations` and the non-authorization declaration above.

The report conclusion vocabulary is separate from formal pass/fail. Diagnostic conclusions may describe observed evidence such as `diagnostic_complete`, `diagnostic_data_rejected`, or `diagnostic_execution_failed`; they must not say `passed`, `approved`, `eligible`, or `ready_for_shadow_run`.

## Error handling

- Formal mode preserves its early-stop behavior when a required stable candidate is absent.
- Diagnostic mode continues only for a missing stable plateau. It must still stop with a non-authorizable diagnostic failure on any fatal data, execution, provenance, or report-integrity error.
- If the declared candidate set has no scoreable training candidate, diagnostic mode fails with an explicit `no_diagnostic_training_candidate` reason; it may not substitute a default configuration.
- Benchmark and attribution failures remain failures. A partial diagnostic report may preserve already-computed window evidence, but cannot present a positive conclusion.

## Compatibility

Existing named experiments and CLI invocations retain formal behavior unless the caller explicitly chooses `research_diagnostic`. Existing formal report schemas remain compatible; added mode and selection fields are additive. The existing `grid_core`, `grid_plus_optional_trend`, and `core_hold_rebalance` profile definitions remain unchanged.

## Testing and acceptance

- Formal regression: a missing plateau still fails before OOS exactly as today.
- Diagnostic selection: the same input with no plateau produces a deterministic training-only fallback, marks it `diagnostic_unstable_selection`, and runs its OOS window.
- Isolation: modifying OOS bars cannot change the diagnostic selected configuration, rank, or training rejection reason.
- Authorization: every diagnostic output has all four false/non-authorizing fields; freeze, shadow, and trading paths reject it.
- Integrity: fatal calendar/data/provenance/execution failures reject both modes; permitted ETF provenance caveats appear in `limitations` without being misrepresented as clean audit evidence.
- Reporting: formal and diagnostic artifacts cannot share an ambiguous path; diagnostic conclusions cannot use formal approval vocabulary.
- Regression: the focused ETF adaptive test suite and a regenerated diagnostic report for 513330.SH, 159915.SZ, and 588000.SH pass the contract checks.

## Rollout

1. Implement and test the run-mode contract without changing formal output.
2. Run diagnostic research for 513330.SH, 159915.SZ, and 588000.SH in a dedicated mode-labeled report directory.
3. Review the OOS and attribution evidence to propose bounded, profile-specific parameter experiments.
4. Any later formal-parameter or shadow-run decision requires a new, separately approved formal validation run.
