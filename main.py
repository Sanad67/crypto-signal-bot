#Before running ensure you are in the venv before activating 
#Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process
#Then activate venv\Scripts\Activate.ps1  

import requests , json
import pandas as pd
import numpy as np


'''
Get request
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
df.to_csv('btc_90d.csv')    
'''
df = pd.read_csv('btc_90d.csv', index_col='Timestamp', parse_dates=True)
#Moving average 
df["MA3"] = df['Price'].rolling(window = 3).mean()
df['MA10'] = df['Price'].rolling(window=10).mean()
df['price_diff'] = df['MA3'] - df['MA10']
df['diff_prev'] = df['price_diff'].shift(1)

#Signal df 
df['Signal'] = ''
df.loc[(df['diff_prev'] <= 0) & (df['price_diff'] > 0), 'Signal'] = 'BUY'
df.loc[(df['diff_prev'] >= 0) & (df['price_diff'] < 0), 'Signal'] = 'SELL'

#Fixed
capital = 10000
crypto = 0 
fee_rate = 0.001

#Buy and sell signal logic 
for index, row in df.iterrows():
    row_pos = df.index.get_loc(index)
    if row_pos + 1 < len(df):
        fill_price = df['Price'].iloc[row_pos + 1]
        if (row['Signal'] == 'BUY') and (crypto == 0):
            capital = capital * (1-fee_rate)
            crypto = capital/ fill_price
            capital = 0
        if (row['Signal'] ==  'SELL') and (crypto > 0):
            capital = crypto * fill_price * (1 - fee_rate)
            crypto = 0

last_price = df['Price'].iloc[-1]
if crypto > 0:
    capital = crypto * last_price * (1 - fee_rate)
    crypto = 0 

# Backtest fills on NEXT bar (no lookahead). ~-11% on 90d hourly MA3/MA10.
# Note: result varies per run — days=90 pulls live data. TODO: snapshot to CSV for reproducibility
print(f"The crypto is: {crypto}")
print(f"The capital is: {capital}")   

#Print all results in a csv file 

        

    






