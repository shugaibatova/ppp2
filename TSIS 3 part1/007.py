# Write a function that takes in a list of integers and returns True if it contains 007 in order
# def spy_game(nums): 
#         pass spy_game([1,2,4,0,0,7,5]) --> True 
#         spy_game([1,0,2,4,0,5,7]) --> 
#         True spy_game([1,7,2,0,4,5,0]) --> False
def spy_game(nums):
    counter0=0
    for n in nums:
        if(n==0):
            counter0+=1
        elif(counter0<3 and n==7):
            return True
    return False
print(spy_game([0,1,4,6,7,0]))