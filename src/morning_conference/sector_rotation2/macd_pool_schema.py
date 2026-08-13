from data_ingestion.db_config import get_connection

DDL = """
CREATE TABLE IF NOT EXISTS sector_rotation_macd_pool (
 id BIGINT NOT NULL AUTO_INCREMENT,
 as_of_date DATE NOT NULL,
 sector_level TINYINT NOT NULL,
 model_version VARCHAR(32) NOT NULL,
 run_id CHAR(36) NOT NULL,
 entity_type VARCHAR(16) NOT NULL DEFAULT 'stock',
 stock_code VARCHAR(50) NOT NULL,
 stock_name VARCHAR(50) NULL,
 sector_1 VARCHAR(30) NULL,
 sector_2 VARCHAR(50) NULL,
 close DECIMAL(10,2) NULL, change_pct DECIMAL(8,2) NULL,
 dif DECIMAL(12,4) NULL, dea DECIMAL(12,4) NULL, macd_hist DECIMAL(12,4) NULL,
 vol_ratio DECIMAL(8,2) NULL, vol_ratio_gc DECIMAL(8,2) NULL, gc_offset TINYINT NULL,
 gc_label VARCHAR(20) NULL, gc_dif DECIMAL(12,4) NULL, gc_dea DECIMAL(12,4) NULL,
 adx_14 DECIMAL(8,2) NULL, rsi_14 DECIMAL(8,2) NULL, hurst_60 DECIMAL(8,4) NULL,
 kama_efficiency DECIMAL(8,4) NULL, above_ma60 TINYINT(1) NULL, sector_2_5d_return DECIMAL(8,2) NULL,
 main_capital_net_inflow_20d DECIMAL(20,2) NULL, chan_first_buy TINYINT(1) NULL,
 created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
 PRIMARY KEY (id), UNIQUE KEY uk_macd_pool_date_level_code (as_of_date, sector_level, model_version, entity_type, stock_code),
 KEY idx_macd_pool_sector (sector_level, sector_1, sector_2), KEY idx_macd_pool_run (run_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='MACD板块池';
"""

ENTITY_DAILY_DDL = """
CREATE TABLE IF NOT EXISTS sector_rotation_macd_entity_daily (
 id BIGINT NOT NULL AUTO_INCREMENT,
 as_of_date DATE NOT NULL, sector_level TINYINT NOT NULL, model_version VARCHAR(32) NOT NULL, run_id CHAR(36) NOT NULL,
 entity_type VARCHAR(16) NOT NULL, stock_code VARCHAR(50) NOT NULL, stock_name VARCHAR(50) NULL,
 sector_1 VARCHAR(30) NULL, sector_2 VARCHAR(50) NULL,
 close DECIMAL(10,2) NULL, change_pct DECIMAL(8,2) NULL, dif DECIMAL(12,4) NULL, dea DECIMAL(12,4) NULL, macd_hist DECIMAL(12,4) NULL,
 vol_ratio DECIMAL(8,2) NULL, vol_ratio_gc DECIMAL(8,2) NULL, gc_offset TINYINT NULL, gc_label VARCHAR(20) NULL, gc_dif DECIMAL(12,4) NULL, gc_dea DECIMAL(12,4) NULL,
 adx_14 DECIMAL(8,2) NULL, rsi_14 DECIMAL(8,2) NULL, hurst_60 DECIMAL(8,4) NULL, kama_efficiency DECIMAL(8,4) NULL, above_ma60 TINYINT(1) NULL,
 is_triggered TINYINT(1) NOT NULL DEFAULT 0, created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
 PRIMARY KEY (id),
 UNIQUE KEY uk_macd_entity_daily (as_of_date, sector_level, model_version, entity_type, stock_code),
 KEY idx_macd_entity_trajectory (sector_level, model_version, entity_type, stock_code, as_of_date)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='MACD full entity daily metrics';
"""

def ensure_macd_pool_table() -> None:
    conn = get_connection(); cur = conn.cursor()
    try:
        cur.execute(DDL); conn.commit()
    finally:
        cur.close(); conn.close()


def ensure_macd_entity_daily_table() -> None:
    conn = get_connection(); cur = conn.cursor()
    try:
        cur.execute(ENTITY_DAILY_DDL); conn.commit()
    finally:
        cur.close(); conn.close()

if __name__ == '__main__':
    ensure_macd_pool_table(); print('sector_rotation_macd_pool ready')


