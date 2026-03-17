
from copy import deepcopy

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

s1 = Student("Manoj", [80, 85, 90])

s2 = deepcopy(s1)

s2.name = "Rahul"
s2.marks.append(95)

print( s1.name, s1.marks)
print( s2.name, s2.marks)

print( id(s1))
print(id(s2))