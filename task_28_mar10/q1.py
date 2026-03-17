

class Student:

    def __init__(self,name,age):

        self.name=name
        self.age=age

    def display(self):

        print(self.name,self.age)


student_instance = Student("vipin",29)
student_instance.display()