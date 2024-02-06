# You are given list of numbers separated by spaces.
# Write a function filter_prime which will take list of numbers as an agrument
# and returns only prime numbers from the list.
def space(n):
    numbers=[int(i) for i in n.split()]
    def filter_Prime(num):
        if(num<2):
            return False
        for i in range(2,num//2+1):
            if(num%i==0):
             return False
        return True
    return [x for x in numbers if filter_Prime(x)]

print(space("1 2 3 4 5 6 7 8 9"))

