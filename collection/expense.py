
expense_month = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,11000,12000]
#                 0    1    2    3    4     5    6   7    8     9     10    11

#                 jan  feb  mar  apr  may  jun  jul  aug  sep   oct   nov   dec

total_expense=0

for exp in expense_month:

    total_expense+=exp

avg_expense=total_expense/len(expense_month)

print("total expense=",total_expense)
print("average expense=",avg_expense)




