


from abc import ABC,abstractmethod

class Bike(ABC):

    @abstractmethod               # decorator what all features are given in the decorator abstract method ,al will be imparted tothe trans and start defined method
    def transmission(self): pass

    @abstractmethod
    def start(self): pass

class Pulsar(Bike):

    def transmission(self):
        
        print("pulsar transmission")

    def start(self):

        print("pulsar start method")

pulsar_instance = Pulsar()

pulsar_instance.transmission()
pulsar_instance.start()
    


