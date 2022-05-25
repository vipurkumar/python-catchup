""" mymod.py 51 """


def countLines(path):
    file = open(path , 'r')

   # length = len(file.readlines())
    l=0
    for el in file:
        l+=1
    file.close()
    return(l)
    

def countChars(path):
    file = open(path , 'r')
    numChars = 0
    for el in file:
        numChars+=len(el)
    file.close()
    return numChars

def countCharswfr(path):
    file = open(path , 'r')
    numChars = 0
    chars = file.read()
    for el in chars:
        numChars = numChars +1
    file.close()
    return numChars


def test(path):
    path = 'mymod.py'
    print(f'Lines: {countLines(path)},',f'Chars: {countChars(path)}', f'Charswfr: {countCharswfr(path)}')
    
    
    

