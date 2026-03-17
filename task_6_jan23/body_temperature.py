
body_temp = float(input("enter your body temperature in celsius="))

if body_temp<36:
    print("low body temperature")
elif body_temp>=36 and body_temp<=37.5:
    print("normal")
elif body_temp>37.5:
    print("fever")