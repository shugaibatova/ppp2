# Write a function that accepts string from user and print all permutations of that string.
from itertools import permutations 
def per(s):
    for i in permutations(s):
        print(''.join(i))
per("shugyla") #as example
