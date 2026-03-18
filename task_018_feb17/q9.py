search_element = int(input("enter a number="))

expense_month = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,-11000,-1]

for exp in expense_month:

    if search_element==exp:

        print("searched element found",exp)

        break

else:
        
    print("searched element  not found")


    
