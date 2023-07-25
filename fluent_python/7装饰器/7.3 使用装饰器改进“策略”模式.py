lst = []

def deco(func):
    print('run deco at',func)
    lst.append(func())
    return func

@deco
def A():
    return 1
@deco
def B():
    return 2
@deco
def C():
    return 3

print(max(i for i in lst))

