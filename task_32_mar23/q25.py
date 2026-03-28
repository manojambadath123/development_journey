


# db_username = "admin"
# db_password = "1234"

# username = input("Enter username= ")
# password = input("Enter password= ")


# if username == db_username and password == db_password:
#     print("Login successful!")
# else:
#     print("Invalid username or password")


db_username = "admin"
db_password = "1234"

username = input("Enter username= ")
password = input("Enter password= ")


if db_username==username:

    if db_password==password:

        print("login successful")

    else:

        print("incorrect password")

else:

    print("incorrect username")