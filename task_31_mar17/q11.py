


from copy import copy


class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


s1 = Student("Manoj",[80,81,82])

s2 = copy(s1)

s2.marks.append(83)
# s2.name = "vipin"

print( s1.name, s1.marks)
print( s2.name, s2.marks)

print( id(s1))
print( id(s2))