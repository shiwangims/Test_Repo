text = "madam1"

if text == text[::-1]:
    print("Palindrome1")
else:
    print("Not Palindrome")
    


def palindrome(text):
    
    for i in range(int(len(text)/2)):
        if text[i] == text[len(text)-i-1]:
            continue
        
        else:
            print("Not Palindrome")
            return
    return 'Palindrome'

    
t= palindrome("radar")
print(t)