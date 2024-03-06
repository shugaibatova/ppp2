# Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and 
#lower case letters

def count(text):
    counter_upper = 0
    counter_lower = 0
    for char in text:
        if char.isupper():
            counter_upper += 1
        elif char.islower():
            counter_lower += 1
    
    return counter_upper, counter_lower

example = str(input())
print(count(example))