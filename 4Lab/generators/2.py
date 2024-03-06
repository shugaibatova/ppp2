
# Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.

def even(N):
    for i in range(0,N+1):
        if(i%2==0):
            yield i
n=int(input())
even_n=even(n)
even_list=list(even_n)

print(*even_list,sep=",")