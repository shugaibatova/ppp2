# Write a Python program to calculate the area of regular polygon.
# Input number of sides: 4
# Input the length of a side: 25
# The area of the polygon is: 625
import math
n=int(input())
l=int(input())
a=(l/2*math.tan(math.pi/n))
P=n*l
area=(a*P)/2
print(round(area))