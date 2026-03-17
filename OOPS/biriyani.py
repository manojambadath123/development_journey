

class Biriyani:

    title:str
    category:str
    place:str
    price:int

    def set_biriyani(self,title,category,place,price):

        self.title=title
        self.category=category  # initialize attributes or initialize instance variables Ie constructor
        self.place=place        # self keyword is used to point current class object
        self.price=price

    def display(self):

        print(self.title,self.category,self.place,self.price)

veg_biriyani_instance = Biriyani()
chk_biriyani_instance = Biriyani()

veg_biriyani_instance.set_biriyani("biriyani","veg","ekm",250)
veg_biriyani_instance.display()

chk_biriyani_instance.set_biriyani("biriyani","chicken","kozhikode",290)
chk_biriyani_instance.display()