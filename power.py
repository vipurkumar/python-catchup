"""
    35.py Logic alternatives
"""
"""
L = [1,2,4,8,16,32,64]
X = 5
found = False
i= 0
while not found and i < len(L):
    if 2 ** X == L[i]:
        found = True
    else:
        i = i+1
    if found:
        print('at index',i)
    else:
        print(X,'not found')
"""
"""
L = [1,2,4,8,16,32,64]
X = 5
i= 0
while  2 ** X != L[i]:
    i=i+1
    print(X,'not found')
print('at index',i)

"""

L = [1,2,4,8,16,32,64]
X = 5
found = False
i= 0
for index,value in enumerate(L):
    if 2 ** X == value:
        print('at index',index)
    else:
        print(index,'not found')







        
