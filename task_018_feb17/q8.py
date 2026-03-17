
expense_month = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,-11000,-1]
#                 0    1    2    3    4     5    6   7    8     9     10    11

#                 jan  feb  mar  apr  may  jun  jul  aug  sep   oct   nov   dec
count_positive = 0
count_negative = 0

for exp in expense_month:

    if exp>0:

        count_positive+=1

    elif exp<0:

        count_negative+=1

print("positive number count=",count_positive)
print("negative number count=",count_negative)