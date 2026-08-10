# 板块轮动 Web 前端

## 启动前准备

1. 先完成 `sector_rotation2.run_daily` 的历史回填；前端只显示 `sector_rotation_run_log.status='succeeded'` 的快照。
2. 在仓库根目录启动只读 API：

```powershell
cd D:\aiQuant\ai_quant_sys
$env:PYTHONPATH = 'src'
uvicorn morning_conference.sector_rotation2.api.app:create_app --factory --host 127.0.0.1 --port 8000
```
-验证健康检查：
  Invoke-RestMethod http://127.0.0.1:8000/healthz
-预期：
  {"status":"ok"}
-验证数据接口：
  http://127.0.0.1:8000/api/v1/sector-rotation/available-dates?level=2&model_version=v1

3. 新开 PowerShell，进入本目录并启动前端：

```powershell
cd D:\aiQuant\ai_quant_sys\web
npm run dev
```

浏览器打开 Vite 输出的本地地址（通常为 `http://localhost:5173`）。若 API 地址不是 `http://127.0.0.1:8000`，在本目录新建 `.env.local`：

```text
VITE_API_BASE_URL=http://127.0.0.1:8000
```

### 板块 K 线依赖与服务自检

板块详情 K 线使用精确锁定的 [`klinecharts@10.0.0`](https://github.com/klinecharts/KLineChart) Core（Apache-2.0 许可证）。依赖版本由 `package-lock.json` 固定；首次在 `web` 目录执行 `npm ci`，不要以 CDN、KLineChart Pro 或浮动版本替换它。

启动 API 后，先在浏览器或 PowerShell 验证行情端点（实际行业名称和截止日需以本地数据为准）：

```powershell
Invoke-RestMethod 'http://127.0.0.1:8000/api/v1/sector-rotation/sector-kline?sector_name=%E5%8D%8A%E5%AF%BC%E4%BD%93&level=2&end_date=2026-08-06'
```

预期返回 `bars`、`actual_end_date` 和 `meta`。`actual_end_date` 可以早于请求日，表示最后一根有效交易日；任何返回 K 线都不得晚于 `end_date`。本功能只读已有的 `trade_sector_daily`，**不新增、不修改表或字段，也不需要执行 DDL**。

## 使用方式

1. 首屏默认显示二级行业的最新成功交易日；切换“交易日”会读取该日快照，切换行业层级会重新读取该层级的最新有效日。
2. 主图的“单日观察”和“动态回放”共用同一个象限。回放时，市场摘要、气泡图、今日关注和详情面板统一跟随时间轴，不会出现两个含义重复的气泡图。
3. 象限图横轴是趋势速度相对得分，纵轴是趋势加速度相对得分，均为 `[-1,1]` 的截面相对位置，不是收益率。气泡颜色表示确认阶段，大小表示量能活跃度，透明度表示阶段置信度，边框表示参与度。
4. “标注密度”可选精简、关注、全部。关注模式优先标注当前选中、综合排名靠前、阶段刚切换、排名大幅变化、加速度极值、加速走弱和修复确认的行业；鼠标悬浮气泡时，“关注原因”区域会解释本次入选原因。
5. 点击气泡或排行榜行业后，回放主图会叠加该行业最近 10 个成功交易日的虚线尾迹。下方“行业轨迹对比”最多保留五个行业，可切换 5/20/60 日，使用稳定颜色对比完整移动路径。
6. 历史坐标缺失时，轨迹会断开并在图下列出缺口数量，不插值、不把缺失当作零分。播放、步进和时间轴只使用预加载历史快照，不会逐帧请求接口。
7. 日期、层级、模式、阶段、搜索、当前行业、轨迹窗口和标注密度会写入 URL，刷新或复制链接后可恢复工作台状态。

### 板块详情 K 线

1. 点击象限气泡或排行榜行业打开详情抽屉。行情卡的请求截止日始终使用当前工作台日期：单日观察切换日期后使用该日期；动态回放播放、步进或拖动时间轴后使用当前帧日期。因此历史回放不会读取未来 K 线。
2. 行情卡内为与抽屉同宽的缩略三联图：上方为传统日 K 线、MA5/10/20/60 和 BOLL(20,2)，中间为成交量与 VOL5/10，底部为 MACD(12,26,9)，柱值为 `2 × (DIF - DEA)`。配色固定为 A 股红涨绿跌，MA5 金、MA10 蓝、MA20 紫、MA60 粉、BOLL 青色虚线、DIF 金、DEA 蓝。
3. 缩略图默认展示 120 个交易日，禁止滚轮缩放、拖拽和平移；点击 60/120/250 日只调整内存中的可见窗口，不会额外请求 `/sector-kline`。接口最多返回 350 根，前端保留最多 100 根前置日线作为长周期指标预热。
4. 点击“放大查看”打开原生弹窗。放大图复用抽屉已读取且经契约校验的数据，支持 60/120/250、范围滑块、滚轮缩放、拖拽与平移；不会重新发起行情请求。首次 `Esc` 只关闭放大弹窗，第二次 `Esc` 才由抽屉处理关闭；弹窗关闭后焦点回到“放大查看”按钮。
5. `price_basis=equal_weight_composite_index` 表示行业等权合成指数口径；`amount` 被映射为 KLineChart 的成交额 `turnover`。它们是研究展示数据，不是可交易证券价格或实时行情。

### K 线 Review 与验收清单

1. 在“单日观察”选择 `2026-08-06`（或本地可用日期），打开任意板块抽屉，核对行情卡 `截至 actual_end_date` 不晚于工作台日期；切换到“动态回放”的不同历史帧后重复核对，确保末根 K 线没有未来数据。
2. 从数据库抽取同一行业、同一交易日的 `open_idx/high_idx/low_idx/close_idx/total_volume/total_amount`，与 K 线 Tooltip 比对 OHLCV 和成交额；`total_amount` 应对应图表成交额。请同时确认价格口径为“等权合成指数”。
3. 依次切换 60/120/250 日，检查图中可见根数变化；在浏览器 Network 面板确认不会新增 `/sector-kline` 请求。缩略图约 340px 高且与抽屉同宽，控制台不应出现 KLineChart 零尺寸警告。
4. 点击“放大查看”，检查滚轮缩放、拖拽、平移、范围滑块和 Tooltip；核对红涨绿跌、MA/BOLL/DIF/DEA 颜色。将浏览器缩窄，确认 dialog 接近全屏且标题、图表、关闭按钮均可操作。
5. 先按一次 `Esc`，确认只关闭放大 dialog 且焦点回到放大按钮；再按一次 `Esc`，确认抽屉关闭。检查无数据、坏行被跳过和预热不足时分别显示本地提示；模拟 API 失败时，只有行情卡显示错误与 `request_id`，评分拆解和详情其他区域仍可读。

## 推荐 Review 顺序

1. 在“单日观察”选择最新日期，确认页面顶部数据源截止日、市场状态、可评分行业数与数据库成功快照一致。
2. 将标注密度切换为“关注”，依次悬浮排名靠前、阶段切换、排名突变、加速度极值、加速走弱或修复确认的气泡，核对悬浮框中的“关注原因”。
3. 点击一个行业，切换“动态回放”，用上一帧、下一帧、时间轴和 0.5×/1×/2× 播放，确认摘要、排行榜、详情和日期同步变化，且主图仅有一个。
4. 观察选中行业的近 10 日虚线尾迹；再从其他日期点击最多四个行业，确认下方对比轨迹不超过五条，且五条轨迹颜色稳定、5/20/60 日窗口有效。
5. 找一个历史坐标不完整的行业，确认轨迹断线且出现“数据缺口”，没有连接缺失日期。
6. 刷新当前网址，确认日期、模式、筛选、行业、窗口和标注密度得到恢复。

## 验证与排障

- API 健康检查：请求 `http://127.0.0.1:8000/healthz`，预期 `{"status":"ok"}`。
- 无数据：先在 MySQL 确认目标日期、层级、模型版本存在 `succeeded` 运行；失败/运行中的任务不会展示。
- API 错误：响应始终是 `error.code`、`error.message`、`error.details`、`error.request_id` 结构。保留 `X-Request-ID` 可定位服务端日志。
- 数据库暂不可用：API 返回 HTTP 503 与 `DATABASE_UNAVAILABLE`，不会向浏览器暴露连接信息。
- 数据不足：页面显示“数据不足”或不绘制行业，不能将其解释为零分或中性信号。
- K 线无数据：`SECTOR_KLINE_NOT_FOUND` 表示请求日及之前没有通过质量校验的日线；检查行业名称、层级、日期以及 `trade_sector_daily` 的 OHLCV/成交额完整性。坏行会被跳过而不是修正，跳过数量见响应 `meta.skipped_bar_count`。
- K 线 API 失败：保留 HTTP 状态、`error.code`、`error.request_id` 和响应头 `X-Request-ID`。`INVALID_PARAMETER` 需修正请求；`DATABASE_UNAVAILABLE` 可稍后重试；`INTERNAL_ERROR` 应以 request_id 查询服务端日志。
- 预热不足：当有效日线不足以为当前可见窗口留下 100 根前置数据时，页面提示“长期指标仍在形成”；这不是缺失日线的填充，也不应解释为指标为零。
- 全量验证：执行 `npm run lint`、`npm run test -- --run`、`npm run build`；Python 执行 `$env:PYTHONPATH='src'; python -m pytest tests -q -k sector_rotation2`。

## 风险提示

页面展示的是基于历史快照的量化研究观察，不构成投资建议，也不保证任何收益。
