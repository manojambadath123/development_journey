

class Animal:
    def eat(self):
        print("Animal is eating")


class Lion(Animal):
    def eat(self):
        print("Lion eats meat")


class Cow(Animal):
    def eat(self):
        print("Cow eats grass")


animal_instance = Animal()
lion_instance = Lion()
cow_instance = Cow()

animal_instance.eat()
lion_instance.eat()
cow_instance.eat()