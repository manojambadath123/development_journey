num = int(input("enter a number="))



expense_month = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,-11000,-1]

for exp in expense_month:

    num_copy = num

    result=0

while(num!=0):

    last_digit = num%10
    result = result*10+last_digit
    num=num//10

if num_copy==result:

    print(num_copy,"is a number palindrome")
else:
    print(num_copy,"is not a number palindrome")


