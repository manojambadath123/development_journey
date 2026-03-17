
score = int(input("enter your energy score count="))

if score>=1 and score<=3:
    print("low energy")
elif score>=4 and score<=7:
    print("moderate energy")
elif score>=8 and score<=10:
    print("high energy")
else:
    print("invalid")