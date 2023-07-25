#高阶函数保活map、filter、reduce 
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']

result = sorted(fruits,key = len)

from functools import reduce
# 归约
result = reduce(lambda a,b: a + b,[1,2,3,4,5,6,7,8,9,10])

print(result)