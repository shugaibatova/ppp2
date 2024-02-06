# Write a program to solve a classic puzzle:
# We count 35 heads and 94 legs among the chickens and rabbits in a farm.
# How many rabbits and how many chickens do we have? 
# create function: solve(numheads, numlegs):
def solve(numheads,numlegs):
    rabbits=int(numlegs/2)-numheads
    chickens=numheads-rabbits
    print( rabbits,"rabbits,",chickens,"chickens")
    
solve(35,94)