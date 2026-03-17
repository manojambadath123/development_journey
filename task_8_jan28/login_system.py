
db_username = "abcd"

db_password = "abcd@123"

username = input("enter username=")

password = input("enter password=")

if db_username==username and db_password==password:

    print("login successful")
else:

    print("invalid credentials")