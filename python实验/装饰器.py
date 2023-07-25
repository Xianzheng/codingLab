from timeit import Timer

def fib(n):
	if n <= 2:
		return 1
	else:
		return fib(n - 1) + fib(n - 2)
	
t1 = Timer("fib(100)", "from __main__ import fib")
print("fib--100", t1.timeit(number=1000), "seconds")
 