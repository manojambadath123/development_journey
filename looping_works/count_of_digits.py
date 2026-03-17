
num = int(input("enter a number="))
digit_count=0
while(num!=0):

    last_digit = num%10
    digit_count+=1
    num = num//10

print("digit count=",digit_count)

