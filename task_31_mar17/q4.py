


from copy import deepcopy

arun_fvt_foods =[

    {"meal_type":"breakfast","meal":"dosa"},
    {"meal_type":"lunch","meal":"fish_meal"},
    {"meal_type":"dinner","meal":"fried rice"}
    
]

hari_fvt_foods = deepcopy(arun_fvt_foods)  

hari_fvt_foods[0]["meal"]="idly"

print(arun_fvt_foods)
print(hari_fvt_foods)