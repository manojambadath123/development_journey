
# mapping using map()



lst =[10,11,12,13,14,15]

def square(n):

    return n**2

squares = list(map(square,lst))

# print(squares)

map_squares = list(map(lambda n:n**2,lst))

print(map_squares)

map_cube = list(map(lambda n : n**3,lst))

# print(map_cube)

comp_cube = [num**3 for num in lst]

# print(comp_cube)


#filter using filter() => if condition is specified with no return value


def is_even(num):

    return num%2==0

evens = list(filter(is_even,lst))

# print(evens)

evens = list(filter(lambda n : n%2==0 ,lst))

# print(evens)

comp_even = [num for num in lst if num%2==0]

# print(comp_even)



#  reduce()  => fuctools.py

# from functools import reduce
# from json import load
# from json import dump
# from builtins import print
# from builtins import input
# from sklearn.metrics import f1_score
# from django.contrib.auth.models import User
