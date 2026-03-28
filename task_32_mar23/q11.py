

lst = [10,20,4,45,99]

largest = second= lst[0]

for num in lst:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print(largest)
print(second)