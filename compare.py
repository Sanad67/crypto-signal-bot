from strategies.ma_crossover import MACrossover
from strategies.rsi import RSIStrategy
import pandas as pd
from backtester import run_backtest


def total_return(start, end):
    return ((end / start) - 1) * 100

df = pd.read_csv('btc_90d.csv', index_col='Timestamp', parse_dates=True)
strategies = [MACrossover(3, 10), RSIStrategy(14)]

for strategy in strategies:
    signals = strategy.generate_signals(df)
    result = run_backtest(df, signals)
    pct = total_return(10000, result)
    print(f"{strategy.name}: {pct:.2f}%")

