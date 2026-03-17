
"""
child class redefines the method that is already defined in parent class
"""

class Parent:

    def vehicle(self):

        print("passion pro")

    def car(self):

        print("swift")

class Child(Parent):

    def vehicle(self):
        
        print("duke")

    def car(self):

        print("bmw")

child_instance = Child()

child_instance.vehicle()
child_instance.car()
