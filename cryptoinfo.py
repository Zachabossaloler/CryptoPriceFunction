import requests
def price(ctx):
    r = requests.get('https://api.coinmarketcap.com/v1/ticker/' + ctx)
    data = r.json()
    price = data[0]['price_usd']
    rank = data[0]['rank']
    max_supply = data[0]['total_supply'] 
    print('Coin: ' + ctx + "\n" + 'Price: $' + price + "\n" + 'Rank: ' + rank + "\n" + "Max Supply: " + max_supply)





