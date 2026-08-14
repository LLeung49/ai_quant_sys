# v2_short_term 补 ``rs_5`` 字段实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:executing-plans` task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 修复 P1 次日观察候选面板的 V 形反弹 / 破位警惕卡片永远空的问题。根因是流水线里 ``rs_5`` 字段从 features 计算到 schema 落盘都缺失，导致 ``labels.classify_short_term_labels`` 读不到值，两条候选标签永不触发。

**Architecture:** 在不修改 v1 / v2 评分公式、不影响其他短期标签的前提下，给 ``sector_rotation_short_term_daily_snapshot`` 加 ``rs_5`` 列；``features.calculate_sector_short_term_features`` 与 ``snapshot_store.persist_short_term_snapshot`` 同步接入；历史 8 月快照从 v1 快照 JOIN 回填，标签按新 ``rs_5`` 重算。

**Tech Stack:** Python 3.13、pandas、pymysql、pytest、MySQL。

## Global Constraints

- v1 主评分、short_term composite / rank、score_eligible 与 ``momentum_shift_score`` 全部不改动；
- 复用 v1 已有 ``rs_5`` 作为回填来源，**口径必须一致**（v1 与 v2 都通过 ``build_market_benchmark`` 构建归一化基准，已在 ``test_sector_rotation2_features`` 中验证）；
- 历史回填仅写 ``rs_5`` + 标签两个字段，不动其他派生列；
- 新 ``rs_5`` 计算与 ``rs_1`` / ``rs_2`` 同口径（同函数 ``_relative_strength``），便于审计；
- 写入字段顺序与 schema 严格对齐，命名沿用 ``rs_n`` 风格。

---

### Task 1: schema 迁移

**Files:**

- Create: `sql/20260814_add_short_term_rs5_column.sql`

- [x] **Step 1: 写迁移脚本。** `ALTER TABLE sector_rotation_short_term_daily_snapshot ADD COLUMN rs_5 DECIMAL(18,8) NULL COMMENT '5 日累计相对强度（vs 市场基准），与 rs_1/rs_2 同口径' AFTER rs_2;`，幂等可重复执行。
- [x] **Step 2: 本地执行迁移。** 已直接应用，确认 ``SHOW COLUMNS`` 输出含 ``rs_5``。
- [x] **Step 3: 文档留痕。** 在 ``板块异动使用指南.md`` §10.1 字段表补 ``rs_5`` 行。

### Task 2: features.py 接入 ``rs_5``

**Files:**

- Modify: `src/morning_conference/sector_rotation2/short_term/features.py`

**Interfaces:**

```python
def _relative_strength(close: pd.Series, benchmark_close: pd.Series, lookback: int) -> float:
    """rs_n = sector_ret_n - bench_ret_n，窗口不足返回 NaN。"""
```

- [x] **Step 1: 抽取 ``_relative_strength`` 辅助函数。** 与 ``rs_1`` / ``rs_2`` 共用同一口径，支持 ``lookback=1/2/5``。
- [x] **Step 2: 重写 ``rs_1`` / ``rs_2`` / 新增 ``rs_5``。** 改用 `_relative_strength` 调用，避免重复代码。
- [x] **Step 3: 简化 ``rs5_accel_1d``。** 复用 ``_relative_strength`` 计算当日 + 昨日两期 rs_5 后相减，替换原内嵌 ``_rs5`` 函数。
- [x] **Step 4: 把 ``rs_5`` 加入返回字典。** 位置在 ``rs_2`` 之后，与 schema / CSV 顺序对齐。

### Task 3: snapshot_store.py / run_daily.py 列顺序同步

**Files:**

- Modify: `src/morning_conference/sector_rotation2/short_term/snapshot_store.py`
- Modify: `src/morning_conference/sector_rotation2/short_term/run_daily.py`

- [x] **Step 1: ``SHORT_TERM_SNAPSHOT_COLUMNS`` 元组插入 ``"rs_5"``。** 紧跟 ``"rs_2"``，与 schema / INSERT VALUES 顺序一致。
- [x] **Step 2: ``persist_short_term_snapshot`` 的 values 元组对应位置加 ``row.get("rs_5")``。** 通过单测验证 tuple 长度 43 与列数对齐。
- [x] **Step 3: ``run_daily._CSV_COLUMNS`` 加 ``"rs_5"``。** 顺序与 schema 一致。

### Task 4: 新增单元测试

**Files:**

- Create: `tests/test_sector_rotation2_short_term_features.py`
- Create: `tests/test_sector_rotation2_short_term_labels.py`

- [x] **Step 1: ``_relative_strength`` 三档 lookback 数值正确性 + 窗口不足返回 NaN。**
- [x] **Step 2: ``calculate_sector_short_term_features`` 字典包含 ``rs_5`` 且数值与手算一致；``rs5_accel_1d`` 等于 rs_5 当日 − 昨日。**
- [x] **Step 3: ``short_rebound_candidate`` / ``short_breakdown_candidate`` 9 项断言：** 阈值上下、``rs_5`` 缺失、``rs_1`` 不达标、``score_eligible=False``。
- [x] **Step 4: 定向 pytest。** `pytest tests/test_sector_rotation2_short_term_features.py tests/test_sector_rotation2_short_term_labels.py -q`，13 项全部通过。

### Task 5: 历史回填脚本与执行

**Files:**

- Create: `src/morning_conference/sector_rotation2/short_term/backfill_rs5.py`

- [x] **Step 1: 写脚本两步走：** (a) UPDATE rs_5 JOIN v1 快照（口径已对齐）；(b) 按日重跑 ``classify_short_term_labels`` 写回 ``short_term_labels`` / ``short_term_intensity``。
- [x] **Step 2: 验证回填效果。** 8/3–8/13 V 形反弹 / 破位命中从 0 → 累计 63 / 77（按日分布见下方验证记录）。
- [x] **Step 3: 不动其它字段。** ``short_term_composite`` / ``short_term_composite_rank`` / ``score_eligible`` 全部保持原值。

### Task 6: 文档与提交

- [ ] **Step 1: 同步使用指南 §10.1 字段表与 §13 字段速查。**
- [ ] **Step 2: 更新建议状态。** 在可视化建议文件中把"方向① V 形反弹 / 破位警惕卡片永远为空"标注为已修复，并链接本次实施计划。
- [ ] **Step 3: 提交。**

## 回填验证记录

| 日期 | V 形反弹 | 破位警惕 |
| --- | --- | --- |
| 2026-08-03 | 8 | 4 |
| 2026-08-04 | 11 | 18 |
| 2026-08-05 | 1 | 12 |
| 2026-08-06 | 1 | 7 |
| 2026-08-07 | 0 | 16 |
| 2026-08-10 | 22 | 9 |
| 2026-08-11 | 10 | 6 |
| 2026-08-12 | 1 | 3 |
| 2026-08-13 | 9 | 2 |

合计 63 + 77 = 140 行新标签（前一次重算统计）。

## 验收

- [x] SQL 迁移幂等可重复执行。
- [x] ``calculate_sector_short_term_features`` 返回字典含 ``rs_5``。
- [x] ``persist_short_term_snapshot`` tuple 长度与列数对齐。
- [x] ``tests/test_sector_rotation2_short_term_features.py`` + ``_labels.py`` 共 13 项断言通过。
- [x] 全量回归 122 项相关测试通过（仅 6 项因 tmp_path 沙箱权限失败，与本次无关）。
- [x] 8 月历史 ``rs_5`` + 标签全部回填成功，前端 V 形反弹 / 破位警惕卡片立即生效。
