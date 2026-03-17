

class Mobile:

    def __init__(self,image,name,price,rating):

        self.image=image
        self.name=name
        self.price=price
        self.rating=rating

    def display(self):

        print(self.image,self.name,self.price,self.rating)

mobile_instance1 = Mobile("iphone16.png","iphone16","120000",5)
mobile_instance1.display()



