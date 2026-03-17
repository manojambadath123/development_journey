
expense_month = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,11000,12000]
#                 0    1    2    3    4     5    6   7    8     9     10    11

#                 jan  feb  mar  apr  may  jun  jul  aug  sep   oct   nov   dec

smallest = expense_month[0]

for i in range(0,12):

    if expense_month[i]<smallest:

        smallest = expense_month[i]

print("smallest number",smallest)


