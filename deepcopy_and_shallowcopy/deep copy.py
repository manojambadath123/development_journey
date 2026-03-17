


from copy import deepcopy,copy

arun_fvt_foods =[

    {"meal_type":"breakfast","meal":"dosa"},
    {"meal_type":"lunch","meal":"fish_meal"},
    {"meal_type":"dinner","meal":"fried rice"}
    
]

hari_fvt_foods = deepcopy(arun_fvt_foods) #deepcopy will create both inner and outer objects or references

hari_fvt_foods[0]["meal"]="idly"

print(arun_fvt_foods)
print(hari_fvt_foods)


arun_fvt_foods =[

    {"meal_type":"breakfast","meal":"dosa"},
    {"meal_type":"lunch","meal":"fish_meal"},
    {"meal_type":"dinner","meal":"fried rice"}
    
]

hari_fvt_foods = copy(arun_fvt_foods) #shallow copy will create only outer object or references

hari_fvt_foods[0]["meal"]="idly"

# print(arun_fvt_foods)
# print(hari_fvt_foods)