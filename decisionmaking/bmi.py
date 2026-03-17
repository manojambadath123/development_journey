
weight_in_kg = int(input("enter weight_in_kg="))

height_in_cm = int(input("enter height_in_cm="))

height_in_m = height_in_cm/100

bmi = weight_in_kg/(height_in_m)**2

print(bmi)

bmi = round(bmi)

print(bmi)

if bmi<20:
    print("under weight")
elif bmi>=20 and bmi<25:
    print("normal")
elif bmi>=25 and bmi<30:
    print("over weight")
else:
    print("obese")


# if bmi<20:
#     print("under weight")
# elif bmi<25:
#     print("normal")
# elif bmi<30:
#     print("over weight")
# else:
#     print("obese")

