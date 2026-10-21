CREATE TABLE `trade_stock_capital_pit` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `stock_code` varchar(16) NOT NULL,
  `report_date` date NOT NULL,
  `announcement_date` date NOT NULL,
  `total_shares` decimal(24,4) DEFAULT NULL,
  `circulating_shares` decimal(24,4) DEFAULT NULL,
  `pit_status` varchar(16) NOT NULL,
  `source_hash` char(64) NOT NULL,
  `first_seen_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `data_source` varchar(64) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_capital_pit` (`stock_code`,`report_date`,`source_hash`),
  KEY `idx_capital_pit_lookup` (`stock_code`,`announcement_date`,`report_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='PIT capital structure history';
