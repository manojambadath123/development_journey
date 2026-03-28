


class Student:

    def __init__(self,name,marks):

        self.name=name
        self.marks = marks

    def display_details(self):

        print(self.name)
        print(self.marks)

student_instance = Student("manoj",[85,80,75])

student_instance.display_details()