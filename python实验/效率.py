import datetime, time

def get_time_stamp1():
    #算毫秒级
    b = datetime.datetime.now()
    print(b)
    a = (i for i in range(20000000))
    c = datetime.datetime.now()
    print(c)

    print('ms',int(c.strftime('%f'))-int(b.strftime('%f')))


def get_time_stamp():
    ct = time.time()
    local_time = time.localtime(ct)
    data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    data_secs = (ct - int(ct)) * 1000
    time_stamp = "%s.%03d" % (data_head, data_secs)
    print(time_stamp)
    stamp = ("".join(time_stamp.split()[0].split("-"))+"".join(time_stamp.split()[1].split(":"))).replace('.', '')
    print(stamp)



from timeit import Timer
'''
def fib(n):
	if n <= 2:
		return 1
	else:
		return fib(n - 1) + fib(n - 2)
	
t1 = Timer("fib(100)", "from __main__ import fib")
print("fib--100", t1.timeit(number=1000), "seconds")
'''
# for i in a:
#     print(i)
'''
def fib(n, _cache={}):
	if n in _cache:
		return _cache[n]
	elif n > 1:
		return _cache.setdefault(n, fib(n - 1) + fib(n - 2))
	return n
 
 
t1 = Timer("fib(100)", "from __main__ import fib")
print("fib--100", t1.timeit(number=1000), "seconds")

#fib--100 0.0004969000000000015 seconds
'''


'''
from functools import lru_cache
# 使用functools装饰器
@lru_cache(maxsize=None)
def fib(n):
	if n <= 2:
		return 1
	else:
		return fib(n - 1) + fib(n - 2)
 
 
t1 = Timer("fib(100)", "from __main__ import fib")
print("fib--100", t1.timeit(number=1000), "seconds")
#fib--100 0.00027500000000001135 seconds
'''
import time
from functools import wraps

def timethis(func):
    '''
    Decorator that reports the execution time.
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper

@timethis
def countdown(n):

     while n > 0:
         n -= 1

countdown(10000000)