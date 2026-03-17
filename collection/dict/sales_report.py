

sales_report = {

    "sun":1800,
    "mon":1700,
    "tue":1600,
    "wed":1500,
    "thu":1400,
    "fri":1300,
    "sat":1200
    
}

# for key in sales_report:

#     print(key,sales_report[key])

total_sales = 0

for key in sales_report:

    sales = sales_report[key]
    total_sales+=sales

print(total_sales)

avg_sale = total_sales/len(sales_report)

print(avg_sale)

for key in sales_report:

    if sales_report[key]<avg_sale:

       print(key,sales_report[key])



largest_sale=sales_report["sun"]   # on which day largest sale had occured

for key in sales_report:

    if sales_report[key]>largest_sale:

        largest_sale = sales_report[key]

print(largest_sale)
