
#multiple inheriance there is two parent class and one child class and child class is ineriheritted from both parent clasess so that we can access all the attributes and defined functions from both child class as well as parent classes
class Father:

    def coaching_skill(self):

        print("father coaching skill")

    def cooking_skill(self):

        print("father cooking skill")

class Mother:

    def cooking_skill(self):

        print(" mother cooking skill")



class Child(Father,Mother):

    pass

child_instance = Child()

child_instance.coaching_skill()

child_instance.cooking_skill()