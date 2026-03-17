

class Animal:

    color:str
    size :str
    sound:str

    def walk(self):

        print("animal walk method")

    def jump(self):

        print("animal jump method")


cat_instance = Animal()
dog_instance = Animal()

cat_instance.walk()
dog_instance.walk()

