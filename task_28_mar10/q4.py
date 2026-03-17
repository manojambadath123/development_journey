

class Car:

    def __init__(self,brand,model):

        self.brand=brand
        self.model=model

    def display(self):

        print(self.brand,self.model)

car_instance = Car("audi","q7")
car_instance.display()