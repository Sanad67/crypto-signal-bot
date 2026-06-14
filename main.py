import requests
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
p = requests.get(url)
data = p.json()
price = data["bitcoin"]["usd"]
print(f"The price is: ${price}")