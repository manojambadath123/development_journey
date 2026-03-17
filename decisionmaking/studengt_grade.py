
mark1 = int(input("enter mark1="))
mark2 = int(input("enter mark2="))
mark3 = int(input("enter mark3="))

total_mark = mark1 + mark2 +mark3

grace_mark = ((2/100)* total_mark)

print(grace_mark)

total_mark = total_mark + grace_mark

print(total_mark)

if total_mark>140:
    print("A")
elif total_mark>130 and total_mark<=140:
    print("B")
elif total_mark>120 and total_mark<=130:
    print("C")
elif total_mark<=120:
    print("fail")
else:
    print("invalid")
