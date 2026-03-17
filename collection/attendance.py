
attendance = ["H","P","P","P","H","P","H","H","P"]
#              0   1   2   3   4   5   6   7   8
holiday_count=0
present_count=0
online_count=0
leave_count=0

# print(attendance)

# attendance[4] = "P"

# print(attendance)


# for i in range(0,9):

#     print(attendance[i],end=" ")


for att in attendance:

    if att =="H":

        holiday_count+=1

    elif att =="P":

        present_count+=1

    elif att =="O":

        online_count+=1

    elif att == "L":

        leave_count+=1

print("holidaycount=",holiday_count)
print("presentcount=",present_count)
print("onlinecount=",online_count)
print("leavecount=",leave_count)



    









