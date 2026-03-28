


try:
        
        num1 = int(input("Enter first number1="))
        num2 = int(input("Enter second number2="))

        result = num1 / num2
        print("Result=", result)

except ZeroDivisionError:
        print("Error! Division by zero is not allowed.")

except ValueError:
        print("Error! Invalid input. Please enter numeric values.")

finally:
        print("Execution completed.")

