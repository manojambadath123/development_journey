

num = int(input("enter a number="))
temp=num
reverse=0

while(num!=0):

    ldigit = num%10
    reverse=reverse*10+ldigit
    num=num//10

if (reverse==temp):

    print("number palindrome")

else:

    print("not number palindrome")



