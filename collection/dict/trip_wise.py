

manali = {

    "dijo":300,
    "akshay":1000,
    "edwin":800,
    "allan":15000,
    "manoj":0,
    "subin":0,
    "sreyesh":500
}

total_expense = 0

for v in manali.values():

    total_expense+=v

print("total expense=",total_expense)

individual_split = round(total_expense/len(manali))

print("individualsplit=",individual_split)


spend_wise = {}

for k,v in manali.items():

    payment = individual_split-v

    spend_wise[k] = payment

print(spend_wise)