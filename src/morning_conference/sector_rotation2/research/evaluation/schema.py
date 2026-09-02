"""DDL for immutable-snapshot forward outcomes and evaluation aggregates."""

FORWARD_LABEL_DDL = """
CREATE TABLE IF NOT EXISTS sector_rotation_research_forward_label (
    id BIGINT NOT NULL AUTO_INCREMENT,
    source_snapshot_id BIGINT NOT NULL,
    snapshot_mode VARCHAR(16) NOT NULL,
    signal_date DATE NOT NULL,
    entity_type VARCHAR(32) NOT NULL,
    entity_code VARCHAR(128) NOT NULL,
    benchmark_type VARCHAR(32) NOT NULL DEFAULT 'none',
    benchmark_code VARCHAR(128) NOT NULL DEFAULT '',
    horizon INT NOT NULL,
    label_type VARCHAR(32) NOT NULL,
    price_basis VARCHAR(32) NOT NULL,
    entry_date DATE DEFAULT NULL,
    exit_date DATE DEFAULT NULL,
    signal_close DECIMAL(20,6) DEFAULT NULL,
    entry_price DECIMAL(20,6) DEFAULT NULL,
    exit_price DECIMAL(20,6) DEFAULT NULL,
    entry_gap DOUBLE DEFAULT NULL,
    forward_return DOUBLE DEFAULT NULL,
    benchmark_return DOUBLE DEFAULT NULL,
    excess_return DOUBLE DEFAULT NULL,
    mae DOUBLE DEFAULT NULL,
    mfe DOUBLE DEFAULT NULL,
    return_status VARCHAR(32) NOT NULL,
    path_status VARCHAR(32) NOT NULL,
    benchmark_status VARCHAR(32) NOT NULL,
    is_complete TINYINT NOT NULL DEFAULT 0,
    excess_is_complete TINYINT NOT NULL DEFAULT 0,
    label_model_version VARCHAR(64) NOT NULL,
    label_config_hash VARCHAR(64) NOT NULL,
    run_id VARCHAR(64) NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY uk_research_forward_label (
        source_snapshot_id, snapshot_mode, benchmark_type, benchmark_code, horizon,
        label_type, price_basis, label_model_version, label_config_hash
    ),
    KEY idx_research_label_signal (snapshot_mode, signal_date, entity_type),
    KEY idx_research_label_entity (entity_code, signal_date),
    KEY idx_research_label_status (return_status, benchmark_status)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
"""

EVALUATION_DDL = """
CREATE TABLE IF NOT EXISTS sector_rotation_research_evaluation (
    id BIGINT NOT NULL AUTO_INCREMENT,
    signal_family VARCHAR(64) NOT NULL,
    signal_model_version VARCHAR(64) NOT NULL,
    condition_key VARCHAR(128) NOT NULL,
    horizon INT NOT NULL,
    label_type VARCHAR(32) NOT NULL,
    event_sampling_mode VARCHAR(16) NOT NULL,
    sample_scope VARCHAR(16) NOT NULL,
    snapshot_mode VARCHAR(16) NOT NULL,
    oos_window_id VARCHAR(64) NOT NULL DEFAULT 'full',
    train_start DATE DEFAULT NULL,
    train_end DATE DEFAULT NULL,
    validation_start DATE DEFAULT NULL,
    validation_end DATE DEFAULT NULL,
    test_start DATE DEFAULT NULL,
    test_end DATE DEFAULT NULL,
    candidate_count INT NOT NULL DEFAULT 0,
    unique_event_count INT NOT NULL DEFAULT 0,
    return_complete_count INT NOT NULL DEFAULT 0,
    excess_complete_count INT NOT NULL DEFAULT 0,
    path_complete_count INT NOT NULL DEFAULT 0,
    model_version VARCHAR(64) NOT NULL,
    config_hash VARCHAR(64) NOT NULL,
    run_id VARCHAR(64) NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY uk_research_eval_header (
        signal_family, signal_model_version, condition_key, horizon, label_type,
        event_sampling_mode, sample_scope, snapshot_mode, oos_window_id, model_version, config_hash
    )
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
"""

EVALUATION_METRIC_DDL = """
CREATE TABLE IF NOT EXISTS sector_rotation_research_evaluation_metric (
    id BIGINT NOT NULL AUTO_INCREMENT,
    evaluation_id BIGINT NOT NULL,
    metric_name VARCHAR(64) NOT NULL,
    metric_value DOUBLE DEFAULT NULL,
    sample_count INT NOT NULL DEFAULT 0,
    ci_low DOUBLE DEFAULT NULL,
    ci_high DOUBLE DEFAULT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY uk_research_eval_metric (evaluation_id, metric_name),
    KEY idx_research_eval_metric_name (metric_name, evaluation_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
"""
