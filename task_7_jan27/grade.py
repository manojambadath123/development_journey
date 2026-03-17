
grade = input("enter a grade=")

match grade:

    case "A":
        print("excellent")
    case "B":
        print("very good")
    case "C":
        print("good")
    case "D":
        print("average")
    case "F":
        print("below average")
    case _:
        print("fail")