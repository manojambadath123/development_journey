
screen_hours = int(input("enter your screen hours="))

if screen_hours<2:
    print("healthy usage")
elif screen_hours>=2 and screen_hours<=5:
    print("moderate usage")
elif screen_hours>5:
    print("excessive usage")