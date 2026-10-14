-- Staging-only market reconstruction schema. No statement touches canonical rows.

CREATE TABLE IF NOT EXISTS trade_stock_daily_raw_rebuild (
  stock_code varchar(16) NOT NULL,
  trade_date date NOT NULL,
  open_price decimal(20,6) NOT NULL,
  high_price decimal(20,6) NOT NULL,
  low_price decimal(20,6) NOT NULL,
  close_price decimal(20,6) NOT NULL,
  volume bigint unsigned NOT NULL,
  amount decimal(24,4) NOT NULL,
  pre_close decimal(20,6) DEFAULT NULL,
  suspend_flag tinyint DEFAULT NULL,
  data_source varchar(32) NOT NULL DEFAULT 'qmt_bridge_rebuild',
  ingested_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  rebuild_batch_id varchar(64) NOT NULL,
  rebuild_source varchar(32) NOT NULL,
  rebuild_fetched_at datetime(6) DEFAULT NULL,
  rebuild_fingerprint char(64) NOT NULL,
  rebuild_validation_status varchar(16) NOT NULL,
  PRIMARY KEY (stock_code, trade_date),
  KEY idx_raw_rebuild_trade_date (trade_date),
  KEY idx_raw_rebuild_batch (rebuild_batch_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS trade_stock_daily_qfq_rebuild (
  stock_code varchar(16) NOT NULL,
  trade_date date NOT NULL,
  open_price decimal(20,6) NOT NULL,
  high_price decimal(20,6) NOT NULL,
  low_price decimal(20,6) NOT NULL,
  close_price decimal(20,6) NOT NULL,
  volume bigint unsigned NOT NULL,
  amount decimal(24,4) NOT NULL,
  turnover_rate decimal(12,4) DEFAULT NULL,
  adjustment_asof date DEFAULT NULL,
  refreshed_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  rebuild_batch_id varchar(64) NOT NULL,
  rebuild_source varchar(32) NOT NULL,
  rebuild_fetched_at datetime(6) DEFAULT NULL,
  rebuild_fingerprint char(64) NOT NULL,
  rebuild_validation_status varchar(16) NOT NULL,
  PRIMARY KEY (stock_code, trade_date),
  KEY idx_qfq_rebuild_trade_date (trade_date),
  KEY idx_qfq_rebuild_batch (rebuild_batch_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS trade_stock_daily_bfq_rebuild (
  stock_code varchar(16) NOT NULL,
  trade_date date NOT NULL,
  open_price decimal(20,6) NOT NULL,
  high_price decimal(20,6) NOT NULL,
  low_price decimal(20,6) NOT NULL,
  close_price decimal(20,6) NOT NULL,
  volume bigint unsigned NOT NULL,
  amount decimal(24,4) NOT NULL,
  turnover_rate decimal(12,4) DEFAULT NULL,
  adjustment_asof date DEFAULT NULL,
  refreshed_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  rebuild_batch_id varchar(64) NOT NULL,
  rebuild_source varchar(32) NOT NULL,
  rebuild_fetched_at datetime(6) DEFAULT NULL,
  rebuild_fingerprint char(64) NOT NULL,
  rebuild_validation_status varchar(16) NOT NULL,
  PRIMARY KEY (stock_code, trade_date),
  KEY idx_bfq_rebuild_trade_date (trade_date),
  KEY idx_bfq_rebuild_batch (rebuild_batch_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS trade_market_rebuild_batch (
  batch_id varchar(64) NOT NULL,
  stock_code varchar(16) NOT NULL,
  start_date date NOT NULL,
  end_date date NOT NULL,
  status varchar(16) NOT NULL,
  source varchar(32) NOT NULL,
  fingerprint char(64) DEFAULT NULL,
  raw_rows int unsigned NOT NULL DEFAULT 0,
  qfq_rows int unsigned NOT NULL DEFAULT 0,
  hfq_rows int unsigned NOT NULL DEFAULT 0,
  gap_count int unsigned NOT NULL DEFAULT 0,
  error_detail text,
  started_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  completed_at datetime DEFAULT NULL,
  PRIMARY KEY (batch_id, stock_code),
  KEY idx_market_rebuild_status (batch_id, status)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS trade_market_rebuild_gap (
  batch_id varchar(64) NOT NULL,
  stock_code varchar(16) NOT NULL,
  price_mode varchar(8) NOT NULL,
  reason varchar(64) NOT NULL,
  first_trade_date date NOT NULL,
  last_trade_date date NOT NULL,
  gap_count int unsigned NOT NULL,
  sample_detail json DEFAULT NULL,
  PRIMARY KEY (batch_id, stock_code, price_mode, reason),
  KEY idx_market_rebuild_gap_reason (batch_id, reason)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS trade_market_rebuild_expected_code (
  batch_id varchar(64) NOT NULL,
  stock_code varchar(16) NOT NULL,
  universe_hash char(64) NOT NULL,
  created_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (batch_id, stock_code),
  KEY idx_market_rebuild_expected_hash (batch_id, universe_hash)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
