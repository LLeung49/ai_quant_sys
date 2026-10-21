# -*- coding: utf-8 -*-
"""
MACD全市场扫描选股策略 - 第一步: 动能+趋势股票池生成

策略说明:
  根据《MACD全市场扫描选股策略》需求文档的第一阶段【门槛筛选】:
  1. 近两天MACD发生金叉 (DIF上穿DEA, T-0或T-1交易日)
  2. DIF与DEA均在0轴以上 (零轴上金叉，确认强势多头趋势)
  3. 成交量放量，成交量在MA20均量的1.5倍以上 (量价配合，动能充足)

模块结构:
  - 继承 `9-形态选股雷达.py` 的全市场高效批量数据加载架构 (SQL单次查询 + pandas分组)
  - 模块化设计 `step1_filter_macd_momentum_trend` 供后续阶段组合调用
  - 自动输出选股结果并导出 CSV 候选池

运行方式: python src/pattern_detection/10-MACD全市场扫描选股.py
"""

import os
import sys
import time
import numpy as np
import pandas as pd
import talib

# 兼容包导入路径
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from data_ingestion.db_config import execute_query
from data_ingestion.utils import get_instrument_names

# ============================================================
# 策略参数配置 (门槛筛选)
# ============================================================
LOAD_BACK = 120                  # 数据加载回看K线数
FAST_PERIOD = 12                 # MACD快线周期
SLOW_PERIOD = 26                 # MACD慢线周期
SIGNAL_PERIOD = 9                # MACD信号线周期
VOL_MA_PERIOD = 20               # 成交量均线周期
VOL_RATIO_THRESHOLD = 1.5        # 成交量放量阈值 (1.5倍MA20)
GC_LOOKBACK_DAYS = 2             # MACD金叉允许的近几天范围 (2天内)
REQUIRE_ZERO_ABOVE = True        # 是否严格要求DIF和DEA都在0轴以上


# ============================================================
# 批量数据加载 (继承模板 SQL 优化逻辑)
# ============================================================

def batch_load_recent(days_back=120, end_date=None):
    """
    批量加载全市场近 N 个交易日的 K 线数据
    比逐只查询快数十倍
    """
    if end_date:
        ref_date = pd.Timestamp(end_date)
    else:
        rows = execute_query("SELECT MAX(trade_date) AS latest FROM trade_stock_daily_qfq")
        if not rows or not rows[0]['latest']:
            return {}
        ref_date = pd.Timestamp(rows[0]['latest'])

    calendar_days = int(days_back * 1.8)
    start_date = (ref_date - pd.Timedelta(days=calendar_days)).strftime('%Y-%m-%d')
    end_str = ref_date.strftime('%Y-%m-%d')

    print(f"  SQL查询范围: {start_date} ~ {end_str}", flush=True)

    sql = """
        SELECT stock_code, trade_date, open_price, high_price, low_price, close_price, volume
        FROM trade_stock_daily_qfq
        WHERE trade_date >= %s AND trade_date <= %s
        ORDER BY stock_code, trade_date ASC
    """
    rows = execute_query(sql, [start_date, end_str])
    if not rows:
        return {}

    print(f"  SQL数据加载完成, 共 {len(rows)} 行记录, 正在按股票分组...", flush=True)

    df_all = pd.DataFrame(rows)
    df_all['trade_date'] = pd.to_datetime(df_all['trade_date'])
    for col in ['open_price', 'high_price', 'low_price', 'close_price', 'volume']:
        df_all[col] = pd.to_numeric(df_all[col], errors='coerce')

    min_bars = SLOW_PERIOD + SIGNAL_PERIOD + VOL_MA_PERIOD  # 26 + 9 + 20 = 55
    result = {}
    for code, group in df_all.groupby('stock_code'):
        sub = group.set_index('trade_date').sort_index()
        sub = sub[['open_price', 'high_price', 'low_price', 'close_price', 'volume']]
        sub.columns = ['open', 'high', 'low', 'close', 'volume']
        if len(sub) >= min_bars and sub.index[-1] == ref_date:
            result[code] = sub.tail(days_back)

    return result


# ============================================================
# 第一步：识别动能+趋势股票池 (MACD零轴上金叉放量)
# ============================================================

def step1_filter_macd_momentum_trend(df, 
                                     fastperiod=FAST_PERIOD, 
                                     slowperiod=SLOW_PERIOD, 
                                     signalperiod=SIGNAL_PERIOD,
                                     vol_ma_period=VOL_MA_PERIOD,
                                     vol_ratio_threshold=VOL_RATIO_THRESHOLD,
                                     gc_lookback=GC_LOOKBACK_DAYS,
                                     require_zero_above=REQUIRE_ZERO_ABOVE):
    """
    第一步门槛筛选：
      1. 近 gc_lookback 天内出现 MACD 金叉 (DIF 上穿 DEA)
      2. 金叉日及最新日的 DIF/DEA 均位于 0 轴上方
      3. 成交量达到 MA20 的 vol_ratio_threshold 倍以上

    参数:
        df: 包含 open/high/low/close/volume 的 DataFrame
    返回:
        (bool, dict) -> (是否满足门槛, 详细指标信息)
    """
    c = df['close'].values.astype(np.float64)
    v = df['volume'].values.astype(np.float64)
    n = len(c)

    if n < (slowperiod + signalperiod):
        return False, {}

    # 计算 MACD (DIF, DEA, MACD柱)
    dif, dea, macd_hist = talib.MACD(c, fastperiod=fastperiod, slowperiod=slowperiod, signalperiod=signalperiod)

    # 计算成交量均线 MA20
    vol_ma = talib.SMA(v, timeperiod=vol_ma_period)

    # 1. 检查近 gc_lookback 天内是否出现金叉
    #    金叉定义: prev_dif <= prev_dea 且 curr_dif > curr_dea
    gc_found = False
    gc_offset = None  # 0 表示最新一日(T-0)，1 表示前一日(T-1)
    
    for offset in range(gc_lookback):
        idx = n - 1 - offset
        prev_idx = idx - 1
        if prev_idx < 0:
            continue

        if np.isnan(dif[idx]) or np.isnan(dea[idx]) or np.isnan(dif[prev_idx]) or np.isnan(dea[prev_idx]):
            continue

        # 判断金叉
        if dif[prev_idx] <= dea[prev_idx] and dif[idx] > dea[idx]:
            gc_found = True
            gc_offset = offset
            break

    if not gc_found:
        return False, {}

    # 2. 检查 DIF/DEA 是否均在 0 轴以上
    #    校验最新日(n-1)以及金叉发生日的 DIF 与 DEA
    gc_idx = n - 1 - gc_offset
    latest_zero_above = (dif[-1] > 0 and dea[-1] > 0) if require_zero_above else True
    gc_zero_above = (dif[gc_idx] > 0 and dea[gc_idx] > 0) if require_zero_above else True

    if not (latest_zero_above and gc_zero_above):
        return False, {}

    # 3. 检查成交量放量情况
    #    最新交易日或金叉日成交量 >= MA20 的 1.5 倍
    vol_ma_latest = vol_ma[-1]
    vol_latest = v[-1]
    vol_ratio_latest = float(vol_latest / vol_ma_latest) if (not np.isnan(vol_ma_latest) and vol_ma_latest > 0) else 0.0

    vol_ma_gc = vol_ma[gc_idx]
    vol_gc = v[gc_idx]
    vol_ratio_gc = float(vol_gc / vol_ma_gc) if (not np.isnan(vol_ma_gc) and vol_ma_gc > 0) else 0.0

    # 量比符合条件 (最新日放量或金叉当日放量)
    volume_pass = (vol_ratio_latest >= vol_ratio_threshold) or (vol_ratio_gc >= vol_ratio_threshold)

    if not volume_pass:
        return False, {}

    # 计算辅助收益指标
    close_latest = float(c[-1])
    close_prev = float(c[-2]) if n >= 2 else close_latest
    change_pct = round((close_latest / close_prev - 1.0) * 100, 2)

    gc_label = f"T-{gc_offset} ({'最新日' if gc_offset == 0 else '前一日'})"

    details = {
        'close': round(close_latest, 2),
        'change_pct': change_pct,
        'dif': round(float(dif[-1]), 4),
        'dea': round(float(dea[-1]), 4),
        'macd_hist': round(float(macd_hist[-1]), 4),
        'vol_ratio': round(vol_ratio_latest, 2),
        'vol_ratio_gc': round(vol_ratio_gc, 2),
        'gc_offset': gc_offset,
        'gc_label': gc_label,
        'gc_dif': round(float(dif[gc_idx]), 4),
        'gc_dea': round(float(dea[gc_idx]), 4),
    }

    return True, details


# ============================================================
# 过滤标的类型与交易状态 (ST/非股票)
# ============================================================

def _is_tradable(code, name, change_pct, vol_ratio):
    """过滤 ST 股票、停牌、异常流动性标的"""
    if 'ST' in name or 'st' in name:
        return False
    if abs(change_pct) >= 9.9:  # 排除涨跌停导致无法交易/延续风险
        return False
    if vol_ratio < 0.3:
        return False
    return True


def _is_stock(code):
    """判断是否为个股 (排除 ETF/LOF/REITs)"""
    if code.startswith(('51', '56', '58', '15', '16')):
        return False
    return True


# ============================================================
# 全市场选股雷达主执行流程
# ============================================================

def run_macd_pool_scanner(end_date=None):
    """
    运行全市场 MACD 动能+趋势选股扫描 (第一步)
    """
    print("=" * 75)
    print("全市场 MACD 扫描选股策略 - 第一步：动能+趋势股票池生成")
    print(f"  筛选条件: 近{GC_LOOKBACK_DAYS}日MACD金叉 | DIF/DEA > 0 (零轴上) | 成交量 >= MA20 * {VOL_RATIO_THRESHOLD}倍")
    print("=" * 75)

    # ---- 1. 批量数据加载 ----
    print("\n[1/3] 正在加载全市场K线数据...")
    t0 = time.time()
    all_data = batch_load_recent(days_back=LOAD_BACK, end_date=end_date)
    load_time = time.time() - t0
    print(f"  数据加载完成: 获得 {len(all_data)} 只标的, 耗时 {load_time:.2f}s")

    if not all_data:
        print("  没有可用数据, 请检查数据库或运行 8-原始行情与复权数据采集.py")
        return None

    sample_code = next(iter(all_data))
    scan_date = all_data[sample_code].index[-1].strftime('%Y-%m-%d')
    print(f"  扫描基准日期: {scan_date}")

    # ---- 2. 运行第一步门槛筛选 ----
    print(f"\n[2/3] 正在对 {len(all_data)} 只标的运行零轴上MACD金叉+放量门槛筛选...")
    t0 = time.time()

    passed_list = []
    for code, df in all_data.items():
        is_pass, details = step1_filter_macd_momentum_trend(df)
        if is_pass:
            details['code'] = code
            passed_list.append(details)

    scan_time = time.time() - t0
    print(f"  筛选完成: 耗时 {scan_time:.2f}s, 初步符合门槛标的数: {len(passed_list)}")

    # ---- 查询股票/ETF中文名称 ----
    hit_codes = [r['code'] for r in passed_list]
    names = get_instrument_names(hit_codes) if hit_codes else {}

    # ---- 3. 输出展示与统计 ----
    print(f"\n[3/3] MACD 动能+趋势股票池明细 ({scan_date})")
    print("=" * 85)

    # 排序：按最新量比降序
    passed_list.sort(key=lambda x: x['vol_ratio'], reverse=True)

    print(f"{'代码':<12} {'名称':<10} {'收盘价':>8} {'涨跌幅%':>8} {'DIF':>8} {'DEA':>8} {'最新量比':>8} {'金叉时点':<14}")
    print("-" * 85)

    stocks_count = 0
    etf_count = 0

    for r in passed_list:
        code = r['code']
        name = names.get(code, code)
        is_stk = _is_stock(code)
        if is_stk:
            stocks_count += 1
        else:
            etf_count += 1

        print(f"{code:<12} {name:<10} {r['close']:>8.2f} {r['change_pct']:>+8.2f}% "
              f"{r['dif']:>8.4f} {r['dea']:>8.4f} {r['vol_ratio']:>8.2f}x {r['gc_label']:<14}")

    print(f"\n{'='*85}")
    print(f"筛选汇总摘要 ({scan_date})")
    print(f"{'='*85}")
    print(f"  全市场标的总数:   {len(all_data)} 只")
    print(f"  符合第一步门槛:   {len(passed_list)} 只 (占全市场 {len(passed_list)/len(all_data)*100:.2f}%)")
    print(f"    - A股个股:     {stocks_count} 只")
    print(f"    - ETF/基金:    {etf_count} 只")
    print(f"  扫描耗时:         {load_time + scan_time:.2f}s")

    # ---- 4. 导出 CSV 候选池 ----
    export_macd_pool_csv(scan_date, passed_list, names)

    return {
        'scan_date': scan_date,
        'total_scanned': len(all_data),
        'pool': passed_list,
        'names': names,
    }


def export_macd_pool_csv(scan_date, passed_list, names):
    """
    将筛选出来的 MACD 动能+趋势股票池导出为 CSV 文件
    """
    if not passed_list:
        print("\n  无符合门槛的标的，跳过 CSV 导出")
        return

    os.makedirs('outputs', exist_ok=True)

    rows = []
    for r in passed_list:
        code = r['code']
        name = names.get(code, code)
        is_stk = _is_stock(code)
        tradable = _is_tradable(code, name, r['change_pct'], r['vol_ratio'])

        rows.append({
            '代码': code,
            '名称': name,
            '标的类型': '个股' if is_stk else 'ETF/基金',
            '交易过滤': '正常' if tradable else 'ST/涨跌停/流动性不足',
            '收盘价': r['close'],
            '涨跌幅%': r['change_pct'],
            'DIF': r['dif'],
            'DEA': r['dea'],
            'MACD柱': r['macd_hist'],
            '最新量比(MA20)': r['vol_ratio'],
            '金叉日量比': r['vol_ratio_gc'],
            '金叉时点': r['gc_label'],
            '金叉日DIF': r['gc_dif'],
            '金叉日DEA': r['gc_dea'],
        })

    df_out = pd.DataFrame(rows)
    df_out = df_out.sort_values(by=['标的类型', '最新量比(MA20)'], ascending=[True, False])

    csv_path = os.path.join('outputs', f'MACD动能趋势股票池_{scan_date}.csv')
    df_out.to_csv(csv_path, index=False, encoding='utf-8-sig')
    print(f"\n  候选池数据已保存至: {csv_path}")


# ============================================================
# 入口
# ============================================================

if __name__ == '__main__':
    run_macd_pool_scanner()
