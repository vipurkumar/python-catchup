"""
    33.py ASCII for loop and list assignments
"""
sum=0
S = 'This is a String'
for elem in S:
    print(elem,ord(elem),sep='::')
    sum=sum + int(ord(elem))
print('Sum of all ASCII =',sum)

y = [ord(el) for el in S]
print(y)

x = map(ord,S)

for i in x:
    print(i)

