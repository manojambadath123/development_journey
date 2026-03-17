
search_element = int(input("enter a number="))

count=0

expense_month = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,-11000,1000]

for exp in expense_month:

    if search_element==exp:

        count+=1

print("count of searched number=",count)

