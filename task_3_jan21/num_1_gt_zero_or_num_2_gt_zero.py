# Read the two numbers from the user
num1_str = input("Enter the first number: ")
num2_str = input("Enter the second number: ")

# Convert the input strings to integers
try:
    num1 = int(num1_str)
    num2 = int(num2_str)

    # Calculate the boolean result
    result = num1 > 0 or num2 > 0

    # Print the result
    print(f"The result of num1 > 0 or num2 > 0 is: {result}")

except ValueError:
    print("Invalid input. Please enter valid integer numbers.")