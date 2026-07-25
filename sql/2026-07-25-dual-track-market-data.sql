-- Dual-track market-data derived tables. Execute manually in the target MySQL database.

DELIMITER //
DROP PROCEDURE IF EXISTS assert_dual_track_prerequisites//
CREATE PROCEDURE assert_dual_track_prerequisites()
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.tables
        WHERE table_schema = DATABASE() AND table_name = 'trade_stock_daily'
    ) THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Missing prerequisite table: trade_stock_daily';
    END IF;
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.tables
        WHERE table_schema = DATABASE() AND table_name = 'trade_stock_daily_raw'
    ) THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Missing prerequisite table: trade_stock_daily_raw';
    END IF;
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.tables
        WHERE table_schema = DATABASE() AND table_name = 'trade_corporate_action'
    ) THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Missing prerequisite table: trade_corporate_action';
    END IF;
END//
CALL assert_dual_track_prerequisites()//
DROP PROCEDURE assert_dual_track_prerequisites//
DELIMITER ;

CREATE TABLE IF NOT EXISTS trade_stock_daily_qfq (
    stock_code VARCHAR(16) NOT NULL,
    trade_date DATE NOT NULL,
    open_price DECIMAL(20, 6) NOT NULL,
    high_price DECIMAL(20, 6) NOT NULL,
    low_price DECIMAL(20, 6) NOT NULL,
    close_price DECIMAL(20, 6) NOT NULL,
    volume BIGINT UNSIGNED NOT NULL,
    amount DECIMAL(24, 4) NOT NULL,
    turnover_rate DECIMAL(12, 4) NULL,
    adjustment_asof DATE NULL,
    refreshed_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (stock_code, trade_date),
    KEY idx_qfq_trade_date (trade_date)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Independent QMT front-adjusted daily prices';

CREATE TABLE IF NOT EXISTS trade_stock_daily_bfq (
    stock_code VARCHAR(16) NOT NULL,
    trade_date DATE NOT NULL,
    open_price DECIMAL(20, 6) NOT NULL,
    high_price DECIMAL(20, 6) NOT NULL,
    low_price DECIMAL(20, 6) NOT NULL,
    close_price DECIMAL(20, 6) NOT NULL,
    volume BIGINT UNSIGNED NOT NULL,
    amount DECIMAL(24, 4) NOT NULL,
    turnover_rate DECIMAL(12, 4) NULL,
    adjustment_asof DATE NULL,
    refreshed_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (stock_code, trade_date),
    KEY idx_bfq_trade_date (trade_date)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Independent QMT back-adjusted daily prices';

CREATE TABLE IF NOT EXISTS trade_price_reconcile_log (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    stock_code VARCHAR(16) NOT NULL,
    trade_date DATE NOT NULL,
    price_mode ENUM('front') NOT NULL DEFAULT 'front',
    old_open_price DECIMAL(20, 6) NULL,
    old_high_price DECIMAL(20, 6) NULL,
    old_low_price DECIMAL(20, 6) NULL,
    old_close_price DECIMAL(20, 6) NULL,
    new_open_price DECIMAL(20, 6) NULL,
    new_high_price DECIMAL(20, 6) NULL,
    new_low_price DECIMAL(20, 6) NULL,
    new_close_price DECIMAL(20, 6) NULL,
    diff_reason VARCHAR(64) NOT NULL DEFAULT 'qfq_mismatch',
    status ENUM('pending', 'queued', 'resolved', 'ignored') NOT NULL DEFAULT 'pending',
    detected_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    resolved_at DATETIME NULL,
    PRIMARY KEY (id),
    UNIQUE KEY uk_reconcile_log (stock_code, trade_date, price_mode),
    KEY idx_reconcile_status (status, detected_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Old and independent front-adjusted price differences';

CREATE TABLE IF NOT EXISTS trade_price_refresh_task (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    stock_code VARCHAR(16) NOT NULL,
    price_mode ENUM('front', 'back') NOT NULL,
    refresh_from DATE NOT NULL,
    reason VARCHAR(64) NOT NULL,
    status ENUM('pending', 'running', 'done', 'failed') NOT NULL DEFAULT 'pending',
    retry_count INT UNSIGNED NOT NULL DEFAULT 0,
    last_error VARCHAR(1000) NULL,
    claim_token CHAR(36) NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY uk_refresh_task (stock_code, price_mode, reason),
    KEY idx_refresh_pending (status, created_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Retryable refresh requests for derived adjusted prices';

CREATE TABLE IF NOT EXISTS trade_legacy_qfq_repair_task (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    stock_code VARCHAR(16) NOT NULL,
    refresh_from DATE NOT NULL,
    refresh_to DATE NOT NULL,
    reason VARCHAR(64) NOT NULL,
    status ENUM('pending', 'running', 'done', 'failed') NOT NULL DEFAULT 'pending',
    retry_count INT UNSIGNED NOT NULL DEFAULT 0,
    last_error VARCHAR(1000) NULL,
    claim_token CHAR(36) NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY uk_legacy_qfq_repair_task (stock_code, refresh_from, refresh_to, reason),
    KEY idx_legacy_qfq_repair_pending (status, created_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
  COMMENT='Confirmed, retryable old front-adjusted price repairs';

-- Safe on repeat runs and upgrades a table created by an earlier draft.
ALTER TABLE trade_price_reconcile_log
    MODIFY COLUMN status
        ENUM('pending', 'queued', 'resolved', 'ignored')
        NOT NULL DEFAULT 'pending';

SET @refresh_claim_exists = (
    SELECT COUNT(*) FROM information_schema.columns
    WHERE table_schema = DATABASE()
      AND table_name = 'trade_price_refresh_task'
      AND column_name = 'claim_token'
);
SET @refresh_claim_ddl = IF(
    @refresh_claim_exists = 0,
    'ALTER TABLE trade_price_refresh_task ADD COLUMN claim_token CHAR(36) NULL AFTER last_error',
    'SELECT 1'
);
PREPARE refresh_claim_stmt FROM @refresh_claim_ddl;
EXECUTE refresh_claim_stmt;
DEALLOCATE PREPARE refresh_claim_stmt;

SET @legacy_claim_exists = (
    SELECT COUNT(*) FROM information_schema.columns
    WHERE table_schema = DATABASE()
      AND table_name = 'trade_legacy_qfq_repair_task'
      AND column_name = 'claim_token'
);
SET @legacy_claim_ddl = IF(
    @legacy_claim_exists = 0,
    'ALTER TABLE trade_legacy_qfq_repair_task ADD COLUMN claim_token CHAR(36) NULL AFTER last_error',
    'SELECT 1'
);
PREPARE legacy_claim_stmt FROM @legacy_claim_ddl;
EXECUTE legacy_claim_stmt;
DEALLOCATE PREPARE legacy_claim_stmt;
