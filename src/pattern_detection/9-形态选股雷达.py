# -*- coding: utf-8 -*-
"""
形态选股雷达 - 截面扫描 (MACD底背离 + K线反转形态)

场景: 每天收盘后对全市场股票和场内基金运行一次形态扫描
  1. MACD底背离: 价格创新低但MACD未创新低, 空方力量衰竭
  2. K线底部形态: 吞没/锤子线/早晨之星等看涨反转形态
  双重共振: 同时满足底背离 + 看涨K线形态的个股 -> 次日重点关注池

TA-Lib用法:
  talib.MACD(close) -> 计算MACD指标
  talib.CDLENGULFING(o, h, l, c) -> 吞没形态(>0看涨, <0看跌)
  talib.CDLHAMMER(o, h, l, c) -> 锤子线
  ... 共61种K线形态函数, 全部以CDL_开头

运行: python 9-形态选股雷达.py
"""
import numpy as np
import pandas as pd
import talib
import time
from data_ingestion.db_config import execute_query
from pattern_detection.instrument_names import get_scan_names
import os

LOAD_BACK=120
LOOKBACK=60
RECENT_WINDOW=10
MIN_MACD_DIFF=0.05
REQUIRE_MACD_BELOW_ZERO=True
REQUIRE_PREV_DOWNTREND=False
MIN_PREV_DECLINE_PCT=0.05
MIN_PATTERN_SIGNAL=100
# ============================================================
# 批量数据加载(一次SQL加载全市场, 避免逐只查询)
# ============================================================

def batch_load_recent(days_back=120, end_date=None):
    """
    批量加载全市场近N个交易日的K线数据

    一次SQL查询加载所有股票, 再按stock_code分组
    比逐只 load_stock_data() 快几十倍

    参数:
        days_back: 每只股票保留的最大交易日数
        end_date: 截止日期, None则取数据库最新日期

    返回:
        dict {stock_code: DataFrame}, DataFrame列为 open/high/low/close/volume
    """
    if end_date:
        ref_date = pd.Timestamp(end_date)
    else:
        rows = execute_query("SELECT MAX(trade_date) AS latest FROM trade_stock_daily_qfq")
        if not rows or not rows[0]['latest']:
            return {}
        ref_date = pd.Timestamp(rows[0]['latest'])

    # 多预留自然日(周末+节假日), 确保取到足够交易日
    calendar_days = int(days_back * 1.8)
    start_date = (ref_date - pd.Timedelta(days=calendar_days)).strftime('%Y-%m-%d')
    end_str = ref_date.strftime('%Y-%m-%d')

    print(f"  SQL查询范围: {start_date} ~ {end_str}")

    sql = """
        SELECT stock_code, trade_date, open_price, high_price, low_price, close_price, volume
        FROM trade_stock_daily_qfq
        WHERE trade_date >= %s AND trade_date <= %s
        ORDER BY stock_code, trade_date ASC
    """
    rows = execute_query(sql, [start_date, end_str])
    if not rows:
        return {}

    df_all = pd.DataFrame(rows)
    df_all['trade_date'] = pd.to_datetime(df_all['trade_date'])
    for col in ['open_price', 'high_price', 'low_price', 'close_price', 'volume']:
        df_all[col] = pd.to_numeric(df_all[col], errors='coerce')

    # 按股票分组, 每只保留最近 days_back 条
    # MACD(26+9=35) + 背离回看(60) -> 至少需要60条数据
    min_bars = 60
    result = {}
    for code, group in df_all.groupby('stock_code'):
        sub = group.set_index('trade_date').sort_index()
        sub = sub[['open_price', 'high_price', 'low_price', 'close_price', 'volume']]
        sub.columns = ['open', 'high', 'low', 'close', 'volume']
        if len(sub) >= min_bars and sub.index[-1] == ref_date:
            result[code] = sub.tail(days_back)
    
    print(f"总标的数：{len(result.keys()):<14}")
    print(f"数据样例：【{next(iter(result), None)}】")
    print(f"{result[next(iter(result), None)]}")
    return result


# ============================================================
# MACD底背离检测
# ============================================================

def detect_bottom_divergence(close, 
        macd_line, 
        lookback=60, 
        recent_window=10, 
        min_macd_diff=0.05, 
        require_macd_below_zero=True,
        require_prev_downtrend=True,
        min_prev_decline_pct=0.05):
    """
    检测MACD底背离

    底背离定义:
      价格创新低(或持平), 但MACD线未创新低 -> 空方动能衰竭

    算法:
      1. 将回看区间分为"前段"和"近段"
      2. 分别找各段的最低价位置
      3. 若近段价格 <= 前段价格, 且近段MACD > 前段MACD -> 底背离

    参数:
        close: 收盘价数组
        macd_line: MACD线数组
        lookback: 总回看K线数 (默认60, 约3个月)
        recent_window: 近段窗口 (默认10, 低点需在最近10根K线内)
        min_macd_diff: DIF相对改善幅度阈值, 默认0.05表示抬高幅度须超过前期DIF绝对值的5%
        require_macd_below_zero: 是否要求近段MACD在零轴下方

    返回:
        (bool, dict) -> (是否存在底背离, 详细信息)
    """
    n = len(close)
    if n < lookback:
        return False, {}

    # 近段: 最后 recent_window 根K线
    # 前段: lookback ~ recent_window 之前的K线
    recent_slice = close[n - recent_window: n]                 # 近段收盘价 
    prev_slice = close[n - lookback: n - recent_window]        # 前段收盘价 

    if len(prev_slice) == 0 or len(recent_slice) == 0:
        return False, {}

    # 各段价格最低点的局部索引
    recent_low_local = int(np.argmin(recent_slice))
    prev_low_local = int(np.argmin(prev_slice))

    # 映射为全局索引
    idx_recent = n - recent_window + recent_low_local     # 近段最低价在全局的index
    idx_prev = n - lookback + prev_low_local              # 前段最低价在全局的index

    prev_dif = float(macd_line[idx_prev])
    recent_dif = float(macd_line[idx_recent])

    # 无效指标或分母接近零时，不判定背离
    if not (np.isfinite(prev_dif) and np.isfinite(recent_dif)):
        return False, {}
    if abs(prev_dif) <= 1e-8:
        return False, {}

    # ---- 判定1: 价格创新低或平底 ----
    price_lower = close[idx_recent] <= close[idx_prev]         # 近n天的低点<=前段低点
    # ---- 判定2: DIF抬高, 且相对前期DIF绝对值的改善幅度超过阈值 ----
    macd_improvement = (recent_dif - prev_dif) / abs(prev_dif)
    macd_higher = (
        recent_dif > prev_dif
        and macd_improvement > min_macd_diff
    )

    # ---- 判定3(可选): 近段MACD必须位于零轴下方 ----
    macd_below_zero = (macd_line[idx_recent] < 0) if require_macd_below_zero else True

    # ---- 判定4(可选):优化点：原代码对"震荡市"友好——前段没下跌趋势也判背离。要求前段最高→最低至少有明显跌幅。
    # 前段最高点 vs 最低点的跌幅必须 >= min_decline_pct
    prev_high = float(np.max(prev_slice))
    prev_low = float(np.min(prev_slice))
    if prev_high <= 0:
        return False, {}
    decline_pct = (prev_high - prev_low) / prev_high
    prev_in_downtrend = decline_pct >= min_prev_decline_pct if require_prev_downtrend else True  # 前段至少下跌5%

    if price_lower and macd_higher and macd_below_zero and prev_in_downtrend:
        return True, {
            'prev_price': round(float(close[idx_prev]), 2),
            'recent_price': round(float(close[idx_recent]), 2),
            'prev_macd': round(float(macd_line[idx_prev]), 4),
            'recent_macd': round(float(macd_line[idx_recent]), 4),
            'days_apart': idx_recent - idx_prev,
        }

    return False, {}


# ============================================================
# K线看涨形态扫描
# ============================================================

# 重点扫描的10种看涨反转形态
BULLISH_PATTERNS = {
    'CDLENGULFING':      '看涨吞没',
    'CDLHAMMER':         '锤子线',
    'CDLMORNINGSTAR':    '早晨之星',
    'CDLPIERCING':       '曙光初现',
    'CDL3WHITESOLDIERS': '三白兵',
    'CDLINVERTEDHAMMER': '倒锤子线',
    'CDL3INSIDE':        '三内部上涨',
    'CDL3OUTSIDE':       '三外部上涨',
    'CDLHARAMI':         '看涨孕线',
    'CDLDRAGONFLYDOJI':  '蜻蜓十字',
}


def scan_bullish_patterns(o, h, l, c, min_signal=100):
    """
    扫描最后一根K线是否出现看涨反转形态

    TA-Lib的CDL函数返回值: >0 看涨, <0 看跌, 0 无信号
    绝对值100=标准信号, 200=强信号

    返回:
        list of (中文名, 英文函数名, 信号强度)
    """
    found = []
    for func_name, cn_name in BULLISH_PATTERNS.items():
        func = getattr(talib, func_name)
        result = func(o, h, l, c)
        last_val = result[-1]
        if last_val >= min_signal:
            found.append((cn_name, func_name, int(last_val)))
    return found


# ============================================================
# 单只股票完整扫描
# ============================================================

def scan_one(df, lookback=60):
    """
    对单只股票运行MACD底背离 + K线形态扫描

    返回:
        dict: has_divergence, bullish_patterns, combined, 及辅助信息
    """
    o = df['open'].values.astype(np.float64)
    h = df['high'].values.astype(np.float64)
    l = df['low'].values.astype(np.float64)
    c = df['close'].values.astype(np.float64)
    v = df['volume'].values.astype(np.float64)

    macd, signal, hist = talib.MACD(c, fastperiod=12, slowperiod=26, signalperiod=9)
    has_div, div_info = detect_bottom_divergence(c, 
            macd,
            lookback, 
            recent_window=RECENT_WINDOW, 
            min_macd_diff=MIN_MACD_DIFF,
          require_macd_below_zero=REQUIRE_MACD_BELOW_ZERO,
          require_prev_downtrend=REQUIRE_PREV_DOWNTREND,
          min_prev_decline_pct=MIN_PREV_DECLINE_PCT,)
    patterns = scan_bullish_patterns(o, h, l, c, min_signal=MIN_PATTERN_SIGNAL)

    # 量比 = 当日成交量 / 20日均量
    vol_ma = talib.SMA(v, timeperiod=20)
    if not np.isnan(vol_ma[-1]) and vol_ma[-1] > 0:
        vol_ratio = float(v[-1] / vol_ma[-1])
    else:
        vol_ratio = 0.0

    # ---- 形态强度分级 ----
    strong_patterns = [p for p in patterns if p[2] >= 200]

    return {
        'has_divergence': has_div,
        'divergence_info': div_info,
        'bullish_patterns': patterns,
        'close': round(float(c[-1]), 2),
        'change_pct': round(float((c[-1] / c[-2] - 1) * 100), 2) if len(c) >= 2 else 0,
        'macd': round(float(macd[-1]), 4) if not np.isnan(macd[-1]) else 0,
        'vol_ratio': round(vol_ratio, 2),
        # 双重共振: 背离 + 至少1种形态 + (量比放大 或 形态信号强)
        'combined': has_div and len(patterns) > 0 and (vol_ratio >= 1.0 or len(strong_patterns) >= 1),
    }


# ============================================================
# 全市场扫描主函数
# ============================================================

def run_radar(end_date=None, lookback=LOOKBACK):
    """
    形态选股雷达 - 全市场截面扫描

    流程:
      1. 一次性加载全市场K线数据(批量SQL)
      2. 逐只运行 talib MACD + CDL形态检测
      3. 按信号强度排序输出: 双重共振 > 单一信号

    参数:
        end_date: 扫描日期, None=数据库最新日期
        lookback: MACD底背离回看周期(默认60个交易日)
        recent_window: 近期窗口(低点需在此范围内, 默认10)
    """
    print("=" * 70)
    print("形态选股雷达 - 截面扫描")
    print("  MACD底背离 + K线看涨反转形态 -> 次日关注池")
    print("=" * 70)

    # ---- 第1步: 批量加载数据 ----
    print("\n[1/3] 批量加载K线数据...")
    t0 = time.time()
    all_data = batch_load_recent(days_back=max(lookback + 60, LOAD_BACK), end_date=end_date)
    load_time = time.time() - t0
    print(f"  加载完成: {len(all_data)} 只标的, 耗时 {load_time:.1f}s")

    if not all_data:
        print("  没有可用数据, 请先运行 8-原始行情与复权数据采集.py")
        return

    sample_code = next(iter(all_data))
    scan_date = all_data[sample_code].index[-1].strftime('%Y-%m-%d')
    print(f"  扫描日期: {scan_date}")

    # ---- 第2步: 逐只扫描 ----
    print(f"\n[2/3] 运行TA-Lib形态扫描 (MACD底背离 + {len(BULLISH_PATTERNS)}种看涨K线形态)...")
    t0 = time.time()

    divergence_list = []
    pattern_list = []
    combined_list = []
    errors = 0

    for code, df in all_data.items():
        # try:
        result = scan_one(df, lookback)
        result['code'] = code

        if result['has_divergence']:
            divergence_list.append(result)
        if result['bullish_patterns']:
            pattern_list.append(result)
        if result['combined']:
            combined_list.append(result)
        # except Exception:
        #     errors += 1

    scan_time = time.time() - t0
    print(f"  扫描完成: 耗时 {scan_time:.1f}s" +
          (f", 跳过异常 {errors} 只" if errors else ""))

    # ---- 查询股票与场内基金名称 ----
    hit_codes = list(set(
        [r['code'] for r in divergence_list] +
        [r['code'] for r in pattern_list]
    ))
    names = get_scan_names(hit_codes)

    # ---- 第3步: 输出结果 ----
    print(f"\n[3/3] 扫描结果 ({scan_date})")
    print("=" * 70)

    combined_list.sort(key=lambda x: (len(x['bullish_patterns']), x['vol_ratio']), reverse=True)
    div_only = sorted((r for r in divergence_list if not r['combined']),
                      key=lambda x: x['vol_ratio'], reverse=True)
    pat_only = sorted((r for r in pattern_list if not r['combined']),
                      key=lambda x: x['vol_ratio'], reverse=True)
    for label, is_stock in (("股票", True), ("ETF/基金", False)):
        for title, records in (("双重共振", combined_list),
                               ("仅MACD底背离", div_only),
                               ("仅看涨K线形态", pat_only)):
            subset = [r for r in records if _is_stock(r['code']) == is_stock]
            limit = None if title == "双重共振" else 30
            print(f"\n--- {label} - {title} ({len(subset)} 只" +
                  (", 显示前30) ---" if limit else ") ---"))
            if not subset:
                print("  (无)")
                continue
            if title == "双重共振":
                print(f"{'代码':<14} {'名称':<10} {'收盘':>8} {'涨跌%':>7} {'量比':>6} {'形态':<20} {'背离信息'}")
            elif title == "仅MACD底背离":
                print(f"{'代码':<14} {'名称':<10} {'收盘':>8} {'涨跌%':>7} {'量比':>6} {'MACD':>10} {'间距'}")
            else:
                print(f"{'代码':<14} {'名称':<10} {'收盘':>8} {'涨跌%':>7} {'量比':>6} {'形态'}")
            print("-" * 70)
            for r in subset[:limit]:
                name = names.get(r['code'], r['code'])
                prefix = (f"{r['code']:<14} {name:<10} {r['close']:>8.2f} "
                          f"{r['change_pct']:>+6.2f}% {r['vol_ratio']:>5.1f}x ")
                if title == "双重共振":
                    max_sig = max(p[2] for p in r['bullish_patterns'])
                    sig_tag = '强' if max_sig >= 200 else '标准'
                    pat_str = ','.join(p[0] for p in r['bullish_patterns'])
                    div = r['divergence_info']
                    div_str = (f"价{div['prev_price']}->{div['recent_price']} "
                               f"MACD{div['prev_macd']}->{div['recent_macd']}")
                    print(f"{prefix}{sig_tag:<8} {pat_str:<20} {div_str}")
                elif title == "仅MACD底背离":
                    print(f"{prefix}{r['macd']:>10.4f} {r['divergence_info']['days_apart']:>4}日")
                else:
                    print(f"{prefix}{','.join(p[0] for p in r['bullish_patterns'])}")
            if limit and len(subset) > limit:
                print(f"  ... 还有 {len(subset) - limit} 只")

    # ---- 汇总 ----
    print(f"\n{'='*70}")
    print(f"扫描汇总 ({scan_date})")
    print(f"{'='*70}")
    print(f"  扫描标的:       {len(all_data)} 只")
    print(f"  MACD底背离:     {len(divergence_list)} 只 "
          f"({len(divergence_list)/len(all_data)*100:.1f}%)")
    print(f"  看涨K线形态:    {len(pattern_list)} 只 "
          f"({len(pattern_list)/len(all_data)*100:.1f}%)")
    print(f"  双重共振(重点): {len(combined_list)} 只 "
          f"({len(combined_list)/len(all_data)*100:.1f}%)")
    print(f"  总耗时:         {load_time + scan_time:.1f}s")

    # ---- 形态命中统计 ----
    if pattern_list:
        pat_counter = {}
        for r in pattern_list:
            for cn, en, _ in r['bullish_patterns']:
                pat_counter[cn] = pat_counter.get(cn, 0) + 1
        print(f"\n  形态命中分布:")
        for cn, cnt in sorted(pat_counter.items(), key=lambda x: -x[1]):
            print(f"    {cn:<12} {cnt:>4} 只")

    return {
        'scan_date': scan_date,
        'total': len(all_data),
        'divergence': divergence_list,
        'patterns': pattern_list,
        'combined': combined_list,
        'names': names,
    }


# ============================================================
# 候选池导出
# ============================================================

def _is_tradable(r, name):
    """
    判断标的是否适合次日交易

    过滤掉:
      - ST/*ST股票(风险警示, 涨跌幅5%)
      - 当日涨停/跌停(次日可能延续极端走势)
      - 量比过低(流动性不足)
    """
    if 'ST' in name or 'st' in name:
        return False
    if abs(r['change_pct']) >= 9.9:
        return False
    if r['vol_ratio'] < 0.3:
        return False
    return True


def _is_stock(code):
    """判断是否为个股(排除ETF/LOF/REIT等基金)"""
    if code.startswith(('51', '56', '58', '15', '16', '18')):
        return False
    return True


def export_candidate_pool(scan_result):
    """
    将扫描结果导出为次日候选池CSV

    过滤规则:
      - 排除ST、涨跌停、量比<0.3
      - 个股和ETF分开统计
      - 按量比降序排列(放量优先)

    输出:
      outputs/候选池_股票_YYYY-MM-DD.csv
      outputs/候选池_ETF基金_YYYY-MM-DD.csv
    """
    if not scan_result:
        return

    scan_date = scan_result['scan_date']
    names = scan_result.get('names', {})
    combined = scan_result['combined']
    divergence = scan_result['divergence']
    patterns = scan_result['patterns']

    os.makedirs('outputs', exist_ok=True)

    # 构建候选池记录
    rows = []

    # 双重共振 -> 信号等级A
    for r in combined:
        name = names.get(r['code'], r['code'])
        if not _is_tradable(r, name):
            continue
        div = r['divergence_info']
        rows.append({
            '信号等级': 'A-双重共振',
            '代码': r['code'],
            '名称': name,
            '类型': '个股' if _is_stock(r['code']) else 'ETF/基金',
            '收盘价': r['close'],
            '涨跌幅%': r['change_pct'],
            '量比': r['vol_ratio'],
            'K线形态': ','.join(p[0] for p in r['bullish_patterns']),
            'MACD': r['macd'],
            '背离前价': div['prev_price'],
            '背离近价': div['recent_price'],
            '背离前MACD': div['prev_macd'],
            '背离近MACD': div['recent_macd'],
            '背离间距日': div['days_apart'],
        })

    # 仅底背离 + 量比>=1.0 -> 信号等级B
    for r in divergence:
        if r['combined']:
            continue
        name = names.get(r['code'], r['code'])
        if not _is_tradable(r, name):
            continue
        if r['vol_ratio'] < 1.0:
            continue
        div = r['divergence_info']
        rows.append({
            '信号等级': 'B-底背离放量',
            '代码': r['code'],
            '名称': name,
            '类型': '个股' if _is_stock(r['code']) else 'ETF/基金',
            '收盘价': r['close'],
            '涨跌幅%': r['change_pct'],
            '量比': r['vol_ratio'],
            'K线形态': '',
            'MACD': r['macd'],
            '背离前价': div['prev_price'],
            '背离近价': div['recent_price'],
            '背离前MACD': div['prev_macd'],
            '背离近MACD': div['recent_macd'],
            '背离间距日': div['days_apart'],
        })

    # 仅K线形态 + 量比>=1.5 -> 信号等级C
    for r in patterns:
        if r['combined']:
            continue
        name = names.get(r['code'], r['code'])
        if not _is_tradable(r, name):
            continue
        if r['vol_ratio'] < 1.5:
            continue
        rows.append({
            '信号等级': 'C-形态放量',
            '代码': r['code'],
            '名称': name,
            '类型': '个股' if _is_stock(r['code']) else 'ETF/基金',
            '收盘价': r['close'],
            '涨跌幅%': r['change_pct'],
            '量比': r['vol_ratio'],
            'K线形态': ','.join(p[0] for p in r['bullish_patterns']),
            'MACD': r['macd'],
            '背离前价': '',
            '背离近价': '',
            '背离前MACD': '',
            '背离近MACD': '',
            '背离间距日': '',
        })

    if not rows:
        print("\n  过滤后无候选标的")
        return

    df = pd.DataFrame(rows).sort_values(['信号等级', '量比'], ascending=[True, False])

    print(f"\n{'='*70}")
    print(f"次日候选池 ({scan_date} 收盘扫描)")
    print(f"{'='*70}")
    print(f"  总计: {len(df)} 只")
    for label, kind in (("股票", "个股"), ("ETF基金", "ETF/基金")):
        group = df[df['类型'] == kind]
        if group.empty:
            continue
        csv_path = os.path.join('outputs', f'候选池_{label}_{scan_date}.csv')
        group.to_csv(csv_path, index=False, encoding='utf-8-sig')
        print(f"\n  {kind}: {len(group)} 只, 已保存: {csv_path}")
        for level in ['A-双重共振', 'B-底背离放量', 'C-形态放量']:
            sub = group[group['信号等级'] == level]
            if sub.empty:
                continue
            print(f"  [{level}] {len(sub)} 只:")
            for _, row in sub.iterrows():
                tag = f"  {row['K线形态']}" if row['K线形态'] else ''
                print(f"    {row['代码']:<14} {row['名称']:<10} "
                      f"收盘{row['收盘价']:>8.2f}  {row['涨跌幅%']:>+6.2f}%  "
                      f"量比{row['量比']:>4.1f}x{tag}")

    return df


# ============================================================
# 入口
# ============================================================

if __name__ == '__main__':
    result = run_radar()
    if result:
        export_candidate_pool(result)
