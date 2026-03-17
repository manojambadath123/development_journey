

class Laptop:

    def __init__(self,brand,ram):

        self.brand=brand
        self.ram=ram

    def display(self):

        print(self.brand,self.ram)


laptop_instance = Laptop("HP",250)

laptop_instance.display()