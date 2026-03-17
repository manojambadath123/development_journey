
num=int(input("enter a number="))#123
reverse=0
while num>0:
    c=num%10
    reverse=reverse*10+c
    num//=10
print("reversed num=",reverse)   