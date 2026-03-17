

class Vehicle:
    def move(self):
        print("Vehicle is moving")


class Car(Vehicle):
    def move(self):
        print("Car is driving on the road")


class Airplane(Vehicle):
    def move(self):
        print("Airplane is flying in the sky")



vehicle_instance = Vehicle()
car_instance = Car()
airplane_instance = Airplane()


vehicle_instance.move()
car_instance.move()
airplane_instance.move()