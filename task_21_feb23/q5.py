

tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')


combined_tuple = tuple1 + tuple2  

print("combined tuple=",combined_tuple)


reversed_tuple_slicing = combined_tuple[::-1]
print(f"Reversed tuple using slicing={reversed_tuple_slicing}")

reversed_iterator = reversed(combined_tuple)

reversed_tuple_function = tuple(reversed_iterator)
print(f"Reversed tuple using reversed() function= {reversed_tuple_function}")