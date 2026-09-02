-- Phase 4.5 / one-time migration: backfill trade_stock_financial_raw_pit
-- from the legacy trade_stock_financial wide table.
--
-- Source rows already migrated by the dual-write collector are skipped via
-- NOT EXISTS on (stock_code, report_date, source_hash).  The legacy table
-- does NOT have announcement_date, so every migrated row is PIT_ESTIMATED;
-- the Repair Alpha runner exposes --allow-estimated-pit for interactive
-- consumption.  Strict historical research ignores these rows.
--
-- Safe to run multiple times: every row is INSERT IGNORE-protected by the
-- unique key (stock_code, source_table, report_date, source_hash).
--
-- The source_hash is computed with SHA2(revenue || net_profit || stock_code
-- || report_date) so it matches the dual-write helper.  The legacy table may
-- have NULL values; we substitute 0 for the hash so the digest is deterministic.

INSERT INTO trade_stock_financial_raw_pit
    (stock_code, source_table, report_date, period_type,
     revenue, net_profit, total_assets, total_equity, operating_cash_flow,
     pit_status, source_updated_at, source_hash, is_restated, data_source,
     announcement_date, source_verified, first_seen_at)
SELECT
    legacy.stock_code,
    ''miniqmt'' AS source_table,
    STR_TO_DATE(legacy.report_date, ''%Y%m%d'') AS report_date,
    ''quarterly'' AS period_type,
    legacy.revenue,
    legacy.net_profit,
    legacy.total_assets,
    legacy.total_equity,
    legacy.operating_cashflow,
    ''pit_estimated'' AS pit_status,
    NOW() AS source_updated_at,
    SHA2(
        CONCAT_WS(''|'', legacy.stock_code,
                  legacy.report_date,
                  IFNULL(legacy.net_profit, 0),
                  IFNULL(legacy.revenue, 0)),
        256
    ) AS source_hash,
    0 AS is_restated,
    IFNULL(legacy.data_source, ''qmt'') AS data_source,
    NULL AS announcement_date,
    0 AS source_verified,
    NOW() AS first_seen_at
FROM trade_stock_financial AS legacy
WHERE NOT EXISTS (
    SELECT 1
      FROM trade_stock_financial_raw_pit AS pit
     WHERE pit.stock_code = legacy.stock_code
       AND pit.source_table = ''miniqmt''
       AND pit.report_date = STR_TO_DATE(legacy.report_date, ''%Y%m%d'')
       AND pit.source_hash = SHA2(
               CONCAT_WS(''|'', legacy.stock_code,
                         legacy.report_date,
                         IFNULL(legacy.net_profit, 0),
                         IFNULL(legacy.revenue, 0)),
               256)
);
