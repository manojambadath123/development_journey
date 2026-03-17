
stock_list1=[10,11,12,13,14,15]

stock_list2=[20,21,22,23,24,25]

stock_list1.extend(stock_list2)

print(stock_list1)

print(stock_list2)

updated_list=[]

for num in stock_list1:

    result = num+5
    updated_list.append(result)

print(updated_list)



