-- Raw/QFQ internal integrity findings.  This table is deliberately separate
-- from trade_price_reconcile_log, which compares the retired legacy table.
CREATE TABLE IF NOT EXISTS trade_qfq_integrity_audit (
    id BIGINT NOT NULL AUTO_INCREMENT,
    stock_code VARCHAR(16) NOT NULL,
    trade_date DATE NOT NULL,
    check_code VARCHAR(64) NOT NULL,
    severity ENUM('warning', 'error') NOT NULL,
    status ENUM(
        'qmt_verified_exception', 'repair_pending', 'repaired', 'failed', 'resolved'
    ) NOT NULL,
    raw_ohlc_json JSON NULL,
    qfq_ohlc_json JSON NULL,
    source_fingerprint CHAR(64) NULL,
    validator_version VARCHAR(32) NOT NULL,
    first_detected_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    last_verified_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    resolved_at DATETIME NULL,
    last_error VARCHAR(1000) NULL,
    note TEXT NULL,
    PRIMARY KEY (id),
    UNIQUE KEY uk_trade_qfq_integrity_audit (stock_code, trade_date, check_code),
    KEY idx_trade_qfq_integrity_status (status, severity, last_verified_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
