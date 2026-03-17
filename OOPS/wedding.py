


class Parent:

    def properties(self):

        print("5kg gold")

    def weds_with(self):

        print("gopalan")

class Child(Parent):

    def weds_with(self):
        
        print("DQ")

child_instance = Child()

child_instance.properties()

child_instance.weds_with()