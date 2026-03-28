


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


try:
    num1 = int(input("Enter first number= "))
    num2 = int(input("Enter second number="))

    result = num1 / num2
    print("Result=", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

except ValueError:
    print("Error: Invalid input! Please enter numbers only.")

except Exception as e:
    print("Unexpected error:", e)

finally:
    print("Program execution completed.")