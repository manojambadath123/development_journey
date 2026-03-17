
employees = ["hari","dixon","joji","libin","shafi"]

fw = open("file_operations\\employees.txt","w")


# fw.write("hari"+"\n")
# fw.write("dixon")

for e in employees:

    fw.write(e+"\n")

fw.write("100")

print("completed")