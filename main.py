#Before running ensure you are in the venv before activating 
#Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process
#Then activate venv\Scripts\Activate.ps1  

import requests , json
import pandas as pd

url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=7"
resp = requests.get(url)
data = resp.json()

prices = data["prices"]
df = pd.DataFrame(prices)
                    
df.rename(columns={0: 'Timestamp', 1: 'Price'}, inplace=True)
df['Timestamp'] = pd.to_datetime(df['Timestamp'], unit = 'ms')
df = df.set_index('Timestamp')
df["MA3"] = df['Price'].rolling(window = 3).mean()
print(df)







