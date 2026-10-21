# Financial PIT recovery completion

User authorization: complete the financial recovery, historical Repair Alpha reconstruction, dependent-output isolation and daily/API/Web acceptance. Preserve existing dirty changes; no commits requested.

## Work plan

- [x] Reconcile the 102-stock publish and two-stock recovery against database inserts and archives.
- [x] Verify the historical snapshot backup SHA-256.
- [x] Archive 1,752,210 forward labels, six evaluations and 120 metrics with SHA-256 manifests.
- [x] Verify transactional linked-label cleanup and insert-error rollback: two focused tests pass; cleanup test failed before implementation.
- [x] Dry-run and commit 2024-01-02 pilot: 713 old / 700 new candidates.
- [x] Rebuild 636 of 637 historical backfill dates; completion evidence is the JSONL ledger and transactional database markers. The remaining 2026-08-27 has no backfill sector input, so its 671 old candidates are rejected and preserved for audit.
- [x] Isolate 15,804 invalid shadow snapshots, 4,356 linked labels and all six stale repair evaluations with 120 metrics, preserving archives and original live provenance. Three backfill headers and 60 metrics were briefly restored from archive for review, then removed because their statistics still reflected obsolete labels.
- [x] Rebuild forward labels for valid reconstructed backfill snapshots. All 32 monthly ledger months succeeded, adding 1,706,922 labels; January 2024 added 28,800 separately. Database join confirms 578,574 valid snapshots and exactly 578,574 labels per 10, 20 and 40 day horizon, 1,735,722 total.
- [x] Rebuild Repair Alpha backfill evaluation aggregates from corrected labels. Three active headers have 20 metrics each. Candidate count per horizon: 578,574; complete returns: 10d 578,126, 20d 578,127, 40d 571,885.
- [x] Audit PIT coverage, archive integrity, historical replacement and downstream metadata. Final read-only evidence: recovery-verification-20261020.json.
- [x] Verify historical Repair Alpha API responses and current market prerequisite. The 2026-10-20 raw market table is empty, so same-day live run and UI point inspection remain externally blocked.
- [x] Run Python and Web gates and document verified outcomes and remaining gaps. Final Python suite: 1,695 passed, one skipped, one existing deprecation warning. Earlier Web suite: 277 passed; build succeeded. Final checkout diff --check found no whitespace errors.

## Evidence and decisions

- Original batch: 3,999 financial + 4,485 capital inserts. Two-stock recovery: 83 financial + 82 capital inserts. Both recovered codes have archived financial and capital responses.
- Snapshot backup: repair-all-pre-full-rebuild-20261020.manifest.json, 614,282 rows, SHA-256 verified.
- Dependency archive: repair-dependencies-20261020/manifest.json, verified before replacement.
- Existing old live/delayed snapshots must never be relabelled as historical live observations after recomputation.
- Current runner scores each day before transactional deletion and insertion; old linked labels are removed in that same transaction.
- The full 637-date target has 636 successfully rebuilt dates. One date, 2026-08-27, lacks backfill sector snapshots; its 671 old candidates were marked rejected. No live-shadow input was reclassified as backfill.
- The historical runner encountered an InnoDB table expansion failure when D: had 6.2 GB free. The failed date rolled back; after the user freed space, a single-day retry and the resumed run succeeded. D: later had 25.7 GB free.
- Latest full Python suite before scoped evaluation-runner changes: 1,691 passed, one skipped. Scoped runner focused suite: 16 passed. Earlier Web suite: 277 passed; build succeeded.
- Final read-only audit currently reports 4,574 AKShare financial PIT rows, 303,412 QMT native financial rows, 4,630 AKShare and 302,971 QMT capital rows; all strict financial date/core/metric checks are zero. The eleven AKShare zero circulating-share rows are retained pending source interpretation; no nonpositive total shares were found. Historical API checks: 2024-01-02=700, rejected 2026-08-27=0, 2026-10-19=660, rejected delayed 2026-08-28=0, all HTTP 200. The 2026-10-20 raw market table remains empty, so same-day live Repair Alpha acceptance is blocked by missing market input.
- Three obsolete backfill Repair Alpha evaluation headers and 60 metrics were briefly restored from archive for inspection, then removed again because their values were stale. All six obsolete Repair Alpha headers and 120 metrics are now archived and absent from active tables. Rebuild aggregates only after every new backfill label month succeeds.
- Final evaluation rebuild produced headers 37, 38, 39 for 10d, 20d and 40d. All have 578,574 candidates and 20 metrics. Evaluation API returns HTTP 200 for all three groups with these counts. Rejected snapshot labels: zero; old nonrejected live/delayed shadows: zero.
- Original runner exit code unavailable; terminal JSON and database inserts establish the published result.
