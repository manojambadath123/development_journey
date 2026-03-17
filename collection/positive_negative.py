
number = [-1,-1,10,11,12,13,-13,-15,4,5]

positive_list=[]
negative_list=[]

for num in number:

    if num>0:

        positive_list.append(num)

    elif num<0:

        negative_list.append(num)

print("positive list=",positive_list)
print("negative list=",negative_list)