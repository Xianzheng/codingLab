'''
l1 = [1,2,3]

l2 = l1

print(l1 == l2)#True
print(l1 is l2)#True
'''
'''
l1 = [1,2,3]

l2 = list(l1)

print(l1 == l2)#True
print(l1 is l2)#False
'''
'''
l1 = [1,2,3]

l2 = list(l1)

l1.remove(1)

print(l1,l2)
#副本对主体没有影响
'''

l1 = [3, [66, 55, 44], (7, 8, 9)]
l2 = list(l1) # ➊
l1.append(100) # ➋
l1[1].remove(55) # ➌
print('l1:', l1)
print('l2:', l2)
l2[1] += [33, 22] # ➍
l2[2] += (10, 11) # ➎
print('l1:', l1)
print('l2:', l2)
