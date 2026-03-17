

def analyze_numbers(*args:tuple,**kwargs:dict):

    if kwargs.get("action")=="max":

        return max(args)
    
    elif kwargs.get("action")=="min":

        return min(args)
    
    elif kwargs.get("action")=="count":

        count =0

        for num in args:

            count+=1

        return count
    
print(analyze_numbers(10,11,12,13,14,15,action="max"))
print(analyze_numbers(10,11,12,13,14,15,action="min"))
print(analyze_numbers(10,11,12,13,14,15,action="count"))