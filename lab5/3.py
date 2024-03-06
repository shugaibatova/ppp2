# Write a Python program to find sequences of lowercase letters joined with a underscore.

import re
a=open(r"row.txt", 'r', encoding='UTF-8')
s=a.read()

def check(text):
    return re.findall(r"\b[a-z]+_[a-z]+\b", text)

print(check(s))