
db_password = "password@123"

db_otp = "2121"

user_password = input("enter a password=")

if db_password==user_password:

    otp = input("enter a otp=")

    if db_otp==otp:

        print("login successful")
    else:
        print("incorrect otp")
else:
    print("incorrect password")




