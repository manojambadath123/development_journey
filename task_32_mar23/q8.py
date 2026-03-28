


num = int(input("enter a number="))

sum_digit =0

while(num!=0):

    ldigit = num%10
    sum_digit+=ldigit
    num=num//10

print(sum_digit)
