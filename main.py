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

print(df[df['Signal'] != ''])







