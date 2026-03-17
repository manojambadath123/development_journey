
from csv import DictReader

fr = open("task_27_mar4\\move.csv","r")

data = list(DictReader(fr))

for i in range(0,4):

    print(data[i])

