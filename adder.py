""" 43.py Adder.py """


def adder(x,*y):
    if not y:
        return x
    else:
        return x + adder(*y)


str1 = 'String1'
str2 = 'String2'

list1 = ["Name1",1]
list2 = ["Name2",2]

float1 = 1.01
float2 = 2.02

int1 = 1
int2 = 2

strx = adder(str1,str2)
print(strx)
