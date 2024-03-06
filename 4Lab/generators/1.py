
#Create a generator that generates the squares of numbers up to some number N.
def sqr(N):
    for i in range(1,N+1):
        yield i**2
n=int(input())
for a in sqr(n):
    print(a)
