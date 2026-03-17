
num = int(input("enter a number="))

sum_even=0
sum_odd=0

i=1

while(i<=num):

    if i%2==0:
        print(i)
        sum_even+=i

    else:
        print(i)
        sum_odd+=i
    
    i+=1

print("sum even=",sum_even)
print("sum odd=",sum_odd)