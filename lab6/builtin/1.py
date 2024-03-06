# Write a Python program with builtin function to multiply all the numbers in a list

def factorial(numbers):
    n = 1
    for i in numbers:
        n *= i
    return n

numbers = [1, 2, 3, 4, 5, 6]
result = factorial(numbers)
print(result)