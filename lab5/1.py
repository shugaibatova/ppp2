# Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.


import re
a = open("row.txt", "r", encoding="UTF-8")
s = a.read()
print(s)
reg = r"a[b]*"
print(re.findall(reg, s))
