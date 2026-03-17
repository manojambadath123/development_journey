

daily_calories = {
    "sun":1800,
    "mon":1700,
    "tue":1600,
    "wed":1500,
    "thu":1400,
    "fri":1300,
    "sat":1200
    

}

# for key in daily_calories:

#     print(key,daily_calories[key])



total_calories = 0 

for key in daily_calories:

    cal = daily_calories[key]

    total_calories+=cal

print(total_calories)

avg_calories = total_calories/len(daily_calories)

print(avg_calories)





