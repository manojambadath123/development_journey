

# numbers=[10,10,20,30,10,40,50,60,50,30,10]

# duplicates_list=[]

# for num in numbers:

#     if numbers.count(num)>1 and num not in duplicates_list:

#         duplicates_list.append(num)


# print(duplicates_list)

numbers=[10,10,20,30,10,40,50,60,50,30,10]

st=set()

for num in numbers:

    num_count=numbers.count(num)

    if num_count>1:

        st.add(num)

print(st)


   

   