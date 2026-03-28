

class Student:
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    
    def display_details(self):
        print("Student Name=", self.name)
        print("Marks=", self.marks)


    def calculate_grade(self):
        if self.marks >= 90:
            print("A")
        elif self.marks >= 75:
            print("B")
        elif self.marks >= 50:
             print("C")
        else:
             print("Fail")


student1 = Student("Manoj", 85)
student2 = Student("Anu", 45)


student1.display_details()
student1.calculate_grade()


student2.display_details()
student2.calculate_grade()