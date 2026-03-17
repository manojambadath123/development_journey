
num = int(input("enter a number="))
sum_digit=0
while(num!=0):

    last_digit = num%10
    sum_digit+=last_digit
    num=num//10
print("sum of digits=",sum_digit)
