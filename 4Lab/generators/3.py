
# Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.


def div_3_4(N):
    for i in range(0,N+1):
        if(i%3==0 and i%4==0):
            yield i
n=int(input())
for a in div_3_4(n):
    print(a)