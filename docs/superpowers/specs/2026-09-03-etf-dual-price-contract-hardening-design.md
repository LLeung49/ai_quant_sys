# ETF 双价格契约补强设计

## 目标

消除自适应 ETF 回测中“复权信号坐标”和“未复权执行坐标”混用的实现空间。数据基础继续提供严格对齐的两套 OHLC 与同日调整比例；后续回测核心只能通过显式转换接口把价格或 ATR 距离带入真实成交、风险预算和账户核算。

## 范围与边界

本次只补强 ETF 自适应策略的价格与公司行动契约，以及对应的 ETF 回测核心实施说明。不实现尚未开始的 `execution.py`、账户账本、订单撮合或策略状态机；它们仍属于 `2026-09-02-etf-adaptive-backtest-core.md` 的后续任务。

用户回测规格的第 3.3 节已经正确规定了两套价格空间，保持不改。旧的其他项目 Phase 6/7 不在范围内。

## 价格坐标契约

`DualPriceBar` 维持现有字段：

- `signal_open/high/low/close`：连续复权坐标，仅用于研究收益、趋势、动量及 MA、MACD、ADX、ATR、布林和唐奇安等技术计算。
- `raw_open/high/low/close`：交易所真实价格坐标，仅用于成交、100 份取整、滑点、佣金、涨跌停、现金、持仓市值和风险金额。
- `adjustment_ratio = signal_close / raw_close`：同一交易日两套坐标之间的唯一比例桥梁。提供者继续验证四个 OHLC 比例一致，并拒绝缺失、错日、未验证或含未来事件的复权投影。

转换函数必须接受正的有限数值与正的有限比例：

```python
def to_signal_price(raw_price: float, adjustment_ratio: float) -> float:
    return raw_price * adjustment_ratio


def to_raw_price(signal_price: float, adjustment_ratio: float) -> float:
    return signal_price / adjustment_ratio


def to_raw_distance(signal_distance: float, adjustment_ratio: float) -> float:
    return signal_distance / adjustment_ratio
```

`to_raw_distance` 明确服务于 ATR、止损距离和加仓距离；`to_raw_price` 服务于完整信号价格阈值转换。禁止用复权价格直接计算份额、费用或账户市值，也禁止从 raw 价格直接减去复权 ATR。

## 公司行动契约

`CorporateAction` 保留现金分红与份额调整的事实字段，并新增稳定、确定性的 `event_id` 属性。标识由 `stock_code`、`effective_date` 与 `action_type.value` 构成；同一来源行至多生成一笔现金分红和一笔份额调整，所以它在当前数据模型中唯一。未来执行账本使用该标识去重：现金分红一次性计入 `cash_per_share * held_shares`，份额调整一次性乘以 `share_multiplier`。不使用复权价格伪造这些账户事件。

配股、股改或无法建模的事件仍按现有 fail-closed 规则拒绝，不能静默降级。

## 回测核心实施约束

回测核心指标模块从 `signal_*` 生成 `IndicatorSnapshot.atr20`，因此该 ATR 是信号坐标距离。趋势模块在 T 日决定交易意图时，先保持信号价格阈值与 ATR；在 T+1 使用 `next_bar.adjustment_ratio` 转换：

```python
atr20_raw = to_raw_distance(snapshot.atr20, next_bar.adjustment_ratio)
stop_distance_raw = trend_config.stop_n * atr20_raw
shares = floor_to_100(budget * risk_per_unit / stop_distance_raw)
```

真实 raw 成交价、raw 止损价、滑点、佣金和账户风险都只使用转换后的值。信号上的比较（例如唐奇安、MACD、ATR 追踪止损）留在信号坐标。若将一个完整信号阈值用于真实撮合，使用 `to_raw_price`；若只转换长度，使用 `to_raw_distance`。

## 测试与验收

数据基础测试新增：

1. raw 价格与 signal 价格的双向转换可逆；
2. 信号 ATR 距离通过 `to_raw_distance` 转换后，按 raw 价格参与风险仓位计算；
3. `CorporateAction.event_id` 对同一动作稳定、对现金分红与份额调整可区分；
4. 无效价格或比例继续 fail-closed。

回测核心计划新增明确的失败测试：以 `signal_atr=0.05`、`ratio=0.25` 验证 raw ATR 为 `0.20`，并验证仓位计算绝不把 `0.05` 直接用于 raw 交易价格。

## 非目标

- 不以当前全历史“前复权”序列替代公司行动账户处理。
- 不改变现有数据表或重刷历史价格。
- 不引入未经来源支持的公司行动类别。
- 不实现回测执行、账户、报表或影子运行模块。
