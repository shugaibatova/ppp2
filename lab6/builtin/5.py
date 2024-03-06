# Write a Python program with builtin function that returns True if all elements of the tuple are true.
def all_elements_true(tuple_to_check):
    return all(tuple_to_check)
tuple1 = (True, True, True)
tuple2 = (True, False, True)
tuple3 =  (False,False,False)

result1 = all_elements_true(tuple1)
result2 = all_elements_true(tuple2)
result3 = all_elements_true(tuple3)


print("All elements in tuple1 are True:", result1)
print("All elements in tuple2 are True:", result2)
print("All elements in tuple3 are True:", result3)

