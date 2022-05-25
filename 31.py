"""
    31.py uses the split and for and if 
"""

txt = 'We are now no longer the nights who say ni'
txtList = txt.split()
for itr in txtList:
    if itr[0].lower()=='n':
        print(itr, end=' ')
print() #for the EOL line
