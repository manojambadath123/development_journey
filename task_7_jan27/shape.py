
shape = input("enter a character of the shape=")

match shape:

    case "c":
        print("circle")
    case "r":
        print("rectangle")
    case "s":
        print("square")
    case _:
        print("invalid")
