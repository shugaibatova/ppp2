# Write a program which can filter prime numbers in a list by using filter function.
# Note: Use lambda to define anonymous functions.
def filter_prime(x):
    if(x <2):
        return False
    for i in range(2, x):
        if(x % i == 0):
            return False
    return True
class List():
    def __init__(self, n):
        self.a = n
    def is_prime(self):
        return list(filter(lambda x : filter_prime(x), self.a))
numbers = List([1,2,4,7,9,11,14,15])
print(numbers.is_prime())



