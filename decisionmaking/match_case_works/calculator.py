
num1 = int(input("enter num1="))
num2 = int(input("enter num2="))

operator = input("enter a operator=")

match operator:

    case "+":
        sum = num1 + num2
        print(sum)
    case "-":
        diff = num1 - num2
        print(diff)
    case "*":
        mult = num1*num2
        print(mult)
    case "/":
        div = num1/num2
        print(div)
    case "%":
        mod = num1 % num2
        print(mod)
    case "**":
        exp = num1**num2
        print(exp)
    case "//":
        floor = num1//num2
        print(floor)
    case _:
        print("invalid operator")