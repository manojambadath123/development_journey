
numbers=[1,1,2,3,3,4,5]

duplicates_list=[]

for num in numbers:

    if numbers.count(num)>1 and num not in duplicates_list:

        duplicates_list.append(num)


print(duplicates_list)