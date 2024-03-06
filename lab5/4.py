

#Write a Python program to find the sequences of one upper case letter followed by lower case letters.
import re
a=open(r"row.txt", 'r', encoding='UTF-8') 
s=a.read()

def find_seq(text):
    pattern = r"[A-Z][a-z]+"
    match = re.findall(pattern, text)   
    return match

print(find_seq(s))