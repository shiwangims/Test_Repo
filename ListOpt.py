
mylist = []

def addlist(substr):
    global mylist   
    mylist.append(substr)

def removlist(rst):
    global mylist  
    if mylist is None:
        raise "empty list" 
    if rst in mylist:
        mylist.remove(rst) 

def reverselist():
    global mylist 
    f = []
    for i in range(len(mylist)-1,-1,-1):
        f.append(mylist[i])
    print( f)
    
    

def findSulist(x):
    if x in mylist:
        return True
    else:
        return False
       

addlist("Apple")
addlist("Banana")
#print(mylist)


#removlist("Apple")
#print(mylist)

addlist("Guava")
print(mylist)

print(reverselist())
print(findSulist("av"))
