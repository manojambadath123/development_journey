
systolic_bp = int(input("enter your systolic bp="))

if systolic_bp<120:
    print("normal")
elif systolic_bp<=129:
    print("elevated")
elif systolic_bp<=139:
    print("high bp")
elif systolic_bp>=140:
    print("high bp stage 2")
