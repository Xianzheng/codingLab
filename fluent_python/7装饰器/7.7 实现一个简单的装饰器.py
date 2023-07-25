#return func("args")相当于给这个函数做一个增强
import time

def countTime(func):
    def count(*args):
        t0 = time.perf_counter()
        a = func(*args)
        t1 = time.perf_counter() - t0
        arg_str = ', '.join(repr(arg) for arg in args)
        print(arg_str, t1)
        return a
    return count

@countTime
def fac(n):
    return 1 if n < 2 else fac(n-1) * n

@countTime
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

print(fibonacci(5))
'''
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
def fac(n):
    return 1 if n < 2 else n * fac(n-1)

fac(6)
'''