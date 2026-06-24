# crypto-signal-bot

A moving-average crossover (3 vs 10 period) backtester for Bitcoin. 
It simulates the strategy on historical price data and reports the 
final capital.


## Strategy
The bot buys when the 3-period moving average crosses above the 
10-period and sells when it crosses below. It backtests this on 
historical Bitcoin price data using a preset starting capital.


## Running it
​```
pip install -r requirements.txt
python main.py
​```
Price data is frozen in a CSV snapshot so results reproduce exactly.

## Output
Reports final capital after running the strategy over the dataset. 
The current backtest returns -33% — the honest result of a simple 
crossover strategy with fees. The goal here is measuring a strategy 
properly, not finding a winning one.

## Note
