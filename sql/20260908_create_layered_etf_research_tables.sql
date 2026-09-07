-- ETF 自适应策略：防御层与宽基 Beta 层研究事实表。
-- 仅保存来源快照、有效期映射和 PIT 事实；策略收益不可参与 ETF 产品选择。

CREATE TABLE IF NOT EXISTS asset_allocation_etf_research_source_snapshot (
    source_hash CHAR(64) NOT NULL,
    source_name VARCHAR(64) NOT NULL,
    source_kind VARCHAR(64) NOT NULL,
    captured_at DATETIME NOT NULL,
    as_of_date DATE NULL,
    payload_json JSON NOT NULL,
    PRIMARY KEY (source_hash),
    KEY idx_research_source_asof (source_name, as_of_date)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
COMMENT='MiniQMT、AkShare 和指数编制方的不可变来源快照';

CREATE TABLE IF NOT EXISTS asset_allocation_etf_research_whitelist_version (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    version_hash CHAR(64) NOT NULL,
    status VARCHAR(16) NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    approved_at DATETIME NULL,
    notes VARCHAR(255) NULL,
    UNIQUE KEY uk_research_whitelist_version_hash (version_hash),
    KEY idx_research_whitelist_status (status)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
COMMENT='人工审阅的指数暴露至主备 ETF 映射版本';

CREATE TABLE IF NOT EXISTS asset_allocation_etf_research_whitelist_entry (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    whitelist_version_id BIGINT NOT NULL,
    exposure_id VARCHAR(96) NOT NULL,
    sub_layer VARCHAR(64) NOT NULL,
    primary_code VARCHAR(16) NOT NULL,
    backup_code VARCHAR(16) NOT NULL,
    effective_from DATE NOT NULL,
    effective_to DATE NULL,
    source_hash CHAR(64) NOT NULL,
    valuation_multiplier DECIMAL(12,8) NOT NULL DEFAULT 1.00000000,
    KEY idx_research_whitelist_active (exposure_id, effective_from, effective_to),
    KEY idx_research_whitelist_layer (sub_layer, effective_from, effective_to),
    CONSTRAINT fk_research_whitelist_version
      FOREIGN KEY (whitelist_version_id)
      REFERENCES asset_allocation_etf_research_whitelist_version(id),
    CONSTRAINT fk_research_whitelist_source
      FOREIGN KEY (source_hash)
      REFERENCES asset_allocation_etf_research_source_snapshot(source_hash)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
COMMENT='有效期内每个指数暴露的主备 ETF 与估值乘数';

CREATE TABLE IF NOT EXISTS asset_allocation_etf_research_market_calendar (
    market VARCHAR(16) NOT NULL,
    trade_date DATE NOT NULL,
    source_hash CHAR(64) NOT NULL,
    PRIMARY KEY (market, trade_date),
    CONSTRAINT fk_research_calendar_source
      FOREIGN KEY (source_hash)
      REFERENCES asset_allocation_etf_research_source_snapshot(source_hash)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
COMMENT='按市场保存的权威交易日历 PIT 快照';

CREATE TABLE IF NOT EXISTS asset_allocation_etf_research_index_valuation_pit (
    index_code VARCHAR(32) NOT NULL,
    as_of_date DATE NOT NULL,
    metric_code VARCHAR(32) NOT NULL,
    metric_value DECIMAL(24,8) NOT NULL,
    source_hash CHAR(64) NOT NULL,
    PRIMARY KEY (index_code, as_of_date, metric_code),
    CONSTRAINT fk_research_valuation_source
      FOREIGN KEY (source_hash)
      REFERENCES asset_allocation_etf_research_source_snapshot(source_hash)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
COMMENT='指数 PE/PB 等点时估值事实；海外和港股缺失时策略乘数固定为 1';

CREATE TABLE IF NOT EXISTS asset_allocation_etf_research_constituent_pit (
    index_code VARCHAR(32) NOT NULL,
    as_of_date DATE NOT NULL,
    stock_code VARCHAR(16) NOT NULL,
    weight DECIMAL(16,10) NULL,
    source_hash CHAR(64) NOT NULL,
    PRIMARY KEY (index_code, as_of_date, stock_code),
    CONSTRAINT fk_research_constituent_source
      FOREIGN KEY (source_hash)
      REFERENCES asset_allocation_etf_research_source_snapshot(source_hash)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
COMMENT='权威红利低波或红利质量指数的历史成分股 PIT 快照';
