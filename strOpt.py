
mystr = 'hi '

def addstring(substr):
    global mystr   
    mystr = mystr + substr



def removStr(rst):
    global mystr  
    if mystr is None:
        raise "empty string" 
    if rst in mystr:
        mystr = mystr.replace(rst,'')
    

def reverseString(abc):
    global mystr 
    mystr = abc[::-1]
    

def findSuString(x):
    if x in mystr:
        return True
    else:
        return False



print(addstring('welcome '))
print(mystr)

# remove wel 

removStr('wel')
print(mystr)

reverseString('Python')
print(mystr)

y = findSuString('on')
print(y)
print(y)


