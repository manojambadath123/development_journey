


def number_checker(*args:tuple,**kwargs:dict):

    type = kwargs.get("type")

    if type=="odd":

        count_o=0

        for num in args:

            if num%2!=0:

                count_o+=1

        return count_o
    
    elif type == "even":

        count_e = 0

        for num in args:

            if num%2==0:

                count_e+=1

        return count_e
    
    elif type == "positive":

        count_p=0

        for num in args:

            if num>0:

                count_p+=1

        return count_p
    
    elif type == "negative":

        count_n = 0

        for num in args:

            if num<0:

                count_n+=1

        return count_n

print(number_checker(10,11,12,13,14,15,type="odd"))
    
print(number_checker(10,11,12,13,14,15,type="even"))
    
print(number_checker(10,11,12,13,14,15,type="positive"))
    
print(number_checker(10,11,12,13,14,15,type="negative"))
    


