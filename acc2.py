name = 'accenture'

mydict = {}

for i in name:
    if i in mydict:
        mydict[i] = mydict[i] + 1
    else:
        mydict[i] = 1

print(mydict)