
db_table_num = 123

user_table_num = int(input("enter table number="))

if db_table_num==user_table_num:

    user_food_avail = input("enter user food availability=")

    if user_food_avail=="yes":

        print("order placed")
    else:

        print("item out of stock")

else:

    print("invalid table number")
