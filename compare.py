from strategies.ma_crossover import MACrossover
from strategies.rsi import RSIStrategy
import pandas as pd
from backtester import run_backtest

df = pd.read_csv('btc_90d.csv', index_col='Timestamp', parse_dates=True)
strategies = [MACrossover(3, 10), RSIStrategy(14)]
for strategy in strategies:
    signals = strategy.generate_signals(df)
    result = run_backtest(df, signals)
    print(f"{strategy.name}: {result}")