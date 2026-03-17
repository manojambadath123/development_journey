
def calculator(n1,n2,op="+"):

    if op=="*":

        mult=n1*n2
        return mult

    elif op=="/":

        div = n1/n2
        return div

    elif op=="-":

        sub = n1-n2
        return sub

    elif op=="+":

        add = n1+n2
        return add

print(calculator(10,2,"*"))
print(calculator(10,2,"-"))
print(calculator(10,2,"/"))
print(calculator(10,2,"+"))
print(calculator(10,2))







    