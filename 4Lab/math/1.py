# Python Math library
# Write a Python program to convert degree to radian.
# Input degree: 15
# Output radian: 0.261904

import math
degree=int(input())
x=math.pi
radian=(x/180)*degree
print(round(radian,6))