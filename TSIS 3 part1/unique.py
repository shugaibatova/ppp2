# Write a Python function that takes a list and returns a new list with unique elements of the first list.
#  Note: don't use collection set.
def unique(list):
    new_list=[]
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list
a=[1,2,3,4,5,3]
print(unique(a))