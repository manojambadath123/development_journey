

class Rectangle:
    def rect(self, length,breadth):
        self.length = length
        self.breadth = breadth

    def area_rect(self):
        print (self.length * self.breadth)


class Circle:
    def circle(self,radius):
        self.radius = radius

    def area_circle(self):
        print(3.14 * self.radius * self.radius)


rect_instance = Rectangle()
circle_instance = Circle()

rect_instance.rect(10,15)
rect_instance.area_rect()

circle_instance.circle(2)
circle_instance.area_circle()
