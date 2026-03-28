


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            print("A+")
        elif self.marks >= 75:
            print("A")
        elif self.marks >= 60:
            print("B")
        elif self.marks >= 50:
            print("C")
        else:
            print("F")

    def display_details(self):
        print(self.name)
        print(self.marks)
        # print(self.calculate_grade())

s1 = Student("Manoj", 82)

s1.display_details()

s1.calculate_grade()