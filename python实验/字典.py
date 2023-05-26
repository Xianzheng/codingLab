prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

i = prices.items()
# print(i)
ii = sorted(i,key = lambda i: i[1])
# print(ii)

min_key_byvalue = min(prices, key=lambda k:prices[k])
print()