#参数传递时，如果是普通传递对参数没有影响
#如果参数是可变数据类型，就可能出现问题

a = [1,2]
b = [3,4]
c = 1
d = 2
def add(a,b):
    a += b
    return a

print(add(a,b))
print(a,b)
print(add(c,d))
print(c,d)

#不要使用可变类型作为参数的默认值

class Train():
    def __init__(self,p):
        self.p = list(p)

    def pick(self,name):
        self.p.append(name)

    def drop(self):
        self.p.pop()

lst = ['a','b','c','d']

train = Train(lst)
train.drop()
train.drop()
print(lst)