

class Employee:

    def __init__(self,name,salary):

        self.name=name
        self.salary=salary

    def display(self):

        print(self.name,self.salary)


emp_instance = Employee("vipin",5000)

emp_instance.display()