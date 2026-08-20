-- Phase 4 / Repair Alpha persistence layer.
-- Existing schema migrations are not modified; this script adds new tables and
-- idempotent migrations on ``trade_stock_financial`` (if it exists).
-- Safe to run multiple times.

-- Raw PIT history: append-only, hash-keyed.  Multiple vendors may report the
-- same statement; the resolver picks the latest announcement known at the
-- research date.
CREATE TABLE IF NOT EXISTS trade_stock_financial_raw_pit (
    id BIGINT NOT NULL AUTO_INCREMENT,
    stock_code VARCHAR(16) NOT NULL,
    source_table VARCHAR(64) NOT NULL,
    report_date DATE NOT NULL,
    announcement_date DATE NULL,
    period_type VARCHAR(16) NOT NULL,
    revenue DECIMAL(24, 4) NULL,
    net_profit DECIMAL(24, 4) NULL,
    net_profit_deduced T T NULL,
    total_assets DECIMAL(24, 4) NULL,
    total_equity DECIMAL(24, 4) NULL,
    operating_cash_flow DECIMAL(24, 4) NULL,
    pit_status VARCHAR(16) NOT NULL,
    source_updated_at DATETIME NOT NULL,
    source_hash CHAR(64) NOT NULL,
    is_restated TINYINT(1) NOT NULL DEFAULT 0,
    first_seen_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    data_source VARCHAR(64) NOT NULL,
    PRIMARY KEY (id),
    UNIQUE KEY uk_financial_raw (stock_code, source_table, report_date, source_hash),
    KEY idx_financial_raw_lookup (stock_code, source_table, report_date, announcement_date)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='PIT-safe financial statement raw history';

-- Capital structure: PIT-aware share count snapshots.
CREATE TABLE IF NOT EXISTS trade_stock_capital_pit (
    id BIGINT NOT NULL AUTO_INCREMENT,
    stock_code VARCHAR(16) NOT NULL,
    report_date DATE NOT NULL,
    announcement_date DATE NOT NULL,
    total_shares DECIMAL(24, 4) NULL,
    circulating_shares DECIMAL(24, 4) NULL,
    pit_status VARCHAR(16) NOT NULL,
    source_hash CHAR(64) NOT NULL,
    first_seen_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    data_source VARCHAR(64) NOT NULL,
    PRIMARY KEY (id),
    UNIQUE KEY uk_capital_pit (stock_code, report_date, source_hash),
    KEY idx_capital_pit_lookup (stock_code, announcement_date, report_date)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='PIT capital structure history';

-- Derived daily valuation metrics.  Computed from raw + capital + close.
CREATE TABLE IF NOT EXISTS trade_stock_valuation_daily (
    as_of_date DATE NOT NULL,
    stock_code VARCHAR(16) NOT NULL,
    sector_name VARCHAR(128) NULL,
    pe DECIMAL(24, 8) NULL,
    pb DECIMAL(24, 8) NULL,
    ps DECIMAL(24, 8) NULL,
    p_ocf DECIMAL(24, 8) NULL,
    market_cap DECIMAL(24, 4) NULL,
    ttm_revenue DECIMAL(24, 4) NULL,
    ttm_net_profit DECIMAL(24, 4) NULL,
    pit_status VARCHAR(16) NOT NULL,
    quality_flags VARCHAR(255) NULL,
    model_version VARCHAR(64) NOT NULL,
    config_hash VARCHAR(64) NOT NULL,
    run_id VARCHAR(64) NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (as_of_date, stock_code, model_version),
    KEY idx_valuation_sector (as_of_date, sector_name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='PIT daily valuation snapshot';
