

# arr = [10,12,13,14,15]

# squares = []

# for num in arr:

#     sq = num**2
#     squares.append(sq)

# print(squares)

# arr = [10,12,13,14,15]

# squares = [num**2 for num in arr]

# print(squares)

# arr = [10,12,13,14,15]

# cubes = [num**3 for num in arr]

# print(cubes)

# arr = [10,12,13,14,15]

# add_ten = [num+10 for num in arr ]

# print(add_ten)

arr = [10,12,13,14,15]

add_ten = [num+10 for num in arr if num>14]

print(add_ten)

