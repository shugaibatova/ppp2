# Write a Python program that invoke square root function after specific milliseconds.
# Sample Input:
# 25100
# 2123
# Sample Output:
# Square root of 25100 after 2123 miliseconds is 158.42979517754858
import time
import math
def root(n, delay):
    sec = delay / 1000.0
    time.sleep(sec)
    
    result = math.sqrt(n)
    print(f"The square root of {n} after {delay} miliseconds is {result}.")
example = int(input())
delay = int(input())
root(example, delay)