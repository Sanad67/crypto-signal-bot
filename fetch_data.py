import requests 
import pandas as pd
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