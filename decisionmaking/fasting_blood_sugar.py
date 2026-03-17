
fast_blood_sugar = int(input("enter fast blood sugar count="))

if fast_blood_sugar<100:
    print("normal")
elif fast_blood_sugar<125:
    print("prediabetes")
elif fast_blood_sugar>=125:
    print("diabetes")