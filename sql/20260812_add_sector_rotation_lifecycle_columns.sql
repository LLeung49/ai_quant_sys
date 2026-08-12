-- Upgrade an existing sector_rotation2 snapshot table created before Lifecycle V0.
-- Execute once. A single ALTER TABLE keeps the upgrade atomic: on failure no partial
-- set of Lifecycle columns is left behind.
ALTER TABLE sector_rotation_sector_daily_snapshot
    ADD COLUMN lifecycle_state VARCHAR(32) NULL COMMENT 'Lifecycle V0 research state' AFTER top10_days_20,
    ADD COLUMN lifecycle_action VARCHAR(32) NULL COMMENT 'Manual-action reference only' AFTER lifecycle_state,
    ADD COLUMN lifecycle_position_multiplier DECIMAL(18,8) NULL COMMENT 'Lifecycle V0 research position multiplier' AFTER lifecycle_action,
    ADD COLUMN lifecycle_reason VARCHAR(128) NULL COMMENT 'Auditable Lifecycle rule reason' AFTER lifecycle_position_multiplier,
    ADD COLUMN lifecycle_changed TINYINT(1) NULL COMMENT 'Whether Lifecycle state changed from the prior trading date' AFTER lifecycle_reason,
    ADD COLUMN lifecycle_age INT NULL COMMENT 'Trading-day duration of the current Lifecycle state' AFTER lifecycle_changed;
