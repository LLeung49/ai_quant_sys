-- Add the missing 5-day relative-strength column to the v2_short_term snapshot.
-- Reason: ``classify_short_term_labels`` reads ``rs_5`` to derive
-- ``short_rebound_candidate`` and ``short_breakdown_candidate``, but the
-- original 20260812 schema only persisted ``rs_1`` / ``rs_2`` /
-- ``rs5_accel_1d``. Without ``rs_5`` those two labels never trigger, which
-- leaves the Next-Day Watch Panel's V-shape rebound / breakdown cards empty.
--
-- This script is idempotent: re-running it after the column exists is a no-op.

ALTER TABLE sector_rotation_short_term_daily_snapshot
    ADD COLUMN rs_5 DECIMAL(18,8) NULL
        COMMENT '5 日累计相对强度（vs 市场基准），与 rs_1/rs_2 同口径'
        AFTER rs_2;
