
#single level inheritance

class Parent:

    def house(self):

        print("parent class house method")

class Child(Parent):   #child is the subclass of parent class called single level inheritance

    def mobile(self):

        print("child class mobile method")

child_instance = Child()

child_instance.mobile()

child_instance.house()



