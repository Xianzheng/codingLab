a = [1,2,3,4,5]

del a #删除的是变量a， [1,2,3,4,5]因为访问不到被自动回收

import weakref
a = {1,2,3,4,5}
c = weakref.ref(a)
print(c())
a = {7,8}
print(c())