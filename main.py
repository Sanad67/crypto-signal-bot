#Before running ensure you are in the venv before activating 
#Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process
#Then activate venv\Scripts\Activate.ps1  

import pandas as pd
from strategies.ma_crossover import MACrossover

df = pd.read_csv('btc_90d.csv', index_col='Timestamp', parse_dates=True)
strategy = MACrossover(3, 10)
signals = strategy.generate_signals(df)
#Fixed
capital = 10000
crypto = 0 
fee_rate = 0.001

#Buy and sell signal logic 
for index, value in signals.items():
    row_pos = signals.index.get_loc(index)
    if row_pos + 1 < len(signals):
        fill_price = df['Price'].iloc[row_pos + 1]
        if (value == 1) and (crypto == 0):
            capital = capital * (1-fee_rate)
            crypto = capital/ fill_price
            capital = 0
        if (value ==  -1) and (crypto > 0):
            capital = crypto * fill_price * (1 - fee_rate)
            crypto = 0

last_price = df['Price'].iloc[-1]
if crypto > 0:
    capital = crypto * last_price * (1 - fee_rate)
    crypto = 0 


print(f"The crypto is: {crypto}")
print(f"The capital is: {capital}")   

#Print all results in a csv file 

        

    






