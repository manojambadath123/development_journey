


class Bird:
    def fly(self):
        print("Birds can fly")


class Sparrow(Bird):
    def fly(self):
        print("Sparrow flies high in the sky")


class Ostrich(Bird):
    def fly(self):
        print("Ostrich cannot fly")


b = Bird()
s = Sparrow()
o = Ostrich()


b.fly()
s.fly()
o.fly()