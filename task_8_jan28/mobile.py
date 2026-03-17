
db_pattern = "abc123"

user_pattern = input("enter user pattern=")

db_finger_print = "12345"

if db_pattern==user_pattern:

    user_finger_print = input("enter your user fingerprint=")

    if user_finger_print==db_finger_print:

        print("phone unlocked")
    else:
        print("finger print mismatch")
else:

    print("wrong pattern")

