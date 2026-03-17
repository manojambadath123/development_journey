

from csv import DictReader

fr = open("task_27_mar4\\move.csv","r")

data = list(DictReader(fr))

import csv

# Replace 'movies.csv' with your actual file name
with open("task_27_mar4\\move.csv", "r") as file:
    reader = csv.reader(file)
    
    # Read the first row (header)
    header = next(reader)
    
    # Print all column names
    print("Column Names:")
    for column in header:
        print(column)