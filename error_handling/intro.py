

# def div(num1,num2):

    # print(num1/num2)


# n1 = int(input("enter num 1="))
# n2 = int(input("enter num 2="))

# div(n1,n2)  # run time error if n1=0 

# print("data base commit")
# print("file write")


# lst =[1,2,3,4,5]

# index = int(input("enter index pos="))

# print(lst[index]) # rum time error if index is >=5

# run time errors eg / by zero , file not found , index error,key error

#error handling keywords 

# try 
# catch   java keywords
# finally
# throw


# try      python key word block
# except
# finally


# raise   keywords
# assert
    
"""
try:
     doubtful code

except:

    handling code

"""

# n1 = int(input("enter num 1="))
# n2 = int(input("enter num 2="))
# try:

#     result = (n1/n2) 

#     print("result= ",result)

# except Exception as e:

#     print(e)

# print("data base commit")
# print("file write")




# lst =[10,11,12,13,14]

# index = int(input("enter index pos="))


# try:

#     print(lst[index])

# except Exception as e:


#     print(e)


# print("database commit")
# print("file write")


# n1 = int(input("enter num 1="))
# n2 = int(input("enter num 2="))
# try:

#     result = (n1/n2) 

#     print("result= ",result)

# except Exception :

#     n2 = int(input("enter num 2="))
#     result = (n1/n2) 

#     print("result= ",result)

    


# finally:
#         print("data base commit")
#         print("file write")


# lst =[10,20,30,40,50,60]

# index = int(input("enter index="))

# try:

#     print(lst[index])

# except Exception as e:

#     index = int(input("enter index="))
#     print(lst[index])

# finally:
#     print("file operation.......")
#     print("db...,commit")



age = int(input("enter age"))

if age<18:

    raise Exception("invalid age")

else:

    print("access granted")



# password = input("enter password=")

# if len(password)<6:

#     raise Exception("invalid password")

# else:

#     print("access granted")