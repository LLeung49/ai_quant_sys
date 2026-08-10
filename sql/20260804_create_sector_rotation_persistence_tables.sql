-- 每次 daily/backfill 运行的审计记录；失败运行保留原因，但不得产生正式快照。
CREATE TABLE IF NOT EXISTS sector_rotation_run_log (
    run_id CHAR(36) NOT NULL COMMENT '本次运行的 UUID 主键',
    as_of_date DATE NOT NULL COMMENT '本次计算归属的交易日',
    sector_level TINYINT NOT NULL COMMENT '申万行业层级：1=一级，2=二级',
    model_version VARCHAR(32) NOT NULL COMMENT '模型口径版本，例如 v1',
    config_hash CHAR(64) NOT NULL COMMENT '完整模型配置的 SHA-256 哈希',
    source_max_trade_date DATE NULL COMMENT '本次读取上游数据可用的最大交易日',
    status VARCHAR(16) NOT NULL COMMENT '运行状态：running、succeeded 或 failed',
    started_at DATETIME NOT NULL COMMENT '运行开始时间',
    finished_at DATETIME NULL COMMENT '运行结束时间；运行中为空',
    eligible_sector_count INT NOT NULL DEFAULT 0 COMMENT '评分有效并产生排名的板块数',
    skipped_sector_count INT NOT NULL DEFAULT 0 COMMENT '覆盖率或评分证据不足而跳过的板块数',
    error_summary TEXT NULL COMMENT '失败时的可检索错误摘要',
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '审计记录创建时间',
    PRIMARY KEY (run_id),
    KEY idx_run_as_of_date (as_of_date, sector_level, model_version)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='sector_rotation2 每日运行审计日志';

-- 每日、每层级、每板块、每模型版本唯一的可复现评分快照。
CREATE TABLE IF NOT EXISTS sector_rotation_sector_daily_snapshot (
    as_of_date DATE NOT NULL COMMENT '快照归属交易日',
    sector_level TINYINT NOT NULL COMMENT '申万行业层级：1=一级，2=二级',
    sector_name VARCHAR(128) NOT NULL COMMENT '板块/行业名称',
    model_version VARCHAR(32) NOT NULL COMMENT '评分模型版本',
    run_id CHAR(36) NOT NULL COMMENT '写入本快照的运行 UUID，关联 run_log',
    membership_asof_mode VARCHAR(32) NOT NULL COMMENT '成员映射口径；v1 为 current_mapping',
    coverage_ratio DECIMAL(18,8) NULL COMMENT '有效 K 线成员数占应有成员数的比例',
    rs_5 DECIMAL(18,8) NULL COMMENT '5 日相对强度：板块收益减基准收益', rs_20 DECIMAL(18,8) NULL COMMENT '20 日相对强度', rs_60 DECIMAL(18,8) NULL COMMENT '60 日相对强度',
    distance_ma20 DECIMAL(18,8) NULL COMMENT '收盘相对 MA20 的偏离比例', distance_ma60 DECIMAL(18,8) NULL COMMENT '收盘相对 MA60 的偏离比例', ma20_slope DECIMAL(18,8) NULL COMMENT 'MA20 最近窗口线性回归斜率',
    rs20_accel DECIMAL(18,8) NULL COMMENT '20 日相对强度相对 5 日前的变化', ma20_accel DECIMAL(18,8) NULL COMMENT 'MA20 斜率变化', macd_hist_delta DECIMAL(18,8) NULL COMMENT 'MACD 柱状线日变化',
    rvol_5_20 DECIMAL(18,8) NULL COMMENT '近 5 日成交额均值与近 20 日均值之比', share_impulse DECIMAL(18,8) NULL COMMENT '成交额份额相对 20 日均值的冲量',
    breadth_up DECIMAL(18,8) NULL COMMENT '板块上涨个股广度', breadth_above_ma20 DECIMAL(18,8) NULL COMMENT '站上个股 MA20 的广度', breadth_new_high_20 DECIMAL(18,8) NULL COMMENT '20 日新高个股广度', breadth_rvol DECIMAL(18,8) NULL COMMENT '个股放量广度',
    score_eligible TINYINT(1) NOT NULL DEFAULT 0 COMMENT '可用权重达到阈值时为 1，才参与综合排名',
    trend_level_score DECIMAL(18,8) NULL COMMENT '趋势位置横截面评分[-1,1]', velocity_score DECIMAL(18,8) NULL COMMENT '趋势速度横截面评分[-1,1]', acceleration_score DECIMAL(18,8) NULL COMMENT '趋势加速度横截面评分[-1,1]', volume_score DECIMAL(18,8) NULL COMMENT '量能横截面评分[-1,1]', participation_score DECIMAL(18,8) NULL COMMENT '参与度横截面评分[-1,1]',
    base_score DECIMAL(18,8) NULL COMMENT '按可用主评分重归一后的基础综合分', composite_score DECIMAL(18,8) NULL COMMENT '基础分乘市场风险暴露系数后的综合分', composite_rank INT NULL COMMENT '按 base_score 降序的横截面名次，1 为最高',
    phase_raw VARCHAR(32) NULL COMMENT '迟滞阈值产生的未确认阶段候选', phase_confirmed VARCHAR(32) NULL COMMENT '三日两次规则确认后的阶段', phase_age INT NULL COMMENT '确认阶段连续持续的交易日数', phase_changed TINYINT(1) NULL COMMENT '确认阶段相对上一日是否变化', phase_confidence DECIMAL(18,8) NULL COMMENT '由速度、加速度、参与度和持续性合成的置信度',
    market_regime VARCHAR(32) NULL COMMENT '市场状态：risk_off、high_volatility、risk_on 或 range', regime_multiplier DECIMAL(18,8) NULL COMMENT '市场状态对应的风险暴露缩放系数',
    rank_change_1d INT NULL COMMENT '昨日名次减今日名次，正值表示排名上升', rank_change_5d INT NULL COMMENT '五日前名次减今日名次，正值表示排名上升', top10_days_20 INT NULL COMMENT '最近 20 个交易日累计处于 Top10 的天数',
    lifecycle_state VARCHAR(32) NULL COMMENT 'Lifecycle V0 研究状态：exit/divergence/crowded/trending/emerging/repair/neutral', lifecycle_action VARCHAR(32) NULL COMMENT '仅供人工执行参考的动作建议，不自动下单', lifecycle_position_multiplier DECIMAL(18,8) NULL COMMENT 'Lifecycle V0 研究仓位乘数，不覆盖 Risk Engine', lifecycle_reason VARCHAR(128) NULL COMMENT 'Lifecycle 状态命中的可审计原因', lifecycle_changed TINYINT(1) NULL COMMENT 'Lifecycle 状态相对上一交易日是否变化', lifecycle_age INT NULL COMMENT '当前 Lifecycle 状态持续的交易日数',
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '快照首次创建时间', updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '同版本重跑时的最后更新时间',
    UNIQUE KEY uq_snapshot (as_of_date, sector_level, sector_name, model_version),
    KEY idx_snapshot_run_id (run_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='sector_rotation2 每日板块特征、评分、状态与排名快照';

-- 仅保存未来第 N 个交易日已存在的成熟标签，禁止用自然日替代交易日。
CREATE TABLE IF NOT EXISTS sector_rotation_sector_forward_return (
    as_of_date DATE NOT NULL COMMENT '收益标签起始交易日',
    sector_level TINYINT NOT NULL COMMENT '申万行业层级',
    sector_name VARCHAR(128) NOT NULL COMMENT '板块/行业名称',
    horizon SMALLINT NOT NULL COMMENT '前瞻交易日周期；当前为 5 或 10',
    target_date DATE NOT NULL COMMENT '第 N 个未来交易日',
    sector_return DECIMAL(18,8) NOT NULL COMMENT '板块从起始日至目标日的收益率',
    benchmark_return DECIMAL(18,8) NOT NULL COMMENT '同区间市场基准收益率',
    excess_return DECIMAL(18,8) NOT NULL COMMENT '板块收益率减市场基准收益率',
    label_ready_at DATETIME NOT NULL COMMENT '标签成熟并可参与研究的生成时间',
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '标签记录创建时间',
    UNIQUE KEY uq_forward_return (as_of_date, sector_level, sector_name, horizon)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='sector_rotation2 板块前瞻收益与超额收益标签';

-- 研究指标采用长表，便于增加 IC、分组收益、换手和状态分桶指标而无需改表。
CREATE TABLE IF NOT EXISTS sector_rotation_backtest_metric (
    evaluation_date DATE NOT NULL COMMENT '本次研究评估生成日期',
    sector_level TINYINT NOT NULL COMMENT '申万行业层级',
    model_version VARCHAR(32) NOT NULL COMMENT '被评估快照的模型版本',
    horizon SMALLINT NOT NULL COMMENT '标签预测周期（交易日）',
    metric_name VARCHAR(64) NOT NULL COMMENT '指标名称，例如 rank_ic_mean 或 top_group_turnover',
    window_name VARCHAR(128) NOT NULL COMMENT '样本窗口/状态分桶名称，例如 full_sample、risk_off',
    metric_value DECIMAL(18,8) NULL COMMENT '指标数值；无可用样本时可为空',
    sample_count INT NOT NULL DEFAULT 0 COMMENT '该指标对应的有效样本数',
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '研究指标记录创建时间',
    UNIQUE KEY uq_backtest_metric (evaluation_date, sector_level, model_version, horizon, metric_name, window_name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='sector_rotation2 回测与研究指标长表';
