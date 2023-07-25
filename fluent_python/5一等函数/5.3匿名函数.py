# lambda 函数的定义体中不能赋值，也不能使用 while
#和 try 等 Python 语句。

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']

sorted(fruits, key=lambda word: word[::-1])

# 除了作为参数传给高阶函数之外，Python 很少使用匿名函数。由于句法
#上的限制，非平凡的 lambda 表达式要么难以阅读
