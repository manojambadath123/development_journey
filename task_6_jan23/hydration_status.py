
color = int(input("enter your urine color count="))

if color>=1 and color<=3:
    print("well hydrated")
elif color>=4 and color<=6:
    print("mild dehydration")
elif color>=7 and color<=8:
    print("severe dehydration")
else:
    print("invalid")