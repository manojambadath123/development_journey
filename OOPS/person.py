

class Person:

    name:str

    age: int
    
    def set_name(self,name):

        self.name = name

    def set_age(self,age):

        self.age = age

    def display(self):

        print(self.name,self.age)

person_instance =Person()

person_instance.set_name("vipin")
person_instance.set_age(24)
person_instance.display()
