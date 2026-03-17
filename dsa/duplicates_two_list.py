

# lst1 = [10,11,12,13,14]

# lst2 = [8,11,11,14,15,16]

# for num in lst1:

#     if num in lst2:

#         print(num)



# lst1 = [10,11,12,13,14]

# lst2 = [8,11,11,14,15,16]

# lst1_set = set(lst1)

# lst2_set = set(lst2)

# print(lst1_set.intersection(lst2_set))



lst1 = [10,11,12,13,14]

lst2 = [8,11,11,14,15,16]

lst1.sort()

lst2.sort()

p1=0
p2=0

while(p1<len(lst1) and p2<len(lst2)):

    if lst1[p1] == lst2[p2]:

        print(lst1[p1])

        p1+=1
        p2+=1

    elif lst1[p1] < lst2[p2]:

        p1+=1

    else:

        p2+=1



