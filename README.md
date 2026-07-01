# crypto-signal-bot

A backtesting framework for cryptocurrency trading strategies. It runs
strategies against historical price data, accounts for fees, and reports
performance so you can compare approaches on equal footing.

## Strategies

Strategies live in a modular library, each sharing a common interface so
they can be swapped and compared. Currently included:

- **MA crossover** — buys when the 3-period moving average crosses above
  the 10-period and sells when it crosses below.
- **RSI** — trades on the relative strength index, entering and exiting on
  overbought/oversold thresholds.

A comparison runner backtests each strategy over the same dataset and
reports their results side by side.

## Running it
Price data is frozen in a CSV snapshot so results reproduce exactly.

## Output

Reports each strategy's final capital, laid out for direct comparison.
Over the same 90 days: **MA crossover: −33%, RSI: −11%.**  The point of
this project is measuring strategies properly and comparing them on equal
footing, not cherry-picking a winner.

## Note

Backtests are only as trustworthy as their assumptions: trades fill on
the next bar (no lookahead), and fees are applied on every fill.
