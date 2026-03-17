

class Circle:

    def __init__(self,radius):

        self.radius=radius

    def solution(self):

        self.area = 3.14*self.radius*self.radius

        print(self.area)

circle_instance = Circle(2)

circle_instance.solution()