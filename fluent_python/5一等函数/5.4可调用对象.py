'''
除了用户定义的函数，调用运算符（即 ()）还可以应用到其他对象
上。如果想判断对象能否调用，可以使用内置的 callable() 函数。
Python 数据模型文档列出了 7 种可调用对象。
'''

def getlist():
    for i in range(10):
        yield i

print(list(getlist()))