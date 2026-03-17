
user_age = int(input("enter a age="))
seat_avail = 20
if user_age>=18:

    seat_count= (input("enter seat count="))

    if seat_count <= seat_avail:

        print("tickets booked")
    else:

        print("no tickets-housefull")
else:

    print("not eligible to watch movie")

