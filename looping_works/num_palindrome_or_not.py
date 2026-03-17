
num = int(input("enter a number="))

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



