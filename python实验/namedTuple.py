from collections import namedtuple
from functools import reduce

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')

print(sub)

sum = reduce(lambda x, y: x * y,[1,2,3,4,5,6])

sum1 = (x * x for x in [1,2,3,4,5])

print(sum1)

for i in sum1:
    print(i)

a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

from collections import ChainMap
c = ChainMap(a,b)

print(dict(c))