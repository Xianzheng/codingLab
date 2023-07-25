'''
Python 3 引入了 nonlocal 声明。它的作用是把变
量标记为自由变量，即使在函数中为变量赋予新值了，也会变成自由变
量。
'''

def b():
    count = 0
    total = 0
    def average(num):
        #在赋值时需要nonlocal变成自由变量
        nonlocal count, total
        total += num
        count += 1
        return total / count
    return average

avg = b()
print(avg(10))
print(avg(20))
print(avg(30))