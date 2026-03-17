
day_num = int(input("enter a day number="))

if day_num>=1 and day_num<=5:
    print("working day")
elif day_num>=6 and day_num<=7:
    print("weekend")
else:
    print("invalid")