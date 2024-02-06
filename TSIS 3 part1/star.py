# Define a functino histogram() that takes a list of integers and prints a histogram to the screen.
# For example, histogram([4, 9, 7]) should print the following:
def star(n):
    h=[]
    for i in n:
        h.append (i*"*")    
    print(*h)
star([4,7,9])