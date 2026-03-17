
rows = int(input("enter no of rows="))

for i in range(1, rows + 1):
    
    for sp in range(rows - i):

        print("  ", end="")


    for star in range(i):


        print("*", end=" ")


    print()
