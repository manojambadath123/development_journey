

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


# multi level inheritance

class GrandParent:

    def properties(self):

        print("grand parent properties")

class Parent(GrandParent):

    def house(self):

        print("parent house method")

class Child(Parent):

    pass

child_instance = Child()

child_instance.house()
child_instance.properties()


#multiple inheriance there is two parent class and one child class and child class is ineriheritted from both parent clasess so that we can access all the attributes and defined functions from both child class as well as parent classes
class Father:

    def coaching_skill(self):

        print("father coaching skill")

    def cooking_skill(self):

        print("father cooking skill")

class Mother:

    def cooking_skill(self):

        print(" mother cooking skill")



class Child(Father,Mother):

    pass

child_instance = Child()

child_instance.coaching_skill()

child_instance.cooking_skill()

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


class Animal:
    def sound(self):
        print("Animal makes a sound")


# Child class (inherits from Animal)
class Dog(Animal):
    def sound(self):   # Method overriding
        print("Dog barks")


class Cat(Animal):
    def sound(self):   # Method overriding
        print("Cat meows")


# Creating objects
a = Animal()
d = Dog()
c = Cat()

# Calling methods
a.sound()   # Parent class method
d.sound()   # Overridden method in Dog
c.sound()   # Overridden method in Cat

