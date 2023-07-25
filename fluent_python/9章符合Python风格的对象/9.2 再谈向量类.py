from array import array
import math
class Vector2d:
    typecode = 'd' 
    def __init__(self, x, y):
        self.x = float(x) 
        self.y = float(y)
    def __iter__(self):
        return (i for i in (self.x, self.y)) 
    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self) 
    def __str__(self):
        return str(tuple(self)) 
    
    def __str__(self):
        return str(tuple(self)) 
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + 
                bytes(array(self.typecode, self))) 
    def __eq__(self, other):
        return tuple(self) == tuple(other) 
    def __abs__(self):
        return math.hypot(self.x, self.y) 
    def __bool__(self):
        return bool(abs(self)) 
    def __format__(self, fmt_spec=''):
        components = (format(c, fmt_spec) for c in self) # ➊
        return '({}, {})'.format(*components) # ➋
    
v1 = Vector2d(3, 4)
print(v1.x, v1.y)

print(v1)

octets = bytes(v1)
print(octets)


class Demo:
    def myPrint(*args):
        print('Hello World')
    @classmethod
    def klassmeth(*args):
        return args 
    @staticmethod
    def statmeth(*args):
        return args 
    
print(Demo.klassmeth())
print(Demo.klassmeth('span'))
print(Demo.statmeth)
print(Demo.statmeth('span'))

a = Demo.klassmeth()
print(a[0]().myPrint())

brl = 1/2.43

print('1 BRL = {rate:0.2f} USD'.format(rate=brl))

print('his name is {name}'.format(name='zhangsan'[:2]))

print(format(2/3, '.1%'))

from datetime import datetime

now = datetime.now()
print( format(now, '%H:%M:%S'))
print( "It's now {:%I:%M %p}".format(now))

print( format(v1, '.2f'))
