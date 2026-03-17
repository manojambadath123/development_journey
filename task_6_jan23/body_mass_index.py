
bmi = float(input("enter your bmi="))

if bmi<18.5:
    print("under weight")
elif bmi>=18.5 and bmi<=24.9:
    print("normal")
elif bmi>=25 and bmi<=29.9:
    print("over weight")
elif bmi>=30:
    print("obese")
