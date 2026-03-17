
num=int(input("enter a number="))
temp=num
reverse=0
while temp>0:
    c=temp%10
    reverse=reverse*10+c
    temp//=10
print("reversed num=",reverse)
if reverse==num:
        print(num,"is a palindrome") 
else:
        print(num," is not a palindrome") 