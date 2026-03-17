

numbers = [10,11,12,13,14,15,17,3,2,1,3,4]

even_list =[]
odd_list = []

for num in numbers:

    if num%2==0:

        even_list.append(num)

    else:

        odd_list.append(num)

print("even list=",even_list)
print("odd list=",odd_list)