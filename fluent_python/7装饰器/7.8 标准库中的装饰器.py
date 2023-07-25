'''
#functools.wraps()
#lru_cache(least recent use) 是标准库装饰器的一个 可以降低重复计算
from functools import lru_cache
import time
def clock(func):
    def clocked(*args): 
        t0 = time.perf_counter()
        result = func(*args) 
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked 


@clock
def fib(n):
    return n if n < 2 else fib(n-1) + fib(n-2)

print(fib(100))
'''
'''
#单分派泛函数
#import html
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
show("xx")
show([1])
show((1,2,3))
show({"a":"b"})
'''