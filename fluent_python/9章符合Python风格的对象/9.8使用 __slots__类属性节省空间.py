class A:
    __slots__ = ('name','age')

a = A()
a.name = 'A'
print(a.name)