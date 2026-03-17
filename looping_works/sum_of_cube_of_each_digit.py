
num = int(input("enter a number="))
sum_digit=0
while(num!=0):

    last_digit = num%10
    # cube_digit = last_digit**3
    sum_digit = sum_digit + last_digit**3
    # sum_digit+=cube_digit
    num= num//10

print("sum of cube of each digit=",sum_digit)
