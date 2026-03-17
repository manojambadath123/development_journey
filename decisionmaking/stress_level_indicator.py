
stress_score = int(input("enter your stress score="))

# if stress_score>=1 and stress_score<=3:
#     print("low stress")
# elif stress_score>=4 and stress_score<=6:
#     print("moderate")
# elif stress_score>=7 and stress_score<=10:
#     print("high stress")

if stress_score<=3:
    print("low stress")
elif  stress_score<=6:
    print("moderate")
elif  stress_score<=10:
    print("high stress")
else:
    print("invalid")