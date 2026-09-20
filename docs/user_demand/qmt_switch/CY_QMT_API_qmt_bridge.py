# -*- coding: gbk -*-
# Author：@跟陈博士学AI
import json
import locale
import math
from tornado.web import Application, RequestHandler, HTTPError
from tornado.ioloop import IOLoop
import logging

# 自定义
ACCOUNT_ID = '你的账户ID'
TOKEN = "learning_ai_with_dr_chen"
PORT = 15588


# ===================================
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
locale.setlocale(locale.LC_CTYPE, 'chinese')


def safe_call(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as e:
        logger.error(f"{func.__name__} 调用失败: {e}")
        return None


def _safe_float(v):
    """QMT 持仓里退市股/老三板可能返 inf/nan (成本 0 → ProfitRate=inf), 标准 JSON 不容忍."""
    try:
        f = float(v)
        return f if math.isfinite(f) else 0.0
    except (TypeError, ValueError):
        return 0.0


# 2026-07-08: 反射字段名按类缓存.
# get_trade_detail_data 返回的是 C++ 包装对象, 之前对每个对象都跑一遍
# dir() + 逐属性 getattr/callable 判定. 持仓几百只/委托上千笔的大账户下,
# 这是单线程泵的主要占用来源 (泵被占住期间, 下单/资金/判活请求全部排队,
# 客户端就会"拉取信息超时"). 属性名集合由类型决定, 按类缓存一次,
# 后续每个对象只做直接取值, 大列表查询耗时降一个量级.
_ATTR_NAMES_CACHE = {}


def export_attrs(obj):
    """对象 -> {属性名: str(值)}. 属性名列表按类型缓存, 值逐对象取."""
    names = _ATTR_NAMES_CACHE.get(type(obj))
    if names is None:
        names = []
        for attr in dir(obj):
            if attr.startswith('_'):
                continue
            try:
                if not callable(getattr(obj, attr)):
                    names.append(attr)
            except Exception:
                pass
        _ATTR_NAMES_CACHE[type(obj)] = names
    attrs = {}
    for attr in names:
        try:
            attrs[attr] = str(getattr(obj, attr))
        except Exception:
            pass
    return attrs


# ============= BaseHandler =============

AUTH_EXEMPT = set()


def no_auth(cls):
    AUTH_EXEMPT.add(cls)
    return cls


class BaseHandler(RequestHandler):
    def prepare(self):
        if self.__class__ not in AUTH_EXEMPT:
            token = self.request.headers.get('X-Token')
            if token != TOKEN:
                raise HTTPError(401, "认证失败：token 无效或缺失")

    def set_default_headers(self):
        self.set_header("Content-Type", "application/json; charset=utf-8")

    def write_error(self, status_code, **kwargs):
        self.finish(json.dumps({
            "error": self._reason,
            "status_code": status_code
        }, ensure_ascii=False))

    def ctx(self):
        return self.application.ContextInfo

    def acc(self):
        return self.application.accountID


# ============= 1. ContextInfo 属性 =============
# ContextInfo.period - 获取当前周期
class ContextPeriodHandler(BaseHandler):
    def get(self):
        self.write(json.dumps({"period": self.ctx().period}, ensure_ascii=False))

# ContextInfo.barpos - 获取当前K线索引号
class ContextBarposHandler(BaseHandler):
    def get(self):
        self.write(json.dumps({"barpos": self.ctx().barpos}, ensure_ascii=False))

# ContextInfo.time_tick_size - 获取当前K线数目
class ContextTimeTickSizeHandler(BaseHandler):
    def get(self):
        self.write(json.dumps({"time_tick_size": self.ctx().time_tick_size}, ensure_ascii=False))

# ContextInfo.stockcode - 获取当前主图品种代码
class ContextStockCodeHandler(BaseHandler):
    def get(self):
        self.write(json.dumps({"stockcode": self.ctx().stockcode}, ensure_ascii=False))

# ContextInfo.dividend_type - 获取当前复权方式
class ContextDividendTypeHandler(BaseHandler):
    def get(self):
        self.write(json.dumps({"dividend_type": self.ctx().dividend_type}, ensure_ascii=False))

# ContextInfo.market - 获取当前主图市场
class ContextMarketHandler(BaseHandler):
    def get(self):
        self.write(json.dumps({"market": self.ctx().market}, ensure_ascii=False))

# ContextInfo.do_back_test - 是否开启回测模式
class ContextDoBackTestHandler(BaseHandler):
    def get(self):
        self.write(json.dumps({"do_back_test": self.ctx().do_back_test}, ensure_ascii=False))

# ContextInfo.benchmark - 获取回测基准
class ContextBenchmarkHandler(BaseHandler):
    def get(self):
        self.write(json.dumps({"benchmark": self.ctx().benchmark}, ensure_ascii=False))

# ContextInfo.capital - 获取回测初始资金
class ContextCapitalHandler(BaseHandler):
    def get(self):
        self.write(json.dumps({"capital": self.ctx().capital}, ensure_ascii=False))

# ContextInfo.get_universe() - 获取股票池中的股票
class ContextUniverseHandler(BaseHandler):
    def get(self):
        self.write(json.dumps({"universe": self.ctx().get_universe()}, ensure_ascii=False))


# ============= 2. 数据查询 (ContextInfo get_*) =============
# ContextInfo.get_stock_name() - 根据代码获取股票名称
class StockNameHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        stockcode = data.get('stockcode', '')
        ret = safe_call(self.ctx().get_stock_name, stockcode)
        self.write(json.dumps({"stockcode": stockcode, "name": ret}, ensure_ascii=False))

# get_open_date() - 根据代码获取上市时间
class OpenDateHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        stockcode = data.get('stockcode', '')
        ret = safe_call(get_open_date, stockcode)
        self.write(json.dumps({"stockcode": stockcode, "open_date": ret}, ensure_ascii=False))

# ContextInfo.get_last_volume() - 获取最新流通股本
class LastVolumeHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        stockcode = data.get('stockcode', '')
        ret = safe_call(self.ctx().get_last_volume, stockcode)
        if ret is None:
            raise HTTPError(500, "获取流通股本失败")
        self.write(json.dumps({"stockcode": stockcode, "last_volume": ret}, ensure_ascii=False))

# ContextInfo.get_bar_timetag() - 获取K线时间戳
class BarTimetagHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        index = int(data.get('index', -1))
        ret = safe_call(self.ctx().get_bar_timetag, index)
        self.write(json.dumps({"index": index, "timetag": ret}, ensure_ascii=False))

# ContextInfo.get_tick_timetag() - 获取最新分笔时间戳
class TickTimetagHandler(BaseHandler):
    def get(self):
        ret = safe_call(self.ctx().get_tick_timetag)
        self.write(json.dumps({"timetag": ret}, ensure_ascii=False))

# ContextInfo.get_sector() - 获取指数成份股
class SectorHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        sector = data.get('sector', '')
        realtime = data.get('realtime', '0')
        if not sector:
            raise HTTPError(400, "need args sector")
        ret = safe_call(self.ctx().get_sector, sector, int(realtime) if realtime != '0' else 0)
        self.write(json.dumps({"sector": sector, "stocks": ret or []}, ensure_ascii=False))

# ContextInfo.get_industry() - 获取行业成份股
class IndustryHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        industry = data.get('industry', '')
        if not industry:
            raise HTTPError(400, "need args industry")
        ret = safe_call(self.ctx().get_industry, industry)
        resp = {"industry": industry, "stocks": ret or []}
        if not ret:
            # 行业/板块名须与QMT底层命名完全一致,为空时给出候选提示
            try:
                from xtquant import xtdata
                sectors = xtdata.get_sector_list() or []
                core = industry.replace('CSRC', '').replace('SW', '').strip()
                candidates = [s for s in sectors
                              if core and (core in s or s in industry)][:20]
                resp["hint"] = "未匹配到该行业名,QMT底层命名可能不同,先调 /api/xtdata/sector_list 确认"
                resp["candidates"] = candidates
            except Exception:
                resp["hint"] = "未匹配到该行业名,请调 /api/xtdata/sector_list 确认准确名称"
        self.write(json.dumps(resp, ensure_ascii=False))
        
# ContextInfo.get_stock_list_in_sector() - 获取板块成份股
class StockListInSectorHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        sectorname = data.get('sectorname', '')
        if not sectorname:
            raise HTTPError(400, "need args sectorname")
        ret = safe_call(self.ctx().get_stock_list_in_sector, sectorname)
        self.write(json.dumps({"sectorname": sectorname, "stocks": ret or []}, ensure_ascii=False))

# ContextInfo.get_weight_in_index() - 获取指数中权重
class WeightInIndexHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        indexcode = data.get('indexcode', '')
        stockcode = data.get('stockcode', '')
        ret = safe_call(self.ctx().get_weight_in_index, indexcode, stockcode)
        self.write(json.dumps({"indexcode": indexcode, "stockcode": stockcode, "weight": ret}, ensure_ascii=False))

# ContextInfo.get_contract_multiplier() - 获取合约乘数
class ContractMultiplierHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        contractcode = data.get('contractcode', '')
        ret = safe_call(self.ctx().get_contract_multiplier, contractcode)
        self.write(json.dumps({"contractcode": contractcode, "multiplier": ret}, ensure_ascii=False))

# ContextInfo.get_risk_free_rate() - 获取无风险利率
class RiskFreeRateHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        index = int(data.get('index', '-1'))
        ret = safe_call(self.ctx().get_risk_free_rate, index)
        self.write(json.dumps({"index": index, "risk_free_rate": ret}, ensure_ascii=False))

# ContextInfo.get_date_location() - 获取日期对应的K线索引
class DateLocationHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        strdate = data.get('strdate', '')
        ret = safe_call(self.ctx().get_date_location, strdate)
        self.write(json.dumps({"strdate": strdate, "location": ret}, ensure_ascii=False))

# ContextInfo.get_history_data() - 获取历史行情数据(多品种字典)
class HistoryDataHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        length = int(data.get('len', '10'))
        period = data.get('period', '1d')
        field = data.get('field', 'close')
        dividend_type = int(data.get('dividend_type', '0'))
        skip_paused = data.get('skip_paused', 'true').lower() == 'true'
        ret = safe_call(self.ctx().get_history_data, length, period, field, dividend_type, skip_paused)
        self.write(json.dumps({"data": ret} if ret else {"error": "获取历史数据失败"}, ensure_ascii=False))

# ContextInfo.get_market_data() - 获取行情数据(DataFrame)
class MarketDataHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        fields = data.get('fields', '')
        stock_code = data.get('stock_code', '')
        start_time = data.get('start_time', '')
        end_time = data.get('end_time', '')
        period = data.get('period', '1d')
        dividend_type = data.get('dividend_type', 'none')
        count = int(data.get('count', '-1'))
        fields_list = [f.strip() for f in fields.split(',')] if fields else []
        stock_list = [s.strip() for s in stock_code.split(',')] if stock_code else []
        ret = safe_call(self.ctx().get_market_data, fields_list, stock_list, start_time, end_time, True, period, dividend_type, count)
        if ret is None:
            raise HTTPError(500, "获取行情数据失败")
        if hasattr(ret, 'to_dict'):
            ret = ret.to_dict()
        self.write(json.dumps({"data": ret}, ensure_ascii=False, default=str))

# ContextInfo.get_market_data_ex() - 获取扩展行情(Level2)
class MarketDataExHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        fields = data.get('fields', '')
        stock_code = data.get('stock_code', '')
        period = data.get('period', 'follow')
        start_time = data.get('start_time', '')
        end_time = data.get('end_time', '')
        count = int(data.get('count', '-1'))
        dividend_type = data.get('dividend_type', 'follow')
        fields_list = [f.strip() for f in fields.split(',')] if fields else []
        stock_list = [s.strip() for s in stock_code.split(',')] if stock_code else []
        ret = safe_call(self.ctx().get_market_data_ex, fields_list, stock_list, period, start_time, end_time, count, dividend_type)
        if ret is None:
            raise HTTPError(500, "获取扩展行情失败")
        result = {}
        for k, v in ret.items():
            if hasattr(v, 'to_dict'):
                result[k] = v.to_dict()
            else:
                result[k] = str(v)
        self.write(json.dumps({"data": result}, ensure_ascii=False, default=str))

# ContextInfo.get_full_tick() - 获取分笔数据
class FullTickHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        stocks = data.get('stocks', '')
        if not stocks:
            raise HTTPError(400, "need args stocks")
        code_list = [s.strip() for s in stocks.split(',')]
        ret = safe_call(self.ctx().get_full_tick, code_list)
        if not ret:
            raise HTTPError(500, "获取分笔行情失败")
        self.write(json.dumps(ret, ensure_ascii=False, default=str))

# ContextInfo.get_divid_factors() - 获取除权除息和复权因子
class DividFactorsHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        stockcode = data.get('stockcode', '')
        ret = safe_call(self.ctx().get_divid_factors, stockcode)
        self.write(json.dumps({"stockcode": stockcode, "factors": ret or {}}, ensure_ascii=False))

# ContextInfo.get_main_contract() - 获取期货主力合约
class MainContractHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        codemarket = data.get('codemarket', '')
        ret = safe_call(self.ctx().get_main_contract, codemarket)
        self.write(json.dumps({"codemarket": codemarket, "main_contract": ret}, ensure_ascii=False))

# timetag_to_datetime() - 毫秒时间戳转日期时间
class TimetagToDatetimeHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        timetag = int(data.get('timetag', '0'))
        fmt = data.get('format', '%Y-%m-%d %H:%M:%S')
        ret = safe_call(timetag_to_datetime, timetag, fmt)
        self.write(json.dumps({"timetag": timetag, "datetime": ret}, ensure_ascii=False))

# ContextInfo.get_total_share() - 获取总股本
class TotalShareHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        stockcode = data.get('stockcode', '')
        ret = safe_call(self.ctx().get_total_share, stockcode)
        self.write(json.dumps({"stockcode": stockcode, "total_share": ret}, ensure_ascii=False))

# ContextInfo.get_trading_dates() - 获取交易日列表
class TradingDatesHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        stockcode = data.get('stockcode', '')
        start_date = data.get('start_date', '')
        end_date = data.get('end_date', '')
        count = data.get('count', '')
        period = data.get('period', '1d')
        count_int = int(count) if count else -1
        ret = safe_call(self.ctx().get_trading_dates, stockcode, start_date, end_date, count_int, period)
        self.write(json.dumps({"dates": ret or []}, ensure_ascii=False))

# ContextInfo.get_svol() - 获取内盘成交量
class SvolHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        stockcode = data.get('stockcode', '')
        ret = safe_call(self.ctx().get_svol, stockcode)
        self.write(json.dumps({"stockcode": stockcode, "svol": ret}, ensure_ascii=False))

# ContextInfo.get_bvol() - 获取外盘成交量
class BvolHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        stockcode = data.get('stockcode', '')
        ret = safe_call(self.ctx().get_bvol, stockcode)
        self.write(json.dumps({"stockcode": stockcode, "bvol": ret}, ensure_ascii=False))

# ContextInfo.get_longhubang() - 获取龙虎榜数据
class LonghubangHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        stock_list = data.get('stock_list', '')
        startTime = data.get('startTime', '')
        endTime = data.get('endTime', '')
        slist = [s.strip() for s in stock_list.split(',')] if stock_list else []
        ret = safe_call(self.ctx().get_longhubang, slist, startTime, endTime)
        if hasattr(ret, 'to_dict'):
            ret = ret.to_dict()
        self.write(json.dumps({"data": ret} if ret else {"error": "获取龙虎榜数据失败"}, ensure_ascii=False, default=str))

# get_top10_share_holder() - 获取十大股东数据
class Top10ShareHolderHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        stock_list = data.get('stock_list', '')
        data_name = data.get('data_name', 'holder')
        start_time = data.get('start_time', '')
        end_time = data.get('end_time', '')
        slist = [s.strip() for s in stock_list.split(',')] if stock_list else []
        ret = safe_call(get_top10_share_holder, slist, data_name, start_time, end_time)
        if hasattr(ret, 'to_dict'):
            ret = ret.to_dict()
        self.write(json.dumps({"data": ret} if ret else {"error": "获取十大股东数据失败"}, ensure_ascii=False, default=str))

# ContextInfo.get_option_detail_data() - 获取期权详细信息
class OptionDetailHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        optioncode = data.get('optioncode', '')
        ret = safe_call(self.ctx().get_option_detail_data, optioncode)
        self.write(json.dumps({"optioncode": optioncode, "detail": ret or {}}, ensure_ascii=False))

# ContextInfo.get_turnover_rate() - 获取换手率
class TurnoverRateHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        stock_list = data.get('stock_list', '')
        startTime = data.get('startTime', '')
        endTime = data.get('endTime', '')
        slist = [s.strip() for s in stock_list.split(',')] if stock_list else []
        ret = safe_call(self.ctx().get_turnover_rate, slist, startTime, endTime)
        if hasattr(ret, 'to_dict'):
            ret = ret.to_dict()
        self.write(json.dumps({"data": ret} if ret else {"error": "获取换手率失败"}, ensure_ascii=False, default=str))

# get_etf_info() - 获取ETF申赎清单及成分股
class EtfInfoHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        stockcode = data.get('stockcode', '')
        ret = safe_call(get_etf_info, stockcode)
        self.write(json.dumps({"stockcode": stockcode, "info": ret or {}}, ensure_ascii=False, default=str))

# get_etf_iopv() - 获取ETF基金份额参考净值
class EtfIopvHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        stockcode = data.get('stockcode', '')
        ret = safe_call(get_etf_iopv, stockcode)
        self.write(json.dumps({"stockcode": stockcode, "iopv": ret}, ensure_ascii=False))

# ContextInfo.get_instrumentdetail() - 获取合约详细信息
class InstrumentDetailHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        stockcode = data.get('stockcode', '')
        ret = safe_call(self.ctx().get_instrumentdetail, stockcode)
        self.write(json.dumps({"stockcode": stockcode, "detail": ret or {}}, ensure_ascii=False, default=str))

# ContextInfo.get_contract_expire_date() - 获取期货合约到期日
class ContractExpireDateHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        codemarket = data.get('codemarket', '')
        ret = safe_call(self.ctx().get_contract_expire_date, codemarket)
        self.write(json.dumps({"codemarket": codemarket, "expire_date": ret}, ensure_ascii=False))

# ContextInfo.get_option_undl_data() - 获取期权标的对应的期权品种列表
class OptionUndlDataHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        undl_code_ref = data.get('undl_code_ref', '')
        ret = safe_call(self.ctx().get_option_undl_data, undl_code_ref)
        self.write(json.dumps({"data": ret or []}, ensure_ascii=False, default=str))

# ContextInfo.get_financial_data() - 获取财务数据
class FinancialDataHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        tabname = data.get('tabname', '')
        colname = data.get('colname', '')
        market = data.get('market', '')
        code = data.get('code', '')
        report_type = data.get('report_type', 'report_time')
        barpos = int(data.get('barpos', '-1'))
        if tabname and colname and market and code:
            ret = safe_call(self.ctx().get_financial_data, tabname, colname, market, code, report_type, barpos)
        else:
            field_list = data.get('fieldList', '')
            stock_list = data.get('stockList', '')
            start_date = data.get('startDate', '')
            end_date = data.get('endDate', '')
            fields = [f.strip() for f in field_list.split(',')] if field_list else []
            stocks = [s.strip() for s in stock_list.split(',')] if stock_list else []
            rtype = data.get('report_type', 'announce_time')
            ret = safe_call(self.ctx().get_financial_data, fields, stocks, start_date, end_date, rtype)
        if hasattr(ret, 'to_dict'):
            ret = ret.to_dict()
        self.write(json.dumps({"data": ret} if ret is not None else {"error": "获取财务数据失败"}, ensure_ascii=False, default=str))

# ============= xtdata 风格财务数据（与 miniQMT/xtquant 结构一致）=============
# xtdata.get_financial_data() - 按报告期组织, 返回 {stock: {table: records}}
class XtdataFinancialDataHandler(BaseHandler):
    def post(self):
        try:
            from xtquant import xtdata
        except ImportError:
            raise HTTPError(501, "QMT环境缺少xtquant包,无法提供xtdata财务数据")
        data = json.loads(self.request.body)
        stock_list = data.get('stock_list', '')
        table_list = data.get('table_list', '')       # 如 Balance,Income,CashFlow,PershareIndex
        start_time = data.get('start_time', '')
        end_time = data.get('end_time', '')
        report_type = data.get('report_type', 'report_time')  # report_time / announce_time
        stocks = [s.strip() for s in stock_list.split(',') if s.strip()]
        tables = [t.strip() for t in table_list.split(',') if t.strip()]
        if not stocks:
            raise HTTPError(400, "need args stock_list")
        # 防止大请求阻塞泵循环(单线程架构,阻塞期间下单等请求全部排队)
        if len(stocks) > 50:
            raise HTTPError(400, "单次最多50只,请客户端分批请求")
        ret = safe_call(xtdata.get_financial_data, stocks, tables,
                        start_time, end_time, report_type)
        if ret is None:
            raise HTTPError(500, "获取xtdata财务数据失败(可能未下载,先调download接口)")
        # {stock: {table: DataFrame}} → {stock: {table: [records]}}
        result = {}
        for stk, tbls in ret.items():
            result[stk] = {}
            for tname, df in (tbls or {}).items():
                if hasattr(df, 'to_dict'):
                    result[stk][tname] = df.to_dict(orient='records')
                else:
                    result[stk][tname] = str(df)
        self.write(json.dumps({"data": result}, ensure_ascii=False, default=str))

# xtdata.download_financial_data() - 首次使用前下载财务数据到本地
class XtdataDownloadFinancialHandler(BaseHandler):
    def post(self):
        try:
            from xtquant import xtdata
        except ImportError:
            raise HTTPError(501, "QMT环境缺少xtquant包")
        data = json.loads(self.request.body)
        stocks = [s.strip() for s in data.get('stock_list', '').split(',') if s.strip()]
        tables = [t.strip() for t in data.get('table_list', '').split(',') if t.strip()]
        if not stocks:
            raise HTTPError(400, "need args stock_list")
        if len(stocks) > 20:
            raise HTTPError(400, "下载较慢,单次最多20只,请分批")
        safe_call(xtdata.download_financial_data, stocks, tables)
        self.write(json.dumps({"status": "success",
                               "message": f"已触发 {len(stocks)} 只财务数据下载"}, ensure_ascii=False))

# xtdata.get_sector_list() - 列出全部板块名称
class XtdataSectorListHandler(BaseHandler):
    def get(self):
        try:
            from xtquant import xtdata
        except ImportError:
            raise HTTPError(501, "QMT环境缺少xtquant包")
        ret = safe_call(xtdata.get_sector_list)
        if ret is None:
            raise HTTPError(500, "获取板块列表失败")
        self.write(json.dumps({"sectors": ret}, ensure_ascii=False, default=str))

# xtdata.get_instrument_detail() - 个股详情(流通股本/名称等, 字段与 miniQMT 一致, 原样透传不做映射)
class XtdataInstrumentDetailHandler(BaseHandler):
    def post(self):
        try:
            from xtquant import xtdata
        except ImportError:
            raise HTTPError(501, "QMT环境缺少xtquant包")
        data = json.loads(self.request.body)
        stock_list = data.get('stock_list', '')
        iscomplete = str(data.get('iscomplete', 'false')).lower() == 'true'
        stocks = [s.strip() for s in stock_list.split(',') if s.strip()]
        if not stocks:
            raise HTTPError(400, "need args stock_list")
        if len(stocks) > 200:
            raise HTTPError(400, "单次最多200只, 请客户端分批请求")
        result = {}
        for stk in stocks:
            try:
                try:
                    result[stk] = xtdata.get_instrument_detail(stk, iscomplete) or None
                except TypeError:
                    # 旧版xtquant不支持iscomplete参数,降级为单参调用
                    result[stk] = xtdata.get_instrument_detail(stk) or None
            except Exception as e:
                result[stk] = {"error": str(e)}
        self.write(json.dumps({"data": result}, ensure_ascii=False, default=str))

# xtdata.get_market_data_ex() - 历史/实时K线(上下文无关,与miniQMT字段一致)
# 注意:与 /api/data/market_data 的区别是不依赖主图周期/复权设置
class XtdataMarketDataExHandler(BaseHandler):
    def post(self):
        try:
            from xtquant import xtdata
        except ImportError:
            raise HTTPError(501, "QMT环境缺少xtquant包")
        data = json.loads(self.request.body)
        field_list = data.get('field_list', '')          # 空=全字段
        stock_list = data.get('stock_list', '')
        period = data.get('period', '1d')                # 1d/1m/5m/tick...
        start_time = data.get('start_time', '')
        end_time = data.get('end_time', '')
        count = int(data.get('count', '-1'))
        dividend_type = data.get('dividend_type', 'none')  # none/front/back/front_ratio/back_ratio
        fill_data = str(data.get('fill_data', 'true')).lower() == 'true'
        fields = [f.strip() for f in field_list.split(',') if f.strip()]
        stocks = [s.strip() for s in stock_list.split(',') if s.strip()]
        if not stocks:
            raise HTTPError(400, "need args stock_list")
        # K线数据量大,防止阻塞泵循环(阻塞期间下单请求也在排队)
        if len(stocks) > 50:
            raise HTTPError(400, "单次最多50只, 请客户端分批请求")
        ret = safe_call(xtdata.get_market_data_ex, fields, stocks, period,
                        start_time, end_time, count, dividend_type, fill_data)
        if ret is None:
            raise HTTPError(500, "获取K线失败(可能未下载,先调download_history_data)")
        result = {}
        for k, v in ret.items():
            if hasattr(v, 'reset_index'):
                df = v.reset_index()
                # 索引列统一命名为 time,方便客户端解析
                if 'index' in df.columns:
                    df = df.rename(columns={'index': 'time'})
                result[k] = df.to_dict(orient='records')
            else:
                result[k] = str(v)
        self.write(json.dumps({"data": result}, ensure_ascii=False, default=str))
 
 
# xtdata.download_history_data() - 下载历史K线到本地(查询前置步骤,较慢)
class XtdataDownloadHistoryHandler(BaseHandler):
    def post(self):
        try:
            from xtquant import xtdata
        except ImportError:
            raise HTTPError(501, "QMT环境缺少xtquant包")
        data = json.loads(self.request.body)
        stocks = [s.strip() for s in data.get('stock_list', '').split(',') if s.strip()]
        period = data.get('period', '1d')
        start_time = data.get('start_time', '')
        end_time = data.get('end_time', '')
        if not stocks:
            raise HTTPError(400, "need args stock_list")
        if len(stocks) > 20:
            raise HTTPError(400, "下载较慢, 单次最多20只, 请分批")
        ok, fail = [], []
        for stk in stocks:
            try:
                xtdata.download_history_data(stk, period, start_time, end_time)
                ok.append(stk)
            except Exception as e:
                fail.append({"stock": stk, "error": str(e)})
        self.write(json.dumps({"status": "success", "downloaded": ok,
                               "failed": fail}, ensure_ascii=False))
 
 
# xtdata.get_stock_list_in_sector() - 板块成分股(xtdata版,与miniQMT调用一致)
# 诚实说明:板块划分口径由QMT底层数据决定,完整版与miniQMT的划分差异
# (如899050.BJ归属)本端点无法消除,漏码请在客户端快照层做miss直通兜底
class XtdataStockListInSectorHandler(BaseHandler):
    def post(self):
        try:
            from xtquant import xtdata
        except ImportError:
            raise HTTPError(501, "QMT环境缺少xtquant包")
        data = json.loads(self.request.body)
        sector_name = data.get('sector_name', '')
        if not sector_name:
            raise HTTPError(400, "need args sector_name")
        ret = safe_call(xtdata.get_stock_list_in_sector, sector_name)
        self.write(json.dumps({"sector_name": sector_name,
                               "stocks": ret or []}, ensure_ascii=False))
 
 
# xtdata.get_trading_dates() - 交易日列表(毫秒时间戳,与miniQMT格式一致)
class XtdataTradingDatesHandler(BaseHandler):
    def post(self):
        try:
            from xtquant import xtdata
        except ImportError:
            raise HTTPError(501, "QMT环境缺少xtquant包")
        data = json.loads(self.request.body)
        market = data.get('market', 'SH')
        start_time = data.get('start_time', '')
        end_time = data.get('end_time', '')
        count = int(data.get('count', '-1'))
        ret = safe_call(xtdata.get_trading_dates, market, start_time, end_time, count)
        self.write(json.dumps({"market": market,
                               "dates": ret or []}, ensure_ascii=False, default=str))
 
 
# xtdata.get_divid_factors() - 除权除息/复权因子(xtdata版结构)
class XtdataDividFactorsHandler(BaseHandler):
    def post(self):
        try:
            from xtquant import xtdata
        except ImportError:
            raise HTTPError(501, "QMT环境缺少xtquant包")
        data = json.loads(self.request.body)
        stock_code = data.get('stock_code', '')
        if not stock_code:
            raise HTTPError(400, "need args stock_code")
        ret = safe_call(xtdata.get_divid_factors, stock_code)
        if hasattr(ret, 'reset_index'):
            df = ret.reset_index()
            if 'index' in df.columns:
                df = df.rename(columns={'index': 'time'})
            ret = df.to_dict(orient='records')
        self.write(json.dumps({"stock_code": stock_code,
                               "factors": ret if ret is not None else []},
                              ensure_ascii=False, default=str))
 
 
# xtdata.get_index_weight() - 指数成分权重(股票池构建常用;旧版xtdata可能无此函数)
class XtdataIndexWeightHandler(BaseHandler):
    def post(self):
        try:
            from xtquant import xtdata
        except ImportError:
            raise HTTPError(501, "QMT环境缺少xtquant包")
        if not hasattr(xtdata, 'get_index_weight'):
            raise HTTPError(501, "当前QMT内嵌xtquant版本不支持get_index_weight")
        data = json.loads(self.request.body)
        index_code = data.get('index_code', '')
        if not index_code:
            raise HTTPError(400, "need args index_code")
        ret = safe_call(xtdata.get_index_weight, index_code)
        if hasattr(ret, 'to_dict'):
            ret = ret.to_dict()
        self.write(json.dumps({"index_code": index_code,
                               "weights": ret or {}}, ensure_ascii=False, default=str))
 
# ContextInfo.get_factor_data() - 获取多因子数据
class FactorDataHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        field_list = data.get('fieldList', '')
        stock_list = data.get('stockList', '')
        stock_code = data.get('stockCode', '')
        start_date = data.get('startDate', '')
        end_date = data.get('endDate', '')
        fields = [f.strip() for f in field_list.split(',')] if field_list else []
        if stock_code:
            ret = safe_call(self.ctx().get_factor_data, fields, stock_code, start_date, end_date)
        else:
            stocks = [s.strip() for s in stock_list.split(',')] if stock_list else []
            ret = safe_call(self.ctx().get_factor_data, fields, stocks, start_date, end_date)
        if hasattr(ret, 'to_dict'):
            ret = ret.to_dict()
        self.write(json.dumps({"data": ret} if ret is not None else {"error": "获取因子数据失败"}, ensure_ascii=False, default=str))

# ContextInfo.get_his_st_data() - 获取历史ST数据
class HisStDataHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        stockCode = data.get('stockCode', '')
        ret = safe_call(self.ctx().get_his_st_data, stockCode)
        self.write(json.dumps({"stockCode": stockCode, "data": ret or {}}, ensure_ascii=False))

# ContextInfo.get_his_index_data() - 获取历史指数数据
class HisIndexDataHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        index = data.get('index', '')
        ret = safe_call(self.ctx().get_his_index_data, index)
        self.write(json.dumps({"index": index, "data": ret or {}}, ensure_ascii=False, default=str))

# ContextInfo.get_all_subscription() - 获取当前所有行情订阅信息
class AllSubscriptionHandler(BaseHandler):
    def get(self):
        ret = safe_call(self.ctx().get_all_subscription)
        self.write(json.dumps({"subscriptions": ret or {}}, ensure_ascii=False, default=str))

# ContextInfo.get_option_list() - 获取指定期权列表
class OptionListHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        undl_code = data.get('undl_code', '')
        dedate = data.get('dedate', '')
        opttype = data.get('opttype', '')
        isavailable = data.get('isavailable', 'true').lower() == 'true'
        ret = safe_call(self.ctx().get_option_list, undl_code, dedate, opttype, isavailable)
        self.write(json.dumps({"option_list": ret or []}, ensure_ascii=False))

# ContextInfo.get_his_contract_list() - 获取过期合约列表
class HisContractListHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        market = data.get('market', '')
        ret = safe_call(self.ctx().get_his_contract_list, market)
        self.write(json.dumps({"market": market, "contracts": ret or []}, ensure_ascii=False))

# ContextInfo.get_option_iv() - 获取期权实时隐含波动率
class OptionIvHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        optioncode = data.get('optioncode', '')
        ret = safe_call(self.ctx().get_option_iv, optioncode)
        self.write(json.dumps({"optioncode": optioncode, "iv": ret}, ensure_ascii=False))

# ContextInfo.bsm_price() - BS模型计算欧式期权理论价格
class BsmPriceHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        optionType = data.get('optionType', 'C')
        objectPrices = data.get('objectPrices', '')
        strikePrice = float(data.get('strikePrice', '0'))
        riskFree = float(data.get('riskFree', '0'))
        sigma = float(data.get('sigma', '0'))
        days = int(data.get('days', '0'))
        dividend = float(data.get('dividend', '0'))
        try:
            op = float(objectPrices)
        except ValueError:
            op = [float(x) for x in objectPrices.split(',')]
        ret = safe_call(self.ctx().bsm_price, optionType, op, strikePrice, riskFree, sigma, days, dividend)
        self.write(json.dumps({"price": ret}, ensure_ascii=False, default=str))

# ContextInfo.bsm_iv() - BS模型计算欧式期权隐含波动率
class BsmIvHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        optionType = data.get('optionType', 'C')
        objectPrices = float(data.get('objectPrices', '0'))
        strikePrice = float(data.get('strikePrice', '0'))
        optionPrice = float(data.get('optionPrice', '0'))
        riskFree = float(data.get('riskFree', '0'))
        days = int(data.get('days', '0'))
        dividend = float(data.get('dividend', '0'))
        ret = safe_call(self.ctx().bsm_iv, optionType, objectPrices, strikePrice, optionPrice, riskFree, days, dividend)
        self.write(json.dumps({"iv": ret}, ensure_ascii=False))

# ContextInfo.get_local_data() - 从本地获取行情数据
class LocalDataHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        stock_code = data.get('stock_code', '')
        start_time = data.get('start_time', '')
        end_time = data.get('end_time', '')
        period = data.get('period', '1d')
        divid_type = data.get('divid_type', 'none')
        count = int(data.get('count', '-1'))
        ret = safe_call(self.ctx().get_local_data, stock_code, start_time, end_time, period, divid_type, count)
        if ret is None:
            raise HTTPError(500, "获取本地行情失败")
        self.write(json.dumps({"data": ret}, ensure_ascii=False, default=str))

# ContextInfo.subscribe_quote() - 订阅行情数据
class SubscribeQuoteHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        stock_code = data.get('stock_code', '')
        period = data.get('period', 'follow')
        dividend_type = data.get('dividend_type', 'follow')
        ret = safe_call(self.ctx().subscribe_quote, stock_code, period, dividend_type)
        self.write(json.dumps({"status": "success" if ret is not None else "failed", "sub_id": ret}, ensure_ascii=False))

# ContextInfo.unsubscribe_quote() - 反订阅行情数据
class UnsubscribeQuoteHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        sub_id = int(data.get('sub_id', '0'))
        safe_call(self.ctx().unsubscribe_quote, sub_id)
        self.write(json.dumps({"status": "success", "sub_id": sub_id}, ensure_ascii=False))


# ============= 3. 判定函数 (is_*) =============
# ContextInfo.is_last_bar() - 判定是否为最后一根K线
class IsLastBarHandler(BaseHandler):
    def get(self):
        ret = safe_call(self.ctx().is_last_bar)
        self.write(json.dumps({"is_last_bar": ret}, ensure_ascii=False))

# ContextInfo.is_new_bar() - 判定是否为新的K线
class IsNewBarHandler(BaseHandler):
    def get(self):
        ret = safe_call(self.ctx().is_new_bar)
        self.write(json.dumps({"is_new_bar": ret}, ensure_ascii=False))

# ContextInfo.is_suspended_stock() - 判定股票是否停牌
class IsSuspendedStockHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        stockcode = data.get('stockcode', '')
        ret = safe_call(self.ctx().is_suspended_stock, stockcode)
        self.write(json.dumps({"stockcode": stockcode, "is_suspended": ret}, ensure_ascii=False))

# is_sector_stock() - 判定股票是否在指定板块中
class IsSectorStockHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        sectorname = data.get('sectorname', '')
        market = data.get('market', '')
        stockcode = data.get('stockcode', '')
        ret = safe_call(is_sector_stock, sectorname, market, stockcode)
        self.write(json.dumps({"sectorname": sectorname, "stockcode": stockcode, "is_in_sector": ret}, ensure_ascii=False))

# is_typed_stock() - 判定股票是否属于某个类别
class IsTypedStockHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        stocktypenum = int(data.get('stocktypenum', '0'))
        market = data.get('market', '')
        stockcode = data.get('stockcode', '')
        ret = safe_call(is_typed_stock, stocktypenum, market, stockcode)
        self.write(json.dumps({"stocktypenum": stocktypenum, "stockcode": stockcode, "result": ret}, ensure_ascii=False))

# get_industry_name_of_stock() - 获取股票行业分类名称
class GetIndustryNameOfStockHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        industryType = data.get('industryType', '')
        stockcode = data.get('stockcode', '')
        ret = safe_call(get_industry_name_of_stock, industryType, stockcode)
        self.write(json.dumps({"industryType": industryType, "stockcode": stockcode, "industry_name": ret}, ensure_ascii=False))


# ============= 4. 交易函数 =============
# passorder() - 综合交易下单(支持股票买卖等)
class PassorderHandler(BaseHandler):
    def post(self):
        try:
            data = json.loads(self.request.body)
            opType = int(data['opType'])
            orderType = int(data.get('orderType', 1101))
            stock = data['stock']
            pr_type = int(data.get('prType', 11))
            price = float(data['price'])
            volume = int(data['volume'])
            quickTrade = int(data.get('quickTrade', 2))
            order_ref = passorder(opType, orderType, self.acc(), stock, pr_type, price, volume, 'qmt', quickTrade, self.ctx())
            self.write(json.dumps({
                "status": "success",
                "opType": opType,
                "stock": stock,
                "order_ref": str(order_ref) if order_ref else "unknown"
            }, ensure_ascii=False))
        except Exception as e:
            logger.exception("passorder下单异常")
            raise HTTPError(400, f"下单失败: {str(e)}")

# algo_passorder() - 算法交易下单
class AlgoPassorderHandler(BaseHandler):
    def post(self):
        try:
            data = json.loads(self.request.body)
            order_ref = algo_passorder(
                int(data['opType']), int(data.get('orderType', 1101)),
                self.acc(), data['stock'], int(data.get('prType', -1)),
                float(data['price']), int(data['volume']),
                data.get('strategyName', ''), int(data.get('quickTrade', 2)),
                data.get('userOrderId', ''), data.get('userOrderParam', {}),
                self.ctx()
            )
            self.write(json.dumps({"status": "success", "order_ref": str(order_ref) if order_ref else "unknown"}, ensure_ascii=False))
        except Exception as e:
            logger.exception("algo_passorder异常")
            raise HTTPError(400, f"算法下单失败: {str(e)}")

# smart_algo_passorder() - 智能算法交易下单
class SmartAlgoPassorderHandler(BaseHandler):
    def post(self):
        try:
            data = json.loads(self.request.body)
            order_ref = smart_algo_passorder(
                int(data['opType']), int(data.get('orderType', 1101)),
                self.acc(), data['stock'], int(data.get('prType', -1)),
                float(data['price']), int(data['volume']),
                data['smartAlgoType'], int(data.get('limitOverRate', 0)),
                int(data.get('minAmountPerOrder', 0)),
                data.get('startTime', ''), data.get('endTime', ''),
                self.ctx()
            )
            self.write(json.dumps({"status": "success", "order_ref": str(order_ref) if order_ref else "unknown"}, ensure_ascii=False))
        except Exception as e:
            logger.exception("smart_algo_passorder异常")
            raise HTTPError(400, f"智能算法下单失败: {str(e)}")

# order_lots() - 指定手数交易
class OrderLotsHandler(BaseHandler):
    def post(self):
        try:
            data = json.loads(self.request.body)
            order_lots(data['stock'], int(data['lots']), data.get('style', 'LATEST'),
                       float(data.get('price', 0)), self.ctx(), data.get('accId', self.acc()))
            self.write(json.dumps({"status": "success", "action": "order_lots", "stock": data['stock']}, ensure_ascii=False))
        except Exception as e:
            logger.exception("order_lots异常")
            raise HTTPError(400, f"下单失败: {str(e)}")

# order_value() - 指定价值交易
class OrderValueHandler(BaseHandler):
    def post(self):
        try:
            data = json.loads(self.request.body)
            order_value(data['stock'], float(data['value']), data.get('style', 'LATEST'),
                        float(data.get('price', 0)), self.ctx(), data.get('accId', self.acc()))
            self.write(json.dumps({"status": "success", "action": "order_value", "stock": data['stock']}, ensure_ascii=False))
        except Exception as e:
            logger.exception("order_value异常")
            raise HTTPError(400, f"下单失败: {str(e)}")

# order_percent() - 指定比例交易
class OrderPercentHandler(BaseHandler):
    def post(self):
        try:
            data = json.loads(self.request.body)
            order_percent(data['stock'], float(data['percent']), data.get('style', 'LATEST'),
                          float(data.get('price', 0)), self.ctx(), data.get('accId', self.acc()))
            self.write(json.dumps({"status": "success", "action": "order_percent", "stock": data['stock']}, ensure_ascii=False))
        except Exception as e:
            logger.exception("order_percent异常")
            raise HTTPError(400, f"下单失败: {str(e)}")

# order_target_value() - 指定目标价值交易
class OrderTargetValueHandler(BaseHandler):
    def post(self):
        try:
            data = json.loads(self.request.body)
            order_target_value(data['stock'], float(data['tar_value']), data.get('style', 'LATEST'),
                               float(data.get('price', 0)), self.ctx(), data.get('accId', self.acc()))
            self.write(json.dumps({"status": "success", "action": "order_target_value", "stock": data['stock']}, ensure_ascii=False))
        except Exception as e:
            logger.exception("order_target_value异常")
            raise HTTPError(400, f"下单失败: {str(e)}")

# order_target_percent() - 指定目标比例交易
class OrderTargetPercentHandler(BaseHandler):
    def post(self):
        try:
            data = json.loads(self.request.body)
            order_target_percent(data['stock'], float(data['tar_percent']), data.get('style', 'LATEST'),
                                 float(data.get('price', 0)), self.ctx(), data.get('accId', self.acc()))
            self.write(json.dumps({"status": "success", "action": "order_target_percent", "stock": data['stock']}, ensure_ascii=False))
        except Exception as e:
            logger.exception("order_target_percent异常")
            raise HTTPError(400, f"下单失败: {str(e)}")

# order_shares() - 指定股数交易
class OrderSharesHandler(BaseHandler):
    def post(self):
        try:
            data = json.loads(self.request.body)
            order_shares(data['stock'], int(data['shares']), data.get('style', 'LATEST'),
                         float(data.get('price', 0)), self.ctx(), data.get('accId', self.acc()))
            self.write(json.dumps({"status": "success", "action": "order_shares", "stock": data['stock']}, ensure_ascii=False))
        except Exception as e:
            logger.exception("order_shares异常")
            raise HTTPError(400, f"下单失败: {str(e)}")


# ============= 5. 期货交易 =============
# buy_open() - 期货买入开仓
class FuturesBuyOpenHandler(BaseHandler):
    def post(self):
        try:
            data = json.loads(self.request.body)
            buy_open(data['stock'], int(data['amount']), data.get('style', 'LATEST'),
                     float(data.get('price', 0)), self.ctx(), data.get('accId', self.acc()))
            self.write(json.dumps({"status": "success", "action": "buy_open", "stock": data['stock']}, ensure_ascii=False))
        except Exception as e:
            logger.exception("buy_open异常")
            raise HTTPError(400, f"期货买入开仓失败: {str(e)}")

# buy_close_tdayfirst() - 期货买入平仓(平今优先)
class FuturesBuyCloseTdayFirstHandler(BaseHandler):
    def post(self):
        try:
            data = json.loads(self.request.body)
            buy_close_tdayfirst(data['stock'], int(data['amount']), data.get('style', 'LATEST'),
                                float(data.get('price', 0)), self.ctx(), data.get('accId', self.acc()))
            self.write(json.dumps({"status": "success", "action": "buy_close_tdayfirst", "stock": data['stock']}, ensure_ascii=False))
        except Exception as e:
            logger.exception("buy_close_tdayfirst异常")
            raise HTTPError(400, f"期货买入平仓(平今)失败: {str(e)}")

# buy_close_ydayfirst() - 期货买入平仓(平昨优先)
class FuturesBuyCloseYdayFirstHandler(BaseHandler):
    def post(self):
        try:
            data = json.loads(self.request.body)
            buy_close_ydayfirst(data['stock'], int(data['amount']), data.get('style', 'LATEST'),
                                float(data.get('price', 0)), self.ctx(), data.get('accId', self.acc()))
            self.write(json.dumps({"status": "success", "action": "buy_close_ydayfirst", "stock": data['stock']}, ensure_ascii=False))
        except Exception as e:
            logger.exception("buy_close_ydayfirst异常")
            raise HTTPError(400, f"期货买入平仓(平昨)失败: {str(e)}")

# sell_open() - 期货卖出开仓
class FuturesSellOpenHandler(BaseHandler):
    def post(self):
        try:
            data = json.loads(self.request.body)
            sell_open(data['stock'], int(data['amount']), data.get('style', 'LATEST'),
                      float(data.get('price', 0)), self.ctx(), data.get('accId', self.acc()))
            self.write(json.dumps({"status": "success", "action": "sell_open", "stock": data['stock']}, ensure_ascii=False))
        except Exception as e:
            logger.exception("sell_open异常")
            raise HTTPError(400, f"期货卖出开仓失败: {str(e)}")

# sell_close_tdayfirst() - 期货卖出平仓(平今优先)
class FuturesSellCloseTdayFirstHandler(BaseHandler):
    def post(self):
        try:
            data = json.loads(self.request.body)
            sell_close_tdayfirst(data['stock'], int(data['amount']), data.get('style', 'LATEST'),
                                 float(data.get('price', 0)), self.ctx(), data.get('accId', self.acc()))
            self.write(json.dumps({"status": "success", "action": "sell_close_tdayfirst", "stock": data['stock']}, ensure_ascii=False))
        except Exception as e:
            logger.exception("sell_close_tdayfirst异常")
            raise HTTPError(400, f"期货卖出平仓(平今)失败: {str(e)}")

# sell_close_ydayfirst() - 期货卖出平仓(平昨优先)
class FuturesSellCloseYdayFirstHandler(BaseHandler):
    def post(self):
        try:
            data = json.loads(self.request.body)
            sell_close_ydayfirst(data['stock'], int(data['amount']), data.get('style', 'LATEST'),
                                 float(data.get('price', 0)), self.ctx(), data.get('accId', self.acc()))
            self.write(json.dumps({"status": "success", "action": "sell_close_ydayfirst", "stock": data['stock']}, ensure_ascii=False))
        except Exception as e:
            logger.exception("sell_close_ydayfirst异常")
            raise HTTPError(400, f"期货卖出平仓(平昨)失败: {str(e)}")


# ============= 6. 任务管理 =============
# cancel_task() - 撤销任务
class CancelTaskHandler(BaseHandler):
    def post(self):
        try:
            data = json.loads(self.request.body)
            taskId = data['taskId']
            accountType = data.get('accountType', 'stock')
            ret = cancel_task(taskId, self.acc(), accountType, self.ctx())
            self.write(json.dumps({"status": "success" if ret else "failed", "taskId": taskId}, ensure_ascii=False))
        except Exception as e:
            logger.exception("cancel_task异常")
            raise HTTPError(400, f"撤销任务失败: {str(e)}")

# pause_task() - 暂停任务
class PauseTaskHandler(BaseHandler):
    def post(self):
        try:
            data = json.loads(self.request.body)
            taskId = data['taskId']
            accountType = data.get('accountType', 'stock')
            ret = pause_task(taskId, self.acc(), accountType, self.ctx())
            self.write(json.dumps({"status": "success" if ret else "failed", "taskId": taskId}, ensure_ascii=False))
        except Exception as e:
            logger.exception("pause_task异常")
            raise HTTPError(400, f"暂停任务失败: {str(e)}")

# resume_task() - 继续任务
class ResumeTaskHandler(BaseHandler):
    def post(self):
        try:
            data = json.loads(self.request.body)
            taskId = data['taskId']
            accountType = data.get('accountType', 'stock')
            ret = resume_task(taskId, self.acc(), accountType, self.ctx())
            self.write(json.dumps({"status": "success" if ret else "failed", "taskId": taskId}, ensure_ascii=False))
        except Exception as e:
            logger.exception("resume_task异常")
            raise HTTPError(400, f"继续任务失败: {str(e)}")

# do_order() - 实时触发前一根bar信号函数
class DoOrderHandler(BaseHandler):
    def post(self):
        try:
            do_order(self.ctx())
            self.write(json.dumps({"status": "success", "message": "信号已触发"}, ensure_ascii=False))
        except Exception as e:
            logger.exception("do_order异常")
            raise HTTPError(400, f"触发信号失败: {str(e)}")


# ============= 7. 账户/订单查询 =============
# get_trade_detail_data() - 获取交易明细(持仓/委托/成交/资金)
# 2026-07-08: 去掉第 4 参 strategyName='qmt' 过滤 — 带过滤只能查到本策略 API 下的单,
# 手动在 QMT 界面挂的委托/成交会被滤掉(查出来是空), 改为账户级全量视图.
class TradeDetailDataHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        account = data.get('account', 'stock')
        datatype = data.get('datatype', 'position')
        ret = safe_call(get_trade_detail_data, self.acc(), account, datatype)
        if ret is None:
            ret = []
        # 2026-07-08: dir() 逐对象反射改为 export_attrs (按类缓存), 大账户提速一个量级
        result = [export_attrs(obj) for obj in ret]
        self.write(json.dumps({"data": result}, ensure_ascii=False))

# get_value_by_order_id() - 根据委托号获取委托/成交信息
class ValueByOrderIdHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        orderId = data.get('orderId', '')
        accountType = data.get('accountType', 'stock')
        datatype = data.get('datatype', 'ORDER')
        ret = safe_call(get_value_by_order_id, orderId, self.acc(), accountType, datatype)
        attrs = export_attrs(ret) if ret else {}
        self.write(json.dumps({"orderId": orderId, "data": attrs}, ensure_ascii=False))

# get_last_order_id() - 获取最新委托/成交的委托号
# 注意: 这里**保留** strategyName='qmt' 过滤 — 语义是"本策略 API 最近一笔委托号",
# 用于下单后回填 order_id. 若去掉过滤, 用户同时在 QMT 界面手动下单会拿到别人的委托号.
class LastOrderIdHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        account = data.get('account', 'stock')
        datatype = data.get('datatype', 'ORDER')
        ret = safe_call(get_last_order_id, self.acc(), account, datatype, 'qmt')
        self.write(json.dumps({"last_order_id": ret}, ensure_ascii=False))

# can_cancel_order() - 查询委托是否可撤销
class CanCancelOrderHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        orderId = data.get('orderId', '')
        accountType = data.get('accountType', 'stock')
        ret = safe_call(can_cancel_order, orderId, self.acc(), accountType)
        self.write(json.dumps({"orderId": orderId, "can_cancel": ret}, ensure_ascii=False))

# get_debt_contract() - 获取两融负债合约明细
class DebtContractHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        accId = data.get('accId', self.acc())
        ret = safe_call(get_debt_contract, accId)
        result = [export_attrs(obj) for obj in (ret or [])]
        self.write(json.dumps({"data": result}, ensure_ascii=False))

# get_assure_contract() - 获取两融担保标的明细
class AssureContractHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        accId = data.get('accId', self.acc())
        ret = safe_call(get_assure_contract, accId)
        result = [export_attrs(obj) for obj in (ret or [])]
        self.write(json.dumps({"data": result}, ensure_ascii=False))

# get_enable_short_contract() - 获取可融券明细
class EnableShortContractHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        accId = data.get('accId', self.acc())
        ret = safe_call(get_enable_short_contract, accId)
        result = [export_attrs(obj) for obj in (ret or [])]
        self.write(json.dumps({"data": result}, ensure_ascii=False))

# get_ipo_data() - 获取当日新股新债信息
class IpoDataHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        typ = data.get('type', '')
        ret = safe_call(get_ipo_data, typ)
        self.write(json.dumps({"data": ret or {}}, ensure_ascii=False, default=str))

# get_new_purchase_limit() - 获取新股申购额度
class NewPurchaseLimitHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        accid = data.get('accid', self.acc())
        ret = safe_call(get_new_purchase_limit, accid)
        self.write(json.dumps({"data": ret or {}}, ensure_ascii=False, default=str))


# ============= 8. 引用函数 (ext_data) =============
# ext_data() - 获取扩展数据数值
class ExtDataHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        extdataname = data.get('extdataname', '')
        stockcode = data.get('stockcode', '')
        deviation = int(data.get('deviation', '0'))
        ret = safe_call(ext_data, extdataname, stockcode, deviation, self.ctx())
        self.write(json.dumps({"extdataname": extdataname, "stockcode": stockcode, "value": ret}, ensure_ascii=False))

# ext_data_rank() - 获取扩展数据排名
class ExtDataRankHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        extdataname = data.get('extdataname', '')
        stockcode = data.get('stockcode', '')
        deviation = int(data.get('deviation', '0'))
        ret = safe_call(ext_data_rank, extdataname, stockcode, deviation, self.ctx())
        self.write(json.dumps({"extdataname": extdataname, "stockcode": stockcode, "rank": ret}, ensure_ascii=False))

# get_factor_value() - 获取因子数据
class GetFactorValueHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        factorname = data.get('factorname', '')
        stockcode = data.get('stockcode', '')
        deviation = int(data.get('deviation', '0'))
        ret = safe_call(get_factor_value, factorname, stockcode, deviation, self.ctx())
        self.write(json.dumps({"factorname": factorname, "stockcode": stockcode, "value": ret}, ensure_ascii=False))

# get_factor_rank() - 获取因子数据排名
class GetFactorRankHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        factorname = data.get('factorname', '')
        stockcode = data.get('stockcode', '')
        deviation = int(data.get('deviation', '0'))
        ret = safe_call(get_factor_rank, factorname, stockcode, deviation, self.ctx())
        self.write(json.dumps({"factorname": factorname, "stockcode": stockcode, "rank": ret}, ensure_ascii=False))


# ============= 9. 原有 Handler（保持兼容） =============
# get_trade_detail_data('position') - 查询持仓列表(封装格式)
class HoldingHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        account = data.get('account', 'stock')
        positions = safe_call(get_trade_detail_data, self.acc(), account, 'position') or []
        holding = {}
        for position in positions:
            stock = position.m_strInstrumentID + '.' + position.m_strExchangeID
            holding[stock] = {
                'StockCode': stock,
                'StockName': position.m_strInstrumentName,
                'Direction': position.m_nDirection,
                'Volume': position.m_nVolume,
                'OpenPrice': _safe_float(position.m_dOpenPrice),
                'FloatProfit': _safe_float(position.m_dFloatProfit),
                'MarketValue': _safe_float(position.m_dMarketValue),
                'StockHolder': position.m_strStockHolder,
                'FrozenVolume': position.m_nFrozenVolume,
                'CanUseVolume': position.m_nCanUseVolume,
                'OnRoadVolume': position.m_nOnRoadVolume,
                'YesterdayVolume': position.m_nYesterdayVolume,
                'LastPrice': _safe_float(position.m_dLastPrice),
                'ProfitRate': _safe_float(position.m_dProfitRate),
                'FutureTradeType': position.m_eFutureTradeType,
                'ExpireDate': position.m_strExpireDate
            }
        self.write(json.dumps(holding, ensure_ascii=False))

# get_trade_detail_data('account') - 查询总资产
# 2026-07-08: 查空时把 账号+类型 写进错误信息 — "资金数据获取失败"这种笼统 500 定位不了问题.
#
# QMT 的 get_trade_detail_data(accountID, strAccountType, datatype) 里, 资金账号和账户类型
# (stock / credit) 是**两个独立参数**: 同一个资金账号下可以同时挂普通账户和信用账户,
# 按类型分别查. 所以"按 credit 查不到"只说明这个账号没开两融权限(或该类型没在 QMT 登录),
# **不代表两融是另一个账号** — 各家券商实现不同, 别把某一家的做法写死成通则.
#
# 查空的三个常见原因:
#   1) 该资金账号没开通对应类型 (stock / credit) 的权限
#   2) 该账号 (或该类型) 没在本 QMT 客户端登录
#   3) 响应请求的是先前运行的旧策略实例 (端口被占, 见 init 日志)
class TotalMoneyHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        account = data.get('account', 'stock')
        _data = safe_call(get_trade_detail_data, self.acc(), account, 'account')
        info = _data[0] if _data else None
        if not info:
            raise HTTPError(500, f"资金数据获取失败: 账号 {self.acc()} 按类型 '{account}' 查不到资金数据, "
                                 f"请确认该账号已开通对应类型的权限且已在本 QMT 登录")
        self.write(json.dumps({"total_money": round(info.m_dBalance, 2)}, ensure_ascii=False))

# get_trade_detail_data('account') - 查询可用资金
class AvailableMoneyHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        account = data.get('account', 'stock')
        _data = safe_call(get_trade_detail_data, self.acc(), account, 'account')
        info = _data[0] if _data else None
        if not info:
            raise HTTPError(500, f"资金数据获取失败: 账号 {self.acc()} 按类型 '{account}' 查不到资金数据, "
                                 f"请确认该账号已开通对应类型的权限且已在本 QMT 登录")
        self.write(json.dumps({"available_money": round(info.m_dAvailable, 2)}, ensure_ascii=False))

# passorder(23/33) - 简化买入下单(封装passorder)
# 2026-07-08: 支持信用账户 — account='credit' 时 opType 用 33(担保品买入), 等同普通现金买入不加杠杆;
# 融资买入(27)等杠杆操作不开放. 普通账户仍走 23.
class BuyHandler(BaseHandler):
    def post(self):
        try:
            data = json.loads(self.request.body)
            stock = data['stock']
            price = float(data['price'])
            volume = int(data['volume'])
            pr_type = data.get('prType', 11)
            account = data.get('account', 'stock')
            op_type = 33 if account == 'credit' else 23
            order_ref = passorder(op_type, 1101, self.acc(), stock, pr_type, price, volume, 'qmt', 2, self.ctx())
            self.write(json.dumps({
                "status": "success", "action": "buy", "stock": stock,
                "order_ref": str(order_ref) if order_ref else "unknown"
            }, ensure_ascii=False))
        except Exception as e:
            logger.exception("买入下单异常")
            raise HTTPError(400, f"下单失败: {str(e)}")

# passorder(24/34) - 简化卖出下单(封装passorder)
# 2026-07-08: 支持信用账户 — account='credit' 时 opType 用 34(担保品卖出); 普通账户仍走 24.
class SellHandler(BaseHandler):
    def post(self):
        try:
            data = json.loads(self.request.body)
            stock = data['stock']
            price = float(data['price'])
            volume = int(data['volume'])
            pr_type = data.get('prType', 11)
            account = data.get('account', 'stock')
            op_type = 34 if account == 'credit' else 24
            order_ref = passorder(op_type, 1101, self.acc(), stock, pr_type, price, volume, 'qmt', 2, self.ctx())
            self.write(json.dumps({
                "status": "success", "action": "sell", "stock": stock,
                "order_ref": str(order_ref) if order_ref else "unknown"
            }, ensure_ascii=False))
        except Exception as e:
            logger.exception("卖出下单异常")
            raise HTTPError(400, f"下单失败: {str(e)}")

# get_trade_detail_data('order') - 查询委托状态列表
# 2026-07-08: 去掉 strategyName='qmt' 过滤, 手动挂的单也要能查到
class OrderStatusHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        account = data.get('account', 'stock')
        orders = safe_call(get_trade_detail_data, self.acc(), account, 'order') or []
        rets = []
        for order in orders:
            rets.append({
                "order_sys_id": order.m_strOrderSysID,
                "status": order.m_nOrderStatus,
                "volume_left": order.m_nVolumeTotal,
                "volume_traded": order.m_nVolumeTraded,
            })
        self.write(json.dumps({"orders": rets}, ensure_ascii=False))

# cancel() - 全部撤单
# 2026-07-08: 去掉 strategyName='qmt' 过滤 — "全部撤单"语义 = 撤掉账户所有可撤委托(含手动单)
class CancelAllHandler(BaseHandler):
    def post(self):
        try:
            data = json.loads(self.request.body)
            account = data.get('account', 'stock')
            orders = safe_call(get_trade_detail_data, self.acc(), account, 'order') or []
            canceled_list = []
            for order in orders:
                if can_cancel_order(order.m_strOrderSysID, self.acc(), account):
                    cancel(order.m_strOrderSysID, self.acc(), account, self.ctx())
                    canceled_list.append({
                        "order_sys_id": order.m_strOrderSysID,
                        "stock": order.m_strInstrumentID,
                        "volume_left": order.m_nVolumeTotal
                    })
            self.write(json.dumps({
                "status": "success",
                "message": f"已发出 {len(canceled_list)} 笔撤单请求",
                "canceled_orders": canceled_list
            }, ensure_ascii=False))
        except Exception as e:
            logger.exception("全部撤单异常")
            raise HTTPError(500, f"撤单失败: {str(e)}")


class CancelByRuleHandler(BaseHandler):
    def post(self):
        try:
            data = json.loads(self.request.body)
            stock = data.get('stock')
            cancel_volume = int(data.get('volume', 0))
            account = data.get('account', 'stock')
            if not stock or cancel_volume <= 0:
                raise HTTPError(400, "参数错误：必须提供 stock 且 volume > 0")
            # 2026-07-08: 去掉 strategyName='qmt' 过滤, 手动挂的单也能按 股票+数量 匹配撤
            orders = safe_call(get_trade_detail_data, self.acc(), account, 'order') or []
            target_orders = []
            for order in orders:
                order_code = f"{order.m_strInstrumentID}.{order.m_strExchangeID}"
                if order.m_nVolumeTotal + order.m_nVolumeTraded == cancel_volume and order_code == stock and can_cancel_order(order.m_strOrderSysID, self.acc(), account):
                    target_orders.append(order)
            if not target_orders:
                self.write(json.dumps({"status": "failed", "message": "未找到符合条件的活跃订单"}, ensure_ascii=False))
                return
            canceled_ids = []
            for t_order in target_orders:
                cancel(t_order.m_strOrderSysID, self.acc(), account, self.ctx())
                canceled_ids.append(t_order.m_strOrderSysID)
            self.write(json.dumps({
                "status": "success",
                "message": f"匹配到 {len(target_orders)} 笔订单并发出撤单请求",
                "canceled_sys_ids": canceled_ids
            }, ensure_ascii=False))
        except Exception as e:
            logger.exception("规则撤单异常")
            raise HTTPError(500, f"撤单失败: {str(e)}")

# cancel() - 按股票+数量匹配规则撤单

# cancel(order_sys_id) - 按委托编号撤单（新增端点，供 QMT HTTP 后端使用，
#                         对应 xtquant 的 cancel_order_stock(account, order_id)）
class CancelByIdHandler(BaseHandler):
    def post(self):
        try:
            data = json.loads(self.request.body)
            order_id = data.get('orderId', '')
            account = data.get('account', 'stock')
            if not order_id:
                raise HTTPError(400, "need args orderId")
            # 2026-07-08: 去掉 strategyName='qmt' 过滤, 手动挂的单也能按委托号撤
            orders = safe_call(get_trade_detail_data, self.acc(), account, 'order') or []
            for order in orders:
                # 匹配交易所委托号(m_strOrderSysID)，确保只撤指定那一笔（不会误撤同名同量单）
                if order.m_strOrderSysID == order_id and can_cancel_order(order.m_strOrderSysID, self.acc(), account):
                    cancel(order.m_strOrderSysID, self.acc(), account, self.ctx())
                    self.write(json.dumps({"status": "success", "order_sys_id": order_id}, ensure_ascii=False))
                    return
            raise HTTPError(404, f"未找到可撤的委托: {order_id}")
        except HTTPError:
            raise
        except Exception as e:
            logger.exception("按ID撤单异常")
            raise HTTPError(500, f"撤单失败: {str(e)}")

# sys: Python版本信息
class PythonVersionHandler(BaseHandler):
    def get(self):
        import sys
        version_info = {
            "python_version": sys.version,
            "python_version_info": {
                "major": sys.version_info.major,
                "minor": sys.version_info.minor,
                "micro": sys.version_info.micro,
                "releaselevel": sys.version_info.releaselevel,
                "serial": sys.version_info.serial,
            }
        }
        self.write(json.dumps(version_info, ensure_ascii=False))

# sys: 关闭HTTP服务
class ShutdownHandler(BaseHandler):
    def post(self):
        self.write(json.dumps({"status": "success", "message": "服务器正在关闭..."}, ensure_ascii=False))
        self.finish()
        server = getattr(self.application, 'http_server', None)
        loop = IOLoop.current()
        def _stop():
            if server:
                server.stop()   # 关闭监听 socket，释放端口
            loop.stop()
        loop.add_callback(_stop)

# get_trade_detail_data('deal') - 查询成交明细
# 2026-07-08: 去掉 strategyName='qmt' 过滤, 手动成交也要能查到
class DealHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        account = data.get('account', 'stock')
        deals = safe_call(get_trade_detail_data, self.acc(), account, 'deal') or []
        rets = [export_attrs(deal) for deal in deals]
        self.write(json.dumps({"deals": rets}, ensure_ascii=False))


# ============= Bridge-only refresh contracts =============
class XtdataDownloadSectorHandler(BaseHandler):
    def post(self):
        try:
            from xtquant import xtdata
            ret = safe_call(xtdata.download_sector_data)
        except ImportError:
            raise HTTPError(501, "QMT环境缺少xtquant包")
        self.write(json.dumps({"status": "success"}, ensure_ascii=False))


class XtdataDownloadEtfInfoHandler(BaseHandler):
    def post(self):
        try:
            from xtquant import xtdata
            ret = safe_call(xtdata.download_etf_info)
        except ImportError:
            raise HTTPError(501, "QMT环境缺少xtquant包")
        self.write(json.dumps({"status": "success"}, ensure_ascii=False))


class XtdataEtfInfoHandler(BaseHandler):
    def post(self):
        try:
            from xtquant import xtdata
            raw = safe_call(xtdata.get_etf_info)
        except ImportError:
            raise HTTPError(501, "QMT环境缺少xtquant包")
        if raw is None:
            raise HTTPError(500, "ETF数据读取失败")
        self.write(json.dumps({"data": raw}, ensure_ascii=False, default=str))


# ============= 路由注册 =============
def make_app():
    return Application([

        # 原有兼容路由
        (r"/api/holding", HoldingHandler),
        (r"/api/money/total", TotalMoneyHandler),
        (r"/api/money/available", AvailableMoneyHandler),
        (r"/api/order/buy", BuyHandler),
        (r"/api/order/sell", SellHandler),
        (r"/api/order/status", OrderStatusHandler),
        (r"/api/order/cancel_all", CancelAllHandler),
        (r"/api/order/cancel_order", CancelByRuleHandler),
        (r"/api/order/cancel_by_id", CancelByIdHandler),
        (r"/api/order/deal", DealHandler),

        # ContextInfo 属性
        (r"/api/context/period", ContextPeriodHandler),
        (r"/api/context/barpos", ContextBarposHandler),
        (r"/api/context/time_tick_size", ContextTimeTickSizeHandler),
        (r"/api/context/stockcode", ContextStockCodeHandler),
        (r"/api/context/dividend_type", ContextDividendTypeHandler),
        (r"/api/context/market", ContextMarketHandler),
        (r"/api/context/do_back_test", ContextDoBackTestHandler),
        (r"/api/context/benchmark", ContextBenchmarkHandler),
        (r"/api/context/capital", ContextCapitalHandler),
        (r"/api/context/universe", ContextUniverseHandler),

        # 数据查询
        (r"/api/data/stock_name", StockNameHandler),
        (r"/api/data/open_date", OpenDateHandler),
        (r"/api/data/last_volume", LastVolumeHandler),
        (r"/api/data/bar_timetag", BarTimetagHandler),
        (r"/api/data/tick_timetag", TickTimetagHandler),
        (r"/api/data/sector", SectorHandler),
        (r"/api/data/industry", IndustryHandler),
        (r"/api/data/stock_list_in_sector", StockListInSectorHandler),
        (r"/api/data/weight_in_index", WeightInIndexHandler),
        (r"/api/data/contract_multiplier", ContractMultiplierHandler),
        (r"/api/data/risk_free_rate", RiskFreeRateHandler),
        (r"/api/data/date_location", DateLocationHandler),
        (r"/api/data/history_data", HistoryDataHandler),
        (r"/api/data/market_data", MarketDataHandler),
        (r"/api/data/market_data_ex", MarketDataExHandler),
        (r"/api/data/full_tick", FullTickHandler),
        (r"/api/data/divid_factors", DividFactorsHandler),
        (r"/api/data/main_contract", MainContractHandler),
        (r"/api/data/timetag_to_datetime", TimetagToDatetimeHandler),
        (r"/api/data/total_share", TotalShareHandler),
        (r"/api/data/trading_dates", TradingDatesHandler),
        (r"/api/data/svol", SvolHandler),
        (r"/api/data/bvol", BvolHandler),
        (r"/api/data/longhubang", LonghubangHandler),
        (r"/api/data/top10_share_holder", Top10ShareHolderHandler),
        (r"/api/data/option_detail", OptionDetailHandler),
        (r"/api/data/turnover_rate", TurnoverRateHandler),
        (r"/api/data/etf_info", EtfInfoHandler),
        (r"/api/data/etf_iopv", EtfIopvHandler),
        (r"/api/data/instrumentdetail", InstrumentDetailHandler),
        (r"/api/data/contract_expire_date", ContractExpireDateHandler),
        (r"/api/data/option_undl_data", OptionUndlDataHandler),
        (r"/api/data/financial_data", FinancialDataHandler),
        (r"/api/xtdata/financial_data", XtdataFinancialDataHandler),
        (r"/api/xtdata/download_financial_data", XtdataDownloadFinancialHandler),
        (r"/api/xtdata/sector_list", XtdataSectorListHandler),
        (r"/api/xtdata/instrument_detail", XtdataInstrumentDetailHandler),
        (r"/api/xtdata/market_data_ex", XtdataMarketDataExHandler),
        (r"/api/xtdata/download_history_data", XtdataDownloadHistoryHandler),
        (r"/api/xtdata/stock_list_in_sector", XtdataStockListInSectorHandler),
        (r"/api/xtdata/download_sector_data", XtdataDownloadSectorHandler),
        (r"/api/xtdata/download_etf_info", XtdataDownloadEtfInfoHandler),
        (r"/api/xtdata/etf_info", XtdataEtfInfoHandler),
        (r"/api/xtdata/trading_dates", XtdataTradingDatesHandler),
        (r"/api/xtdata/divid_factors", XtdataDividFactorsHandler),
        (r"/api/xtdata/index_weight", XtdataIndexWeightHandler),
        (r"/api/data/factor_data", FactorDataHandler),
        (r"/api/data/his_st_data", HisStDataHandler),
        (r"/api/data/his_index_data", HisIndexDataHandler),
        (r"/api/data/all_subscription", AllSubscriptionHandler),
        (r"/api/data/option_list", OptionListHandler),
        (r"/api/data/his_contract_list", HisContractListHandler),
        (r"/api/data/option_iv", OptionIvHandler),
        (r"/api/data/bsm_price", BsmPriceHandler),
        (r"/api/data/bsm_iv", BsmIvHandler),
        (r"/api/data/local_data", LocalDataHandler),

        # 订阅
        (r"/api/data/subscribe_quote", SubscribeQuoteHandler),
        (r"/api/data/unsubscribe_quote", UnsubscribeQuoteHandler),

        # 判定函数
        (r"/api/check/is_last_bar", IsLastBarHandler),
        (r"/api/check/is_new_bar", IsNewBarHandler),
        (r"/api/check/is_suspended_stock", IsSuspendedStockHandler),
        (r"/api/check/is_sector_stock", IsSectorStockHandler),
        (r"/api/check/is_typed_stock", IsTypedStockHandler),
        (r"/api/check/get_industry_name_of_stock", GetIndustryNameOfStockHandler),

        # 交易
        (r"/api/trade/passorder", PassorderHandler),
        (r"/api/trade/algo_passorder", AlgoPassorderHandler),
        (r"/api/trade/smart_algo_passorder", SmartAlgoPassorderHandler),
        (r"/api/trade/order_lots", OrderLotsHandler),
        (r"/api/trade/order_value", OrderValueHandler),
        (r"/api/trade/order_percent", OrderPercentHandler),
        (r"/api/trade/order_target_value", OrderTargetValueHandler),
        (r"/api/trade/order_target_percent", OrderTargetPercentHandler),
        (r"/api/trade/order_shares", OrderSharesHandler),

        # 期货交易
        (r"/api/trade/futures/buy_open", FuturesBuyOpenHandler),
        (r"/api/trade/futures/buy_close_tdayfirst", FuturesBuyCloseTdayFirstHandler),
        (r"/api/trade/futures/buy_close_ydayfirst", FuturesBuyCloseYdayFirstHandler),
        (r"/api/trade/futures/sell_open", FuturesSellOpenHandler),
        (r"/api/trade/futures/sell_close_tdayfirst", FuturesSellCloseTdayFirstHandler),
        (r"/api/trade/futures/sell_close_ydayfirst", FuturesSellCloseYdayFirstHandler),

        # 任务管理
        (r"/api/trade/cancel_task", CancelTaskHandler),
        (r"/api/trade/pause_task", PauseTaskHandler),
        (r"/api/trade/resume_task", ResumeTaskHandler),
        (r"/api/trade/do_order", DoOrderHandler),

        # 账户/订单查询
        (r"/api/trade/trade_detail_data", TradeDetailDataHandler),
        (r"/api/trade/value_by_order_id", ValueByOrderIdHandler),
        (r"/api/trade/last_order_id", LastOrderIdHandler),
        (r"/api/trade/can_cancel_order", CanCancelOrderHandler),
        (r"/api/trade/debt_contract", DebtContractHandler),
        (r"/api/trade/assure_contract", AssureContractHandler),
        (r"/api/trade/enable_short_contract", EnableShortContractHandler),
        (r"/api/trade/ipo_data", IpoDataHandler),
        (r"/api/trade/new_purchase_limit", NewPurchaseLimitHandler),

        # 引用函数
        (r"/api/ext/ext_data", ExtDataHandler),
        (r"/api/ext/ext_data_rank", ExtDataRankHandler),
        (r"/api/ext/get_factor_value", GetFactorValueHandler),
        (r"/api/ext/get_factor_rank", GetFactorRankHandler),

        # 系统
        (r"/api/sys/python_version", PythonVersionHandler),
        (r"/api/sys/shutdown", ShutdownHandler),

    ], debug=False)


import os
import datetime
import socket as _socket
import traceback

LOG_FILE = os.path.join(os.getcwd(), "qmt_http_server.log")  # 落在 bin.x64 目录下


def _port_in_use(port):
    with _socket.socket(_socket.AF_INET, _socket.SOCK_STREAM) as s:
        return s.connect_ex(('127.0.0.1', port)) == 0


def _flog(msg):
    """文件日志:pump在定时器回调中执行,print不一定进QMT日志面板,异常记录靠这个"""
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            ts = datetime.datetime.now().strftime('%H:%M:%S.%f')[:-3]
            f.write(f"[{ts}] {msg}\n")
    except Exception:
        pass


_loop = None        # asyncio 事件循环,模块级引用,供定时器使用


def init(ContextInfo):
    global _loop
    print("===== init 开始执行 =====")
    ContextInfo.accountID = ACCOUNT_ID
    if _port_in_use(PORT):
        # 2026-07-08: 这条日志出现 = 本实例根本没启动 HTTP 服务, 正在响应请求的是
        # **先前运行的那个策略实例** (用的是它那份代码里的 ACCOUNT_ID). QMT 里停止
        # 策略不一定释放端口. 切换账号 / 更新过代码之后看到这条, 必须整个重启 QMT,
        # 再只运行一行策略.
        print(f"端口 {PORT} 已被占用: 正在响应请求的是先前启动的实例(绑定旧 ACCOUNT_ID), "
              f"本实例跳过启动. 如刚切换账号/更新代码, 请完全重启 QMT 后只运行本策略")
        return
    try:
        import asyncio, time
        _loop = asyncio.new_event_loop()
        asyncio.set_event_loop(_loop)
        app = make_app()
        app.ContextInfo = ContextInfo
        app.accountID = ACCOUNT_ID
        server = app.listen(PORT, address='127.0.0.1')
        app.http_server = server
        # ACCOUNT_ID 打进启动日志: 学员一眼核对"服务实际绑的账号"是不是自己以为的那个
        print(f"===== HTTP Server 已启动: 127.0.0.1:{PORT}, ACCOUNT_ID={ACCOUNT_ID}, 进入常驻泵 =====")
        while True:                        # 永不返回,持续泵
            _loop.call_soon(_loop.stop)
            _loop.run_forever()
            time.sleep(0.05)
    except Exception:
        print("HTTP服务启动失败:")
        print(traceback.format_exc())

def handlebar(ContextInfo):
    pass
