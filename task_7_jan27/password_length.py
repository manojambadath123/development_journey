
password = input("enter a password=")

count = len(password)

print(count)


if count>=8:
    print("valid password")
else:
    print("invalid password")