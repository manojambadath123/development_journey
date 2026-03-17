
minutes = int(input("enter your time of exercise in minutes="))

if minutes<30:
    print("insufficient exercise")
elif minutes>=30 and minutes<=60:
    print("good exercise")
elif minutes>60:
    print("intense exercise")