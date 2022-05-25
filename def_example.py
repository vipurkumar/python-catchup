

l = [1,2,3]
n = l[:]
print(f'l {l}')
print(f'n {n}')
def alter(p):
    p[0] = 'new'
    return p

print(f'altered l {alter(l)}')
print(f'altered n {alter(n)}')
