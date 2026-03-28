


lst1 = [1,2,2,3]

lst2 = [4,5,6,2]

lst3=[]

lst1.extend(lst2)

print(lst1)

for num in lst1:

    if num not in lst3:

        lst3.append(num)

print(lst3)

