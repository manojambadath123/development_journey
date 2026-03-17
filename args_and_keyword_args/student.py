

def student_details(*args:tuple):
    
    print(args[0],args[3])  # there is no clarity in [1]and [2] index values


# student_details("vipin",1234,1236,"vipin@gmail.com","cs")


def employee_details (**kwargs:dict):


    print(kwargs.get("name"),kwargs.get("dept"))  # here there is more clarity since it is accessed through keys


# employee_details(name="vipin",dept="hr",salary=23000)


