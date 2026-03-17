

# function with no parameter and no return value
# function with parameter  and no return value
# function with parameter and return value

def say_hello():

    print("hello")


# say_hello()
    

def say_hai():

    print("hai")


# say_hai()
# say_hai()
# say_hai()
    



def say_morning():

    print("good morning")

# say_morning()
# say_morning()
# say_morning()

# from builtins import *

# function with parameter  and no return value

def addition(num1,num2):

    result = num1+num2

    print("sum=",result)


# addition(100,200)
# addition(500,700)
#addition(100) 

     
def subtraction(num1,num2):

    result=num1-num2

    print("subtraction=",result)


# subtraction(100,50)
# subtraction(50,100)

def cube(num):

    result=num**3

    print("cube=",result)

# cube(2)
# cube(3)
# cube(4)

def max_two(num1,num2):

    if num1>num2:

        print(f"{num1} is larger than {num2}")

    else:

        print(f"{num2} is larger than {num1}")

# max_two(50,100)
# max_two(100,50)


def last_digit_max(num1,num2):

    last_digit_num1=num1%10
    last_digit_num2=num2%10

    if last_digit_num1>last_digit_num2:

        print(num1)

    elif last_digit_num2>last_digit_num1:

        print(num2)

    else:
        print(num1,num2)


# last_digit_max(127,892)
# last_digit_max(127,98)
# last_digit_max(127,97)

def smart_sub(n1,n2):

    if n1>n2:

        return n1-n2
    
    else:

        return n2-n1

# print(smart_sub(10,20))
# print(smart_sub(20,10))


def odd(num):
    is_odd = True

    if num%2!=0:

        is_odd = True

        return is_odd

    else:

        is_odd = False

        return is_odd


# print(odd(3))
# print(odd(4))


def even(num):
    is_even = True
    
    if num%2==0:

        is_even = True

        return is_even

    else:

        is_even = False

        return is_even


# print(even(3))
# print(even(4))


def positive(num):
    is_positive = True
    
    if num>0:

        is_positive = True

        return is_positive

    else:

        is_positive = False

        return is_positive


# print(positive(3))
# print(positive(-3))


def zero(num):
    is_zero = True
    
    if num==0:

        is_zero = True

        return is_zero

    else:

        is_zero = False

        return is_zero


# print(zero(0))
# print(zero(3))
# print(zero(-3))


def exponent(base,pow=2):

    result = base**pow

    return result

# print(exponent(10,pow=3))


def calculator(n1,n2,op="+"):

    if op=="*":

        mult=n1*n2
        return mult

    elif op=="/":

        div = n1/n2
        return div

    elif op=="-":

        sub = n1-n2
        return sub

    elif op=="+":

        add = n1+n2
        return add

# print(calculator(10,2,"*"))
# print(calculator(10,2,"-"))
# print(calculator(10,2,"/"))
# print(calculator(10,2,"+"))
# print(calculator(10,2))

#fibonacci series

def fibonacci_number(number):

    is_fibo =False

    previous = 0
    current = 1
    next = previous+current

    while(next<=number):


        

        previous=current
        current=next

        next = previous + current
    
        if next==number:

            is_fibo = True

            return is_fibo  # or break
        
        
        
    return is_fibo



print(fibonacci_number(3))
print(fibonacci_number(5))
print(fibonacci_number(10))


def fibonacci_number(number):


    previous = 0
    current = 1
    next = previous+current

    print(previous,current,next,end=" ")

    while(next<number):

         

        previous=current
    
        current=next

        next = previous + current
       

        print(next,end=" ")
    
       

print(fibonacci_number(3))
# print(fibonacci_number(5))
# print(fibonacci_number(10))


def fibonacci_number(number):


    previous = 0
    current = 1
    next = previous+current

    print(previous,current,next,end=" ")

    while(next<=number-3):

        
        

        previous=current
        current=next

        next = previous + current

        print(next,end=" ")

        

        


        
       

print(fibonacci_number(3))
print(fibonacci_number(5))
# print(fibonacci_number(10))