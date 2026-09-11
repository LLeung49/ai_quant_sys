# ETF Adaptive Strategy Lab Design

**Date:** 2026-09-12  
**Status:** approved design, awaiting implementation-plan review  
**Scope:** defensive base and broad-beta research only; no broker order submission.

## Goal

Turn the existing GRID/TREND engine into an auditable strategy laboratory that can
derive, compare and diagnose strategy variants without weakening the formal OOS
research or daily-advice gates.

The laboratory must answer two distinct questions:

1. Does a variant improve risk-adjusted OOS evidence relative to the same fair
   benchmark?
2. If it does not, was the cause a regime/mode decision, a stop/re-entry rule,
   execution cost, or deliberate time out of market?

## Evidence motivating this work

The 2026-09-11 evidence-gated run used the same selected configuration for every
formal target and every OOS window: GRID step 3.5%, unit 10%, initial allocation
60%; TREND risk 0.5%, add 0.75 ATR, 3 units, amount filter 1.2, MACD filter on,
and stop 2.5 ATR. The current stable-neighborhood rule chooses a midpoint of a
passing plateau, not a risk-adjusted training winner. This is safe against a
single peak but is not sufficient evidence of instrument-specific adaptation.

The run also showed lower drawdown/CVaR across most targets with material return
lag and frequent exits. `513330.SH` is the first research target because it has
positive annual excess and broad risk-adjusted improvement but only three of six
non-lagging OOS windows. `159915.SZ` and `588000.SH` follow because their risk
improvement is strong but their poor windows are concentrated and diagnosable.

## Invariants

- Preserve T+1 execution, raw/qfq coordinate rules, corporate-action handling,
  cost model, data audit, immutable configuration hash and no-look-ahead rules.
- A candidate is selected only from the training dates of its own walk-forward
  window. OOS dates never affect selection, screening, scoring or tie-breaking.
- Parameter stability remains a hard eligibility gate. A high-scoring isolated
  point is not production eligible.
- Reports and daily advice consume recorded results only. They never replay a
  strategy or construct hypothetical fills while reporting.
- A `passed` research conclusion is still necessary but not sufficient for an
  operation sheet; the existing layer approval, universe hash and current data
  checks remain mandatory.
- No automated brokerage order is in scope.

## Architecture

### 1. Strategy and benchmark policy contracts

Introduce explicit immutable `StrategySpec` and `BenchmarkSpec` contracts.
Each spec has a stable ID, version, config payload, capability flags and a
factory that supplies a decision policy to the existing engine. The engine owns
the session loop, state persistence, corporate actions and execution simulator;
the policy owns only close-time intent generation and fill-state transitions.

`FULL_ADAPTIVE` is implemented as a composed GRID/TREND policy. `GRID_ONLY` and
`TREND_ONLY` are true capability-restricted policies, not merely different
default configuration values. This prevents an inactive mode from becoming
active through regime transition.

`BUY_AND_HOLD` becomes a benchmark policy using the same execution simulator,
data range, eligibility and corporate-action path as the strategy. `FIXED_HALF`
must either be reimplemented with that simulator and an explicit rebalance
schedule or be retired from formal comparisons; hand-written, cost-free fills
are not a formal benchmark.

The existing `BaselineKind` remains a backward-compatible label during the
migration, but research execution is driven by the specifications. Every stored
run records both specs and their hashes.

### 2. Training candidate selection

Add a primitive-only `TrainingCandidateScore` for every candidate and training
subperiod. It records excess return, drawdown improvement, Sharpe, Sortino,
Calmar, CVaR improvement, turnover, cost drag, exposure, positive-subperiod
share and candidate configuration.

Selection is two-stage:

1. reject candidates outside the existing stability neighborhood or execution
   bounds;
2. among the stable plateau, select a deterministic risk-adjusted Pareto
   representative using, in order: higher positive-subperiod share, higher
   Sortino excess, higher Sharpe excess, lower cost drag, then a conservative
   configuration order as final tie-breaker.

The selected point, all screened points, the axes and the rejection reason are
persisted per training window. No aggregate weighted score may bypass a failed
metric or stability condition.

### 3. Event and opportunity-cost attribution

Extend recorded research artifacts with daily strategy state metadata: active
mode, target exposure, actual exposure, pending order, risk lock/cooldown and
the reason for each state change. Derive attribution from this recorded stream:

- GRID, TREND and GRID-to-TREND transition holding-period contribution;
- protective-stop and cooldown periods;
- cash-period opportunity cost versus the fair B&H path;
- commissions, slippage and rejected-order impact.

Attribution is explanatory, not a selector. Totals must reconcile to the
recorded strategy-versus-B&H NAV difference within a documented tolerance.

### 4. Experiment manifests and reports

Create an explicit `ExperimentSpec` for a bounded study: target IDs, strategy
spec, benchmark specs, allowed axes/ranges, training/OOS schedule, cost model
and data cutoff. Each experiment emits a manifest hash and a parameter-surface
artifact. Formal instrument reports add a decision-oriented diagnostic section
that names the largest contributor to excess return shortfall or improvement.

The report retains the current JSON, CSV, Markdown, daily NAV/exposure and
charts. It additionally exports candidate scores and attribution CSV/JSON.

## Targeted studies

Studies run sequentially, never as an all-ETF optimizer.

1. **513330.SH, Hong Kong internet:** vary GRID step/unit, GRID stop width and
   cooldown, then trend stop and MACD filter. Success requires at least four of
   six non-lagging OOS windows while retaining positive risk-adjusted evidence.
2. **159915.SZ, ChiNext:** investigate re-entry delay and trend participation by
   varying cooldown, grid stop and trend entry filters. The objective is better
   upside capture without losing the recorded drawdown advantage.
3. **588000.SH, STAR 50:** first diagnose the extreme underperforming window;
   only then test stop and transition variants associated with that diagnosis.
4. **Defensive dividend and CSI 300:** test only milder stop/re-entry variants
   after the three prioritized studies. They are a defensive validation group,
   not a return-maximization exercise.
5. **Nasdaq 100 and S&P 500:** retain B&H plus scheduled rebalancing as the
   formal comparison. Do not force them into this GRID/TREND optimization loop
   unless a separately approved structural hypothesis is supplied.
6. **A500:** reference-only until it supplies the required number of OOS windows.

No study can turn an existing failed result into an approved daily operation
sheet without a fresh formal layer evaluation.

## Acceptance criteria

- A test proves GRID-only never emits TREND intents and TREND-only never emits
  GRID intents, including when ADX changes regime.
- All formal benchmarks use the shared execution/cost/corporate-action path.
- Changing OOS prices cannot alter selected training configuration, candidate
  scores or plateau membership.
- The reported selected candidate is a member of the recorded stable plateau;
  a non-stable high scorer is rejected with an explicit reason.
- Mode/cash/cost attribution reconciles to recorded NAV excess and has no
  invented trade or state data.
- An experiment run records config, axes, data fingerprint, target universe,
  all candidate scores, decision and artifacts atomically.
- Existing formal approval and daily-advice gates fail closed for experiments
  without a passed layer result or with mismatched hashes.

## Non-goals

- No ETF universe expansion, portfolio optimizer, industry-momentum strategy
  or short-term trading strategy.
- No automatic order submission.
- No relaxation of OOS, stability, cost or research-approval gates to make a
  result pass.
