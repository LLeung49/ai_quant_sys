WATCHLIST_DDL = """
CREATE TABLE IF NOT EXISTS research_watchlist (
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
    watch_status VARCHAR(32) NOT NULL DEFAULT 'watch',
    note TEXT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY uk_research_watch (user_id, snapshot_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
"""

