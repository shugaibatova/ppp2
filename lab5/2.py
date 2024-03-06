# Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
import re
a = open("row.txt", "r", encoding="UTF-8")
s = a.read()
print(s)

def ab23(text):
    pattern = "ab{2,3}"
    if re.fullmatch(pattern, text):
        return "Match found"
    else:
        return "No match"
    
print(ab23(s))