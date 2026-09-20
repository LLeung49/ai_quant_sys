# -*- coding: utf-8 -*-
"""
数据库连接配置
从 .env 读取配置
"""
import os
from pathlib import Path
import pymysql
from dotenv import dotenv_values


def resolve_env_path() -> Path:
    """解析当前进程应读取的环境配置文件路径。

    输入：可选环境变量 ``AI_QUANT_ENV_FILE``；未传入时从本文件所在目录逐级向上寻找
    ``.env``，以兼容主仓库与其 ``.worktrees`` 下的隔离工作目录。
    输出：优先返回显式指定路径；否则返回首个存在的 ``.env``；若均不存在，返回原有的
    仓库根目录候选路径，交由 ``dotenv_values`` 产生空配置并保持既有默认值语义。
    """
    configured_path = os.environ.get("AI_QUANT_ENV_FILE")
    if configured_path:
        return Path(configured_path).expanduser()

    module_path = Path(__file__).resolve()
    for directory in module_path.parents:
        candidate = directory / ".env"
        if candidate.is_file():
            return candidate

    return Path(__file__).parent.parent.parent / ".env"

# 从 .env 读取（在本文件上级目录）
_env_path = resolve_env_path()
_env = dotenv_values(_env_path)

DB_CONFIG = {
    'host': _env.get('WUCAI_SQL_HOST', 'localhost'),
    'user': _env.get('WUCAI_SQL_USERNAME', 'root'),
    'password': _env.get('WUCAI_SQL_PASSWORD', ''),
    'database': _env.get('WUCAI_SQL_DB', 'wucai_trade'),
    'port': int(_env.get('WUCAI_SQL_PORT', '3306')),
    'charset': 'utf8mb4'
}

# Kimi API
KIMI_API_KEY = _env.get('KIMI_API_KEY', '')
KIMI_BASE_URL = _env.get('KIMI_BASE_URL', 'https://api.moonshot.cn/v1')
KIMI_MODEL = _env.get('KIMI_MODEL', 'kimi-latest')

# DashScope/Qwen
DASHSCOPE_API_KEY = _env.get('DASHSCOPE_API_KEY', '')
QWEN_MODEL = _env.get('QWEN_MODEL', 'qwen-flash')

# MiniMax
MINIMAX_API_KEY = _env.get('MINIMAX_API_KEY', '')
MINIMAX_BASE_URL = _env.get('MINIMAX_BASE_URL', 'https://api.minimaxi.com/v1')
MINIMAX_MODEL = _env.get('MINIMAX_MODEL', 'MiniMax-M3')


# 回测参数（可在 .env 中修改）
INITIAL_CASH = int(_env.get('BACKTEST_INITIAL_CASH', '1000000'))
COMMISSION = float(_env.get('BACKTEST_COMMISSION', '0.0002'))
POSITION_PCT = int(_env.get('BACKTEST_POSITION_PCT', '95'))



def get_connection():
    """获取数据库连接"""
    return pymysql.connect(**DB_CONFIG)


def execute_query(sql, params=None):
    """执行查询，返回字典列表"""
    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql, params or ())
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


def execute_update(sql, params=None):
    """执行单条更新/插入"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(sql, params or ())
    conn.commit()
    affected = cursor.rowcount
    cursor.close()
    conn.close()
    return affected


def execute_many(sql, data_list):
    """批量执行插入/更新"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.executemany(sql, data_list)
    conn.commit()
    affected = cursor.rowcount
    cursor.close()
    conn.close()
    return affected

