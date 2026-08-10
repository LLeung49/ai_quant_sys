# sector_rotation2 可视化 API 契约与字段字典

## 1. 契约目标

本 API 只读取 `sector_rotation_run_log.status='succeeded'` 对应的已持久化快照，不在请求期间重算指标、阶段或排名。所有数值字段输出为 JSON number，数据库 `NULL` 输出为 JSON `null`。当前接口前缀为 `/api/v1/sector-rotation`，字段语义版本为 `meta.field_version='v1'`。

成功响应都包含：

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `sector_level` | integer | 申万行业层级，当前仅允许 1 或 2 |
| `model_version` | string | 评分模型口径版本，例如 `v1` |
| `meta.run_status` | `succeeded` | 明确响应只包含成功运行数据 |
| `meta.field_version` | `v1` | API 字段语义版本，与模型版本含义不同 |
| `meta.source_max_trade_date` | string/null | 对应运行读取到的上游最大交易日；跨日响应取最大值 |
| `meta.eligible_sector_count` | integer/null | 对应最新响应交易日可评分行业数 |
| `meta.skipped_sector_count` | integer/null | 对应最新响应交易日证据不足行业数 |
| `meta.market_regime` | string/null | 已持久化的市场状态，不在 API 中重算 |
| `meta.regime_multiplier` | number/null | 市场状态风险缩放系数 |

`available-dates` 不代表某一次运行，因此其运行级字段为 `null`；具体快照、行业历史与回放接口返回对应运行元信息。

## 2. 接口

### 2.1 `GET /healthz`

用于确认 HTTP 服务存活。成功返回 `{"status":"ok"}`，不代表数据库中一定存在板块快照。

### 2.2 `GET /api/v1/sector-rotation/available-dates`

参数：`level`（默认 2）、`model_version`（默认 `v1`）。返回存在成功运行记录的交易日倒序列表 `dates`；没有成功日期时返回空列表。

### 2.3 `GET /api/v1/sector-rotation/snapshot`

参数：`as_of_date`、`level`、`model_version`。返回一个交易日的完整行业截面：

```json
{
  "as_of_date": "2026-08-04",
  "sector_level": 2,
  "model_version": "v1",
  "meta": {
    "run_status": "succeeded",
    "field_version": "v1",
    "source_max_trade_date": "2026-08-04",
    "eligible_sector_count": 113,
    "skipped_sector_count": 0,
    "market_regime": "high_volatility",
    "regime_multiplier": 0.85
  },
  "sectors": []
}
```

### 2.4 `GET /api/v1/sector-rotation/sector-history`

参数：重复传入 1 至 5 个 `sector_name`，以及 `start_date`、`end_date`、`level`、`model_version`。`points` 只包含数据库实际存在的成功快照点。前端依据成功交易日集合补出 `null` 断点，不做插值。超过 5 个行业时，接口返回统一的参数校验错误，且不会执行数据库查询。

### 2.5 `GET /api/v1/sector-rotation/replay`

参数：`start_date`、`end_date`、`level`、`model_version`。返回区间内全部行业的成功快照点，按日期和行业排序。前端一次预加载并在浏览器内逐帧播放，播放期间不重复请求。

### 2.6 `GET /api/v1/sector-rotation/sector-kline`

读取一个行业的合成指数**日 K 线**，供详情抽屉中的主图、成交量图和 MACD 图共同使用。该接口独立于评分快照：它只读行情表 `trade_sector_daily`，不会在请求期间计算成分股、重算轮动指标，也不会写入任何数据。

| 参数 | 类型 | 必填 | 约束 | 说明 |
| --- | --- | --- | --- | --- |
| `sector_name` | string | 是 | 1～64 个字符；去除首尾空白后不得为空 | 完整行业名称，精确匹配，不支持模糊查询 |
| `level` | integer | 是 | 仅 `1` 或 `2` | 申万行业层级 |
| `end_date` | string | 是 | `YYYY-MM-DD` | 请求的行情截止日；响应中任何 bar 都不会晚于它 |

查询条件固定为 `sector_name + sector_level + trade_date <= end_date`。数据库先按交易日倒序截取最近 **350** 根候选日线，再恢复为严格升序返回；因此响应的 `bars` 最多 350 根。前端默认显示最近 120 根，但仍保留前序数据作为指标预热；当可见窗口为 250 根时，最多可使用前置 **100 根**完成 MA60、BOLL20、VOL10 和 MACD(12,26,9) 的预热。数据少于可见窗口或预热目标时，接口仍返回真实有效数据，前端以“长期指标仍在形成”提示，不补零、不插值。

成功示例：

```json
{
  "sector_name": "半导体",
  "sector_level": 2,
  "requested_end_date": "2026-08-06",
  "actual_end_date": "2026-08-05",
  "price_basis": "equal_weight_composite_index",
  "bars": [
    {
      "trade_date": "2026-08-05",
      "timestamp": 1785859200000,
      "open": 1098.23,
      "high": 1124.68,
      "low": 1087.41,
      "close": 1116.52,
      "volume": 1234567.0,
      "amount": 987654321.0
    }
  ],
  "meta": {
    "field_version": "v1",
    "source": "trade_sector_daily",
    "bar_count": 350,
    "skipped_bar_count": 2,
    "warmup_target": 100
  }
}
```

`actual_end_date` 是清洗后最后一根有效 bar 的实际交易日，可能早于 `requested_end_date`（例如非交易日、停牌或当天行异常）；它是抽屉和弹窗标题中应显示的截止日。`timestamp` 为该 `trade_date` 在 `Asia/Shanghai` 时区 `00:00:00` 对应的 Unix **毫秒**时间戳，而不是浏览器本地零点。

| 成功字段 | 类型 | 含义 |
| --- | --- | --- |
| `price_basis` | literal | 固定为 `equal_weight_composite_index`，即行业等权合成指数口径，不是可交易 ETF、个股价格或收益率 |
| `bars[].open/high/low/close` | number | 行业合成指数 OHLC，传给 KLineChart 主 K 线图 |
| `bars[].volume` | number | 原始行业合成成交量，传给成交量副图 |
| `bars[].amount` | number | 原始行业合成成交额；前端映射为 KLineChart 的 `turnover` 字段 |
| `meta.bar_count` | integer | 清洗后实际返回的有效 bar 数量，范围 1～350 |
| `meta.skipped_bar_count` | integer | 本次 350 根候选行中因质量规则被排除的行数 |
| `meta.warmup_target` | integer | 固定 100；前端用于判断长周期指标是否拥有充足预热数据 |

数据边界清洗规则如下：日期必须可解析；数值统一转换为有限 JSON number；`volume`、`amount` 必须非负；`low <= min(open, close) <= max(open, close) <= high`；未来日期、重复日期和任何不满足前述条件的候选行均跳过。系统不会把 `NaN` 转为 0，不会修正高低价，也不会将坏行补成相邻交易日。每个交易日只保留清洗后遇到的第一条有效记录，最终按交易日严格升序输出。

该端点不需要、也不允许执行任何 DDL。部署前只需存在并持续维护已有的 `trade_sector_daily` 行情数据；接口为只读查询。

## 3. 核心行业字段

| 字段 | 来源 | 前端含义 | `null` 处理 |
| --- | --- | --- | --- |
| `sector_name` | 快照表 | 行业名称 | 不应为空 |
| `score_eligible` | 快照表 | 是否具备综合评分资格 | `0` 不进入默认排名 |
| `velocity_score` | 快照表 | 趋势速度横截面相对得分 `[-1,1]`，主图横轴 | 缺失时不绘制气泡 |
| `acceleration_score` | 快照表 | 趋势加速度横截面相对得分 `[-1,1]`，主图纵轴 | 缺失时不绘制气泡 |
| `volume_score` | 快照表 | 量能活跃度相对得分，编码气泡大小 | 缺失时使用中性基础大小，不解释为零信号 |
| `participation_score` | 快照表 | 行业内部参与度相对得分，编码气泡描边 | 缺失时使用弱描边 |
| `phase_confirmed` | 快照表 | 三日两次规则确认后的阶段 | 显示“方向未明” |
| `phase_changed` | 快照表 | 相比前一日确认阶段是否切换 | 缺失时不触发“阶段刚切换”关注原因 |
| `phase_age` | 快照表 | 当前确认阶段连续交易日数 | 显示数据不足 |
| `phase_confidence` | 快照表 | 阶段证据置信度，编码气泡透明度 | 使用保守默认透明度 |
| `base_score` | 快照表 | 可用主评分重归一后的基础分 | 显示数据不足 |
| `composite_score` | 快照表 | 基础分乘市场状态缩放系数 | 显示数据不足 |
| `composite_rank` | 快照表 | 同日基础分排名，1 为最高 | 不参与默认排序 |
| `rank_change_1d` | 快照表 | 昨日名次减今日名次；正值表示上升 | 不显示变化原因 |
| `rank_change_5d` | 快照表 | 五日前名次减今日名次；正值表示上升 | 不显示变化原因 |
| `coverage_ratio` | 快照表 | 有效成员数据覆盖率 | 必须显示数据不足，不可当作 0% |

速度、加速度、量能、参与度及综合分都是同日行业截面上的相对观察值，不是收益率，也不构成收益预测。

## 4. 稳定错误信封

所有已处理错误使用同一结构，并在响应头同步返回 `X-Request-ID`：

```json
{
  "error": {
    "code": "SNAPSHOT_NOT_FOUND",
    "message": "未找到已成功运行的板块快照",
    "details": null,
    "request_id": "..."
  }
}
```

| HTTP | `error.code` | 场景 |
| --- | --- | --- |
| 404 | `SNAPSHOT_NOT_FOUND` | 指定日没有成功快照 |
| 404 | `HISTORY_NOT_FOUND` | 所选行业区间没有成功历史点 |
| 404 | `REPLAY_NOT_FOUND` | 回放区间没有成功快照 |
| 422 | `REQUEST_VALIDATION_ERROR` | 层级、数量或其他请求参数不合法 |
| 422 | `INVALID_DATE_RANGE` | 日期格式错误，或开始日晚于结束日 |
| 503 | `DATABASE_UNAVAILABLE` | 数据库连接或查询暂不可用；响应不泄漏连接详情 |
| 500 | `INTERNAL_SERVER_ERROR` | 未预料的服务端异常；响应不泄漏实现细节 |
| 其他 | `HTTP_ERROR` | 其他显式 HTTP 异常的保底错误码 |

`/sector-kline` 对参数和服务异常采用以下四个专用稳定错误码；其余既有端点继续沿用上表的错误码，避免破坏原有调用方。

| HTTP | `error.code` | 场景与调用方处理建议 |
| --- | --- | --- |
| 422 | `INVALID_PARAMETER` | 行业名称为空/超长、层级不是 1 或 2、日期格式不是 `YYYY-MM-DD` 等。修正参数后重试；框架级参数校验的字段位置在 `details` 中。 |
| 404 | `SECTOR_KLINE_NOT_FOUND` | 在请求截止日及之前没有一条通过质量校验的行情。前端只替换行情卡为空状态，详情抽屉其余评分内容仍保留。 |
| 503 | `DATABASE_UNAVAILABLE` | 数据库连接或查询暂不可用。稍后重试；响应不包含连接信息或 SQL。 |
| 500 | `INTERNAL_ERROR` | 未预料的 K 线处理错误。记录 `request_id` 并对照服务端日志排查；响应不泄漏实现细节。 |

无论成功或失败，响应头均包含 `X-Request-ID`；错误信封中的 `error.request_id` 与其相同。排障时应同时保留请求 URL、HTTP 状态、`error.code` 和该请求编号。

定位问题时优先记录 `error.code` 和 `request_id`，再用 `request_id` 对照服务端日志。
