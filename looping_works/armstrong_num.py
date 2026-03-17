
num = int(input("enter a number="))
digit_count=0
temp1=temp2=num
sum_digit=0
while(temp1!=0):

    last_digit1=temp1%10
    digit_count+=1
    temp1=temp1//10

print("digit count=",digit_count)

while(temp2!=0):

    last_digit2 = temp2%10
    cube_digit = last_digit2**digit_count
    sum_digit+=cube_digit
    temp2=temp2//10

print(sum_digit)

if num==sum_digit:

    print(num,"is a armstrong number")
else:
    print(num,"is not a armstrong number")


