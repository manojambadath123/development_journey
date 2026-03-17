
from csv import DictReader

fr = open("file_operations\\tips.csv","r")

data = list(DictReader(fr))

# print(data)

# print(data[0])

day_wise_summary={}

for t in data:

    day = t.get("day")

    tip = float(t.get("tip"))

    if day in day_wise_summary:

        day_wise_summary[day]+=tip

    else:

        day_wise_summary[day]=tip

# print(day_wise_summary)


# day with highest revenue

day_wise_revenue = {}

for t in data:

    day = t.get("day")
    total_bill = float(t.get("total_bill"))

    if day in day_wise_revenue:

        day_wise_revenue[day]+=total_bill

    else:

        day_wise_revenue[day]=total_bill

# print(day_wise_revenue)

# day_wise_revenue_max = [[v,k] for k,v in day_wise_revenue.items()]

# print(day_wise_revenue_max)

# print(sorted(day_wise_revenue_max,reverse=True)[0][1])



# female or male customers give more tip

sex_wise_tip ={}

for t in data:

    sex = t.get("sex")
    tip_count = float(t.get("tip"))

    if sex in sex_wise_tip:

        sex_wise_tip[sex]+=tip_count

    else:

        sex_wise_tip[sex]=tip_count

print(sex_wise_tip)

max_sex_wise_tip = [[v,k] for k,v in sex_wise_tip.items()]

print(max_sex_wise_tip)

print(sorted(max_sex_wise_tip,reverse=True))
print(sorted(max_sex_wise_tip,reverse=True)[0][0])



print(sorted(sex_wise_tip,key = lambda x: sex_wise_tip.get(x),reverse=True))

  