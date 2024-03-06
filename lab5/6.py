# Write a Python program to replace all occurrences of space, comma, or dot with a colon.


import re 
a=open(r"row.txt",'r',encoding='UTF-8')
s=a.read()
def replace(text):
    pattern=r"[,.]"
    r=re.sub(pattern,":",text)
    return r
print(replace(s))