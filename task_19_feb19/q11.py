

numbers = [10,20,30,20,40,10,50]

for num in numbers:

    num_count = numbers.count(num)

    if num_count>1:

        numbers.remove(num)

print(numbers)