# Targeted adaptive ETF studies v1

These three immutable `ExperimentSpec` inputs are local research studies. They
use `FULL_ADAPTIVE_SPEC` v1 and `BUY_AND_HOLD_SPEC` v1, request 2021-01-01 through
2026-09-11, and begin with CNY 100,000. `targeted_study()` binds each name to one
ETF; an alternative target raises `ValueError`. Nasdaq (`513100.SH`), S&P 500
(`513500.SH`), and A500 (`563360.SH`) are excluded from every study manifest.

## Evidence motivating the studies

The existing, unmodified source is
`reports/etf_validation_risk_adjusted_2026-09-11-evidence-gated/`. Its recorded
cutoff is 2026-09-10, within the requested as-of date; the directory date must
not be confused with the last observed market date.

| Study | Target | Historical observation and research question |
| --- | --- | --- |
| `hk_internet` | `513330.SH` | Historical annual-return excess +4.8872 percentage points, but `oos_evidence` blocks publication. Study whether grid spacing/sizing and exit/filter settings retain a stable training region. |
| `chinext_reentry` | `159915.SZ` | Historical annual-return excess -4.6626 percentage points and `oos_evidence` blocker. Study cooldown, stop distances, and entry filters as possible contributors to missed re-entry. |
| `star50_extreme_window` | `588000.SH` | Historical annual-return excess -10.8843 percentage points and `persistent_failure_evidence` blocker. Diagnose the largest contributor to the extreme lagging window before any parameter screening. |

These historical comparisons motivate hypotheses. They are not complete OOS
evidence, parameter recommendations, or proof of the hypotheses.

## Exact immutable parameter boundaries

All screened values come directly from `research/parameters.py`; no new value
is declared by these studies.

| Axis | Source constant | Exact values | Studies |
| --- | --- | --- | --- |
| `step_pct` | `GRID_STEPS` | 0.010, 0.015, 0.020, 0.025, 0.030, 0.035, 0.040, 0.045, 0.050, 0.055, 0.060 | hk_internet |
| `unit_pct` | `GRID_UNITS` | 0.05, 0.10, 0.15, 0.20 | hk_internet |
| `atr_stop_multiple` | `GRID_ATR_STOP_MULTIPLES` | 2.0, 3.0, 4.0 | all three |
| `cooldown_sessions` | `GRID_COOLDOWN_SESSIONS` | 0, 3, 5, 10 | all three |
| `stop_n` | `TREND_STOP_N` | 1.5, 2.0, 2.5, 3.0 | all three |
| `require_macd_bullish` | `TREND_REQUIRE_MACD_BULLISH` | False, True | hk_internet, chinext_reentry |
| `amount_ratio_min` | `AMOUNT_RATIO` | None, 1.0, 1.2, 1.5 | chinext_reentry |

The runner enumerates the Cartesian surface separately within each family,
without taking a Cartesian product across grid and trend families. Per training
window, `hk_internet` has 528 grid and 8 trend candidates; `chinext_reentry` has
12 grid and 32 trend candidates; STAR 50 would have 12 grid and 4 trend candidates
only after its diagnostic gate passes. This retains exact adjacent candidates
for every tuned numeric axis and both MACD choices. No legacy sizing axis is
silently tuned. The generic fixed-universe runner retains its existing plan.

Every field outside the declared axes stays frozen at the strategy spec:
grid step 0.02, unit 0.10, fixed initial allocation 0.50, one grid order per day,
ATR stop 3.0 and cooldown 5; trend stop 2.0, risk per unit 0.005, add distance 0.5,
maximum units 4, bullish MACD required and amount filter None. A field varies
only in studies that declare its axis. Cost remains commission 0.0001, minimum
commission CNY 5, slippage 3 bps, sell tax 0 and transfer fee 0.

Training retains the existing 504-session history, four training subperiods,
exact-neighbor stability rule and risk-adjusted candidate selection. All
parameter selection uses training data. Each subsequent validation replay uses
its previously selected configuration and the existing point-in-time price,
corporate-action, tradability, cost and next-session execution contracts.

## STAR 50 diagnostic gate

Before creating a provider or screening parameters, the CLI reads the existing
STAR 50 source directory and writes `diagnostic.json` under its own study
directory. It selects the most negative persisted window excess and requires
finite, reconciled `excess_attribution.json` contributors matching the recorded
`experiment_windows` attribution, with nonempty daily-state and NAV artifacts.
The source identity and cutoff must match STAR 50 and fall within the study's
date range. The diagnostic records hashes of the supporting source files.

The largest absolute return contributor is selected from `grid_return`,
`trend_return`, `transition_return`, and `cash_opportunity_cost`. Execution cost
is a separate currency diagnostic already included in NAV and cannot be added
again to return attribution. Trade counts, trade value, and a textual guess
cannot substitute for missing excess attribution. Missing, malformed, ambiguous,
or unreconciled evidence keeps `parameter_execution_allowed=false`; the CLI
returns exit code 4 before parameter execution.

Current evidence identifies `wf_003`, beginning 2024-08-22, with strategy return
0.0788418931 versus benchmark return 0.5878990933: excess -0.5090572002, or
-50.9057 percentage points. The legacy source lacks `excess_attribution.json`
and daily-state attribution. Its largest contributor remains unknown. The
parameter phase is blocked; no stop/cooldown change follows from this result.

## Reproduction and generated artifacts

Run from the repository root:

```powershell
$env:PYTHONPATH='src'
python -m pytest tests/asset_allocation/etf_adaptive/research/test_experiment.py::test_targeted_study_manifest_cannot_include_nonprioritized_code -q
python -m asset_allocation.etf_adaptive.run_instrument_validation --experiment hk_internet --start-date 2021-01-01 --as-of-date 2026-09-11 --output-dir reports/etf_adaptive_targeted_studies/hk_internet
python -m asset_allocation.etf_adaptive.run_instrument_validation --experiment chinext_reentry --start-date 2021-01-01 --as-of-date 2026-09-11 --output-dir reports/etf_adaptive_targeted_studies/chinext_reentry
python -m asset_allocation.etf_adaptive.run_instrument_validation --experiment star50_extreme_window --start-date 2021-01-01 --as-of-date 2026-09-11 --output-dir reports/etf_adaptive_targeted_studies/star50_extreme_window
```

Each directory contains `experiment.json`, including the complete strategy,
benchmark, dates, immutable allowed axes and canonical experiment hash.
Completed runner invocations publish instrument summaries and the existing
recorded-evidence report bundle under the single ETF subdirectory. Empty OOS
tables and attribution arrays are missing evidence, not successful results.
The blocked STAR 50 run publishes only its manifest and diagnostic artifact.

| Study | Experiment hash | Executed 2026-09-14 |
| --- | --- | --- |
| hk_internet | `d940e723f1ba1fa36fa356dd983d34b956357817819bf390b49e14c96d30ec02` | CLI exit 0; validation failed: `no_stable_training_parameters`; 0 OOS windows |
| chinext_reentry | `6f721bf8a905b5411da127bee4b8fdf0f386cdb3d71369075df7010c05a93bf2` | CLI exit 0; validation failed: `no_stable_training_parameters`; 0 OOS windows |
| star50_extreme_window | `5d4938b92e7ecd042148e509a8ee379b4265ed40b852c619037e5a41f4238405` | CLI exit 4; diagnostic blocked: `missing_largest_contributor_evidence` |

Hong Kong internet and ChiNext used the default database-backed, read-only
validation provider. Both stopped during training and therefore produced no
complete OOS evidence or parameter recommendation. Their failed-result artifacts
also lack a complete run manifest and candidate score surfaces; those gaps stay
explicit in the existing publication blockers. STAR 50 needed no new market-data
read because the persisted diagnostic gate failed first.

All generated reports remain uncommitted research evidence. Every study is
research-only, `trading_authorized=false`, and the current results are
`do_not_trade` with `activation_eligible=false`. No operation sheet is generated.
Persisted evidence gates and layer benchmark gates remain necessary for any
later activation; these studies do not authorize shadow promotion, broker
connections, or automatic orders. Pre-existing reports and diagnostics are
preserved.
