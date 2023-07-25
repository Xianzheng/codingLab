'''
class A():

    def __init__(self):

        self.series = []

    def __call__(self,num):
        self.series.append(num)
        return sum(self.series) / len(self.series)
    
avg = A()
print(avg(10))
print(avg(12))
print(avg(15))
'''
'''
def a():
    lst = []
    def avg(num):
        #只有在赋值时才需要nonlocal变成自由变量
        lst.append(num)
        average = sum(lst)/len(lst)
        return average
    return avg

avg = a()
print(avg(10))
print(avg(20))
print(avg(30))
'''



