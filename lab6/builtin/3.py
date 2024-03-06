# Write a Python program with builtin function that checks whether a passed string is palindrome or not.

def palin(text):
    text = text.lower()
    inverse = text[::-1]
    return text == inverse

example = str(input())
if palin(example):
    print("YES")
else:
    print("NO")