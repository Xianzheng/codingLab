#在运行时被创建
#可被赋值
#可当参数传入
#可当结果传出

def fib(n):
    '''return fibbonacci sequence '''
    return 1 if n < 2 else  fib(n-1) + fib(n-2) 

def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)

a = list(map(factorial,range(10)))

print(a)