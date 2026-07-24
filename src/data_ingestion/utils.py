# -*- coding: utf-8 -*-
"""
utils.py — 通用工具集合

针对过去几轮采集中反复踩的坑做成纯函数工具:

  1. 类型安全转换: 处理 pandas NaN / None / 不可转换值的 fallback
  2. 时间格式化 / 解析
  3. 集合分批 / 按键去重
  4. 字符串归一化 (用于标题模糊去重)
  5. 多线程下线程安全的 print
  6. lxml DTD 网络加载修复 (解决 pd.read_html / AkShare 的 OSError)
  7. 网络重试装饰器 (指数退避)
  8. 缺失值 / 错误类型的友好报错
  9. 标的代码-名称映射 (akshare 拉取股票 + 场内基金, 本地 JSON 缓存, 7 天自动刷新)

零业务耦合, 仅依赖 stdlib + pandas + (可选) akshare.
"""

from __future__ import annotations

import functools
import itertools
import json
import re
import threading
import time
from datetime import date, datetime
from pathlib import Path
from typing import Any, Callable, Iterable, Iterator, TypeVar

import pandas as pd

__all__ = [
    # 类型安全
    "safe_int", "safe_float", "safe_str", "safe_bool", "safe_divide",
    # 时间
    "today_str", "now_str", "safe_date", "safe_datetime",
    # 集合 / 序列
    "chunked", "dedupe_by",
    # 字符串
    "truncate", "normalize_title",
    # 线程
    "PrintLock",
    # lxml
    "disable_lxml_external_dtd",
    # 重试
    "retry",
    # 校验
    "require_value",
    # 名称映射
    "get_instrument_names",
]


# ============================================================
# 1. 类型安全转换 (核心: 处理 pandas NaN / None / 不可转换值)
# ============================================================
# 为什么需要:
#   - NaN / np.nan / math.nan 都是 truthy, "or 默认值" 兜底全部失效
#   - NaN -> int() 直接 ValueError
#   - 下面 5 个函数是对这种情况的统一封装

def safe_int(val: Any, default: int = 0) -> int:
    """int() 容错版: NaN / None / 'abc' 等无法转换的值都返回 default.

    Examples:
        safe_int(float('nan'))    -> 0
        safe_int(None)            -> 0
        safe_int('123')           -> 123
        safe_int('abc')           -> 0
        safe_int(None, default=-1) -> -1
        safe_int(3.7)             -> 3   (int() 截断小数)
    """
    if pd.isna(val):
        return default
    try:
        return int(val)
    except (TypeError, ValueError):
        return default


def safe_float(val: Any, default: float = 0.0) -> float:
    """float() 容错版: NaN / None / 'abc' 都返回 default.

    Examples:
        safe_float(float('nan')) -> 0.0
        safe_float('3.14')       -> 3.14
        safe_float('abc')        -> 0.0
    """
    if pd.isna(val):
        return default
    try:
        return float(val)
    except (TypeError, ValueError):
        return default


def safe_str(val: Any, default: str = "", strip: bool = True) -> str:
    """str() 容错版: NaN / None 返回 default; 默认 strip 前后空白.

    Examples:
        safe_str(float('nan'))            -> ''
        safe_str('  茅台  ')              -> '茅台'
        safe_str(pd.NA, default='N/A')    -> 'N/A'
    """
    if pd.isna(val):
        return default
    s = str(val)
    return s.strip() if strip else s


def safe_bool(val: Any, default: bool = False) -> bool:
    """宽松布尔: NaN/None -> default; '0'/'false'/''/0 -> False; 其他 -> True."""
    if pd.isna(val):
        return default
    if isinstance(val, bool):
        return val
    if isinstance(val, (int, float)):
        return bool(val)
    if isinstance(val, str):
        v = val.strip().lower()
        if v in ("", "0", "false", "no", "none"):
            return False
        return True
    return bool(val)


def safe_divide(numerator: Any, denominator: Any, default: float = 0.0) -> float:
    """除法 + 除零保护: 除数 0 或任意一侧无法转 float 时返回 default.

    Examples:
        safe_divide(10, 2)                       -> 5.0
        safe_divide(1, 0)                        -> 0.0
        safe_divide(1, 0, default=float('nan'))  -> nan
    """
    try:
        n, d = float(numerator), float(denominator)
        if d == 0:
            return default
        return n / d
    except (TypeError, ValueError):
        return default


# ============================================================
# 2. 时间
# ============================================================

def today_str() -> str:
    """返回今天日期的 ISO 字符串, 如 '2026-07-23'."""
    return date.today().isoformat()


def now_str() -> str:
    """返回当前时间的 ISO 字符串, 如 '2026-07-23T14:30:45.123456'."""
    return datetime.now().isoformat()


def safe_date(val: Any, default: date | None = None, fmt: str = "%Y-%m-%d") -> date | None:
    """解析日期:
       - NaN/None/'' -> default
       - datetime -> .date()
       - 其他按 fmt 解析 (解析失败 -> default)
    """
    if pd.isna(val) or val in (None, ""):
        return default
    if isinstance(val, datetime):
        return val.date()
    if isinstance(val, date):
        return val
    try:
        return datetime.strptime(str(val).strip(), fmt).date()
    except (TypeError, ValueError):
        return default


def safe_datetime(
    val: Any,
    default: datetime | None = None,
    fmt: str = "%Y-%m-%d %H:%M:%S",
) -> datetime | None:
    """解析日期时间, 同 safe_date 的语义."""
    if pd.isna(val) or val in (None, ""):
        return default
    if isinstance(val, datetime):
        return val
    try:
        return datetime.strptime(str(val).strip(), fmt)
    except (TypeError, ValueError):
        return default


# ============================================================
# 3. 集合 / 序列
# ============================================================

T = TypeVar("T")


def chunked(seq: Iterable[T], size: int) -> Iterator[list[T]]:
    """把可迭代对象切成 size 大小的批次 (生成器), 尾批可能偏小.

    Examples:
        list(chunked([1,2,3,4,5], 2))   -> [[1, 2], [3, 4], [5]]
        list(chunked([], 3))           -> []
    """
    if size <= 0:
        raise ValueError("chunk size must be > 0")
    it = iter(seq)
    while True:
        chunk = list(itertools.islice(it, size))
        if not chunk:
            return
        yield chunk


def dedupe_by(items: list[T], key: Callable[[T], Any]) -> list[T]:
    """按 key() 去重, 保留首次出现的元素, 保持原顺序.

    Example:
        dedupe_by([{'id':1,'v':'a'}, {'id':1,'v':'b'}], key=lambda x: x['id'])
        -> [{'id': 1, 'v': 'a'}]
    """
    seen: set = set()
    result: list[T] = []
    for item in items:
        k = key(item)
        if k in seen:
            continue
        seen.add(k)
        result.append(item)
    return result


# ============================================================
# 4. 字符串
# ============================================================

def truncate(s: Any, n: int = 200, suffix: str = "...") -> str:
    """字符串截断到 n 字符, 超长追加 suffix. NaN/None 返回 ''."""
    if s is None or pd.isna(s):
        return ""
    s = str(s)
    return s if len(s) <= n else s[:n] + suffix


_NORMALIZE_RE = re.compile(r"[\s/\-—()（）]")


def normalize_title(t: Any) -> str:
    """标题归一化 (用于模糊去重): 去空白 / 斜杠 / 连字符 / 中英文括号.

    Examples:
        normalize_title('全国 两会')          -> '全国两会'
        normalize_title('中央经济工作(会议)') -> '中央经济工作会议'
    """
    return _NORMALIZE_RE.sub("", safe_str(t))


# ============================================================
# 5. 多线程 / 锁
# ============================================================

class PrintLock:
    """线程安全的 print 包装, 替代各脚本里手写的 _print_lock + safe_print."""

    _lock = threading.Lock()

    @classmethod
    def print(cls, *args, **kwargs) -> None:
        with cls._lock:
            print(*args, **kwargs)


# ============================================================
# 6. lxml DTD 网络加载修复
# ============================================================

def disable_lxml_external_dtd() -> None:
    """全局替换 lxml 默认 HTMLParser, 禁用外部 DTD 网络 + 容错解析.

    在脚本顶层 import 后调用一次, 之后所有 pd.read_html / AkShare 内部调用
    都不再尝试拉 www.w3.org 的 XHTML DTD. 解决:
        OSError: Error reading file '<!DOCTYPE html PUBLIC ...'

    用法:
        from utils import disable_lxml_external_dtd
        disable_lxml_external_dtd()
    """
    import lxml.html as _lxml_html
    from lxml import etree as _lxml_etree

    _lxml_html.html_parser = _lxml_etree.HTMLParser(
        no_network=True,
        recover=True,
    )


# ============================================================
# 7. 网络重试 (装饰器)
# ============================================================

def retry(
    max_attempts: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    exceptions: tuple[type[BaseException], ...] = (Exception,),
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """失败时指数退避重试, 最后一次抛出. 默认 1s -> 2s -> 4s.

    @retry(max_attempts=3, delay=2.0, backoff=2.0)
    def fetch(...):
        return requests.get(...)

    exceptions: 只对这些类型做重试, 其他异常立刻抛出.
    """

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            t = delay
            last_err: BaseException | None = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_err = e
                    if attempt == max_attempts:
                        raise
                    time.sleep(t)
                    t *= backoff
            # 实际上不会到这里, 兜底
            if last_err is not None:
                raise last_err
            return None

        return wrapper

    return decorator


# ============================================================
# 8. 校验 / 友好报错
# ============================================================

def require_value(
    name: str,
    value: Any,
    expected_type: type | tuple[type, ...] | None = None,
) -> Any:
    """校验值有效, 否则抛出带可读提示的 RuntimeError.

    Examples:
        require_value('API_KEY', '')                        -> RuntimeError
        require_value('NUM_WORKERS', 4, expected_type=int)  -> 4

    expected_type: 可选, 要求类型匹配; 不传则只校验非空 (适用字符串).
    """
    empty = value is None or (isinstance(value, str) and value.strip() == "")
    if empty:
        raise RuntimeError(
            f"[utils] 校验失败: {name} 未配置或为空. "
            f"请检查 .env / db_config 中 {name} 是否设置, 留意拼写."
        )
    if expected_type is not None and not isinstance(value, expected_type):
        raise RuntimeError(
            f"[utils] 校验失败: {name} 类型应为 {expected_type}, "
            f"实际为 {type(value).__name__}."
        )
    return value


# ============================================================
# 9. 标的代码-名称映射 (akshare 拉取 + 本地 JSON 缓存)
# ============================================================
# 为什么需要:
#   - 学员库 wucai_trade_charles 没有 trade_stock_status 这类名称表
#   - 调用方经常需要"代码 -> 显示名"做打印 / 导出
#   - akshare.stock_info_a_code_name() 一次拉全市场 (~5000 行), 用本地 JSON 缓存
#   - 默认 7 天内复用文件, 超期或缺失则从接口刷新

# 项目根: src/data_ingestion/utils.py -> parents[2] -> ai_quant_sys/
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
_TMP_DATA_DIR = _PROJECT_ROOT / "tmp_data"
_NAME_MAP_FILE = _TMP_DATA_DIR / "instrument_name_map.json"
_NAME_MAP_MAX_AGE_DAYS = 7

# 进程内缓存 (模块级单例, 一次进程只加载一次)
_NAME_MAP_CACHE: dict[str, str] | None = None


def _code6_to_full(code6: str) -> str:
    """6位代码补交易所后缀 (幂等: 已带后缀则原样返回).

    akshare 多家接口返回的 code 形制不统一 (有的 6 位, 有的带后缀, 有的全大写),
    这个函数统一收敛成 'XXXXXX.SH/SZ/BJ' 标准形. 已带后缀直接返回, 避免重复拼接.

    后缀规则:
      沪市主板/科创板/B股/可转债:  60/68/90/11/13 -> .SH
      深市主板/创业板/B股:          00/30/20      -> .SZ
      北交所:                       43/83/87/88   -> .BJ
      沪市 ETF/LOF:                51/56/58       -> .SH
      深市 ETF/LOF:                15/16/18       -> .SZ

    Examples:
        _code6_to_full('600519')   -> '600519.SH'
        _code6_to_full('000001')   -> '000001.SZ'
        _code6_to_full('300750')   -> '300750.SZ'
        _code6_to_full('510300')   -> '510300.SH'
        _code6_to_full('159611')   -> '159611.SZ'   (深市 ETF)
        _code6_to_full('830799')   -> '830799.BJ'
        _code6_to_full('600519.SH') -> '600519.SH'  (幂等)
    """
    code6 = code6.strip()
    upper = code6.upper()
    # 幂等: 已带标准后缀直接返回 (避免 XXXXX.SH.SH)
    if upper.endswith((".SH", ".SZ", ".BJ")):
        return upper

    # 沪市: 60xxxx(主板), 68xxxx(科创板), 90xxxx(B股), 11/13xxxx(可转债)
    if code6.startswith(("60", "68", "90", "11", "13")):
        return f"{code6}.SH"
    # 深市: 00xxxx(主板), 30xxxx(创业板), 20xxxx(B股)
    if code6.startswith(("00", "30", "20")):
        return f"{code6}.SZ"
    # 北交所: 43/83/87/88xxxx
    if code6.startswith(("43", "83", "87", "88")):
        return f"{code6}.BJ"
    # 沪市 ETF/LOF: 51xxxx, 56xxxx, 58xxxx
    if code6.startswith(("51", "56", "58")):
        return f"{code6}.SH"
    # 深市 ETF/LOF: 15xxxx (创业板 ETF 等), 16xxxx, 18xxxx (REITs 等)
    if code6.startswith(("15", "16", "18")):
        return f"{code6}.SZ"
    return f"{code6}.SH"  # 兜底


def _fetch_stock_name_map_from_akshare() -> dict[str, str]:
    """从 akshare 拉取 A 股股票代码-名称映射 (不含场内基金).

    接口: ak.stock_info_a_code_name(), 返回列 code(6位str) + name.
    """
    disable_lxml_external_dtd()
    import akshare as ak  # 延迟导入, 未用到时不强依赖

    df = ak.stock_info_a_code_name()
    return {
        _code6_to_full(str(row["code"])): str(row["name"])
        for _, row in df.iterrows()
        if pd.notna(row.get("code")) and pd.notna(row.get("name"))
    }


def _fetch_etf_name_map_from_akshare() -> dict[str, str]:
    """从 akshare 拉取场内基金 (ETF/LOF/REITs) 代码-名称映射.

    接口: ak.fund_etf_spot_em(), 返回列 含 '代码'(6位str) + '名称'.
    覆盖沪市 (51/56/58 开头) 和深市 (15/16/18 开头) 所有场内基金.

    注意: 该接口是实时行情接口, 数据可能偶发为空, 调用方需容错.
    """
    disable_lxml_external_dtd()
    import akshare as ak

    df = ak.fund_etf_spot_em()
    return {
        _code6_to_full(str(row["代码"])): str(row["名称"])
        for _, row in df.iterrows()
        if pd.notna(row.get("代码")) and pd.notna(row.get("名称"))
    }


def _fetch_name_map_from_akshare() -> dict[str, str]:
    """从 akshare 拉取全市场代码-名称 (股票 + 场内基金, 后者补充前者).

    调用前自动 disable_lxml_external_dtd() 防止 AkShare 触发 www.w3.org 网络请求.
    返回: {code_with_suffix: name}, 如 {'600519.SH': '贵州茅台', '159611.SZ': '...ETF'}.

    场内基金拉取失败时不影响主流程, 仅打印警告后只返回股票部分.
    """
    stock_map = _fetch_stock_name_map_from_akshare()
    try:
        etf_map = _fetch_etf_name_map_from_akshare()
    except Exception as e:
        print(f"  [utils] 警告: 场内基金映射拉取失败 ({e}), 仅用股票映射")
        etf_map = {}
    # 合并: 股票优先, ETF 补充 (理论上无 key 冲突, 股票代码和场内基金代码不重叠)
    return {**stock_map, **etf_map}


def _save_name_map(name_map: dict[str, str]) -> None:
    """保存映射到 tmp_data/instrument_name_map.json, 含生成时间戳."""
    _TMP_DATA_DIR.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated_at": datetime.now().isoformat(),
        "count": len(name_map),
        "mapping": name_map,
    }
    with _NAME_MAP_FILE.open("w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)


def _load_name_map_from_file(max_age_days: int = _NAME_MAP_MAX_AGE_DAYS) -> dict[str, str] | None:
    """从 JSON 文件加载, 文件缺失或超期返回 None.

    超期判定: 文件 mtime 距今 > max_age_days 天. 文件格式异常也返回 None.
    """
    if not _NAME_MAP_FILE.exists():
        return None
    try:
        mtime = datetime.fromtimestamp(_NAME_MAP_FILE.stat().st_mtime)
        age_days = (datetime.now() - mtime).days
        if age_days > max_age_days:
            return None
        with _NAME_MAP_FILE.open("r", encoding="utf-8") as f:
            payload = json.load(f)
        mapping = payload.get("mapping")
        if not isinstance(mapping, dict):
            return None
        return mapping
    except (json.JSONDecodeError, OSError, KeyError, ValueError):
        return None


def _refresh_name_map() -> dict[str, str]:
    """强制从 akshare 拉取并写盘, 返回新映射.

    akshare 拉取失败时, 如果本地存在过期文件, fallback 使用之 (宁可旧也别空).
    """
    try:
        name_map = _fetch_name_map_from_akshare()
        _save_name_map(name_map)
        print(f"  [utils] 名称映射已刷新: {len(name_map)} 只, 路径 {_NAME_MAP_FILE}")
        return name_map
    except Exception as e:
        stale = _load_name_map_from_file(max_age_days=10_000)  # 忽略年龄限制
        if stale:
            print(f"  [utils] 警告: akshare 拉取失败 ({e}), 使用过期本地缓存 {len(stale)} 条")
            return stale
        print(f"  [utils] 警告: akshare 拉取失败且无本地缓存 ({e}), 名称将退化为代码")
        return {}


def get_instrument_names(codes: Iterable[str], *, force_refresh: bool = False) -> dict[str, str]:
    """获取代码-显示名称映射.

    加载策略 (进程级单例缓存):
      1. 已缓存 -> 直接返回
      2. 文件存在且 < 7 天 -> 从文件加载
      3. 否则 -> 从 akshare 拉取并刷新文件

    akshare 失败时 fallback 到过期本地文件, 再不行返回 {code: code}.

    参数:
        codes: 代码列表, 形如 ['600519.SH', '000001.SZ'] (含交易所后缀)
        force_refresh: True 时强制从 akshare 重新拉取, 跳过文件缓存

    返回:
        {code: name} 字典, 找不到时 value=code 自身 (调用方可安全 get(code, code))

    Examples:
        get_instrument_names(['600519.SH'])
        -> {'600519.SH': '贵州茅台'}
    """
    global _NAME_MAP_CACHE

    if force_refresh or _NAME_MAP_CACHE is None:
        if force_refresh:
            _NAME_MAP_CACHE = _refresh_name_map()
        else:
            cached = _load_name_map_from_file()
            if cached:
                _NAME_MAP_CACHE = cached
            else:
                _NAME_MAP_CACHE = _refresh_name_map()

    return {code: _NAME_MAP_CACHE.get(code, code) for code in codes}
