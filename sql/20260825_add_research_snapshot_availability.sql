-- Add operational availability metadata without touching existing snapshots.
-- MySQL DATETIME values are timezone-naive Asia/Shanghai application times.

DELIMITER //

CREATE PROCEDURE add_research_snapshot_availability_columns()
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.columns
        WHERE table_schema = DATABASE()
          AND table_name = 'research_candidate_snapshot'
          AND column_name = 'data_available_at'
    ) THEN
        ALTER TABLE research_candidate_snapshot
            ADD COLUMN data_available_at DATETIME NULL;
    END IF;

    IF NOT EXISTS (
        SELECT 1 FROM information_schema.columns
        WHERE table_schema = DATABASE()
          AND table_name = 'research_candidate_snapshot'
          AND column_name = 'run_at'
    ) THEN
        ALTER TABLE research_candidate_snapshot
            ADD COLUMN run_at DATETIME NULL;
    END IF;

    IF NOT EXISTS (
        SELECT 1 FROM information_schema.columns
        WHERE table_schema = DATABASE()
          AND table_name = 'research_candidate_snapshot'
          AND column_name = 'execution_eligible_at'
    ) THEN
        ALTER TABLE research_candidate_snapshot
            ADD COLUMN execution_eligible_at DATETIME NULL;
    END IF;

    IF NOT EXISTS (
        SELECT 1 FROM information_schema.columns
        WHERE table_schema = DATABASE()
          AND table_name = 'research_candidate_snapshot'
          AND column_name = 'availability_basis'
    ) THEN
        ALTER TABLE research_candidate_snapshot
            ADD COLUMN availability_basis VARCHAR(32) NULL;
    END IF;

    IF NOT EXISTS (
        SELECT 1 FROM information_schema.statistics
        WHERE table_schema = DATABASE()
          AND table_name = 'research_candidate_snapshot'
          AND index_name = 'idx_research_snapshot_execution'
    ) THEN
        ALTER TABLE research_candidate_snapshot
            ADD KEY idx_research_snapshot_execution (snapshot_mode, execution_eligible_at);
    END IF;
END //

CALL add_research_snapshot_availability_columns() //
DROP PROCEDURE add_research_snapshot_availability_columns //

DELIMITER ;
