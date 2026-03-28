

cube = lambda num: num**3

print(cube(2))

odd_even = lambda n:"even" if n%2==0 else "odd"

print(odd_even(10))
print(odd_even(11))

lst=[1,2,3,4]

map_squares = list(map(lambda n:n**2,lst))

print(map_squares)


evens = list(filter(lambda n : n%2==0 ,lst))

print(evens)