
num = int(input("enter a number="))

sum_digits=0

while(num!=0):

    last_digit = num %10

    sum_digits+=last_digit

    num = num//10

print("sum of digits =",sum_digits)
