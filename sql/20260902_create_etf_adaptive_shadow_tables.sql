-- ETF 自适应策略 · 影子运行持久化表（2026-09-02 影子运行计划 Task 1）
-- 一次 daily run 在单事务内写入 run_log + 状态 + 订单建议，
-- 保证部分状态/建议永远不可见。
-- 唯一键 (as_of_date, model_version, config_hash) 强制 identity 不可被
-- 不同 config 复用，触发 ConfigConflictError。

CREATE TABLE IF NOT EXISTS asset_allocation_etf_adaptive_frozen_config (
    config_hash CHAR(64) NOT NULL,
    config_json JSON NOT NULL,
    selection_json JSON NOT NULL,
    data_cutoff DATE NOT NULL,
    activation_date DATE NOT NULL,
    review_date DATE NOT NULL,
    activated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (config_hash)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
COMMENT='影子运行使用的冻结研究与参数快照';

CREATE TABLE IF NOT EXISTS asset_allocation_etf_adaptive_run (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    as_of_date DATE NOT NULL COMMENT '本次信号交易日',
    stock_code VARCHAR(16) NOT NULL COMMENT '标的代码',
    model_version VARCHAR(64) NOT NULL COMMENT '模型版本号',
    config_hash CHAR(64) NOT NULL COMMENT '本次使用的 AdaptiveConfig SHA-256',
    run_id CHAR(36) NOT NULL COMMENT '本次运行的 UUID v4',
    execution_eligible_date DATE NOT NULL COMMENT '订单可执行的最早交易日（T+1）',
    status VARCHAR(32) NOT NULL COMMENT 'succeeded / failed',
    error_json JSON NULL COMMENT '失败时的错误摘要',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE KEY uk_adaptive_run (as_of_date, model_version, config_hash, stock_code)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
COMMENT='ETF 自适应影子运行日志（按 identity 强制唯一）';

CREATE TABLE IF NOT EXISTS asset_allocation_etf_adaptive_state (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    run_id CHAR(36) NOT NULL,
    stock_code VARCHAR(16) NOT NULL,
    as_of_date DATE NOT NULL,
    config_hash CHAR(64) NOT NULL,
    state_json JSON NOT NULL COMMENT 'StrategyState 的 JSON 序列化',
    cash DECIMAL(20,4) NOT NULL,
    position_shares INT NOT NULL,
    regime VARCHAR(16) NULL,
    UNIQUE KEY uk_adaptive_state (as_of_date, stock_code, config_hash),
    KEY idx_state_run (run_id),
    CONSTRAINT fk_state_run FOREIGN KEY (run_id) REFERENCES asset_allocation_etf_adaptive_run(run_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
COMMENT='每个 run 的最新 StrategyState（按 (date, code, config) 唯一）';

CREATE TABLE IF NOT EXISTS asset_allocation_etf_adaptive_order_advice (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    run_id CHAR(36) NOT NULL,
    stock_code VARCHAR(16) NOT NULL,
    as_of_date DATE NOT NULL,
    execution_eligible_date DATE NOT NULL,
    signal_date DATE NOT NULL,
    side VARCHAR(16) NOT NULL,
    reason VARCHAR(64) NOT NULL,
    config_hash CHAR(64) NOT NULL,
    target_budget DECIMAL(20,4) NOT NULL,
    risk_per_unit DECIMAL(20,8) NOT NULL,
    quantity_rationale VARCHAR(255) NOT NULL,
    signal_thresholds_json JSON NOT NULL,
    KEY idx_advice_run (run_id),
    CONSTRAINT fk_advice_run FOREIGN KEY (run_id) REFERENCES asset_allocation_etf_adaptive_run(run_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
COMMENT='T+1 订单建议，仅供人工审阅，绝不下单';

CREATE TABLE IF NOT EXISTS asset_allocation_etf_adaptive_fill_observation (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    execution_eligible_date DATE NOT NULL,
    stock_code VARCHAR(16) NOT NULL,
    config_hash CHAR(64) NOT NULL,
    raw_open DECIMAL(20,4) NULL,
    raw_close DECIMAL(20,4) NULL,
    slippage_bps DECIMAL(10,4) NULL,
    fill_complete TINYINT(1) NOT NULL,
    notes VARCHAR(255) NULL,
    observed_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    KEY idx_fill_obs_date (execution_eligible_date, stock_code)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
COMMENT='影子运行次日的真实成交观察，用于跟踪滑点、复现信号';

CREATE TABLE IF NOT EXISTS asset_allocation_etf_adaptive_health_check (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    run_id CHAR(36) NOT NULL,
    check_name VARCHAR(64) NOT NULL,
    passed TINYINT(1) NOT NULL,
    detail_json JSON NULL,
    observed_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    KEY idx_health_run (run_id),
    CONSTRAINT fk_health_run FOREIGN KEY (run_id) REFERENCES asset_allocation_etf_adaptive_run(run_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
COMMENT='影子运行期每日健康检查结果（数据新鲜度、状态连续性、配置一致性）';
