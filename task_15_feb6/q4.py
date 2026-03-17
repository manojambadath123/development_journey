
rows = int(input("enter no of rows="))

for i in range(rows,0,-1):
    
    for star in range(i):


        print("*", end=" ")

    for sp in range(rows-i):


        print(" ", end=" ")

    print()