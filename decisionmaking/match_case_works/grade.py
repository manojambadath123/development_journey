
grade = input("enter a grade=")

match grade:

    case "A":
        print("excellent")
    case "B":
        print("good")
    case "C":
        print("average")
    case _:
        print("fail")