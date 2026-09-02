-- v2_short_term 短期异动研究层（sector_rotation2）的派生表。
-- 本脚本与 v1 完全独立：新建 sector_rotation_short_term_daily_snapshot 短期快照表，
-- 共用 sector_rotation_run_log 运行审计表（按 model_version 区分）。
-- 执行前请确保 v1 派生表已存在；所有 CREATE 语句可安全重复执行。

DELIMITER //
DROP PROCEDURE IF EXISTS assert_short_term_prerequisites//
CREATE PROCEDURE assert_short_term_prerequisites()
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.tables
        WHERE table_schema = DATABASE() AND table_name = 'sector_rotation_run_log'
    ) THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Missing prerequisite table: sector_rotation_run_log';
    END IF;
END//
CALL assert_short_term_prerequisites()//
DROP PROCEDURE assert_short_term_prerequisites//
DELIMITER ;

CREATE TABLE IF NOT EXISTS sector_rotation_short_term_daily_snapshot (
    as_of_date DATE NOT NULL COMMENT '快照归属交易日',
    sector_level TINYINT NOT NULL COMMENT '申万行业层级：1=一级，2=二级',
    sector_name VARCHAR(128) NOT NULL COMMENT '板块/行业名称',
    model_version VARCHAR(32) NOT NULL COMMENT '短期模型版本，固定为 v2_short_term',
    run_id CHAR(36) NOT NULL COMMENT '关联 sector_rotation_run_log 的运行 UUID',
    coverage_ratio DECIMAL(18,8) NULL COMMENT '与 v1 同口径的成员覆盖率',
    -- 收益与相对强度
    ret_1 DECIMAL(18,8) NULL COMMENT '1 日绝对收益',
    ret_2 DECIMAL(18,8) NULL COMMENT '2 日累计绝对收益',
    ret_3 DECIMAL(18,8) NULL COMMENT '3 日累计绝对收益',
    rs_1 DECIMAL(18,8) NULL COMMENT '1 日相对强度（vs 市场基准）',
    rs_2 DECIMAL(18,8) NULL COMMENT '2 日累计相对强度',
    rs5_accel_1d DECIMAL(18,8) NULL COMMENT '5 日相对强度的 1 日变化',
    ma5_slope DECIMAL(18,8) NULL COMMENT '5 日均线日级斜率',
    -- 量能与份额脉冲
    rvol_1_20 DECIMAL(18,8) NULL COMMENT '当日成交 / 20 日均额',
    rvol_1_60 DECIMAL(18,8) NULL COMMENT '当日成交 / 60 日均额',
    amount_share_today DECIMAL(18,8) NULL COMMENT '当日板块成交额占有效市场总成交额的比例',
    share_impulse_1d DECIMAL(18,8) NULL COMMENT '当日份额相对昨日份额的冲量',
    -- 个股短期广度
    breadth_up DECIMAL(18,8) NULL COMMENT '当日上涨家数占比',
    breadth_above_ma5 DECIMAL(18,8) NULL COMMENT '站上 5 日均线家数占比',
    breadth_new_high_5 DECIMAL(18,8) NULL COMMENT '5 日新高家数占比',
    breadth_strong_1d DECIMAL(18,8) NULL COMMENT '单日涨幅 >5% 个股占比',
    breadth_weak_1d DECIMAL(18,8) NULL COMMENT '单日跌幅 <-5% 个股占比',
    breadth_rvol_1d DECIMAL(18,8) NULL COMMENT '个股 RVOL > 1.5 家数占比',
    limit_up_ratio DECIMAL(18,8) NULL COMMENT '涨停家数占有效家数比例',
    limit_down_ratio DECIMAL(18,8) NULL COMMENT '跌停家数占有效家数比例',
    intraday_range DECIMAL(18,8) NULL COMMENT '个股日内振幅的板块等权均值（待个股 OHLC 接入）',
    ret_dispersion DECIMAL(18,8) NULL COMMENT '个股 ret_1 的横截面标准差',
    -- 连续性轻量指标
    streak_pos_ret INT NULL COMMENT '连续 ret_1 > 0 的天数，上限 5',
    streak_high_breadth INT NULL COMMENT '连续 breadth_up > 0.5 的天数，上限 5',
    streak_top_limit_up INT NULL COMMENT '连续 limit_up >= 1 的天数，上限 5',
    -- 评分
    score_eligible TINYINT(1) NOT NULL DEFAULT 0 COMMENT '可用权重达阈值时为 1',
    pulse_score DECIMAL(18,8) NULL COMMENT 'rs_1/rs_2 截面评分',
    volume_spike_score DECIMAL(18,8) NULL COMMENT 'rvol_1_20/share_impulse_1d 截面评分',
    breadth_spike_score DECIMAL(18,8) NULL COMMENT '短期广度四指标截面评分',
    limit_score DECIMAL(18,8) NULL COMMENT '涨跌停占比截面评分',
    momentum_shift_score DECIMAL(18,8) NULL COMMENT 'rs5_accel_1d/ma5_slope 截面评分',
    short_term_composite DECIMAL(18,8) NULL COMMENT '短期评分按权重合成',
    short_term_composite_rank INT NULL COMMENT '短期综合的横截面名次',
    -- 异动标签
    short_term_labels VARCHAR(255) NULL COMMENT '命中标签集合，逗号分隔',
    short_term_intensity ENUM('intense','moderate','mild','none') NOT NULL DEFAULT 'none' COMMENT '短期异动强度',
    -- 质量
    eligible_member_count INT NULL COMMENT '有效成分股家数',
    valid_member_count INT NULL COMMENT '有完整 OHLCV/成交额数据的成分股家数',
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (as_of_date, sector_level, sector_name, model_version),
    KEY idx_short_run_id (run_id),
    KEY idx_short_labels (short_term_labels),
    KEY idx_short_intensity (short_term_intensity),
    KEY idx_short_rank (short_term_composite_rank)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='sector_rotation2 短期异动参考快照（v2_short_term）';
