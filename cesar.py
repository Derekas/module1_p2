from typing import Text

def encrypt(text,s):
    text=text.upper()
    
    result=""
    for i in text:
        if i.isspace():
            result+=""
            continue
        result+= text[(text.index(i)+shift)%len(text)]
    return result

text=input("Introduce un texto")
shift=int(input("Introduce el shift"))
print(encrypt(text,shift))
