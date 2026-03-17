
weight_in_kg = int(input("enter weight_in_kg="))

height_in_cm = int(input("enter height_in_cm="))

height_in_m = height_in_cm/100

bmi = weight_in_kg/(height_in_m)**2

print(bmi)

if bmi<18.5:
    print("under weight")
elif bmi>=18.5 and bmi<=24.9:
    print("normal")
elif bmi>=25 and bmi<=29.9:
    print("over weight")
elif bmi>=30:
    print("obese")


