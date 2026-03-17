
# num = int(input("enter a number="))

# while(num!=0):

#     last_digit = num%10
#     print(last_digit)
#     num = num//10
    

num = int(input("enter a number="))

result = 0

while(num!=0):

    last_digit = num%10
    result=result*10+last_digit
    num = num//10
    
print(result)

while(result!=0):

    last_digit=result%10
    print(last_digit,end="")
    result=result//10