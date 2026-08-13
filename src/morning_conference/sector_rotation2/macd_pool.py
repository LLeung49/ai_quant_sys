"""MACD sector pool filters and scanners."""
from __future__ import annotations

from dataclasses import dataclass, asdict
import math
import numpy as np
import pandas as pd

ENTITY_VOLUME_THRESHOLDS = {"stock": 1.5, "etf": 1.5, "sector_l1": 0.8, "sector_l2": 0.8}
ETF_PREFIXES = ("15", "16", "50", "51", "56", "58")
ETF_EXCLUDED_NAME_KEYWORDS = ("债", "国债", "信用债", "短融", "货币", "现金管理", "同业存单")


def is_excluded_bond_etf(code: str, name: str | None = None) -> bool:
    """Exclude bond/money-market ETFs from the MACD pool universe."""
    normalized_code = str(code).split(".")[0]
    if normalized_code.startswith("511"):
        return True
    return any(keyword in str(name or "") for keyword in ETF_EXCLUDED_NAME_KEYWORDS)


@dataclass
class MacdPoolHit:
    stock_code: str
    stock_name: str | None = None
    sector_1: str | None = None
    sector_2: str | None = None
    details: dict | None = None

    def to_dict(self) -> dict:
        result = asdict(self)
        result.update(result.pop("details") or {})
        return result


def _ema(values: np.ndarray, period: int) -> np.ndarray:
    return pd.Series(values).ewm(span=period, adjust=False, min_periods=period).mean().to_numpy()


def step1_filter_macd_momentum_trend(df: pd.DataFrame, fastperiod: int = 12, slowperiod: int = 26,
                                     signalperiod: int = 9, vol_ma_period: int = 20,
                                     vol_ratio_threshold: float = 1.5, gc_lookback: int = 2,
                                     require_zero_above: bool = True) -> tuple[bool, dict]:
    if df is None or len(df) < slowperiod + signalperiod:
        return False, {}
    close = pd.to_numeric(df["close"], errors="coerce").to_numpy(float)
    volume = pd.to_numeric(df["volume"], errors="coerce").to_numpy(float)
    dif = _ema(close, fastperiod) - _ema(close, slowperiod)
    dea = pd.Series(dif).ewm(span=signalperiod, adjust=False, min_periods=signalperiod).mean().to_numpy()
    hist = dif - dea
    vol_ma = pd.Series(volume).rolling(vol_ma_period, min_periods=vol_ma_period).mean().to_numpy()
    gc_offset = None
    for offset in range(gc_lookback):
        i = len(close) - 1 - offset
        if i < 1 or any(math.isnan(x) for x in (dif[i], dea[i], dif[i-1], dea[i-1])):
            continue
        if dif[i-1] <= dea[i-1] and dif[i] > dea[i]:
            gc_offset = offset
            break
    if gc_offset is None:
        return False, {}
    gi = len(close) - 1 - gc_offset
    if require_zero_above and not (dif[-1] > 0 and dea[-1] > 0 and dif[gi] > 0 and dea[gi] > 0):
        return False, {}
    vr_latest = volume[-1] / vol_ma[-1] if np.isfinite(vol_ma[-1]) and vol_ma[-1] > 0 else 0.0
    vr_gc = volume[gi] / vol_ma[gi] if np.isfinite(vol_ma[gi]) and vol_ma[gi] > 0 else 0.0
    if max(vr_latest, vr_gc) < vol_ratio_threshold:
        return False, {}
    prev = close[-2] if len(close) > 1 and close[-2] else close[-1]
    return True, {"close": float(close[-1]), "change_pct": round((close[-1]/prev-1)*100, 2),
                  "dif": float(dif[-1]), "dea": float(dea[-1]), "macd_hist": float(hist[-1]),
                  "vol_ratio": round(float(vr_latest), 2), "vol_ratio_gc": round(float(vr_gc), 2),
                  "gc_offset": gc_offset, "gc_label": f"T-{gc_offset}",
                  "gc_dif": float(dif[gi]), "gc_dea": float(dea[gi])}


def step2_filter_trap_avoidance(df: pd.DataFrame) -> dict:
    close = pd.to_numeric(df.get("close"), errors="coerce").to_numpy(float)
    if len(close) == 0:
        return {"adx_14": None, "rsi_14": None, "hurst_60": None, "kama_efficiency": None, "above_ma60": None}
    high = pd.to_numeric(df.get("high", df["close"]), errors="coerce").to_numpy(float)
    low = pd.to_numeric(df.get("low", df["close"]), errors="coerce").to_numpy(float)
    tr = np.maximum(high[1:] - low[1:], np.maximum(abs(high[1:] - close[:-1]), abs(low[1:] - close[:-1])))
    up = np.diff(high); down = -np.diff(low)
    plus = np.where((up > down) & (up > 0), up, 0.0); minus = np.where((down > up) & (down > 0), down, 0.0)
    adx = None
    if len(tr) >= 28:
        atr = pd.Series(tr).rolling(14, min_periods=14).mean(); pdi = 100 * pd.Series(plus).rolling(14, min_periods=14).mean() / atr; mdi = 100 * pd.Series(minus).rolling(14, min_periods=14).mean() / atr; dx = (100 * abs(pdi - mdi) / (pdi + mdi)).replace([np.inf, -np.inf], np.nan); adx_val = dx.rolling(14, min_periods=14).mean().iloc[-1]; adx = float(adx_val) if np.isfinite(adx_val) else None
    delta = np.diff(close)
    gains, losses = np.maximum(delta, 0), np.maximum(-delta, 0)
    avg_gain = pd.Series(gains).rolling(14, min_periods=14).mean().iloc[-1] if len(gains) >= 14 else np.nan
    avg_loss = pd.Series(losses).rolling(14, min_periods=14).mean().iloc[-1] if len(gains) >= 14 else np.nan
    rsi = 100 - 100 / (1 + avg_gain / avg_loss) if np.isfinite(avg_loss) and avg_loss > 0 else (100.0 if avg_gain > 0 else None)
    n = min(60, len(close)); sample = close[-n:]
    hurst = None
    if n >= 20 and np.std(sample) > 0:
        hurst = float(np.log(np.sum(np.abs(np.diff(sample))) / np.std(sample)) / np.log(n))
    efficiency = None
    if len(close) > 1:
        window = close[-min(11, len(close)):]
        path_length = np.sum(np.abs(np.diff(window)))
        efficiency = float(abs(window[-1] - window[0]) / path_length) if path_length > 0 else 0.0
    ma60 = pd.Series(close).rolling(60, min_periods=60).mean().iloc[-1]
    return {"adx_14": adx, "rsi_14": rsi, "hurst_60": hurst, "kama_efficiency": efficiency,
            "above_ma60": int(close[-1] > ma60) if np.isfinite(ma60) else None}


def evaluate_macd_entity(group: pd.DataFrame, *, entity_type: str, volume_threshold: float,
                         enable_step2: bool = True, gc_lookback: int = 10) -> dict:
    """Calculate daily metrics for one entity and mark whether it enters the pool."""
    group = group.sort_values("trade_date").tail(120)
    if len(group) < 2:
        return {"entity_type": entity_type, "is_triggered": 0}
    ok, details = step1_filter_macd_momentum_trend(group, vol_ratio_threshold=volume_threshold, gc_lookback=gc_lookback)
    if not details:
        close = pd.to_numeric(group["close"], errors="coerce").to_numpy(float)
        volume = pd.to_numeric(group["volume"], errors="coerce").to_numpy(float)
        dif = _ema(close, 12) - _ema(close, 26)
        dea = pd.Series(dif).ewm(span=9, adjust=False, min_periods=9).mean().to_numpy()
        hist = dif - dea
        vol_ma = pd.Series(volume).rolling(20, min_periods=20).mean().to_numpy()
        prev = close[-2] if len(close) > 1 and close[-2] else close[-1]
        details = {"close": float(close[-1]), "change_pct": round((close[-1] / prev - 1) * 100, 2),
                   "dif": float(dif[-1]) if np.isfinite(dif[-1]) else None,
                   "dea": float(dea[-1]) if np.isfinite(dea[-1]) else None,
                   "macd_hist": float(hist[-1]) if np.isfinite(hist[-1]) else None,
                   "vol_ratio": round(float(volume[-1] / vol_ma[-1]), 2) if np.isfinite(vol_ma[-1]) and vol_ma[-1] > 0 else None,
                   "vol_ratio_gc": None, "gc_offset": None, "gc_label": None, "gc_dif": None, "gc_dea": None}
    details["entity_type"] = entity_type
    details["is_triggered"] = int(ok)
    if enable_step2:
        details.update(step2_filter_trap_avoidance(group))
    return details

def run_macd_pool_scan(level: int, as_of_date: str, end_date: str | None = None, enable_step2: bool = True, volume_thresholds: dict[str, float] | None = None) -> pd.DataFrame:
    # Run the MACD pool scan.
    from data_ingestion.db_config import execute_query
    end_date = end_date or as_of_date
    thresholds = {**ENTITY_VOLUME_THRESHOLDS, **(volume_thresholds or {})}
    start_date = (pd.Timestamp(end_date) - pd.Timedelta(days=220)).strftime("%Y-%m-%d")
    rows = execute_query("SELECT d.stock_code, s.stock_name, s.sector_1, s.sector_2, d.trade_date, d.close_price AS close, d.volume FROM trade_stock_daily d LEFT JOIN trade_stock_status s ON s.stock_code=d.stock_code WHERE d.trade_date >= %s AND d.trade_date <= %s ORDER BY d.stock_code, d.trade_date", (start_date, end_date))
    if not rows:
        return pd.DataFrame()
    all_data = pd.DataFrame(rows)
    hits = []
    for code, group in all_data.groupby("stock_code"):
        group = group.sort_values("trade_date").tail(120)
        entity_type = "etf" if str(code).split(".")[0].startswith(ETF_PREFIXES) else "stock"
        if entity_type == "stock" and str(group.iloc[-1].get("stock_name") or "").upper().find("ST") >= 0:
            continue
        ok, details = step1_filter_macd_momentum_trend(group, vol_ratio_threshold=thresholds[entity_type])
        if not ok:
            continue
        details["stock_code"] = code
        details["entity_type"] = entity_type
        latest = group.iloc[-1]
        details.update({"stock_name": latest.get("stock_name"), "sector_1": latest.get("sector_1"), "sector_2": latest.get("sector_2")})
        if enable_step2:
            details.update(step2_filter_trap_avoidance(group))
        hits.append(details)
    return pd.DataFrame(hits)









def run_macd_sector_scan(level: int, as_of_date: str, enable_step2: bool = True, volume_thresholds: dict[str, float] | None = None, gc_lookback: int = 10) -> pd.DataFrame:
    """Scan申万一级/二级板块指数 using trade_sector_daily."""
    thresholds = {**ENTITY_VOLUME_THRESHOLDS, **(volume_thresholds or {})}
    from data_ingestion.db_config import execute_query
    start_date = (pd.Timestamp(as_of_date) - pd.Timedelta(days=220)).strftime("%Y-%m-%d")
    rows = execute_query("SELECT sector_name, sector_level, trade_date, close_idx AS close, total_volume AS volume, change_pct FROM trade_sector_daily WHERE sector_level=%s AND trade_date BETWEEN %s AND %s ORDER BY sector_name, trade_date", (level, start_date, as_of_date))
    hits=[]
    if not rows: return pd.DataFrame()
    for name, group in pd.DataFrame(rows).groupby("sector_name"):
        group=group.sort_values("trade_date").tail(120)
        ok, details=step1_filter_macd_momentum_trend(group, vol_ratio_threshold=thresholds[f"sector_l{level}"])
        if not ok: continue
        details.update({"entity_type": f"sector_l{level}", "stock_code": name, "stock_name": name, "sector_1": name if level == 1 else None, "sector_2": name if level == 2 else None})
        if enable_step2: details.update(step2_filter_trap_avoidance(group))
        hits.append(details)
    return pd.DataFrame(hits)











def run_macd_daily_pool(as_of_date: str, enable_step2: bool = True, volume_thresholds: dict[str, float] | None = None) -> pd.DataFrame:
    """日常 MACD 板块池：仅扫描 ETF、申万一级和申万二级，不扫描个股。"""
    metrics = run_macd_daily_metrics(as_of_date, enable_step2, volume_thresholds)
    return metrics[metrics["is_triggered"] == 1].drop(columns=["is_triggered"]).reset_index(drop=True) if not metrics.empty else metrics


def run_macd_daily_metrics(as_of_date: str, enable_step2: bool = True, volume_thresholds: dict[str, float] | None = None) -> pd.DataFrame:
    """Evaluate every daily ETF and Shenwan L1/L2 entity, including non-triggers."""
    from data_ingestion.db_config import execute_query

    thresholds = {**ENTITY_VOLUME_THRESHOLDS, **(volume_thresholds or {})}
    start_date = (pd.Timestamp(as_of_date) - pd.Timedelta(days=220)).strftime("%Y-%m-%d")
    frames: list[dict] = []
    stock_rows = execute_query(
        "SELECT d.stock_code, s.stock_name, s.sector_1, s.sector_2, d.trade_date, d.close_price AS close, d.volume "
        "FROM trade_stock_daily d LEFT JOIN trade_stock_status s ON s.stock_code=d.stock_code "
        "WHERE d.trade_date BETWEEN %s AND %s ORDER BY d.stock_code, d.trade_date",
        (start_date, as_of_date),
    )
    if stock_rows:
        for code, group in pd.DataFrame(stock_rows).groupby("stock_code"):
            if not str(code).split(".")[0].startswith(ETF_PREFIXES):
                continue
            latest_name = group.iloc[-1].get("stock_name")
            if is_excluded_bond_etf(code, latest_name):
                continue
            details = evaluate_macd_entity(group, entity_type="etf", volume_threshold=thresholds["etf"], enable_step2=enable_step2)
            latest = group.iloc[-1]
            details.update({"stock_code": code, "stock_name": latest.get("stock_name"), "sector_1": latest.get("sector_1"), "sector_2": latest.get("sector_2")})
            frames.append(details)
    for level in (1, 2):
        sector_rows = execute_query(
            "SELECT sector_name, sector_level, trade_date, close_idx AS close, total_volume AS volume "
            "FROM trade_sector_daily WHERE sector_level=%s AND trade_date BETWEEN %s AND %s ORDER BY sector_name, trade_date",
            (level, start_date, as_of_date),
        )
        if not sector_rows:
            continue
        for name, group in pd.DataFrame(sector_rows).groupby("sector_name"):
            details = evaluate_macd_entity(group, entity_type=f"sector_l{level}", volume_threshold=thresholds[f"sector_l{level}"], enable_step2=enable_step2)
            details.update({"stock_code": name, "stock_name": name, "sector_1": name if level == 1 else None, "sector_2": name if level == 2 else None})
            frames.append(details)
    return pd.DataFrame(frames)



