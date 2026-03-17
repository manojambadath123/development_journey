

from csv import DictReader

fr = open("task_27_mar4\\move.csv","r")

data = list(DictReader(fr))

# print(data)


for m in data:
        # Check if any field contains the letter 'i'
        if any('i' in cell.lower() for cell in m):
            print(m)