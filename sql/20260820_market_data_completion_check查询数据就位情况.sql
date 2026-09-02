-- 行情日线完成度检查
-- 用法：修改 @target_date 后，依次执行下面两个查询。
-- 参考股票/ETF集合取目标日前最近一个已存在的 raw 交易日，避免把当天尚未发布的代码误当成新增代码。

SET @target_date = '2026-08-20';

-- 查询一：按 raw/qfq/bfq、股票/ETF 分组统计完成度。
WITH
reference_day AS (
    SELECT MAX(trade_date) AS trade_date
    FROM trade_stock_daily_raw
    WHERE trade_date < @target_date
),
expected AS (
    SELECT DISTINCT
        r.stock_code,
        CASE
            WHEN LEFT(SUBSTRING_INDEX(r.stock_code, '.', 1), 2)
                 IN ('15', '16', '18', '51', '56', '58')
                THEN 'etf'
            ELSE 'stock'
        END AS asset_type
    FROM trade_stock_daily_raw r
    JOIN reference_day d ON d.trade_date = r.trade_date
),
actual AS (
    SELECT 'raw' AS price_mode, stock_code, trade_date
    FROM trade_stock_daily_raw
    WHERE trade_date = @target_date
    UNION ALL
    SELECT 'qfq' AS price_mode, stock_code, trade_date
    FROM trade_stock_daily_qfq
    WHERE trade_date = @target_date
    UNION ALL
    SELECT 'bfq' AS price_mode, stock_code, trade_date
    FROM trade_stock_daily_bfq
    WHERE trade_date = @target_date
),
mode_groups AS (
    SELECT 'raw' AS price_mode
    UNION ALL SELECT 'qfq'
    UNION ALL SELECT 'bfq'
),
asset_types AS (
    SELECT 'stock' AS asset_type
    UNION ALL SELECT 'etf'
)
SELECT
    @target_date AS target_date,
    g.price_mode,
    a.asset_type,
    COUNT(e.stock_code) AS expected_count,
    COUNT(DISTINCT CASE WHEN x.stock_code IS NOT NULL THEN e.stock_code END)
        AS completed_count,
    COUNT(e.stock_code)
        - COUNT(DISTINCT CASE WHEN x.stock_code IS NOT NULL THEN e.stock_code END)
        AS missing_count,
    ROUND(
        100.0 * COUNT(DISTINCT CASE WHEN x.stock_code IS NOT NULL THEN e.stock_code END)
        / NULLIF(COUNT(e.stock_code), 0),
        2
    ) AS completion_pct
FROM mode_groups g
CROSS JOIN asset_types a
LEFT JOIN expected e
    ON e.asset_type = a.asset_type
LEFT JOIN actual x
    ON x.price_mode = g.price_mode
   AND x.stock_code = e.stock_code
GROUP BY g.price_mode, a.asset_type
ORDER BY FIELD(g.price_mode, 'raw', 'qfq', 'bfq'), FIELD(a.asset_type, 'stock', 'etf');

-- 查询二：列出未完成的代码。
WITH
reference_day AS (
    SELECT MAX(trade_date) AS trade_date
    FROM trade_stock_daily_raw
    WHERE trade_date < @target_date
),
expected AS (
    SELECT DISTINCT
        r.stock_code,
        CASE
            WHEN LEFT(SUBSTRING_INDEX(r.stock_code, '.', 1), 2)
                 IN ('15', '16', '18', '51', '56', '58')
                THEN 'etf'
            ELSE 'stock'
        END AS asset_type
    FROM trade_stock_daily_raw r
    JOIN reference_day d ON d.trade_date = r.trade_date
),
actual AS (
    SELECT 'raw' AS price_mode, stock_code
    FROM trade_stock_daily_raw
    WHERE trade_date = @target_date
    UNION ALL
    SELECT 'qfq' AS price_mode, stock_code
    FROM trade_stock_daily_qfq
    WHERE trade_date = @target_date
    UNION ALL
    SELECT 'bfq' AS price_mode, stock_code
    FROM trade_stock_daily_bfq
    WHERE trade_date = @target_date
),
mode_groups AS (
    SELECT 'raw' AS price_mode
    UNION ALL SELECT 'qfq'
    UNION ALL SELECT 'bfq'
)
SELECT
    @target_date AS target_date,
    g.price_mode,
    e.asset_type,
    e.stock_code
FROM expected e
CROSS JOIN mode_groups g
LEFT JOIN actual x
    ON x.price_mode = g.price_mode
   AND x.stock_code = e.stock_code
WHERE x.stock_code IS NULL
ORDER BY FIELD(g.price_mode, 'raw', 'qfq', 'bfq'),
         FIELD(e.asset_type, 'stock', 'etf'),
         e.stock_code;
