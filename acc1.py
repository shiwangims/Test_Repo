text = '''One sunny morning, Riya went to the park to enjoy the sunshine.
The park was beautiful, beautiful, and full of flowers.
She saw a little dog running, running, and running around the garden.
The dog was happy, happy, and very happy. Riya gave the dog some food, and the dog ate, ate, and ate happily.
After some time, Riya went home, home, and home with a big smile. It was a beautiful, beautiful, beautiful day!'''

list = text.split(" ")

mydict = {}

for i in list:
    if i in mydict:
        mydict[i] = mydict[i] + 1
    else:
        mydict[i] = 1


print(mydict)

