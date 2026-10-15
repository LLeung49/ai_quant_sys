# -*- coding: utf-8 -*-
"""申万行业分类同步与查询，运行时数据源为 AKShare。"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any, Dict, List

from data_ingestion.db_config import execute_many, execute_query

_CATALOG_COLUMNS = ("行业代码", "行业名称", "上级行业")
_MEMBER_COLUMNS = ("证券代码", "证券名称")


def _require_columns(frame: Any, required: tuple[str, ...], source: str) -> None:
    missing = [name for name in required if name not in frame.columns]
    if missing:
        raise ValueError(f"{source} 缺少字段: {', '.join(missing)}")


def _canonical_stock_code(value: object) -> str:
    raw = str(value).strip().upper()
    if "." in raw:
        symbol, suffix = raw.split(".", 1)
        if suffix in {"SH", "SZ", "BJ"} and len(symbol) == 6 and symbol.isdigit():
            return f"{symbol}.{suffix}"
        raw = symbol
    symbol = raw.zfill(6)
    if len(symbol) != 6 or not symbol.isdigit():
        raise ValueError(f"无法识别证券代码: {value!r}")
    if symbol.startswith(("4", "8", "9")):
        suffix = "BJ"
    elif symbol.startswith(("5", "6", "7")):
        suffix = "SH"
    else:
        suffix = "SZ"
    return f"{symbol}.{suffix}"


def fetch_sw_classification_from_akshare(ak_module: Any | None = None) -> Dict[str, Dict[str, str]]:
    """先完整拉取申万二级行业和成分，再返回统一代码映射。"""
    if ak_module is None:
        import akshare as ak_module
    catalog = ak_module.sw_index_second_info()
    _require_columns(catalog, _CATALOG_COLUMNS, "sw_index_second_info")
    if catalog.empty:
        raise RuntimeError("AKShare 返回空的申万二级行业目录")

    classification: Dict[str, Dict[str, str]] = {}
    for item in catalog.loc[:, list(_CATALOG_COLUMNS)].to_dict("records"):
        industry_code = str(item["行业代码"]).strip().split(".", 1)[0]
        sector_2 = str(item["行业名称"]).strip()
        sector_1 = str(item["上级行业"]).strip()
        if not industry_code or not sector_1 or not sector_2:
            raise ValueError(f"申万行业目录存在空值: {item!r}")
        members = ak_module.index_component_sw(symbol=industry_code)
        _require_columns(members, _MEMBER_COLUMNS, f"index_component_sw({industry_code})")
        for member in members.loc[:, list(_MEMBER_COLUMNS)].to_dict("records"):
            stock_code = _canonical_stock_code(member["证券代码"])
            current = {
                "stock_name": str(member["证券名称"]).strip() or stock_code,
                "sector_1": sector_1,
                "sector_2": sector_2,
            }
            prior = classification.get(stock_code)
            if prior is not None and prior != current:
                raise ValueError(
                    f"证券 {stock_code} 同时属于冲突的申万二级行业: "
                    f"{prior['sector_2']} / {sector_2}"
                )
            classification[stock_code] = current
    if not classification:
        raise RuntimeError("AKShare 申万二级行业成分为空")
    return classification


def upsert_stock_status(classification: Dict[str, Dict[str, str]]) -> int:
    """成功构建完整分类后，一次性 UPSERT 到现有状态表。"""
    if not classification:
        return 0
    rows = [
        (code, info.get("stock_name"), info.get("sector_1"), info.get("sector_2"))
        for code, info in sorted(classification.items())
    ]
    return execute_many("""
        INSERT INTO trade_stock_status (stock_code, stock_name, sector_1, sector_2)
        VALUES (%s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            stock_name = VALUES(stock_name),
            sector_1 = COALESCE(VALUES(sector_1), sector_1),
            sector_2 = COALESCE(VALUES(sector_2), sector_2)
    """, rows)


def sync_sw_classification(ak_module: Any | None = None) -> int:
    print("同步 AKShare 申万分类到 trade_stock_status")
    classification = fetch_sw_classification_from_akshare(ak_module)
    affected = upsert_stock_status(classification)
    print(f"[OK] 分类证券={len(classification)}，数据库影响行={affected}")
    return len(classification)


def list_sectors_from_db(level: int = 2) -> List[str]:
    field = "sector_1" if level == 1 else "sector_2"
    rows = execute_query(
        f"SELECT DISTINCT {field} AS name FROM trade_stock_status "
        f"WHERE {field} IS NOT NULL ORDER BY {field}"
    )
    return [row["name"] for row in rows]


def get_sector_member_codes(sector_name: str, level: int = 2) -> List[str]:
    field = "sector_1" if level == 1 else "sector_2"
    rows = execute_query(
        f"SELECT stock_code FROM trade_stock_status WHERE {field} = %s ORDER BY stock_code",
        (sector_name,),
    )
    return [row["stock_code"] for row in rows]


def get_industry_map(level: int = 2) -> Dict[str, str]:
    field = "sector_1" if level == 1 else "sector_2"
    rows = execute_query(
        f"SELECT stock_code, {field} AS name FROM trade_stock_status WHERE {field} IS NOT NULL"
    )
    return {row["stock_code"]: row["name"] for row in rows}


def list_all_stocks_with_sector(level: int = 2) -> List[Dict]:
    field = "sector_1" if level == 1 else "sector_2"
    return execute_query(
        f"SELECT stock_code, stock_name, {field} AS sector_name "
        f"FROM trade_stock_status WHERE {field} IS NOT NULL ORDER BY stock_code"
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="同步 AKShare 申万分类到 trade_stock_status")
    parser.add_argument("--show", action="store_true", help="只展示数据库已有行业")
    parser.add_argument("--level", type=int, choices=(1, 2), default=2)
    args = parser.parse_args(argv)
    if args.show:
        for index, sector in enumerate(list_sectors_from_db(args.level), 1):
            count = len(get_sector_member_codes(sector, args.level))
            print(f"[{index:>3}] {sector:<20s} 成分股 {count} 只")
        return 0
    sync_sw_classification()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
