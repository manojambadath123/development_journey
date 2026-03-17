

class Rectangle:

    def __init__(self,length,breadth):

        self.length=length
        self.breadth=breadth

    def area(self):

        self.area = self.length*self.breadth
        print(self.area)

rect_instance = Rectangle(10,15)
rect_instance.area()