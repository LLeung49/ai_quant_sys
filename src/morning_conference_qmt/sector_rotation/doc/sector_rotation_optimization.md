整体看，这套框架的**分层结构是合理的**：数据底座、导数指标、强度评分、phase 分类、综合排名、输出层已经比较清晰，也给后续回测和可视化留出了接口。当前真正需要优化的不是“再增加几个技术指标”，而是解决三个核心问题：

1. 指标之间存在重复和量纲不一致；

2. phase 目前是硬阈值投票，容易跳变和误判；

3. 强度、趋势阶段、量能被过早压缩成一个总分，损失了决策信息。

你的当前实现是 MOM、RS、VOL_RATIO 等权生成强度分，再加上固定的 `PHASE_BONUS` 得到最终排名；其中 phase 加分甚至与横截面 Z-score 处于相同甚至更大的量级。 这会导致最终排名很大程度上由 phase 分类决定，因此 phase 一旦误判，排名偏差会被放大。

---

# 一、先不要强调“0阶、一阶、二阶”，改成四类状态指标

你现在的分类在工程上可以理解，但数学上不完全严谨。

例如：

- `MOM_21` 本身已经是价格变化率；

- `ROC_20` 和 `MOM_21` 本质高度接近；

- `MACD_HIST` 更接近两个平滑趋势速度之间的差值，不是严格意义上的价格二阶导；

- `ROC_ACCEL = ROC_20 - ROC_20.shift(5)` 才比较接近“速度变化”。

当前 MOM_21、ROC_20，以及 MA20_SLOPE 都是在不同平滑尺度上描述趋势方向和强弱，相关性可能非常高。你目前把 MOM_21 放在强度层，把 ROC_20 放在速度层，但两者窗口只相差一天。

建议不要继续纠结它们属于几阶导，而是改成下面四类。

## 1. 趋势位置 Trend Level

回答：“这个板块当前处于强势还是弱势区域？”

建议指标：

- 20日相对收益；

- 60日相对收益；

- 距离 MA20、MA60 的百分比；

- 横截面排名百分位；

- 相对于全市场、同风格板块的超额收益。

这里最好主要使用**相对强度**，而不只是绝对涨幅。

例如：

[  
RS_{20}=R_{sector,20}-R_{benchmark,20}  
]

[  
RS_{60}=R_{sector,60}-R_{benchmark,60}  
]

当前 `MOM_21` 与 `RS_60` 一个是绝对收益，一个是超额收益，方向合理，但建议加入 `RS_20`，并考虑弱化或删除与 `ROC_20` 高度重复的 `MOM_21`。

---

## 2. 趋势速度 Trend Velocity

回答：“当前向上或向下运动有多快？”

推荐使用两个不同尺度：

- 短周期速度：5日或10日超额收益；

- 中周期速度：20日超额收益；

- 平滑价格趋势斜率。

但不建议同时重权使用：

- MOM_21；

- ROC_20；

- MA20_SLOPE。

三者相关度很可能非常高。

可以定义统一的速度分：

[  
V =  
0.4 \times PCTL(RS_5)  
+0.35 \times PCTL(RS_{20})  
+0.25 \times PCTL(Slope_{MA20})  
]

其中 `PCTL` 是当日板块横截面百分位，转换到 ([-1,1])。

使用百分位比直接使用原始值更适合板块间比较，因为：

- 不容易被极端板块拉动；

- 不要求指标服从正态分布；

- 不同指标量纲可以自然统一。

---

## 3. 趋势加速度 Trend Acceleration

回答：“趋势是在增强还是衰减？”

你当前的：

- `MA20_ACCEL`

- `ROC_ACCEL`

- `MACD_HIST` 或 MACD_HIST 变化

方向基本正确。

但建议明确区分：

### 速度变化

[  
A_{ROC}=RS_{20,t}-RS_{20,t-5}  
]

最好使用**超额收益速度的变化**，而不是板块绝对 ROC 的变化，否则市场整体大涨时，大多数板块都会同时被判为加速。

### 斜率变化

[  
A_{Slope}=Slope_{t}-Slope_{t-5}  
]

### 短中周期动量差

[  
A_{multi}=RS_5-\frac{5}{20}RS_{20}  
]

它表达最近5日的平均上涨速度是否高于过去20日平均速度。

建议最终形成连续加速度分：

[  
A =  
0.4 \times PCTL(A_{ROC})  
+0.35 \times PCTL(A_{Slope})  
+0.25 \times PCTL(\Delta MACD_HIST)  
]

注意：你文档的指标表写的是 `MACD_HIST`，phase 投票描述写的是“MACD_HIST变化”。 这两个含义不同，代码和文档必须统一：

- `MACD_HIST > 0`：短趋势速度高于长趋势速度；

- `ΔMACD_HIST > 0`：这种趋势差还在扩大。

如果判断“加速度”，应该更偏向使用 `ΔMACD_HIST`，而不是仅使用 `MACD_HIST` 的正负。

---

## 4. 参与度与资金确认 Participation

这是目前体系中最值得补充的一层。

仅仅看价格上涨和成交额放大，无法区分：

- 少数权重股拉动；

- 板块内多数股票共同上涨；

- 板块金额增长只是因为整个市场普遍放量；

- 板块成员数量较多导致天然成交额较大。

建议至少增加以下指标：

### 上涨家数占比

[  
Breadth=\frac{上涨股票数}{有效成分股数}  
]

### 站上 MA20 的股票占比

[  
AboveMA20=\frac{close_i>MA20_i的股票数}{有效成分股数}  
]

### 创20日新高股票占比

[  
NewHigh20=\frac{创20日新高数}{有效成分股数}  
]

### 等权收益和市值加权收益差

如果市值加权涨很多、等权涨幅不明显，说明行情主要由少数龙头拉动。

这一层对板块轮动尤其重要。比单独增加 RSI、KDJ 等技术指标更有价值。

---

# 二、当前 phase 判断的主要问题

你现在使用速度组和加速度组投票，然后把结果映射到四个象限。速度投票中 ROC 权重为2、MA20斜率权重为1；速度为0时，无论加速度如何都直接进入 neutral。

这个方案简单、可解释，但有五个问题。

## 1. 硬阈值导致 phase 高频跳变

例如：

- 今天 ROC_20 = 0.51%，判正；

- 明天 ROC_20 = 0.49%，判中性。

实际趋势没有明显改变，但 phase 会发生切换。

建议把硬方向改成连续得分，并设置缓冲区：

```text
V > +0.20：向上
V < -0.20：向下
-0.20 <= V <= +0.20：震荡
```

同时引入 hysteresis，避免在边界反复切换：

```text
neutral → up：要求 V > 0.25
up → neutral：只有 V < 0.10 才退出
```

进入条件和退出条件不同，可以显著降低 phase 抖动。

---

## 2. 没有持续性确认

单日加速度转正，不一定意味着趋势真正发生变化。

建议增加：

- 连续2日或3日满足；

- 最近3日中至少2日满足；

- phase 最短保持2日；

- `phase_age`：当前 phase 已持续多少天；

- `phase_confidence`：当前分类置信度。

例如：

```text
candidate_phase = accel_up
confirmed_phase =
    candidate_phase 最近3天出现至少2次
    且 V_score > 0.2
```

这也正好解决文档中提到的“没有持续性度量”。

---

## 3. `decel_down` 不应天然获得较高推荐度

当前逻辑中：

- 速度向下；

- 加速度向上；

就被定义为 `decel_down`，并给予 `+2.0`，仅次于主升阶段。

但“跌得慢了”不等于“马上会上涨”。

这类板块可能处于：

- 下跌中继；

- 超跌反弹；

- 横盘后继续下跌；

- 真正的底部反转。

因此建议把 `decel_down` 拆成：

### Bottoming Candidate：筑底候选

满足：

- V < 0；

- A > 0；

- 但 RS20 仍弱；

- 暂不加分。

### Reversal Confirmed：反转确认

额外要求至少两个条件：

- 5日超额收益转正；

- 收盘重新站上 MA20；

- Breadth > 50%；

- 成交量确认；

- V 穿越0；

- 相对强度排名连续提升。

只有反转确认之后，才进入较高推荐状态。

也就是说，你的四象限适合描述**运动状态**，但不能直接等价为**投资建议**。

---

## 4. phase 应加入“位置”维度

同样是 `V > 0, A > 0`：

- 刚从底部启动；

- 已连续上涨两个月；

- 已经偏离 MA20 很远；

风险收益比完全不同。

因此 phase 最好不是单纯二维，而是：

```text
趋势方向 V
趋势变化 A
趋势位置 L
参与度 P
```

仍然可以保留四象限作为主分类，但增加标签：

```text
accel_up + low_position + breadth_expand
accel_up + high_position + breadth_diverge
decel_down + oversold
decel_down + weak_breadth
```

这样比单纯 `accel_up` 更有决策价值。

---

## 5. 建议输出 phase confidence

例如：

[  
Confidence =  
0.35|V|+  
0.35|A|+  
0.20Participation+  
0.10Persistence  
]

或者更简单地输出：

```text
phase_confidence ∈ [0, 100]
```

这样可视化时可以：

- 低置信度点降低透明度；

- 高置信度点高亮；

- 排名时对低置信度 phase 降权。

---

# 三、量能应该怎样做板块间比较

你提出的：

> 本板块成交量 / 本板块成交量 MA20

是一个合理起点，但它主要回答：

> 这个板块相对于自己过去是否放量？

它并不能完整回答：

> 这个板块今天是否比其他板块更受到资金关注？

因此建议同时构建三类量能指标。

## 1. 自身相对放量 RVOL

建议使用成交额而不是成交量：

[  
RVOL_{5,20}=  
\frac{MA_5(amount)}{MA_{20}(amount)}  
]

相比你现在的 `5日 / 60日`，5/20更适合中短期轮动；5/60更稳定，但反应较慢。当前实现使用的是近5日成交额除以近60日均值。

可以两个都保留：

```text
RVOL_FAST = MA5 / MA20
RVOL_SLOW = MA5 / MA60
```

前者看近期资金突然进入，后者看中期量能环境。

---

## 2. 市场成交额占比

[  
AmountShare_t=  
\frac{板块成交额_t}{全市场成交额_t}  
]

然后再看它自身的历史变化：

[  
ShareImpulse=  
\frac{AmountShare_t}{MA_{20}(AmountShare)}  
]

这个指标非常重要，因为它剔除了全市场整体放量的影响。

例如：

- 板块成交额上涨50%；

- 全市场成交额上涨80%；

那么这个板块实际上是在失去资金关注。

只看自身 RVOL 会误认为放量，但 `ShareImpulse` 会低于1。

---

## 3. 横截面量能排名

将每个板块的 `log(RVOL)` 或 `ShareImpulse` 做横截面百分位：

[  
VolumeScore=  
2\times PCTL(\log RVOL)-1  
]

转换到 ([-1,1])。

这样才适合用于四象限中散点大小的板块间对比。

### 推荐的气泡大小指标

我建议不要直接用原始成交额，也不要直接用原始 `MA5/MA20`，而是：

[  
BubbleSize =  
PCTL\left(  
0.5\log(RVOL_{5,20})  

+ 0.5\log(ShareImpulse)  
  \right)  
  ]

原因是：

- 原始成交额严重受板块规模影响；

- RVOL 可以识别自身放量；

- ShareImpulse 可以识别相对全市场的资金抢占；

- 百分位可以控制极端值和图形大小。

---

## 4. 成员数量问题

你的板块数据中已经输出 `member_count`。 如果板块成交额是所有成分股成交额求和，那么成员数量多的板块天然成交额更高。

处理方式不是简单除以成员数量，因为不同股票规模差异很大。更好的方法是：

- 使用板块成交额占全市场成交额比例；

- 或使用板块自由流通市值换手率；

- 或对成分股个体 RVOL 取中位数。

推荐增加：

[  
MedianStockRVOL=  
median_i\left(\frac{amount_{i,t}}{MA20(amount_i)}\right)  
]

它能回答：

> 是整个板块普遍放量，还是少数大股票贡献了成交额？

可以同时输出：

```text
sector_rvol        板块总成交额放量
median_stock_rvol  典型成分股放量
breadth_rvol       放量股票占比
```

---

# 四、四象限散点图应该怎么设计

你提出的基本方案是对的，但建议横纵轴不要直接使用单一原始指标。

## 推荐设计

### 横坐标：综合速度分 `V_score`

不要只用 ROC_20，而是：

```text
V_score =
0.4 × RS5_pct
+ 0.35 × RS20_pct
+ 0.25 × MA20_SLOPE_pct
```

范围统一为 ([-1,1])。

### 纵坐标：综合加速度分 `A_score`

```text
A_score =
0.4 × ROC_ACCEL_pct
+ 0.35 × MA20_ACCEL_pct
+ 0.25 × MACD_HIST_DELTA_pct
```

### 点大小：量能确认

```text
volume_score =
0.5 × RVOL_FAST_pct
+ 0.5 × SHARE_IMPULSE_pct
```

### 点颜色：phase

仍然保留四象限颜色。

### 点透明度：phase confidence

低置信度变淡，高置信度更加明显。

### 点边框或形状：参与度

例如：

- 实心圆：上涨家数占比 > 60%；

- 空心圆：上涨主要由少数股票驱动。

### 添加5日轨迹

这是四象限最值得增加的功能。

单个点只能展示今天状态，短轨迹可以展示：

- 从左下向右上移动：潜在反转；

- 在右上继续向外移动：加速主升；

- 从右上往右下移动：仍上涨但开始减速；

- 从右下向左下移动：趋势转弱。

相比单纯看当前 quadrant，轨迹方向往往更有价值。

---

# 五、综合评分不建议继续简单相加

当前：

[  
Composite = StrengthScore + PhaseBonus  
]

最大的问题是 phase 是离散分类，`+3、+2、-2` 影响过大，而且没有历史验证。文档本身也已经指出这一点。

建议分三步改造。

## 第一阶段：先取消大额固定 bonus

改成：

```text
composite_score =
0.45 × strength_score
+ 0.25 × velocity_score
+ 0.15 × acceleration_score
+ 0.15 × participation_score
```

全部输入先转成百分位或 robust Z-score。

phase 只作为标签，不直接进入评分。

---

## 第二阶段：加入 phase confidence，而非 phase bonus

例如：

```text
phase_adjustment =
direction × confidence × 0.3
```

其中：

- accel_up：direction = +1；

- accel_down：direction = -1；

- decel_up：direction = -0.3；

- decel_down：direction = 0，等待确认。

这样不会因为一次 phase 分类就让板块排名直接提高3个标准差。

---

## 第三阶段：通过历史 IC 和回测确定权重

对每个指标计算：

- 未来5日超额收益 IC；

- 未来10日超额收益 IC；

- Rank IC；

- 分组收益；

- 换手率；

- 最大回撤；

- 不同市场环境下的稳定性。

权重不要仅根据总收益调整，而要综合：

[  
Weight_i \propto  
\frac{Mean(IC_i)}{Std(IC_i)}  
]

并且进行滚动训练、样本外验证。

需要特别避免：

- 使用全历史一次性优化；

- 反复调参数直到历史收益最好；

- 同一时期既选择指标又评估指标。

---

# 六、建议增加市场状态层

板块轮动效果高度依赖市场环境。

同一个 `accel_up`：

- 在指数多头、成交额扩张时，延续概率可能更高；

- 在市场缩量下跌时，可能只是短暂避险轮动。

建议增加 `market_regime`：

```text
risk_on
risk_off
range
high_volatility
```

可以根据：

- 全市场指数是否高于 MA20/MA60；

- 市场宽度；

- 全市场成交额；

- 涨跌停家数；

- 市场波动率；

- 小盘/大盘相对强弱；

来判断。

最终评分可以变为：

```text
score = base_score × regime_multiplier
```

而不是所有行情下使用同一套 phase bonus。

---

# 七、推荐的最终数据结构

建议每日每个板块输出以下字段组。

## 原始指标

```text
ret_5
ret_20
rs_5
rs_20
rs_60
ma20_slope
roc_accel
ma20_accel
macd_hist
macd_hist_delta
rvol_5_20
rvol_5_60
amount_share
share_impulse
breadth_up
breadth_above_ma20
breadth_new_high
```

## 标准化指标

```text
trend_level_score
velocity_score
acceleration_score
volume_score
participation_score
```

## 状态字段

```text
phase_raw
phase_confirmed
phase_age
phase_confidence
phase_changed
market_regime
```

## 排名字段

```text
strength_rank
velocity_rank
acceleration_rank
participation_rank
composite_rank
rank_change_1d
rank_change_5d
top10_days_20
```

这比继续增加单一 `composite_score` 更适合后续可视化。

---

# 八、可视化建议的优先级

你文档里已经规划了热力图、四象限、phase 时序、TopN 漂移、雷达图。 我建议优先顺序稍作调整：

## 第一优先：四象限 + 5日轨迹

每天直接回答：

- 谁在进入主升？

- 谁在退出主升？

- 谁从杀跌向筑底移动？

- 哪些点量价和宽度共同确认？

## 第二优先：排名热力图

不是只画 composite score，而是分别显示：

- 强度排名；

- 速度排名；

- 加速度排名；

- 参与度排名；

- 综合排名。

这样可以看出某板块排名上升到底是价格、加速度还是量能推动。

## 第三优先：phase 状态带

每个板块按日期显示 phase，并叠加 `phase_confidence`。

## 第四优先：TopN 持续性与迁移

重点字段：

- 首次进入 Top10；

- 连续在榜天数；

- 1日排名变化；

- 5日排名变化；

- 从第几名升到第几名。

## 雷达图优先级较低

雷达图适合人工对比2～4个候选板块，但不适合同时监控几十个板块，也不适合作为每日主视图。

---

# 九、最值得先改的五件事

按照收益成本比排序：

1. **把 phase 的硬投票改成连续 `velocity_score` 和 `acceleration_score`，phase 仅作为分区标签。**

2. **取消或大幅降低固定 `PHASE_BONUS`，尤其是 `decel_down +2`。**

3. **量能同时使用 `RVOL` 和板块成交额市场占比变化，不使用原始成交额做气泡大小。**

4. **加入板块宽度指标，区分多数股票共振和少数龙头拉升。**

5. **保存每日历史快照，增加 phase_age、排名变化和5日轨迹。**

总结来说，你目前的框架已经具备一个不错的“板块状态监控系统”雏形，但暂时还不适合直接把 `composite_rank` 当成买入顺序。更合理的设计是：

> **强度负责筛选候选板块，速度和加速度负责判断切入阶段，量能与宽度负责确认，市场状态负责控制仓位，phase 负责解释而不是决定一切。**

四象限图可以作为核心视图，但建议采用：

```text
X = velocity_score
Y = acceleration_score
气泡大小 = volume_score
颜色 = phase
透明度 = phase_confidence
边框 = breadth confirmation
轨迹 = 最近5日运动路径
```

这会比直接使用 `ROC_20 × MA20_ACCEL × 原始成交量` 稳健很多。
