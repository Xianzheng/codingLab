
def A(func):
    def inner():
        print('Hello')
        func()
    return inner


def B():
    print('word')
    
A(B)()