# Write a Python program to insert spaces between words starting with capital letters.

import re
a=open(r"row.txt",'r',encoding='UTF-8')
s=a.read()
def ins_space(text):
    capital=re.sub(r"([A-Z][a-z]+)", r" \1", text)
    return capital
print(ins_space(s))