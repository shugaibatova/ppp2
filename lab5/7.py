# Write a python program to convert snake case string to camel case string.

import re
a=open(r"row.txt",'r',encoding='UTF-8')
s=a.read()
def tocamel(snake):
    camel=re.sub(r"(?:^|_)([a-z])",lambda match: match.group(1).upper(), snake)
    return camel
print(tocamel(s))
