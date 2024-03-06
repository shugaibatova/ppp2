# Write a Python program to convert a given camel case string to snake case.
import re
a=open(r"row.txt",'r',encoding='UTF-8')
s=a.read()
def tosnake(camel):
    snake = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", camel)
    snake = snake.lower()
    return snake

print(tosnake(s))