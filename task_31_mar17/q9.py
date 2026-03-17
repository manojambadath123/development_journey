

numbers = [[1, 2],
           [3, 4], 
           [5, 6]
           ]


numbers_copy = numbers[::]


numbers_copy[0][0] = 100


print(numbers)
print(numbers_copy)
