
# num=int(input("enter a number="))
# digitcount=0
# while num>0:
#     digitcount+=1
#     num//=10
# print("digit count=",digitcount)

num=int(input("enter a number="))

digitcount=0
while num>0:
    c=num%10
    print(c)
    digitcount+=1
    num//=10
print("digit count=",digitcount)

