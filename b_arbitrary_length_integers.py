"""
 This little Python program demonstrates that
 integers are not limited to e.g. 10 or 18 digits.
"""

#print('All powers of 2:')
n = 0
m = 1
inp=input("Enter the power of: ")
tillwhen= input("Enetr the upper value: ")
"""while len(str(m)) < int(tillwhen):
    print(inp +"^" + str(n) + ' = ' + str(m))
    n += 1
    m *= int(inp)
"""

while n <= int(tillwhen):
    print(inp +"^" + str(n) + ' = ' + str(m))
    n += 1
    m *= int(inp)
