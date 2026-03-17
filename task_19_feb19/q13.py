

list = [10,45,23,89,67,89,34]

largest = list[0]

for num in list:

    if num>largest:

        second_largest=largest
        largest=num

        
print("largest number=",largest)
print("second largest number=",second_largest)