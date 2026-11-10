mydict = {}

def adddict(key:str='yhem', values:int=0):
    global mydict   
    mydict[key] = values

def removdict(rst):
    global mydict  
    if mydict is None:
        raise "empty dict" 
    if rst in mydict:
        mydict.pop(rst) 


    
    

def findSudict(x):
    if x in mydict:
        return True
    else:
        return False
    
    
    
adddict('Juhi',23)
adddict('Ruhi',13)
adddict('pihu',3)
print(mydict)

removdict('pihu')
print(mydict)

print(findSudict('Juhi'))
print(mydict['Juhi'])