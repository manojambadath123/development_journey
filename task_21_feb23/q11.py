
student_marks = {
    'Alice': 85,
    'Bob': 72,
    'Charlie': 90,
    'David': 75,
    'Eve': 78,
    'Frank': 65
}


print("Students who scored above 75:")

for name, marks in student_marks.items():

    if marks > 75:
        
        print(name,marks)