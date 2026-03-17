rating = float(input("enter  a rating="))

if rating<4.0:
    print("unsatisfied")
elif rating>=4.0 and rating<4.5:
    print("neutral")
else:
    print("satisfied")