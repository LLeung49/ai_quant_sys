# ETF Diagnostic Research Mode Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a permanently non-authorizable ETF diagnostic run mode that continues OOS evaluation with a deterministic training-only fallback when formal stable-plateau selection fails.

**Architecture:** One data, training, execution, benchmark, attribution, and artifact pipeline remains shared. An explicit run mode controls only the missing-stable-plateau branch: formal mode preserves its early stop, while diagnostic mode records an unstable training selection and runs the immediately following OOS window. Report and CLI contracts force diagnostic artifacts to be non-promotable.

**Tech Stack:** Python 3, dataclasses/enums, pytest, JSON/CSV/Markdown artifacts.

**Spec:** `docs/superpowers/specs/2026-09-18-etf-diagnostic-research-mode-design.md`

## Global Constraints

- Formal selection, OOS isolation, costs, data-quality failures, drawdown/CVaR gates, shadow controls, and human review remain unchanged.
- Diagnostic fallback uses training data only and is frozen for only the following OOS window.
- Every diagnostic artifact sets `research_only: true`, `activation_eligible: false`, `shadow_run_eligible: false`, and `trading_authorized: false`.
- Diagnostic artifacts require a `research_diagnostic` output-path component and cannot enter freeze, shadow-run, or order authorization.
- ETF adjustment/corporate-action caveats are visible limitations only when the existing provider produced a valid non-forward-looking price series; fatal provider errors remain fatal.

## File Structure

- `src/asset_allocation/etf_adaptive/research/candidate_scoring.py`: deterministic fallback ranking.
- `src/asset_allocation/etf_adaptive/research/instrument_validation.py`: run mode, per-window selection metadata, continuation, and manifest.
- `src/asset_allocation/etf_adaptive/research/experiment.py`: immutable mode/provenance binding.
- `src/asset_allocation/etf_adaptive/research/validation_report.py`: diagnostic-safe decision, limitation, JSON/CSV/Markdown serialization.
- `src/asset_allocation/etf_adaptive/run_instrument_validation.py`: explicit CLI mode and path isolation.
- Corresponding `test_candidate_scoring.py`, `test_instrument_validation.py`, `test_validation_report.py`, and `test_run_instrument_validation.py`: TDD coverage.

### Task 1: Add deterministic training-only fallback ranking

**Files:**
- Modify: `src/asset_allocation/etf_adaptive/research/candidate_scoring.py`
- Test: `tests/asset_allocation/etf_adaptive/research/test_candidate_scoring.py`

**Produces:** `select_diagnostic_representative(scores: Sequence[TrainingCandidateScore]) -> TrainingCandidateScore | None`.

- [ ] Write tests proving unstable-but-complete scores select deterministically and scores with unavailable/invalid training metrics do not select.
- [ ] Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/research/test_candidate_scoring.py -q` — expect failure before implementation.
- [ ] Extract the current formal lexicographic rank tuple into `_selection_rank`; keep `select_stable_representative` stable-only and implement the diagnostic selector using only scores with `rejection_reason in (None, "outside_stable_plateau")` and valid metrics.
- [ ] Re-run the focused test; expect pass.
- [ ] Commit: `git commit -m "feat: rank ETF diagnostic training fallback"`.

### Task 2: Add run-mode contract and diagnostic OOS continuation

**Files:**
- Modify: `src/asset_allocation/etf_adaptive/research/instrument_validation.py`
- Test: `tests/asset_allocation/etf_adaptive/research/test_instrument_validation.py`

**Produces:** `ResearchRunMode` (`formal_validation`, `research_diagnostic`); `ValidationWindowResult.selection_status`, `.formal_selection_rejection`, `.training_selection_rank`; `run_instrument_validation(..., run_mode=ResearchRunMode.FORMAL_VALIDATION)`.

- [ ] Write tests proving formal mode still stops with `no_stable_grid_training_parameters`; diagnostic mode selects an unstable training candidate, has OOS NAV/events, and keeps `activation_eligible is False`; changing only OOS bars cannot change selected hash or rank.
- [ ] Run the focused test module; expect failure because the types and fields do not exist.
- [ ] Introduce the enum/defaults and pass mode through public/profile/private selection calls.
- [ ] On missing plateau, use the Task 1 selector only in diagnostic mode. Preserve candidate scores, set `selection_status="diagnostic_unstable_selection"`, preserve the formal rejection, and execute the next OOS window. If no complete score is rankable, return explicit `no_diagnostic_training_candidate`; do not substitute defaults.
- [ ] Preserve formal early return unchanged. Persist run mode and forced false diagnostic authorization fields in result manifest and result status.
- [ ] Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/research/test_instrument_validation.py -q` — expect pass.
- [ ] Commit: `git commit -m "feat: run ETF diagnostic OOS research mode"`.

### Task 3: Bind provenance and publish non-authorizable diagnostic reports

**Files:**
- Modify: `src/asset_allocation/etf_adaptive/research/experiment.py`
- Modify: `src/asset_allocation/etf_adaptive/research/validation_report.py`
- Test: `tests/asset_allocation/etf_adaptive/research/test_validation_report.py`

**Produces:** mode-bound experiment evidence; diagnostic summary fields; diagnostic-only conclusion vocabulary; serialized limitations.

- [ ] Write tests that a diagnostic summary has `run_mode`, all four non-authorizing flags, per-window selection metadata, and caveats; test a manifest changed to `trading_authorized=true` becomes an integrity blocker; test fatal data remains a diagnostic failure.
- [ ] Run the focused report module; expect failure before serialization changes.
- [ ] Bind run mode and authorization fields in experiment evidence. Reject mode/authorization disagreement rather than coercing it.
- [ ] Make publication return only `diagnostic_complete`, `diagnostic_data_rejected`, or `diagnostic_execution_failed` for diagnostic results; never formal `passed`/approval vocabulary.
- [ ] Add run mode/selection metadata to summary, windows CSV, candidate ledger, and Markdown. Add a `limitations` helper based on recorded provider provenance; never downgrade `DataQualityError`.
- [ ] Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/research/test_validation_report.py -q` — expect pass.
- [ ] Commit: `git commit -m "feat: publish non-authorizable ETF diagnostic evidence"`.

### Task 4: Expose the mode safely and regenerate controlled research

**Files:**
- Modify: `src/asset_allocation/etf_adaptive/run_instrument_validation.py`
- Test: `tests/asset_allocation/etf_adaptive/test_run_instrument_validation.py`
- Create generated, uncommitted reports under `reports/etf_round2_20260917/research_diagnostic/`.

**Produces:** `--run-mode {formal_validation,research_diagnostic}` (default formal), diagnostic path guard, mode-safe aggregate reports, and three controlled diagnostic reports.

- [ ] Write CLI tests that reject a diagnostic output directory lacking a `research_diagnostic` component and assert every aggregate diagnostic authorization flag is false.
- [ ] Run the CLI test module; expect failure before CLI support.
- [ ] Add the explicit option, parse to `ResearchRunMode`, reject ambiguous diagnostic paths before provider construction, pass mode to validation, and serialize mode/authorization fields to all aggregate artifacts.
- [ ] Run focused CLI tests and then `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive -q`; expect pass.
- [ ] Run three read-only-data diagnostic experiments for `513330.SH`, `159915.SZ`, and `588000.SH` with `grid_plus_optional_trend` into their mode-labeled directories.
- [ ] Verify each summary has `research_diagnostic`, false authorization fields, selection metadata, OOS/attribution or an explicit fatal diagnostic failure, and visible limitations.
- [ ] Commit code/tests only: `git commit -m "feat: expose explicit ETF diagnostic run mode"`.

## Plan Self-Review

- Tasks 1-2 preserve formal behavior while adding training-only fallback, OOS isolation, and fatal-error boundaries.
- Task 3 covers immutable non-authorization provenance, report vocabulary, integrity, and data caveats.
- Task 4 covers explicit caller intent, path separation, regression coverage, and the three requested research artifacts.
- No task permits a diagnostic result to become freeze-, shadow-, or trading-eligible.
