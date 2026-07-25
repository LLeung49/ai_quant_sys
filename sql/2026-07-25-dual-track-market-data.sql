-- Dual-track market-data derived tables. Execute manually in the target MySQL database.

CREATE TABLE trade_stock_daily_qfq (
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

CREATE TABLE trade_stock_daily_bfq (
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

CREATE TABLE trade_price_reconcile_log (
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
    status ENUM('open', 'queued', 'resolved', 'ignored') NOT NULL DEFAULT 'open',
    detected_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    resolved_at DATETIME NULL,
    PRIMARY KEY (id),
    UNIQUE KEY uk_reconcile_log (stock_code, trade_date, price_mode),
    KEY idx_reconcile_status (status, detected_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Old and independent front-adjusted price differences';

CREATE TABLE trade_price_refresh_task (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    stock_code VARCHAR(16) NOT NULL,
    price_mode ENUM('front', 'back') NOT NULL,
    refresh_from DATE NOT NULL,
    reason VARCHAR(64) NOT NULL,
    status ENUM('pending', 'running', 'done', 'failed') NOT NULL DEFAULT 'pending',
    retry_count INT UNSIGNED NOT NULL DEFAULT 0,
    last_error VARCHAR(1000) NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY uk_refresh_task (stock_code, price_mode, reason),
    KEY idx_refresh_pending (status, created_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Retryable refresh requests for derived adjusted prices';
