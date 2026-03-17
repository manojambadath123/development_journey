
calories = int(input("enter your intake of calories="))

if calories<1500:
    print("low intake")
elif calories>=1500 and calories<=2500:
    print("balanced intake")
elif calories>2500:
    print("excess intake")