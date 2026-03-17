
intake = int(input("intake of water in liters="))

if intake<2:
    print("dehydrated")
elif intake>=2 and intake<=3:
    print("adequate intake")
elif intake>3:
    print("excess intake")