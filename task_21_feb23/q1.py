

tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')

print(f"Before swapping=Tuple 1: {tuple1}  Tuple 2: {tuple2}")


tuple1, tuple2 = tuple2, tuple1

print(f"After swapping: Tuple 1: {tuple1} Tuple 2: {tuple2}")