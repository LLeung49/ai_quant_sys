-- Phase 3 / Trend Alpha eligibility columns on ``trade_stock_status``.
-- Adds the columns required by ``load_stock_universe`` (listing_date,
-- is_suspended, is_tradable).  All columns are nullable so existing rows
-- remain readable and missing history is treated as eligibility_unknown.
--
-- Each ALTER guards its column with ``information_schema.columns`` so the
-- script is safe to re-run.  All statements are idempotent.

SET @db := DATABASE();

-- listing_date: stock listing date (used for 120-day listing-age gate).
SET @c := (SELECT COUNT(*) FROM information_schema.columns
            WHERE table_schema = @db AND table_name = 'trade_stock_status'
              AND column_name = 'listing_date');
SET @sql := IF(@c = 0,
    'ALTER TABLE trade_stock_status ADD COLUMN listing_date DATE NULL COMMENT ''Stock listing date; null means unknown (eligibility_unknown)''',
    'SELECT 1');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

-- is_suspended: latest known suspension flag (true => exclude from universe).
SET @c := (SELECT COUNT(*) FROM information_schema.columns
            WHERE table_schema = @db AND table_name = 'trade_stock_status'
              AND column_name = 'is_suspended');
SET @sql := IF(@c = 0,
    'ALTER TABLE trade_stock_status ADD COLUMN is_suspended TINYINT(1) NULL COMMENT ''Latest suspension flag; null means unknown''',
    'SELECT 1');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

-- is_tradable: latest known tradable flag (false => exclude from universe).
SET @c := (SELECT COUNT(*) FROM information_schema.columns
            WHERE table_schema = @db AND table_name = 'trade_stock_status'
              AND column_name = 'is_tradable');
SET @sql := IF(@c = 0,
    'ALTER TABLE trade_stock_status ADD COLUMN is_tradable TINYINT(1) NULL COMMENT ''Latest tradable flag; null means unknown''',
    'SELECT 1');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;
