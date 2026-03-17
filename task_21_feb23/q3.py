
tuple1 = (1,2,3,4,5,6)

print(tuple1)

even_list=[]

for tp in tuple1:

    if tp%2==0:

        even_list.append(tp)

print(even_list)

tuple2 = tuple(even_list)

print(tuple2)




