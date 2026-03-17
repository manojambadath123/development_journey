#single level inheritance using constructor initialization

class Brand:

    def __init__(self,bname):

        self.bname=bname

    def display_brand(self):

        print(self.bname)

class Product(Brand):

    def __init__(self,bname,ptitle,price):

        super().__init__(bname)

        self.ptitle=ptitle
        self.price=price

    def display_product(self):

        super().display_brand()

        print(self.ptitle,self.price)

product_instance1 = Product("lewis","jeans",2500)
product_instance1.display_product()

product_instance2 = Product("flying machine","jeans",1500)
product_instance2.display_product()

