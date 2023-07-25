'''
#错误
a = 1
b = 2

def A():
    print(a)
    print(b)
    b = 3

A()

#UnboundLocalError: local variable 'b' referenced before assignment
'''

#在func中没强调就是个局部变量，强调全局变量用global
a = 1
b = 2

def A():
    global b
    print(a)
    print(b)
    b = 3
    

A()
print(b)