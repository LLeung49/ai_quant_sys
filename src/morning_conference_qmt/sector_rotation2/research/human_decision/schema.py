DECISION_DDL = """
CREATE TABLE IF NOT EXISTS research_human_decision (
    id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(64) NOT NULL,
    snapshot_id BIGINT NOT NULL,
    entity_type VARCHAR(32) NOT NULL,
    entity_code VARCHAR(128) NOT NULL,
    strategy_type VARCHAR(64) NOT NULL,
    as_of_date DATE NOT NULL,
    model_version VARCHAR(64) NOT NULL,
    config_hash VARCHAR(64) NOT NULL,
    snapshot_mode VARCHAR(16) NOT NULL,
    decision VARCHAR(16) NOT NULL,
    note TEXT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    KEY idx_decision_snapshot (user_id,snapshot_id,created_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
"""

