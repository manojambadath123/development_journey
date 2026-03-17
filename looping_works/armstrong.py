
num = int(input("enter a number="))

num_copy = num

result=0

num_length = len(str(num))

print("lenth of number=",num_length)

while(num!=0):

    last_digit = num % 10
    expo = last_digit**num_length
    result+=expo
    num=num//10

if num_copy==result:

    print(num_copy,"is an armstrong number")

else:

    print(num_copy,"is not an armstrong number")