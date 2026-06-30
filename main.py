#Before running ensure you are in the venv before activating 
#Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process
#Then activate venv\Scripts\Activate.ps1  

import pandas as pd
from strategies.ma_crossover import MACrossover
from backtester import run_backtest

df = pd.read_csv('btc_90d.csv', index_col='Timestamp', parse_dates=True)
strategy = MACrossover(3, 10)
signals = strategy.generate_signals(df)

capital = run_backtest(df, signals)

print(f"The capital is: {capital}")   


        

    






