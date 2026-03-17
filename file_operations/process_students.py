

fr_all_students = open("file_operations\\all_students.txt","r")

fr_passed_students = open("file_operations\\passed_students.txt","r")

all_students_list = [line.rstrip("\n") for line in fr_all_students]

print(all_students_list)

passed_students_list = [line.rstrip("\n") for line in fr_passed_students]

print(passed_students_list)

failed_students = set(all_students_list).difference(passed_students_list)

print(failed_students)