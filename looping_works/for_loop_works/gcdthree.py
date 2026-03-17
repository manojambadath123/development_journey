num1=int(input("enter a number1="))
num2=int(input("enter a number2="))
num3=int(input("enter a number3="))
gcd=0

if num1<num2 and num1<num3:
    smallest=num1
elif num2<num1 and num2<num3:
    smallest=num2
else:
    smallest=num3

for i in range(1,smallest+1):

    if num1%i==0 and num2%i==0 and num3%i==0:

        gcd = i
        print(i)
print("greatest common divisor=",gcd)
