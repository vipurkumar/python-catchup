"""
    37.py File Operations
"""

#{'CONO': 0, 'CONAME': 0, 'COSTREET': 0, 'COSTRNO': 0, 'COTOWN': 0, 'COTOWNNO': 0, 'COCOUNTR': 0}
d = {} 
f = open(r'C:\Users\Duser\Desktop\Python\Vipur\companies.csv' , 'r')

header = f.readline().rstrip('\n').split(',')
header = header[1:]

for line in f:
    data = line.rstrip('\n').split(',')
    key = data[0]
    inner = data[1:]
    inner_dict = dict(zip(header, inner))
    d[key] = inner_dict
    print(f'Key {key}')

f.close()

