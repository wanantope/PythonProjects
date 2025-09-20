import requests

url = 'https://api.binance.com/api/v3/ticker/price'

response = requests.get(url, params={'symbol': 'BTCUSDT'})


price = response.json()
print(price)

while True:
    response = requests.get(url, params={'symbol': 'BTCUSDT'})
    price = response.json()['price']
    print("Цена биткоина: ", price)
