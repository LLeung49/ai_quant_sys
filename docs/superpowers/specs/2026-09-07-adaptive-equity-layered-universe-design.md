# Adaptive Equity Layered Universe Design

## Scope

The GRID/TREND strategy manages only approved equity sleeves of the existing
account allocation. It does not optimise the account-level percentages.

| Asset layer | Sub-layer | Strategy assets |
|---|---|---|
| Defensive | dividend-low-vol ETF | domestic dividend, low-volatility, value, quality, high-dividend ETFs |
| Defensive | dividend-low-vol blue chips | point-in-time official dividend/low-vol index constituents, subject to stock-specific controls |
| Broad beta | domestic core | A500, CSI 300 and other domestic broad-market ETFs |
| Broad beta | domestic growth | ChiNext, STAR and domestic growth broad ETFs |
| Broad beta | overseas mature | approved domestic-listed Nasdaq 100 and S&P 500 QDII ETFs |
| Broad beta | Hong Kong/offshore China | approved domestic-listed Hang Seng Technology and Hang Seng Internet QDII ETFs |

Bond, cash, precious-metal, leveraged, inverse and unapproved sector assets
remain outside the strategy.

## Point-in-time universe

Domestic high-dividend low-volatility stocks derive from historical constituent
files of CSI Dividend Low Volatility, CSI Dividend Quality and CSI Dividend
indices. A constituent is eligible only when its dated membership, price,
corporate-action, trade-status and liquidity evidence is available. Named
blue-chip stocks are watch-list candidates, not unconditional inclusions.

QDII ETFs are permitted only in the two explicitly named international
sub-layers. They retain domestic exchange T+1 execution and domestic ETF lot
rules, but are separately classified, budgeted, audited and reported.

## Portfolio research and freeze

Each sub-layer receives its existing account budget. Research considers every
eligible product and stock within that sub-layer, uses point-in-time
walk-forward validation, and selects a variable-cardinality basket. A product
is retained only if it contributes cost-adjusted out-of-sample evidence or
meaningful diversification measured by return correlation, downside
correlation and drawdown overlap. There is no fixed count rule.

The frozen manifest records layer, sub-layer, budget, instrument type,
instrument weight, selected configuration hash and review dates. Weights sum
to one inside each selected sub-layer; individual caps are configurable rather
than hard-coded as a universal 50 percent rule.

## Execution and daily shadow

Every target receives `sub_layer_budget * target_weight`, has independent
state and emits an auditable next-session order recommendation. ETF and stock
targets share signal/regime/risk semantics, but stock execution models Chinese
equity tax, corporate actions, delisting and concentration constraints.

Daily eligibility uses dated classification plus price, liquidity and trading
status. Shadow operation does not optimise, substitute products or submit
orders. It runs for at least 60 sessions before a separate small-capital,
human-confirmed live design.
