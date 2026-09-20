# QMT HTTP Bridge 迁移验证报告

日期：2026-09-20

## 结论

适配层和六个 `_qmt_bridge` 复制版本已完成离线契约验证。生产调度入口未切换，原始消费者文件保持不变。本报告的真实 QMT 冒烟状态为 `BLOCKED`：当前执行环境未连接已启动并配置真实账户的 QMT Bridge，因此不能声称线上数据等价。

## 离线验证

执行命令（使用工作区可写临时目录）：

```text
PYTHONPATH=src;src/data_ingestion python -m pytest --basetemp .test-tmp/bridge-task5 tests/test_price_projection_store.py tests/test_dual_track_workflow.py tests/test_market_data_logging.py tests/test_price_projection_store_qmt_bridge.py tests/test_market_data_logging_qmt_bridge.py tests/test_financial_collector_qmt_bridge.py -q
49 passed

PYTHONPATH=src;src/data_ingestion python -m pytest tests/data_ingestion/test_qmt_data_gateway.py tests/data_ingestion/test_qmt_bridge_server_contract.py -q
13 passed

PYTHONPATH=src;src/data_ingestion python -m pytest tests/research/test_etf_providers.py tests/research/test_etf_providers_qmt_bridge.py tests/test_sector_rotation_qmt_bridge.py -q
50 passed
```

## 消费者状态

| 消费者 | 离线契约/回归 | 真实 QMT 冒烟 | 说明 |
| --- | --- | --- | --- |
| 三投影行情 | PASS | BLOCKED | `none/front/back` 与原投影函数兼容；未连接真实缓存。 |
| 传统行情 | PASS | BLOCKED | 保留成交量手→股换手率计算；未连接真实缓存。 |
| 财务 | PASS | BLOCKED | 嵌套财务 DataFrame 与 `report_time` 保留；未取得真实财报批次。 |
| Morning K线 | PASS | BLOCKED | 后复权调用契约已验证；未连接真实缓存。 |
| 行业分类 | PASS | BLOCKED | 依赖新 `download_sector_data` 端点；未验证 QMT 返回行业全集。 |
| ETF篮子 | PASS | BLOCKED | 缺权重仍拒绝；未验证真实 ETF 全量加权篮子。 |

## 尚需在 QMT 客户端执行

1. 使用复制的 `CY_QMT_API_qmt_bridge.py` 启动 Bridge，配置真实 Token。
2. 设置外部环境的 `QMT_BRIDGE_URL` 和 `QMT_BRIDGE_TOKEN`，请求一只股票、一只 ETF、一个 SW 行业和一批财务数据。
3. 保存四类响应的代码、日期范围、行数、字段和数值误差对照；确认行业下载与 ETF 下载端点返回成功。
4. 只有六项真实冒烟均通过，才允许创建后续独立的调度入口切换变更。

## 不变性检查

原始六个消费者、`run_daily_pipeline.py`、数据库标签和生产入口均未在本阶段修改。复制版本可回退或并行运行，不会覆盖原始脚本。
