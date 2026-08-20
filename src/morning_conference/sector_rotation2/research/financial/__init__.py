"""PIT-safe financial data layer and Repair Alpha model.

The ``financial`` package owns:

- Raw statement ingestion with append-only history and source-hash dedup
  (``trade_stock_financial_raw_pit``)
- PIT resolver (``PIT_EXACT`` / ``PIT_VERIFIED`` / ``PIT_ESTIMATED``)
- Daily valuation snapshot derivation (``trade_stock_valuation_daily``)
- Capital structure persistence (``trade_stock_capital_pit``)
- Repair Alpha service entry point used by the daily runner

Strict historical research only consumes ``PIT_EXACT`` or
``PIT_VERIFIED`` rows; ``PIT_ESTIMATED`` rows are exposed interactively
only when the runner is launched with ``--allow-estimated-pit``.
"""
