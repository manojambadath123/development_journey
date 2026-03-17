
#polymorphism method overloading

class Calculator:

    def add(self,n1,n2):

        return n1+n2
    
    def add(self,n1,n2,n3):

        return n1+n2+n3
    
    def add(self,n1,n2,n3,n4):

        return n1+n2+n3+n4
    
cal_instance = Calculator()

print(cal_instance.add(10,20,30,40))
print(cal_instance.add(10,20,30)) # error => python doesnot support polymorphism method overloading for that we use *args and *kwargs
print(cal_instance.add(10,20)) # error 