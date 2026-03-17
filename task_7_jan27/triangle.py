
char = input("enter a character=")

match char:

    case "e":
        print("equilateral")
    case "i":
        print("isosceles")
    case "s":
        print("scalene")
    case _:
        print("invalid")
