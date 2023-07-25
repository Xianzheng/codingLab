'''
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

8
min_key_byvalue = min(prices, key=lambda k:prices[k])
print()
'''

dic = {
    'a':'apple',
    'b':'banana',
    'c':'cherry',
}

a = (i for i in list(dic.keys()))


class A:

    def __init__(self):
        self.items = [1, 2]

    def __contains__(self, item):
        return item in self.items

a = A()
print(1 in a)   # True
print(2 in a)   # True
print(3 in a)   # False
