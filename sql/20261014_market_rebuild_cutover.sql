-- Execute only after market_rebuild_audit reports can_cutover=true.
-- Replace the placeholder before calling the procedure.

DELIMITER $$
DROP PROCEDURE IF EXISTS cutover_market_rebuild$$
CREATE PROCEDURE cutover_market_rebuild(IN p_batch_id varchar(64))
BEGIN
  DECLARE bad_count bigint DEFAULT 0;
  DECLARE complete_count bigint DEFAULT 0;

  SELECT COUNT(*) INTO complete_count
  FROM trade_market_rebuild_batch
  WHERE batch_id=p_batch_id AND status='complete';
  IF complete_count = 0 THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT='approved rebuild batch has no completed codes';
  END IF;

  SELECT COUNT(*) INTO bad_count
  FROM trade_market_rebuild_batch
  WHERE batch_id=p_batch_id AND status<>'complete';
  IF bad_count <> 0 THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT='approved rebuild batch contains incomplete codes';
  END IF;

  SELECT
    (SELECT COUNT(*) FROM trade_stock_daily_raw_rebuild
      WHERE rebuild_batch_id<>p_batch_id OR open_price=0 OR high_price=0 OR low_price=0 OR close_price=0)
    +
    (SELECT COUNT(*) FROM trade_stock_daily_qfq_rebuild
      WHERE rebuild_batch_id<>p_batch_id OR open_price=0 OR high_price=0 OR low_price=0 OR close_price=0)
    +
    (SELECT COUNT(*) FROM trade_stock_daily_bfq_rebuild
      WHERE rebuild_batch_id<>p_batch_id OR open_price=0 OR high_price=0 OR low_price=0 OR close_price=0)
  INTO bad_count;
  IF bad_count <> 0 THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT='zero_price or foreign batch rows found in rebuild tables';
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
