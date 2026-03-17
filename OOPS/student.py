

class Student:

    
    def __init__(self,rollno,name,course):

        self.rollno=rollno
        self.name=name
        self.course=course
        
    def display(self):

        print(self.rollno,self.name,self.course)

student_instance1= Student(1,"vipin","django")
student_instance2= Student(2,"deepak","datascience")

# student_instance1.set_student(1,"vipin","django")
student_instance1.display()

# student_instance2.set_student(2,"deepak","datascience")
student_instance2.display()

