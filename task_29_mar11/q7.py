

class Shape:
    def draw(self):
        print("Drawing a shape")


class Square(Shape):
    def draw(self):
        print("Drawing a Square")


class Triangle(Shape):
    def draw(self):
        print("Drawing a Triangle")

shape_instance = Shape()
square_instance = Square()
triangle_instance = Triangle()


shape_instance.draw()
square_instance.draw()
triangle_instance.draw()