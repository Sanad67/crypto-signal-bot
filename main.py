#Before running ensure you are in the venv before activating 
#Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process
#Then activate venv\Scripts\Activate.ps1  

import requests , json
import pandas as pd
import numpy as np

url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=90"

try:
    resp = requests.get(url)
    data = resp.json()
    prices = data["prices"]
except (requests.RequestException, KeyError) as e:
    print(e)
    exit()
    
df = pd.DataFrame(prices)
                    
df.rename(columns={0: 'Timestamp', 1: 'Price'}, inplace=True)
df['Timestamp'] = pd.to_datetime(df['Timestamp'], unit = 'ms')
df = df.set_index('Timestamp')
df["MA3"] = df['Price'].rolling(window = 3).mean()
df['MA10'] = df['Price'].rolling(window=10).mean()

df['price_diff'] = df['MA3'] - df['MA10']
df['diff_prev'] = df['price_diff'].shift(1)


df['Signal'] = ''
df.loc[(df['diff_prev'] <= 0) & (df['price_diff'] > 0), 'Signal'] = 'BUY'
df.loc[(df['diff_prev'] >= 0) & (df['price_diff'] < 0), 'Signal'] = 'SELL'

#print(df[df['Signal'] != ''])

capital = 10000
crypto = 0 

for index, row in df.iterrows():

    if (row['Signal'] == 'BUY') and (crypto == 0):
        crypto = capital/ row['Price']
        capital = 0
    if (row['Signal'] ==  'SELL') and (crypto > 0):
        capital = crypto * row['Price']
        crypto = 0

last_price = df['Price'].iloc[-1]
if crypto > 0:
    capital = crypto * last_price
    crypto = 0 

# Backtest done: $10k -> $8762 on 90d hourly MA3/MA10 crossover (~-12%).
# Next: fix lookahead (fill on NEXT bar, not signal bar), then add fees.

print(f"The crypto is: {crypto}")
print(f"The capital is: {capital}")     

        
    






