

class Person:

    def __init__(self,name,city):

        self.name=name
        self.city=city

    def display(self):

        print(self.name,self.city)


person_instance = Person("vipin","ekm")

person_instance.display()