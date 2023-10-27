total = []
while True:
    inp = input()
    if inp == 'q':
        break
    
    lst = inp.split(" ",1)
    lst.insert(1,':')
    total.append(''.join(lst)+';')

for i in total:
    print(i)

