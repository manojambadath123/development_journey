


from copy import deepcopy,copy


original = [1, 2, [3, 4]]


shallow_copy = copy(original)


deep_copy = deepcopy(original)


shallow_copy[2][0] = 100


print( original)
print(shallow_copy)
print(deep_copy)


