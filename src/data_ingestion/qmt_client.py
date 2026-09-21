# -*- coding: utf-8 -*-
# Author：@跟陈博士学AI
import json
import requests

TOKEN = "lucienleung49"

class QMTClient:
    def __init__(self, base_url="http://127.0.0.1:15588"):
        self.base = base_url
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json; charset=utf-8"})
        self.session.headers.update({"X-Token": TOKEN})

    def _req(self, method, path, timeout=10, **kwargs):
        url = f"{self.base}{path}"
        try:
            resp = self.session.request(method, url, timeout=timeout, **kwargs)
            resp.raise_for_status()
            # stdlib json 默认接受 NaN/Infinity(财报/instrument_detail 缺失值会输出裸 NaN)
            return json.loads(resp.text)
        except requests.RequestException as e:
            return {"error": str(e), "status_code": getattr(e.response, 'status_code', 500)}

    def get_holding(self, account='stock'):
        return self._req('POST', f'/api/holding', json={"account": account})

    def get_total_money(self, account='stock'):
        return self._req('POST', f'/api/money/total', json={"account": account})

    def get_available_money(self, account='stock'):
        return self._req('POST', f'/api/money/available', json={"account": account})

    def buy_stock(self, stock, price, volume, pr_type=11):
        """
        prType(下单选价类型):（特别的对于套利：这个prType只对篮子起作用,期货的采用默认的方式）
        -1:无效(只对于algo_passorder起作用)
        0:卖5价
        1:卖4价
        2:卖3价
        3:卖2价
        4:卖1价
        5:最新价
        6:买1价
        7:买2价(组合不支持)
        8:买3价(组合不支持)
        9:买4价(组合不支持)
        10:买5价(组合不支持)
        11:（指定价）模型价（只对单股情况支持,对组合交易不支持）
        12:涨跌停价
        13:挂单价
        14:对手价
        18:市价最优价[郑商所][期货]
        19:市价即成剩撤[大商所][期货]
        20:市价全额成交或撤[大商所][期货]
        21:市价最优一档即成剩撤[中金所][期货]
        22:市价最优五档即成剩撤[中金所][期货]
        23:市价最优一档即成剩转[中金所][期货]
        24:市价最优五档即成剩转[中金所][期货]
        26:限价即时全部成交否则撤单[上交所|深交所][期权]
        27:市价即成剩撤[上交所][期权]
        28:市价即全成否则撤[上交所][期权]
        29:市价剩转限价[上交所][期权]
        42:最优五档即时成交剩余撤销申报[上交所][股票]
        43:最优五档即时成交剩转限价申报[上交所][股票]
        44:对手方最优价格委托[上交所[股票]][深交所[股票][期权]]
        45:本方最优价格委托[上交所[股票]][深交所[股票][期权]]
        46:即时成交剩余撤销委托[深交所][股票][期权]
        47:最优五档即时成交剩余撤销委托[深交所][股票][期权]
        48:全额成交或撤销委托[深交所][股票][期权]
        49:盘后定价
        :param stock:
        :param price:
        :param volume:
        :param pr_type:
        :return:
        """
        return self._req('POST', '/api/order/buy', json={
            "stock": stock, "price": price, "volume": volume, "prType": pr_type
        })

    def sell_stock(self, stock, price, volume, pr_type=11):
        return self._req('POST', '/api/order/sell', json={
            "stock": stock, "price": price, "volume": volume, "prType": pr_type
        })

    def get_sector(self, sector):
        return self._req('POST', '/api/data/sector', json={
            "sector": sector,
        })

    def get_full_tick(self, stocks):
        return self._req('POST', f'/api/data/full_tick', json={
            "stocks": stocks})

    def get_market_data_ex(self, stocks: list[str]):
        # Server 端读的是 stock_code(逗号串), 之前发 "stocks" 键会被整个忽略(拿到空数据)
        if isinstance(stocks, (list, tuple)):
            stocks = ','.join(stocks)
        return self._req('POST', f'/api/data/market_data_ex', json={
            "stock_code": stocks})

    def get_order_status(self, account='stock'):
        """
        EEntrustStatus //委托状态
        ENTRUST_STATUS_WAIT_END: 0 //委托状态已经在 ENTRUST_STATUS_CANCELED 或以上，但是成交数额还不够，等成交回报来
        ENTRUST_STATUS_UNREPORTED: 48 //未报
        ENTRUST_STATUS_WAIT_REPORTING: 49 //待报
        ENTRUST_STATUS_REPORTED: 50 //已报
        ENTRUST_STATUS_REPORTED_CANCEL: 51 //已报待撤
        ENTRUST_STATUS_PARTSUCC_CANCEL: 52 //部成待撤
        ENTRUST_STATUS_PART_CANCEL: 53 //部撤
        ENTRUST_STATUS_CANCELED: 54 //已撤
        ENTRUST_STATUS_PART_SUCC: 55 //部成
        ENTRUST_STATUS_SUCCEEDED: 56 //已成
        ENTRUST_STATUS_JUNK: 57 //废单
        ENTRUST_STATUS_DETERMINED: 86 //已确认
        ENTRUST_STATUS_UNKNOWN: 255 //未知
        :return:
        """
        params = {"account": account}
        query = "&".join([f"{k}={v}"for k, v in params.items()])
        return self._req('POST', f'/api/order/status', json=params)

    def cancel_all_orders(self, account='stock'):
        """
        危险操作：一键撤销所有活跃状态的订单
        """
        return self._req('POST', f'/api/order/cancel_all', json={"account": account})

    def cancel_order(self, stock, volume, account='stock'):
        """
        根据股票代码和未成交数量撤单。
        请注意：如果该股票有多笔未成交数量相同的订单，会被全部撤销！
        """
        return self._req('POST', '/api/order/cancel_order', json={
            "stock": stock,
            "volume": volume,
            "account": account
        })

    def python_version(self):
        """
        获取 Python 版本信息
        """
        return self._req('GET', '/api/sys/python_version')

    def close(self):
        """
        关闭整个 QMT HTTP 服务
        """
        return self._req('POST', '/api/sys/shutdown')

    # ============= 数据获取（补充，对应 xtquant 的取数能力）=============
    def get_kline(self, stock_code, period='1d', count=-1, start_time='', end_time='',
                  fields=None, dividend_type='none'):
        """
        取 K 线行情（封装 /api/data/market_data）。
        替代 xtdata.get_market_data_ex(field_list, stock_list, period, start_time, end_time, count)。
        :param stock_code: '600000.SH' 或 ['600000.SH','000001.SZ']
        :param period: '1d'/'1m'/'5m'/'15m'/'30m'/'1h'/'1w'/'1mon'
        :param count: 取多少根，-1 表示按 start_time/end_time
        :param dividend_type: 'none'/'front'/'back'（前复权用 front）
        """
        fields = fields or ['open', 'high', 'low', 'close', 'volume', 'amount']
        if isinstance(fields, (list, tuple)):
            fields = ','.join(fields)
        if isinstance(stock_code, (list, tuple)):
            stock_code = ','.join(stock_code)
        return self._req('POST', '/api/data/market_data', json={
            "stock_code": stock_code, "fields": fields, "period": period,
            "start_time": start_time, "end_time": end_time,
            "count": count, "dividend_type": dividend_type,
        })

    def get_market_data_ex2(self, stock_code, period='follow', count=-1, start_time='', end_time='',
                            fields=None, dividend_type='follow'):
        """扩展行情全参数版（封装 /api/data/market_data_ex）。"""
        fields = fields or ['open', 'high', 'low', 'close', 'volume', 'amount']
        if isinstance(fields, (list, tuple)):
            fields = ','.join(fields)
        if isinstance(stock_code, (list, tuple)):
            stock_code = ','.join(stock_code)
        return self._req('POST', '/api/data/market_data_ex', json={
            "stock_code": stock_code, "fields": fields, "period": period,
            "start_time": start_time, "end_time": end_time,
            "count": count, "dividend_type": dividend_type,
        })

    def get_stock_list_in_sector(self, sectorname):
        """取板块成分股（封装 /api/data/stock_list_in_sector）。替代 xtdata.get_stock_list_in_sector('沪深A股')。"""
        return self._req('POST', '/api/data/stock_list_in_sector', json={"sectorname": sectorname})

    def get_stock_name(self, stockcode):
        """根据代码取股票名称（封装 /api/data/stock_name）。"""
        return self._req('POST', '/api/data/stock_name', json={"stockcode": stockcode})

    def get_trading_dates(self, stockcode='', start_date='', end_date='', count=-1, period='1d'):
        """取交易日列表（封装 /api/data/trading_dates）。"""
        return self._req('POST', '/api/data/trading_dates', json={
            "stockcode": stockcode, "start_date": start_date, "end_date": end_date,
            "count": count, "period": period,
        })

    def get_financial_data(self, fields, stocks, start_date='', end_date='', report_type='announce_time'):
        """
        取财务数据（封装 /api/data/financial_data）。替代 xtdata.download_financial_data2/get_financial_data。
        :param fields: 如 ['Balance.total_share','Income.net_profit', ...] 或逗号串
        :param stocks: ['600519.SH', ...] 或逗号串
        """
        if isinstance(fields, (list, tuple)):
            fields = ','.join(fields)
        if isinstance(stocks, (list, tuple)):
            stocks = ','.join(stocks)
        return self._req('POST', '/api/data/financial_data', json={
            "fieldList": fields, "stockList": stocks,
            "startDate": start_date, "endDate": end_date, "report_type": report_type,
        })

    def get_sector_list(self):
        """取全部板块名称列表（封装 GET /api/xtdata/sector_list）。替代 xtdata.get_sector_list()。"""
        return self._req('GET', '/api/xtdata/sector_list')

    def find_sectors(self, keyword):
        """按关键字搜索QMT板块/行业名(解决底层命名与直觉不一致的问题,
        如'CSRC餐饮业'实际叫'CSRC住宿和餐饮业')。返回匹配的名称列表。"""
        ret = self.get_sector_list()
        sectors = ret.get('sectors', []) if isinstance(ret, dict) else []
        return [s for s in sectors if keyword in s]

    def get_industry(self, industry):
        """取行业成分股。注意:industry 必须与QMT底层命名完全一致,
        建议先用 find_sectors('餐饮') 确认准确名称再传入。"""
        return self._req('POST', '/api/data/industry', json={
            "industry": industry,
        })

    def get_instrument_detail(self, stock_list, iscomplete=False):
        """批量取个股详情（封装 /api/xtdata/instrument_detail）。替代 xtdata.get_instrument_detail。
        :param stock_list: '600519.SH' 或 ['600519.SH', ...]
        :param iscomplete: True 时返回扩展字段（如申万行业码，取决于 QMT 内嵌 xtquant 版本）
        """
        if isinstance(stock_list, (list, tuple)):
            stock_list = ','.join(stock_list)
        return self._req('POST', '/api/xtdata/instrument_detail', json={
            "stock_list": stock_list, "iscomplete": bool(iscomplete),
        })

    # ============= 账户/委托/成交明细（封装 /api/trade/trade_detail_data + /api/order/deal）=============
    def get_account_detail(self, account='stock'):
        """查账户资金全字段（datatype=account）：含 market_value/frozen_cash 等。替代 query_stock_asset。"""
        return self._req('POST', '/api/trade/trade_detail_data', json={"account": account, "datatype": "account"})

    def get_orders_detail(self, account='stock'):
        """查当日委托全字段（datatype=order）。替代 query_stock_orders。"""
        return self._req('POST', '/api/trade/trade_detail_data', json={"account": account, "datatype": "order"})

    def get_positions_detail(self, account='stock'):
        """查持仓全字段（datatype=position）。替代 query_stock_positions。"""
        return self._req('POST', '/api/trade/trade_detail_data', json={"account": account, "datatype": "position"})

    def get_deals(self, account='stock'):
        """查当日成交明细（封装 /api/order/deal）。替代 query_stock_trades。"""
        return self._req('POST', '/api/order/deal', json={"account": account})

    # ============= 撤单（按委托编号）=============
    def cancel_order_by_id(self, order_id, account='stock'):
        """
        按委托编号撤单（封装 /api/order/cancel_by_id，需 Server 新端点）。
        替代 xtquant 的 cancel_order_stock(account, order_id)。
        """
        return self._req('POST', '/api/order/cancel_by_id', json={"orderId": order_id, "account": account})


# ============= 测试示例 =============
def unit_test():
    client = QMTClient()
    account_type = "stock"  # 根据实际账户调整

    # # 1. 查询资金
    # print("[1] 总资金:", client.get_total_money(account_type))
    # print("[2] 可用资金:", client.get_available_money(account_type))

    # # 2. 查询持仓
    # print("[3] 持仓信息:", json.dumps(client.get_holding(account_type), indent=2, ensure_ascii=False))

    # # 3. 委托状态
    # print("[4] 委托状态:", client.get_order_status())

    # 4. QMT 内置 Python 版本（不依赖交易连接，可用来判断服务是否存活）
    print("[5] QMT Python:", client.python_version())
    # 5. 板块 / 行业 / 行情
    print("[6] 沪深300成分股:", client.get_sector('000300.SH'))
    print("[6] 沪深300成分股:", client.get_stock_list_in_sector('沪深A股'))
    # 第二步:用上一步返回的准确名称取成分,例如:
    print("[7] 行业成份股:", client.get_industry('CSRC1住宿和餐饮业'))    
    print("[8] market_data_ex:", client.get_market_data_ex(['600000.SH', '000001.SZ']))
    print("[9] full_tick:", client.get_full_tick('600000.SH'))
    # print("[10] instrument_detail:", client.get_instrument_detail('600519.SH'))    # 不可用
    print("[11] financial_data:", client.get_financial_data(['Balance.total_share','Income.net_profit'], '600519.SH,000001.SZ'))

    # ⚠️ 实盘下单（默认注释，确认无误后再放开）
    # print("[10] 买入:", client.buy_stock("600000.SH", 6.80, 100))

    # client.close()  # 关闭 HTTP 服务


if __name__ == "__main__":

    unit_test()
