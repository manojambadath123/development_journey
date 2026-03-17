
temp = int(input("enter a temperature in celsius="))

if temp<20:
    print(temp,"is cold")
elif temp>=20 and temp<=30:
    print(temp,"is normal")
elif temp>30:
    print(temp,"is hot")