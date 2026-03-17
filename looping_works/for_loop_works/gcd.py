num1=int(input("enter a number1="))
num2=int(input("enter a number2="))
gcd=0

if num1<num2:
    smallest=num1
else:
    smallest=num2

for i in range(1,smallest+1):

    if num1%i==0 and num2%i==0:

        gcd = i
        print(i)
print("greatest common divisor=",gcd)

