
steps = int(input("enter your steps="))

# if steps<5000:
#     print("sedentary")
# elif steps>=5000 and steps<=9999:
#     print("moderately active")
# elif steps>=10000:
#     print("active")

if steps<5000:
    print("sedentary")
elif steps<=9999:
    print("moderately active")
elif steps>=10000:
    print("active")