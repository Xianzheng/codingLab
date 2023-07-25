'''
class Person:
    def __init__(self, first_name):
        self.__first_name = first_name

    @property
    def first_name(self):
        return self.__first_name

# a = Person('Guido')

# print(a.first_name)

class lazyproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2

    @lazyproperty
    def perimeter(self):
        print('Computing perimeter')
        return 2 * math.pi * self.radius
    
class Age:
    def __get__(self, obj, objtype=None):
        print(obj)
        if obj.name == 'zhangsan':
            return 20
        elif obj.name == 'lisi':
            return 25
        else:
            return ValueError("unknow")

class Person:

    age = Age()

    def __init__(self, name):
        self.name = name

p1 = Person('zhangsan')
print(p1.age)   # 20

p2 = Person('lisi')
print(p2.age)   # 25

p3 = Person('wangwu')
print(p3.age)   # unknow

class A:
    def __init__(self):
        print('A')

    @classmethod
    def B(self):
        print('B')
        return A()
    
    @staticmethod
    def C():
        print('C')
    


A().B()

import math

class Structure1:
    # Class variable that specifies expected fields
    _fields = []

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        # Set the arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

# Example class definitions
class Stock(Structure1):
    _fields = ['name', 'shares', 'price']

a = Stock(1,2,3)
'''
class Fruit(object):
    total = 0
    
    @classmethod
    def print_total(cls):
        print(cls.total)
        # print(id(Fruit.total))
        # print(id(cls.total))

    @classmethod
    def set_total(cls, value):
        print(f"调用类方法 {cls} {value}")
        cls.total = value

    