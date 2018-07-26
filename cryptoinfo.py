mport requests
def price(ctx):
    r = requests.get('https://api.coinmarketcap.com/v1/ticker/' + ctx)
    data = r.json()
    price = data[0]['price_usd']
    print('$' + price)





