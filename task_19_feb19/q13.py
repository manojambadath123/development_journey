

list = [10,45,23,89,67,89,34]

largest = second_largest= list[0]

for num in list:

    if num>largest:

        second_largest=largest
        largest=num
    elif num>second_largest and num!=largest:
        second_largest = num

        
print("largest number=",largest)
print("second largest number=",second_largest)