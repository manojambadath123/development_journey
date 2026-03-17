
fr = open("file_operations\\food_logs.txt","r")

food_logs = []

for line in fr:

    data = line.rstrip("\n").split(",")

    log = {"id":data[0],"meal_type":data[1],"name":data[2],"calorie":float(data[3]),"date":data[4],"owner":data[5]}

    food_logs.append(log)

print(food_logs)

#all calorie

all_calorie = [f.get("calorie") for f in food_logs]
# print(all_calorie)

#dinner time meal names

meal_names = [f.get("name") for f in food_logs if f.get("meal_type")=="dinner"]

# print(meal_names)


#highest calorie meal name

high_calorie = max([f.get("calorie") for f in food_logs])

highest_calorie_name = [f.get("name") for f in food_logs if f.get("calorie")==high_calorie]

# print(highest_calorie_name)




