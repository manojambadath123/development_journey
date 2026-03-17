
oxygen_level = int(input("enter your oxygen level="))

# if oxygen_level<90:
#     print("critical")
# elif oxygen_level>=90 and oxygen_level<=94:
#     print("mild concern")
# elif oxygen_level>=95:
#     print("normal")


if oxygen_level<90:
    print("critical")
elif  oxygen_level<=94:
    print("mild concern")
elif oxygen_level>=95:
    print("normal")

