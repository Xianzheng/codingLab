class Count():
    
    def __init__(self,start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 2

c = Count(10)
print(list(c))
print(list(reversed(c)))

from math import hypot
class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)
    def __abs__(self):
        return hypot(self.x, self.y)
    def __bool__(self):
        return bool(abs(self))
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
class String:
    def __init__(self,string):
        self.string = string

    def __len__(self):
        return len(self.string)

    def __repr__(self) -> str:
        return self.string
    
# t = (1, 2, [30, 40])
# t[2] += [2,4]
# print(t)

a = [2,1,4,3]

# a.sort()
# print(a)
print(sorted(a))
print(a)

a1 = [1,2,3,4,5,6,7]

a1 = list(filter(lambda x: x % 2 == 0,a1))
print(a1)