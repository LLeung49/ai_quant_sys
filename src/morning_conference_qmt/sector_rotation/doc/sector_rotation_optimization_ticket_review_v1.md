# sector_rotation 优化项实现复核（v1）

**复核日期：2026-08-06**  
**复核范围：** 原方案 `sector_rotation_optimization.md` 对比当前 `morning_conference.sector_rotation2` 实际代码、DDL 与自动化测试。  
**结论口径：** “已实现”仅代表代码和测试存在；“已验证”须以真实行情回填/人工复核为准，当前尚未完成。

## 总结

原方案中最核心的五项改造已经落地：连续横截面评分、取消 `PHASE_BONUS`、RVOL+资金份额、参与度广度、历史快照/phase 历史。新版已能以独立包运行并落库。

但不能将所有优化点都判定为“完成”：市场状态的日常编排输入不完整；滚动样本外只生成窗口、尚未实际评估；研究指标未写入 `sector_rotation_backtest_metric`；可视化明确未开发；历史成分、大小盘风格和市值集中度因数据条件未实现。

| 状态 | 数量 | 含义 |
| --- | ---: | --- |
| 已实现 | 15 | 代码与单元测试覆盖，待真实数据验证 |
| 部分实现 / 有偏差 | 8 | 有主体实现，但与原优化目标或字段语义不完全一致 |
| 未实现 / 有意延后 | 6 | 本期未做，或依赖当前没有的数据 |

## 一、指标层优化复核

| 原优化点 | 当前实现与证据 | 状态 | 复核结论 / 后续动作 |
| --- | --- | --- | --- |
| 用 Trend Level 替代模糊“0 阶”概念 | `trend_level_score = RS20/RS60/distance_ma20/distance_ma60`；`strength_score` 仅为兼容别名 | 已实现 | 满足“位置”层要求；未加入同风格相对强弱。 |
| 使用 RS5、RS20、MA20 slope 构成速度分 | `velocity_score` 按三者 signed percentile 等权组内合成 | 已实现 | 采用百分位统一量纲，满足原建议。 |
| 使用 RS20 变化、斜率变化、MACD 柱变化构成加速度分 | `rs20_accel`、`ma20_accel`、`macd_hist_delta` | 已实现 | 使用的是 `ΔMACD_HIST`，已消除旧文档“MACD 柱/柱变化”歧义。 |
| 多周期加速度 `RS5 - 0.25*RS20` | `multi_horizon_acceleration` 已计算 | 部分实现 | 当前仅诊断输出，不进入 `acceleration_score`；应待 IC 结果决定是否替换现有项。 |
| 横截面百分位并映射至 [-1,1] | `signed_percentile`，样本不足/常数列返回 NaN | 已实现 | 符合量纲统一、抗极端值目标。 |
| RVOL_FAST=MA5/MA20，RVOL_SLOW=MA5/MA60 | `rvol_5_20`、`rvol_5_60` | 已实现 | 两项均计算；当前 `volume_score` 仅用 fast RVOL 与 share impulse。 |
| AmountShare 与 ShareImpulse | `amount_share`、`share_impulse` | 已实现 | 已剔除全市场共同放量。 |
| 横截面量能分/气泡大小 | `volume_score=log(RVOL5/20)+log(share_impulse)` 的百分位组分 | 已实现 | 已具备可视化数据字段；尚无图形。 |
| 个股典型放量和放量广度 | `median_stock_rvol`、`breadth_rvol` | 已实现 | 当前快照 DDL 未保存 `median_stock_rvol`，应在真实 review 时确认是否需补列。 |
| 上涨、站上 MA20、20 日新高广度 | `breadth_up`、`breadth_above_ma20`、`breadth_new_high_20` | 已实现 | 参与度评分使用上述字段及 breadth_rvol。 |
| 等权收益与市值加权收益差，识别龙头主导 | 无历史自由流通市值输入 | 未实现（有意延后） | 原规格已明确禁止使用当前市值回填历史；取得可靠历史市值后另立规格。 |
| 同风格、小盘/大盘相对强弱 | 无指数/风格基准输入 | 未实现 | 市场状态与趋势位置尚未覆盖该维度。 |

## 二、phase、评分和市场状态复核

| 原优化点 | 当前实现与证据 | 状态 | 复核结论 / 风险 |
| --- | --- | --- |
| phase 从硬投票改为连续 V/A | `velocity_score`、`acceleration_score` 驱动 `phase_raw` | 已实现 | 旧版硬投票已移除。 |
| 进入/保持 hysteresis | 进入 ±0.25、保持 ±0.10 | 已实现 | 已有边界测试。 |
| 最近三日两次确认、最短持续、phase_age | `apply_phase_history` 使用当前+前两日 raw phase，维护 age | 已实现 | 需连续回填后才能在真实数据中验证。 |
| confidence | 速度、加速度、参与度、phase_age 合成 `phase_confidence` | 已实现 | 缺参与度时重归一，范围 [0,1]。 |
| `decel_down` 不直接推荐；拆筑底候选/反转确认 | `bottoming_candidate`、至少两项反转条件后 `reversal_confirmed`，不参与评分 | 已实现 | 代码中旧 `decel_down` 不再作为状态名称。 |
| phase 加入位置、参与度标签 | Trend Level 和 Participation 已单独输出 | 部分实现 | 未组合为 `accel_up + low_position + breadth_expand` 等多标签文本。 |
| 取消固定 PHASE_BONUS | `base_score` 仅由 trend/velocity/acceleration/participation 加权；排名按 base_score | 已实现 | `phase` 不影响 rank，符合最关键改造。 |
| 用 phase confidence 小幅调整排名 | 未实现，且 v1 设计明确禁止 phase 改排名 | 有意不实现 | 这是对原方案第二阶段的审慎收缩；应在样本外证据后再讨论。 |
| 市场状态 risk_on/risk_off/range/high_volatility | `market_regime.py` 有优先级和乘数 | 部分实现 | **重要：** `run_daily.py` 当前给 `classify_market_regime` 的 limit_up/limit_down 固定为 0，且 breadth 仅为当日中位数；因此 risk_off 条件在日常编排中不会命中，市场状态输入需修复为 `load_market_aggregates` 的真实历史聚合。 |
| regime 只缩放风险暴露、不重排 | `composite_rank` 按 base_score，`composite_score=base*multiplier` | 已实现 | 同日公共乘数不改变名次。 |

## 三、快照、排名历史、输出和研究复核

| 原优化点 | 当前实现与证据 | 状态 | 复核结论 / 风险 |
| --- | --- | --- |
| 保存每日历史快照和审计 | `run_log`、`daily_snapshot`，同键 UPSERT | 已实现 | 已在真实库执行 DDL，正在回填验证。 |
| phase_age、rank_change 1/5d、Top10 持续性 | 已计算并落库 | 部分实现 | `top10_days_20` 当前实现为“连续在 Top10 的天数”，不是严格“过去 20 日累计在榜天数”；字段命名/算法需二选一统一。 |
| 幂等重跑 | 快照/标签均 UPSERT；run_log 每次新增审计 | 已实现 | 上游数据或 current_mapping 变化时历史结果改变是预期行为。 |
| CSV、TopN、数据质量输出 | `report.py` 三类文件 | 已实现 | 仅在快照成功提交后输出。 |
| 5/10 日前瞻标签 | 按未来第 N 个交易日构造并写入 forward_return | 已实现 | 需在足够回填后验证真实标签成熟度。 |
| IC、Rank IC、五分组、胜率、回撤、换手 | `backtest.py/evaluate_factor` | 已实现 | 为基础统计实现；真实样本检验尚未完成。 |
| 按市场状态分桶研究 | `evaluate_by_regime` | 部分实现 | 函数存在，但受上述 market_regime 编排输入缺口影响，真实分桶结果暂不可信。 |
| 252/63/21 滚动样本外 | `rolling_oos_windows` 只生成窗口边界 | 部分实现 | 未对每个窗口执行训练/验证评价，也未写研究指标。 |
| 写入 backtest_metric 长表 | DDL 已建表 | 未实现 | `run_backtest.py` 当前只输出 CSV，未调用该表的持久化函数。 |

## 四、可视化和数据结构复核

| 原优化点 | 当前状态 | 结论 |
| --- | --- | --- |
| 四象限：X=velocity、Y=acceleration、大小=volume、颜色=phase、透明度=confidence、边框=participation | 所需核心字段已计算/大部分已落快照 | 数据准备已完成，图形未开发，符合“先优化数据、后做可视化”的决策。 |
| 5 日轨迹 | 每日快照可查询；未提供轨迹查询/图形接口 | 部分完成；回填至少 5 日后可由查询层构造。 |
| 排名热力图、phase 带、TopN 漂移、雷达图 | 未实现 | 有意延后至真实数据验证通过后。 |

## 五、相对原方案的验收结论

### 已达到的关键目标

1. 新版不再以离散 phase bonus 主导排名；连续评分与解释状态分离。
2. 增加了 RS 多周期、量能份额、个股/板块广度和资金确认。
3. 具备历史快照、可回填 phase、排名变化、标签和基础研究链路。
4. 运行具备审计、失败记录、参数化写库、NaN→NULL 处理与进度日志。

### 必须在继续大范围回填前修复或确认的事项

1. **市场状态输入：** 在 `run_daily.py` 接入真实 `load_market_aggregates` 历史数据，不得继续传固定 0 的涨跌停数；修复后应从受影响起始日重刷快照。
2. **Top10 字段语义：** 明确要“连续在榜天数”还是“过去 20 日累计在榜天数”，并使算法、字段名、DDL COMMENT、报告一致。
3. **研究落库与 OOS：** 若 `sector_rotation_backtest_metric` 是正式交付物，补持久化；若要求真正的滚动样本外，则按窗口实际计算而非只输出边界。
4. **真实数据验收：** 按单日验证指南，至少核查上涨、下跌、震荡各类日期；当前只能证明代码测试通过，不能证明指标有效。

### 有意保留到下一规格的事项

- 历史行业成员映射；
- 历史自由流通市值、等权/市值加权差与集中度；
- 小盘/大盘和风格相对强弱；
- 图形化主视图、轨迹交互与自动调权。

## 最终判断

若以“原方案最重要的结构性优化是否落地”为标准：**已基本落地**。  
若以“原方案每个建议、每个研究闭环和可视化都完成”为标准：**未完全完成**，尤其是市场状态真实输入、Top10 语义、OOS 实评估和可视化仍需后续迭代。
