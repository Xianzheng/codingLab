'''
def A(a,b):
    return a+b

b = A
def make_averager1():
    series = []
    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)
    return averager

a = make_averager1()


def make_averager():
    count = 0
    total = 0
    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count
    return averager
    
b = make_averager()
'''

'''
#简单的装饰器，输出函数的运行时间
import time
def clock(func):
    def clocked(*args): # ➊
        t0 = time.perf_counter()
        result = func(*args) # ➋
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked #

@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)


# print('*' * 40, 'Calling factorial(6)')
# print('6! =', factorial(100))
import functools 

@functools.lru_cache()
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)
if __name__=='__main__':
    print(fibonacci(10))
'''

'''
#singledispatch demo
from functools import singledispatch
from functools import singledispatch
from collections import  abc
@singledispatch
def show(obj):
    print (obj, type(obj), "obj")

#参数字符串
@show.register(str)
def _(text):
    print (text, type(text), "str")

#参数int
@show.register(int)
def _(n):
    print (n, type(n), "int")


#参数元祖或者字典均可
@show.register(tuple)
@show.register(dict)
def _(tup_dic):
    print (tup_dic, type(tup_dic), "int")



show(1)

'''
'''
registry = []
def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func
@register
def f1():
    print('running f1()')
    print('running main()')
    print('registry ->', registry)

print('f1 %s' % 1)
'''
'''

import time
DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'
def clock(fmt=DEFAULT_FMT): 
    def decorate(func): 
        def clocked(*_args): 
            t0 = time.time()
            _result = func(*_args) 
            elapsed = time.time() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args) 
            print('args is',args)
            result = repr(_result) 
            print(fmt.format(**locals())) 
            return _result 
        return clocked 
    return decorate 
if __name__ == '__main__':
    @clock()
    def snooze(seconds):
        time.sleep(seconds)
    
    for i in range(3):
        snooze(.123)

'''

'''
#深拷贝,浅拷贝
lst1 = [1,2,3,4,5]

lst2 = list(lst1)

lst3 = lst1
# print(lst1.pop())
# print(lst1)
# print(lst2)
# print(lst3)

class A():

    def __init__(self) -> None:
        self.lst = []

    def __repr__(self) -> list:
        return ','.join(map(str,self.lst))

a = A()
a.lst.extend([1,2,3,4])

from copy import copy,deepcopy

b = copy(a)
c = deepcopy(a)

a.lst.pop()
'''

'''
# del 删除的是标签，不是对象
import weakref as w

s1 = {1,2,3}
s2 = s1

def b():
    print('hell0')

e = w.finalize(s1,b)

print(e.alive)

del s1

print(e.alive)

s2 = {4,5,6}

print(e.alive)
'''

def chain(*a):
    for it in a:
        for i in it:
            yield i

print(chain('ABC',tuple(range(1,3))))
