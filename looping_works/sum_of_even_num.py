
num = int(input("enter a number="))

sum=0

i=1 #i=0

while(i<=num):

    if i%2==0:
        print(i)
        sum=sum+i

    i+=1 #i+=2

print("sum of even num from 1 to ",num,"is",sum)