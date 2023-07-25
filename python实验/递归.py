dic = {}
def f(n):
    if n < 2:
        return 1
    else:
        if n in dic:
            return dic[n]
        else:
            dic[n] = f(n-1) + f(n-2)
            return dic[n]
def f1(n):
    if n <= 2:
        return 1
    else:
        return f(n-2) + f(n - 1)


print(f1(100))