def deco(func):
    print('running deco',func)
    return func

@deco
def A():
    print('run A')

@deco
def B():
    print('run B')   

def main():
    print('run main')
    A()
    B()

if __name__ == '__main__':
    main()

# registry = [] 
# def register(func): 
#     print('running register(%s)' % func) 
#     registry.append(func) 
#     return func 
# @register 
# def f1():
#     print('running f1()')
# @register
# def f2():
#     print('running f2()')
# def f3(): 
#     print('running f3()')
# def main(): 
#     print('running main()')
#     print('registry ->', registry)
#     f1()
#     f2()
#     f3()
# if __name__=='__main__':
#     main() 