import functools

def a(x):

   return 0 if x < 1 else x + a(x - 1)
    
print(a(400))