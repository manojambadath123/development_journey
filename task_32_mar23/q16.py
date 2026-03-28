


# lst1 = [1,2,3,4,5]

# set_a = set(lst1)

# lst2 = [4,5,6,7,8]

# set_b = set(lst2)

# set_i = set_a.intersection(set_b)

# print(set_i)

lst1 = [1,2,3,4,5]

lst2 = [4,5,6,7,8]

lst3=[]

for num in lst1:

    if num in lst2:

        lst3.append(num)
print(lst3)



