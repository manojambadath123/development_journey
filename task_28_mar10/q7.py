

class Product:

    def __init__(self,name,price):

        self.name=name
        self.price=price

    def display(self):

        print(self.name,self.price)


product_instance = Product("mobile",25000)

product_instance.display()