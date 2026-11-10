#a = lambda x , y :  x * y 
#print(a(3,4))


text = '''One sunny morning, Riya went to the park to enjoy the sunshine.
The park was beautiful, beautiful, and full of flowers.
She saw a little dog running, running, and running around the garden.
The dog was happy, happy, and very happy. Riya gave the dog some food, and the dog ate, ate, and ate happily.'''

a = text.split(" ")

mydict = {}

for i in a:
    if i in mydict:
        mydict[i] = mydict[i] + 1
    else:
        mydict[i] = 1
        
print(mydict)
    