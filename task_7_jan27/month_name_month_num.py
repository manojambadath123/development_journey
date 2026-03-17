
month_num = int(input("enter a month number="))

match month_num:

    case 1:
        print("JAN")
    case 2:
        print("FEB")
    case 3:
        print("MAR")
    case 4:
        print("APR")
    case 5:
        print("MAY")
    case 6:
        print("JUN")
    case 7:
        print("JUL")
    case 8:
        print("AUG")
    case 9:
        print("SEP")
    case 10:
        print("OCT")
    case 11:
        print("NOV")
    case 12:
        print("DEC")
    case _:
        print("invalid")