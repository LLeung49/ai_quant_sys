# -*- coding: utf-8 -*-
# 21-CASE-A: 每日增量
"""
run_daily.py -- 每日增量

执行顺序:
    1. Task 8 已维护 trade_stock_daily_qfq
    2. 重算最近 60 个交易日的 trade_sector_daily
       (60 天足够覆盖任何延迟到位的成分股 K 线 + 重新校验 close_idx 链)
    3. 默认不刷新 trade_stock_status 申万分类 (申万官方分类一年才调一次)
       学员手工觉得需要时, 用 --refresh-meta 触发

预期耗时:
    单日增量约 5-15 分钟, 建议 8:30 cron 触发, 给晨会 (9:00) 留充足准备时间

执行命令
D:/Programs/Python/Python313/python.exe d:/aiQuant/ai_quant_sys/src/morning_conference/sector_rotation/2-run_data_daily.py --level 2

结果查询：
1. 窗口内板块涨幅
    SELECT sector_name,
        ROUND(MAX(CASE WHEN trade_date = '2026-07-31' THEN close_idx END) /
            MAX(CASE WHEN trade_date = '2026-07-01' THEN close_idx END) - 1, 4) AS ret_window
    FROM   trade_sector_daily
    WHERE  sector_level = 2
    GROUP BY sector_name
    ORDER BY ret_window DESC
    LIMIT 10;
2. 板块收盘数据
    SELECT sector_name,trade_date,close_idx
    FROM   trade_sector_daily
    WHERE  sector_level = 2 and sector_name='白色家电'
    ORDER BY trade_date DESC;
3. 板块内股票数据
    
"""
from __future__ import annotations
import sys
from pathlib import Path

from numpy import full

sys.path.insert(0, str(Path(__file__).resolve().parent))

from industry_meta_qmt_bridge import sync_sw_classification
from sector_index_builder import rebuild_all_sectors


def main():
    import argparse
    parser = argparse.ArgumentParser(description="CASE-A 每日增量")
    parser.add_argument("--refresh-meta", action="store_true",
                        help="强制刷新申万分类 (默认不刷新, 一周或一月触发一次即可)")
    parser.add_argument("--days", type=int, default=60,
                        help="重算板块指数的最近交易日数 (默认 60)")
    parser.add_argument("--level", type=int, choices=[1, 2], default=2)
    args = parser.parse_args()

    print("\n" + "#" * 70)
    print("# CASE-A 板块数据 -- 每日增量")
    print("#" * 70)

    if args.refresh_meta:
        sync_sw_classification()

    print("\n[INFO] 假定 Task 8 已维护 trade_stock_daily_qfq\n")
    rebuild_all_sectors(level=args.level, days=args.days, full=False)

    print("\n" + "#" * 70)
    print("# 每日增量完成")
    print("#" * 70 + "\n")


if __name__ == "__main__":
    main()

