

def calculator(*args:tuple,**kwargs:dict):

    #args(10,20,30,40)
    #kwargs{"key":"+"}

    if kwargs.get("key")=="+":

        return sum(args)
    
    elif kwargs.get("key")=="*":

        p=1

        for num in args:

            p*=num

        return p
    
    elif kwargs.get("key")=="/":

        div = 1

        for num in args:

            div = div /num

        return div

# print(calculator(10,20,30,40,key="+"))
# print(calculator(10,20,30,40,key="*"))
# print(calculator(20,10,key="/"))


  


