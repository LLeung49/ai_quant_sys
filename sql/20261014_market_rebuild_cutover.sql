-- Execute only after market_rebuild_audit reports can_cutover=true.
-- Replace the placeholder before calling the procedure.

DELIMITER $$
DROP PROCEDURE IF EXISTS cutover_market_rebuild$$
CREATE PROCEDURE cutover_market_rebuild(IN p_batch_id varchar(64))
BEGIN
  DECLARE bad_count bigint DEFAULT 0;
  DECLARE complete_count bigint DEFAULT 0;
  DECLARE expected_count bigint DEFAULT 0;

  IF p_batch_id LIKE 'pilot-%' OR p_batch_id LIKE 'qmt-cache-validation%' THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT='sample batch ids cannot be cut over';
  END IF;

  SELECT COUNT(*) INTO expected_count
  FROM trade_market_rebuild_expected_code WHERE batch_id=p_batch_id;
  IF expected_count = 0 THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT='approved rebuild batch has no expected universe';
  END IF;

  SELECT COUNT(*) INTO complete_count
  FROM trade_market_rebuild_batch
  WHERE batch_id=p_batch_id AND status='complete';
  IF complete_count <> expected_count THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT='completed codes differ from expected universe';
  END IF;

  SELECT COUNT(*) INTO bad_count
  FROM information_schema.tables
  WHERE table_schema=DATABASE() AND table_name IN (
    'trade_stock_daily_raw_rollback_20261014',
    'trade_stock_daily_qfq_rollback_20261014',
    'trade_stock_daily_bfq_rollback_20261014'
  );
  IF bad_count <> 0 THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT='rollback table name already exists';
  END IF;

  SELECT COUNT(*) INTO bad_count FROM (
    SELECT current_codes.stock_code
    FROM (
      SELECT stock_code FROM trade_stock_daily_raw
      UNION SELECT stock_code FROM trade_stock_daily_qfq
      UNION SELECT stock_code FROM trade_stock_daily_bfq
    ) current_codes
    LEFT JOIN trade_market_rebuild_expected_code e
      ON e.batch_id=p_batch_id AND e.stock_code=current_codes.stock_code
    WHERE e.stock_code IS NULL
    UNION ALL
    SELECT e.stock_code
    FROM trade_market_rebuild_expected_code e
    LEFT JOIN (
      SELECT stock_code FROM trade_stock_daily_raw
      UNION SELECT stock_code FROM trade_stock_daily_qfq
      UNION SELECT stock_code FROM trade_stock_daily_bfq
    ) current_codes ON current_codes.stock_code=e.stock_code
    WHERE e.batch_id=p_batch_id AND current_codes.stock_code IS NULL
  ) universe_diff;
  IF bad_count <> 0 THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT='expected universe differs from canonical universe';
  END IF;

  SELECT COUNT(*) INTO bad_count
  FROM trade_market_rebuild_batch
  WHERE batch_id=p_batch_id AND status<>'complete';
  IF bad_count <> 0 THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT='approved rebuild batch contains incomplete codes';
  END IF;

  SELECT
    (SELECT COUNT(*) FROM trade_stock_daily_raw_rebuild
      WHERE rebuild_batch_id IS NULL OR rebuild_batch_id<>p_batch_id
         OR open_price=0 OR high_price=0 OR low_price=0 OR close_price=0
         OR low_price>high_price OR low_price>LEAST(open_price,close_price)
         OR high_price<GREATEST(open_price,close_price)
         OR NOT (open_price <=> open_price) OR NOT (high_price <=> high_price)
         OR NOT (low_price <=> low_price) OR NOT (close_price <=> close_price)
         OR NOT (amount <=> amount))
    +
    (SELECT COUNT(*) FROM trade_stock_daily_qfq_rebuild
      WHERE rebuild_batch_id IS NULL OR rebuild_batch_id<>p_batch_id
         OR open_price=0 OR high_price=0 OR low_price=0 OR close_price=0
         OR low_price>high_price OR low_price>LEAST(open_price,close_price)
         OR high_price<GREATEST(open_price,close_price)
         OR NOT (open_price <=> open_price) OR NOT (high_price <=> high_price)
         OR NOT (low_price <=> low_price) OR NOT (close_price <=> close_price)
         OR NOT (amount <=> amount))
    +
    (SELECT COUNT(*) FROM trade_stock_daily_bfq_rebuild
      WHERE rebuild_batch_id IS NULL OR rebuild_batch_id<>p_batch_id
         OR open_price=0 OR high_price=0 OR low_price=0 OR close_price=0
         OR low_price>high_price OR low_price>LEAST(open_price,close_price)
         OR high_price<GREATEST(open_price,close_price)
         OR NOT (open_price <=> open_price) OR NOT (high_price <=> high_price)
         OR NOT (low_price <=> low_price) OR NOT (close_price <=> close_price)
         OR NOT (amount <=> amount))
  INTO bad_count;
  IF bad_count <> 0 THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT='invalid price or foreign batch rows found in rebuild tables';
  END IF;

  SELECT COUNT(*) INTO bad_count
  FROM trade_market_rebuild_batch m
  LEFT JOIN (
    SELECT stock_code, COUNT(*) n FROM trade_stock_daily_raw_rebuild
    WHERE rebuild_batch_id=p_batch_id GROUP BY stock_code
  ) r ON r.stock_code=m.stock_code
  LEFT JOIN (
    SELECT stock_code, COUNT(*) n FROM trade_stock_daily_qfq_rebuild
    WHERE rebuild_batch_id=p_batch_id GROUP BY stock_code
  ) q ON q.stock_code=m.stock_code
  LEFT JOIN (
    SELECT stock_code, COUNT(*) n FROM trade_stock_daily_bfq_rebuild
    WHERE rebuild_batch_id=p_batch_id GROUP BY stock_code
  ) b ON b.stock_code=m.stock_code
  WHERE m.batch_id=p_batch_id AND m.status='complete'
    AND (m.raw_rows<>COALESCE(r.n, 0)
      OR m.qfq_rows<>COALESCE(q.n, 0)
      OR m.hfq_rows<>COALESCE(b.n, 0));
  IF bad_count <> 0 THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT='metadata row counts differ from staging';
  END IF;

  SELECT COUNT(*) INTO bad_count
  FROM trade_stock_daily_raw_rebuild r
  LEFT JOIN trade_stock_daily_qfq_rebuild q
    ON q.stock_code=r.stock_code AND q.trade_date=r.trade_date
  LEFT JOIN trade_stock_daily_bfq_rebuild b
    ON b.stock_code=r.stock_code AND b.trade_date=r.trade_date
  WHERE q.stock_code IS NULL OR b.stock_code IS NULL
     OR r.volume<>q.volume OR r.amount<>q.amount
     OR r.volume<>b.volume OR r.amount<>b.amount;
  IF bad_count <> 0 THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT='projection coverage or volume/amount mismatch';
  END IF;

  SELECT
    (SELECT COUNT(*) FROM trade_stock_daily_qfq_rebuild q
     LEFT JOIN trade_stock_daily_raw_rebuild r
       ON r.stock_code=q.stock_code AND r.trade_date=q.trade_date
          AND r.rebuild_batch_id=p_batch_id
     WHERE q.rebuild_batch_id=p_batch_id AND r.stock_code IS NULL)
    +
    (SELECT COUNT(*) FROM trade_stock_daily_bfq_rebuild b
     LEFT JOIN trade_stock_daily_raw_rebuild r
       ON r.stock_code=b.stock_code AND r.trade_date=b.trade_date
          AND r.rebuild_batch_id=p_batch_id
     WHERE b.rebuild_batch_id=p_batch_id AND r.stock_code IS NULL)
  INTO bad_count;
  IF bad_count <> 0 THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT='adjusted table contains rows absent from raw';
  END IF;

  RENAME TABLE
    trade_stock_daily_raw TO trade_stock_daily_raw_rollback_20261014,
    trade_stock_daily_qfq TO trade_stock_daily_qfq_rollback_20261014,
    trade_stock_daily_bfq TO trade_stock_daily_bfq_rollback_20261014,
    trade_stock_daily_raw_rebuild TO trade_stock_daily_raw,
    trade_stock_daily_qfq_rebuild TO trade_stock_daily_qfq,
    trade_stock_daily_bfq_rebuild TO trade_stock_daily_bfq;
END$$

DROP PROCEDURE IF EXISTS rollback_market_rebuild$$
CREATE PROCEDURE rollback_market_rebuild()
BEGIN
  DECLARE bad_count bigint DEFAULT 0;

  SELECT COUNT(*) INTO bad_count
  FROM information_schema.tables
  WHERE table_schema=DATABASE() AND table_name IN (
    'trade_stock_daily_raw_rejected_20261014',
    'trade_stock_daily_qfq_rejected_20261014',
    'trade_stock_daily_bfq_rejected_20261014'
  );
  IF bad_count <> 0 THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT='rejected table name already exists';
  END IF;

  RENAME TABLE
    trade_stock_daily_raw TO trade_stock_daily_raw_rejected_20261014,
    trade_stock_daily_qfq TO trade_stock_daily_qfq_rejected_20261014,
    trade_stock_daily_bfq TO trade_stock_daily_bfq_rejected_20261014,
    trade_stock_daily_raw_rollback_20261014 TO trade_stock_daily_raw,
    trade_stock_daily_qfq_rollback_20261014 TO trade_stock_daily_qfq,
    trade_stock_daily_bfq_rollback_20261014 TO trade_stock_daily_bfq;
END$$
DELIMITER ;

-- Example after an approved audit:
-- CALL cutover_market_rebuild('market-YYYYMMDD-HHMMSS');
