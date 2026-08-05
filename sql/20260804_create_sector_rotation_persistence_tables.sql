CREATE TABLE IF NOT EXISTS sector_rotation_run_log (
    run_id CHAR(36) NOT NULL,
    as_of_date DATE NOT NULL,
    sector_level TINYINT NOT NULL,
    model_version VARCHAR(32) NOT NULL,
    config_hash CHAR(64) NOT NULL,
    source_max_trade_date DATE NULL,
    status VARCHAR(16) NOT NULL,
    started_at DATETIME NOT NULL,
    finished_at DATETIME NULL,
    eligible_sector_count INT NOT NULL DEFAULT 0,
    skipped_sector_count INT NOT NULL DEFAULT 0,
    error_summary TEXT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (run_id),
    KEY idx_run_as_of_date (as_of_date, sector_level, model_version)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS sector_rotation_sector_daily_snapshot (
    as_of_date DATE NOT NULL,
    sector_level TINYINT NOT NULL,
    sector_name VARCHAR(128) NOT NULL,
    model_version VARCHAR(32) NOT NULL,
    run_id CHAR(36) NOT NULL,
    membership_asof_mode VARCHAR(32) NOT NULL,
    coverage_ratio DECIMAL(18,8) NULL,
    score_eligible TINYINT(1) NOT NULL DEFAULT 0,
    base_score DECIMAL(18,8) NULL,
    composite_score DECIMAL(18,8) NULL,
    composite_rank INT NULL,
    phase_raw VARCHAR(32) NULL,
    phase_confirmed VARCHAR(32) NULL,
    phase_age INT NULL,
    phase_changed TINYINT(1) NULL,
    phase_confidence DECIMAL(18,8) NULL,
    market_regime VARCHAR(32) NULL,
    regime_multiplier DECIMAL(18,8) NULL,
    rank_change_1d INT NULL,
    rank_change_5d INT NULL,
    top10_days_20 INT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY uq_snapshot (as_of_date, sector_level, sector_name, model_version),
    KEY idx_snapshot_run_id (run_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS sector_rotation_sector_forward_return (
    as_of_date DATE NOT NULL,
    sector_level TINYINT NOT NULL,
    sector_name VARCHAR(128) NOT NULL,
    horizon SMALLINT NOT NULL,
    target_date DATE NOT NULL,
    sector_return DECIMAL(18,8) NOT NULL,
    benchmark_return DECIMAL(18,8) NOT NULL,
    excess_return DECIMAL(18,8) NOT NULL,
    label_ready_at DATETIME NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE KEY uq_forward_return (as_of_date, sector_level, sector_name, horizon)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS sector_rotation_backtest_metric (
    evaluation_date DATE NOT NULL,
    sector_level TINYINT NOT NULL,
    model_version VARCHAR(32) NOT NULL,
    horizon SMALLINT NOT NULL,
    metric_name VARCHAR(64) NOT NULL,
    window_name VARCHAR(128) NOT NULL,
    metric_value DECIMAL(18,8) NULL,
    sample_count INT NOT NULL DEFAULT 0,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE KEY uq_backtest_metric (evaluation_date, sector_level, model_version, horizon, metric_name, window_name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
