"""
    32.py FizzBuzz 
"""

numRange = range(1,101)
for elem in numRange:
    if elem%3==0 and elem%5==0: #check div 5
        print('FizzBuzz',elem)
    elif elem%3==0:
        print('Fizz',elem)
    elif elem%5==0:
        print('FizzBuzz', elem)
        
    
